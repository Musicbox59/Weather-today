# Wetter Heute

Einfache Wetter-App als **eine einzige HTML-Datei** (`index.html`) – ohne Anmeldung, ohne Werbung, ohne API-Schlüssel.

## Funktionen
- **Einstellungen (⚙)**: Einheiten wählbar – Temperatur °C/°F, Wind km/h, m/s, mph, Knoten oder Beaufort, Niederschlag mm/cm oder Zoll, Luftdruck hPa, inHg oder mmHg, Uhrzeit 24 h oder 12 h; Schnellauswahl Metrisch / Imperial
- **Deutsch / Englisch** – umschaltbar über die Fahnen oben (🇦🇹 DE / 🇬🇧 EN); ohne Auswahl richtet sich die Sprache nach dem Browser
- **Standort** per GPS des Smartphones, per **Ortssuche** (Name oder PLZ) oder per **Punkt auf der Karte**
- **Ortssuche** nach Name oder Postleitzahl – auch österreichische PLZ (4-stellig), Ortsteile und Weiler; Treffer aus Österreich, Deutschland und der Schweiz zuerst
- **Favoriten** mit dem ☆-Stern speichern; eigene Seite „☰ Favoriten“: jeder Ort als Balken mit aktuellem Wetter-Symbol, Temperatur, Höchst-/Tiefstwert, Wind, Regen/Schnee und Sonnenstunden; sortieren, umbenennen, löschen
- **Favoriten sichern**: als Datei (JSON) herunterladen und wiederherstellen oder als Sicherungs-Link (Lesezeichen) aufbewahren
- Ansichten: **Heute** (aktuell, Tagesverlauf, stündlich), **3 Tage**, **7 Tage**, **21 Tage**, **Radar**
- **Hinweis für Allergiker**: Pollenflug von heute auf der Startseite; Wetter-Symbol eines Tages antippen zeigt die Pollenbelastung (Erle, Birke, Gräser, Beifuß, Ambrosia, Olive) für diesen Tag – Europa, ca. 3 Tage voraus
- **Was ziehe ich an?** – Outfit-Vorschlag für jeden Tag als Modepuppe (Frau/Mann umschaltbar): berücksichtigt gefühlte Temperatur im Tagesverlauf, Regen, Schnee, Wind, UV sowie die Region (Höhenlage, Alpenraum mit Trachtenjanker, Küste mit Friesennerz, Süden)
- **Bauernregel des Tages**: halbtransparentes Symbol rechts unten öffnet einen augenzwinkernden Wetterspruch (60 Sprüche, Deutsch und Englisch, jeder Tag ein anderer; Vortag/Folgetag durchblättern)
- **Niederschlagsradar**: in Deutschland automatisch das DWD-Radar (1 km), weltweit RainViewer – umschaltbar; animierte 2D-Karte (ca. letzte 2 Stunden + Kurzfrist-Prognose, falls verfügbar) mit Markierung der aktuellen Position, Zeitleiste und Play/Pause
- Darstellung angelehnt an klassische Wetterportale: Symbole, rote Höchst-/blaue Tiefstwerte, Temperaturkurven, Regenwahrscheinlichkeit

## Datenquellen (kostenlos & seriös)
| Zweck | Dienst |
|---|---|
| Vorhersage Tag 1–16 | [Open-Meteo](https://open-meteo.com) – Modelle u. a. DWD ICON, ECMWF, NOAA GFS |
| Trend Tag 17–21 | Open-Meteo Ensemble-API, NOAA GEFS (Mittel aus 31 Läufen) |
| Pollenvorhersage | Copernicus CAMS über Open-Meteo Air-Quality-API (Europa) |
| Ortssuche | Open-Meteo Geocoding (GeoNames); Postleitzahlen, Ortsteile & Weiler über Nominatim / OpenStreetMap |
| Ortsname zu GPS/Kartenpunkt | Nominatim / OpenStreetMap |
| Niederschlagsradar Deutschland | [DWD GeoServer](https://maps.dwd.de) – WMS-Layer `dwd:Niederschlagsradar` |
| Niederschlagsradar weltweit | [RainViewer](https://www.rainviewer.com/api.html) (weltweite Radar-Mosaike, u. a. DWD) |
| Karte | Leaflet + OpenStreetMap, Radar-Hintergrund CARTO |

## App-Symbol
Sonne mit freundlichem Gesicht unter einem Regenschirm, dazu Regentropfen (`icons/icon.svg`).
Es ist als Tab-Symbol und als iPhone-Startbildschirm-Symbol direkt in `index.html` eingebettet und erscheint als Logo in der Kopfzeile.
`manifest.webmanifest` und der Ordner `icons/` sorgen dafür, dass die App – über eine Webadresse geöffnet und zum Startbildschirm hinzugefügt – mit diesem Symbol und ohne Adresszeile startet.

## Nutzung
GPS funktioniert im Browser nur über **HTTPS**. Am einfachsten über GitHub Pages:
Repository → *Settings* → *Pages* → Branch auswählen → Ordner `/ (root)`.
Danach die Seite auf dem Smartphone öffnen und über „Zum Startbildschirm hinzufügen“ wie eine App nutzen.
Wichtig: `index.html`, `manifest.webmanifest` und den Ordner `icons/` gemeinsam hochladen.
