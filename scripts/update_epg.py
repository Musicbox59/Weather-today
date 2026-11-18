#!/usr/bin/env python3
"""Lädt echte TV-Programmdaten (XMLTV) und schreibt data/epg.json für tv.html.

Quelle: epgshare01.online (frei verfügbare XMLTV-Dateien für Österreich und Deutschland).
Aufruf:  python3 scripts/update_epg.py                 -> lädt die Quellen aus EPG_URLS
         python3 scripts/update_epg.py datei.xml[.gz]  -> verarbeitet lokale Dateien (zum Testen)
"""
import gzip
import io
import json
import re
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path

EPG_URLS = [
    "https://epgshare01.online/epgshare01/epg_ripper_AT1.xml.gz",   # enthält alle Sender der Seite (Daten: tv-media.at)
]
OUT = Path(__file__).resolve().parent.parent / "data" / "epg.json"
DAYS_BACK, DAYS_AHEAD = 1, 8
MAX_DESC = 420

# Sender-ID in tv.html -> mögliche Namen in der Quelle (normalisiert, beste Treffer zuerst)
CHANNELS = {
    "orf1":    ["orf1", "orfeins"],
    "orf2":    ["orf2", "orf2w", "orf2wien", "orf2n", "orf2o"],
    "orf3":    ["orf3", "orfiii", "orf3kultur", "orfiiikultur"],
    "servus":  ["servustv", "servustvoesterreich", "servustvosterreich", "servustvaustria", "servustvdeutschland"],
    "arte":    ["arte", "artedeutsch", "artegerman"],
    "bayern":  ["brfernsehen", "brfernsehensued", "brfernsehensud", "bayerischesfernsehen", "br", "brsued", "brnord"],
    "zdf":     ["zdf"],
    "ard":     ["daserste", "dasersteard", "ard", "ardaserste"],
    "dreisat": ["3sat"],
    "puls4":   ["puls4"],
    "atv":     ["atv"],
    "srf1":    ["srf1", "srfeins"],
    "rtl":     ["rtl", "rtltelevision"],
    "vox":     ["vox"],
}
DROP = {"hd", "uhd", "sd", "at", "de", "ch", "tv", "austria", "germany", "deutschland", "oesterreich", "osterreich", "hevc", "1080", "720"}


def norm(name):
    """'ORF1.HD.at' -> 'orf1', 'Das Erste HD' -> 'daserste'."""
    s = name.lower().replace("ö", "oe").replace("ü", "ue").replace("ä", "ae")
    tokens = [t for t in re.split(r"[^a-z0-9]+", s) if t]
    full = "".join(tokens)
    short = "".join(t for t in tokens if t not in DROP)
    return full, short


def open_source(src):
    if re.match(r"https?://", src):
        req = urllib.request.Request(src, headers={"User-Agent": "tv-programm-epg/1.0"})
        for attempt in range(3):
            try:
                with urllib.request.urlopen(req, timeout=180) as r:
                    data = r.read()
                break
            except Exception as e:  # noqa: BLE001
                print(f"  Fehler {src}: {e}", file=sys.stderr)
                if attempt == 2:
                    return None
                time.sleep(5 * (attempt + 1))
    else:
        data = Path(src).read_bytes()
    if data[:2] == b"\x1f\x8b":
        data = gzip.decompress(data)
    return io.BytesIO(data)


def parse_time(s):
    # 20261118201500 +0100
    m = re.match(r"(\d{14})\s*([+-]\d{4})?", s or "")
    if not m:
        return None
    dt = datetime.strptime(m.group(1), "%Y%m%d%H%M%S")
    off = m.group(2) or "+0000"
    tz = timezone(timedelta(hours=int(off[:3]), minutes=int(off[0] + off[3:])))
    return int(dt.replace(tzinfo=tz).timestamp())


def text_of(el, tag, prefer=("de", "ger", "deu")):
    found = el.findall(tag)
    if not found:
        return ""
    for f in found:
        if (f.get("lang") or "").lower() in prefer and f.text:
            return f.text.strip()
    return (found[0].text or "").strip()


def main(sources):
    now = int(time.time())
    t_min, t_max = now - DAYS_BACK * 86400, now + DAYS_AHEAD * 86400
    out = {k: [] for k in CHANNELS}
    chosen = {}  # unsere ID -> (rang, quell-ID)

    for src in sources:
        print("Lade", src)
        fh = open_source(src)
        if fh is None:
            continue
        for ev, el in ET.iterparse(fh, events=("end",)):
            if el.tag == "channel":
                names = [el.get("id", "")] + [d.text or "" for d in el.findall("display-name")]
                for ours, wanted in CHANNELS.items():
                    for n in names:
                        full, short = norm(n)
                        for rank, w in enumerate(wanted):
                            if w in (full, short):
                                best = chosen.get(ours)
                                if best is None or rank < best[0]:
                                    chosen[ours] = (rank, el.get("id"))
                el.clear()
            elif el.tag == "programme":
                cid = el.get("channel")
                ours = next((k for k, v in chosen.items() if v[1] == cid), None)
                if ours:
                    s, e = parse_time(el.get("start")), parse_time(el.get("stop"))
                    if s and e and e > t_min and s < t_max:
                        p = {"s": s, "e": e, "t": text_of(el, "title")}
                        st = text_of(el, "sub-title")
                        if st:
                            p["st"] = st
                        d = text_of(el, "desc")
                        if d:
                            p["d"] = d if len(d) <= MAX_DESC else d[:MAX_DESC].rsplit(" ", 1)[0] + " …"
                        cats = [c.text.strip() for c in el.findall("category") if c.text]
                        if cats:
                            p["c"] = list(dict.fromkeys(cats))[:3]
                        y = text_of(el, "date")[:4]
                        if y.isdigit():
                            p["y"] = int(y)
                        co = [c.text.strip() for c in el.findall("country") if c.text]
                        if co:
                            p["co"] = "/".join(dict.fromkeys(co))
                        icon = el.find("icon")
                        if icon is not None and icon.get("src"):
                            p["img"] = icon.get("src")
                        cr = el.find("credits")
                        if cr is not None:
                            actors = [[a.text.strip(), a.get("role", "")] for a in cr.findall("actor") if a.text][:5]
                            if actors:
                                p["a"] = actors
                            dirs = [x.text.strip() for x in cr.findall("director") if x.text][:2]
                            if dirs:
                                p["dir"] = dirs
                        sr = el.find("star-rating/value")
                        if sr is not None and sr.text and "/" in sr.text:
                            a, b = sr.text.split("/", 1)
                            try:
                                p["r"] = round(float(a) / float(b) * 5 * 2) / 2
                            except ValueError:
                                pass
                        for epn in el.findall("episode-num"):
                            if epn.get("system") == "onscreen" and epn.text:
                                p["ep"] = epn.text.strip()
                            elif epn.get("system") == "xmltv_ns" and epn.text and "ep" not in p:
                                parts = epn.text.split(".")
                                try:
                                    se = int(parts[0].split("/")[0]) + 1 if parts[0].strip() else None
                                    en = int(parts[1].split("/")[0]) + 1 if len(parts) > 1 and parts[1].strip() else None
                                    if se and en:
                                        p["ep"] = f"Staffel {se}, Folge {en}"
                                    elif en:
                                        p["ep"] = f"Folge {en}"
                                except ValueError:
                                    pass
                        out[ours].append(p)
                el.clear()

    for k in out:
        seen, uniq = set(), []
        for p in sorted(out[k], key=lambda x: x["s"]):
            if p["s"] in seen:
                continue
            seen.add(p["s"])
            uniq.append(p)
        out[k] = uniq

    found = {k: v[1] for k, v in chosen.items()}
    print("Zuordnung:", json.dumps(found, ensure_ascii=False))
    print("Sendungen:", {k: len(v) for k, v in out.items()})
    if not any(out.values()):
        print("Keine Programmdaten gefunden – data/epg.json bleibt unverändert.", file=sys.stderr)
        return 1
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({
        "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source": "epgshare01.online / tv-media.at",
        "sourceIds": found,
        "channels": {k: v for k, v in out.items() if v},
    }, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print("Geschrieben:", OUT, OUT.stat().st_size, "Bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:] or EPG_URLS))
