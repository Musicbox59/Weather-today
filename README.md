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
