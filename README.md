# Wetter Heute

Einfache Wetter-App als **eine einzige HTML-Datei** (`index.html`) – ohne Anmeldung, ohne Werbung, ohne API-Schlüssel.

## Funktionen
- **Standort** per GPS des Smartphones, per **Ortssuche** (Name oder PLZ) oder per **Punkt auf der Karte**
- **Favoriten** mit dem ☆-Stern speichern (lokal im Browser, keine Anmeldung)
- Ansichten: **Heute** (aktuell, Tagesverlauf, stündlich), **3 Tage**, **7 Tage**, **21 Tage**
- Darstellung angelehnt an klassische Wetterportale: Symbole, rote Höchst-/blaue Tiefstwerte, Temperaturkurven, Regenwahrscheinlichkeit

## Datenquellen (kostenlos & seriös)
| Zweck | Dienst |
|---|---|
| Vorhersage Tag 1–16 | [Open-Meteo](https://open-meteo.com) – Modelle u. a. DWD ICON, ECMWF, NOAA GFS |
| Trend Tag 17–21 | Open-Meteo Ensemble-API, NOAA GEFS (Mittel aus 31 Läufen) |
| Ortssuche | Open-Meteo Geocoding (GeoNames) |
| Ortsname zu GPS/Kartenpunkt | Nominatim / OpenStreetMap |
| Karte | Leaflet + OpenStreetMap |

## Nutzung
GPS funktioniert im Browser nur über **HTTPS**. Am einfachsten über GitHub Pages:
Repository → *Settings* → *Pages* → Branch auswählen → Ordner `/ (root)`.
Danach die Seite auf dem Smartphone öffnen und über „Zum Startbildschirm hinzufügen“ wie eine App nutzen.

## TV-Programm (`tv.html`)
Programmvorschau als einzelne HTML-Datei: je Sender eine Spalte, die Zeit läuft senkrecht. Startet immer beim Ausschnitt ab **20:15**; durch Wischen nach oben/unten sieht man die übrigen Sendungen (05:00–05:00), nach links/rechts weitere Sender.
- Startsender: ORF 1, ORF 2, ORF III, ServusTV, Arte, Bayern 3, ZDF, ARD (weitere über ☰ ein-/ausblenden und sortieren)
- Je Sendung: Art (Doku, Thriller, …), Produktionsjahr, Land; bei Filmen Kritik in Sternen
- Tippen auf eine Sendung zeigt Details: Hauptdarsteller, Kritik-Zusammenfassung, YouTube-Trailer (auf Android optional direkt im Quetta-Browser)
- Tage bis +6, „Jetzt“-Linie, Hell/Dunkel
- 🐦 **Amsel** fliegt über die Seite, setzt sich auf Kopfbereich, Senderköpfe und Trennstriche zwischen Sendungen und singt (`media/amsel.mp3`; Ton über 🔊 im Kopf an/aus)
- 💡 **Ratgeber** (Button unten rechts): täglich ein Tipp statt Fernsehen – für Ihn, für Sie, für beide – plus eine Anekdote aus der Fernsehgeschichte
- **Programmdaten live:** Die Seite lädt beim Öffnen echte Programmdaten direkt aus dem Internet (XMLTV von epgshare01.online, Daten von tv-media.at) und speichert sie 4 Stunden im Browser. Weil die Quelle keinen direkten Browser-Zugriff erlaubt (CORS), läuft der Abruf bei Bedarf über einen öffentlichen CORS-Proxy (codetabs, allorigins, corsproxy.io). Die Fußzeile zeigt Quelle, Weg und Stand.
  - Die Quelle liefert Titel, Untertitel, Beschreibung, Kategorien, Land, Regie, Darsteller und Bilder – **kein Produktionsjahr und keine Bewertungssterne**. Diese werden nur bei den Demo-Daten angezeigt.
  - Optional: `.github/workflows/epg.yml` speichert die Daten zusätzlich zweimal täglich als `data/epg.json` im Repository (Rückfall, falls kein Proxy erreichbar ist).
  - Klappt beides nicht, zeigt die Seite Demo-Daten.
