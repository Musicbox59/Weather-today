# Wetter Heute

Einfache Wetter-App als **eine einzige HTML-Datei** (`index.html`) – ohne Anmeldung, ohne Werbung, ohne API-Schlüssel.

## Funktionen
- **Standort** per GPS des Smartphones, per **Ortssuche** (Name oder PLZ) oder per **Punkt auf der Karte**
- **Favoriten** mit dem ☆-Stern speichern (lokal im Browser, keine Anmeldung)
- Ansichten: **Heute** (aktuell, Tagesverlauf, stündlich), **3 Tage**, **7 Tage**, **21 Tage**, **Radar**
- **Niederschlagsradar**: in Deutschland automatisch das DWD-Radar (1 km), weltweit RainViewer – umschaltbar; animierte 2D-Karte (ca. letzte 2 Stunden + Kurzfrist-Prognose, falls verfügbar) mit Markierung der aktuellen Position, Zeitleiste und Play/Pause
- Darstellung angelehnt an klassische Wetterportale: Symbole, rote Höchst-/blaue Tiefstwerte, Temperaturkurven, Regenwahrscheinlichkeit

## Datenquellen (kostenlos & seriös)
| Zweck | Dienst |
|---|---|
| Vorhersage Tag 1–16 | [Open-Meteo](https://open-meteo.com) – Modelle u. a. DWD ICON, ECMWF, NOAA GFS |
| Trend Tag 17–21 | Open-Meteo Ensemble-API, NOAA GEFS (Mittel aus 31 Läufen) |
| Ortssuche | Open-Meteo Geocoding (GeoNames) |
| Ortsname zu GPS/Kartenpunkt | Nominatim / OpenStreetMap |
| Niederschlagsradar Deutschland | [DWD GeoServer](https://maps.dwd.de) – WMS-Layer `dwd:Niederschlagsradar` |
| Niederschlagsradar weltweit | [RainViewer](https://www.rainviewer.com/api.html) (weltweite Radar-Mosaike, u. a. DWD) |
| Karte | Leaflet + OpenStreetMap, Radar-Hintergrund CARTO |

## Nutzung
GPS funktioniert im Browser nur über **HTTPS**. Am einfachsten über GitHub Pages:
Repository → *Settings* → *Pages* → Branch auswählen → Ordner `/ (root)`.
Danach die Seite auf dem Smartphone öffnen und über „Zum Startbildschirm hinzufügen“ wie eine App nutzen.
