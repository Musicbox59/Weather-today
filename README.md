# Wetter Heute

Einfache Wetter-App als **eine einzige HTML-Datei** (`index.html`) – ohne Anmeldung, ohne Werbung, ohne API-Schlüssel.

## Funktionen
- **Einstellungen (⚙)**: Einheiten wählbar – Temperatur °C/°F, Wind km/h, m/s, mph, Knoten oder Beaufort, Niederschlag mm/cm oder Zoll, Luftdruck hPa, inHg oder mmHg, Uhrzeit 24 h oder 12 h; Schnellauswahl Metrisch / Imperial
- **Deutsch / Englisch** – umschaltbar über die Fahnen oben (🇦🇹 DE / 🇬🇧 EN); ohne Auswahl richtet sich die Sprache nach dem Browser
- **Standort** per GPS des Smartphones, per **Ortssuche** (Name oder PLZ) oder per **Punkt auf der Karte**
- **Ortssuche** nach Name oder Postleitzahl – auch österreichische PLZ (4-stellig), Ortsteile und Weiler; Treffer aus Österreich, Deutschland und der Schweiz zuerst
- **Favoriten auf der Karte**: In der Karte und im Radar sind alle Favoriten mit ★ und Namen markiert – Antippen öffnet das heutige Wetter dieses Ortes
- **Favoriten** mit dem ☆-Stern speichern; eigene Seite „☰ Favoriten“: jeder Ort als Balken mit aktuellem Wetter-Symbol, Temperatur, Höchst-/Tiefstwert, Wind, Regen/Schnee und Sonnenstunden; sortieren, umbenennen, löschen
- **Favoriten sichern**: als Datei (JSON) herunterladen und wiederherstellen oder als Sicherungs-Link (Lesezeichen) aufbewahren
- Ansichten: **Heute** (aktuell, stündlich mit Wind samt Einheit und Böen), **3 Tage**, **7 Tage**, **21 Tage**, **Radar**
- **Biowetter – Hinweis für Wetterfühlige** (Ansicht „Heute“, unter der stündlichen Vorschau): Ampel für die nächsten 4 Tage und Warnhinweise mit Zeitpunkt, Stärke (gering/mäßig/stark), betroffenen Beschwerden und Tipp. Erkannt werden: Luftdruckabfall und rascher Luftdruckanstieg (Änderung in 12 Std.), Temperatursturz/-anstieg zum Vortag, Schwüle (Taupunkt), Hitzebelastung und Kältereiz (gefühlte Temperatur), nasskaltes Wetter, große Tag-Nacht-Schwankung sowie Föhn-Verdacht im Alpenraum (Südwind, trockene Luft, Böen, fallender Luftdruck). In der 3-Tage-Ansicht steht pro Tag eine Kurzzeile. Abgeleitet aus der Open-Meteo-Vorhersage, kein medizinischer Rat.
- **Böen** überall mit Einheit und kleinem Windsack (hängt bei schwachen Böen, steht bei Sturm waagrecht; ab 40 km/h orange, ab 60 km/h rot) – auch je Tagesabschnitt in der 3-Tage-Ansicht.
- **Lebendiger Himmel** hinter dem aktuellen Wetter: Farbverlauf passend zu Tag, Morgen- und Abenddämmerung oder Nacht; klare Nacht mit funkelnden Sternen und dem Mond in der echten Mondphase; ziehende Wolken (bei Sturm schneller), Nebelschwaden, Regen (bei Wind schräg), Schnee, Gewitter mit Blitz. Die Schrift wechselt automatisch auf hell, wenn der Himmel dunkel ist; bei „Bewegung reduzieren“ stehen die Animationen still.
- **Wetter erklärt** (ⓘ-Knopf rechts unten in der aktuellen Wetterkarte): erklärt das augenblickliche Wetter – was es ist und wie es entsteht (z. B. Strahlungs- und Advektionsnebel, Quellwolken, Landregen, Schauer, Gewitter, Hagel, gefrierender Regen), dazu die Messwerte mit Deutung (Taupunkt-Abstand, Luftdruck und Tendenz, Windkühle/Schwüle), besondere Lagen (Inversion/Hochnebel, Glättegefahr, Föhn, rasch fallender Luftdruck), Verhaltenstipps und einen Ausblick auf die nächsten 12 Stunden.
- **Sprachausgabe** (Sprech-Knopf neben ⓘ in der aktuellen Wetterkarte): liest das heutige Wetter (aktuell, Tageswerte, Regen, Wind/Böen, deutliche Biowetter-Belastungen) und eine kurze Prognose für die nächsten drei Tage samt Temperaturtrend vor – auf Deutsch oder Englisch, in den eingestellten Einheiten. Nutzt die Sprachausgabe des Browsers (Web Speech API, ohne externen Dienst); nochmal antippen stoppt.
- **Amsel** (anfangs ausgeblendet, einblenden unter ⚙ Einstellungen → Amsel; wird gespeichert): fliegt über die Seite, setzt sich auf Balken, Knöpfe, Karten und Wolken, pickt, hüpft, schaut sich um und singt ihr Lied (Noten steigen auf). Antippen lässt sie sofort singen. Der Ton ist beim Aufruf eingeschaltet; Browser geben Ton aber oft erst nach der ersten Berührung der Seite frei – dann singt sie ab da. Lautsprecher-Knopf links unten schaltet den Gesang an/aus (wird gespeichert). Der Gesang ist in der HTML-Datei eingebettet, sie funktioniert also auch einzeln.
- **Hinweis für Allergiker**: Pollenflug von heute auf der Startseite; Wetter-Symbol eines Tages antippen zeigt die Pollenbelastung (Erle, Birke, Gräser, Beifuß, Ambrosia, Olive) für diesen Tag – Europa, ca. 3 Tage voraus
- **Klima-Cockpit (📊 neben dem Ortsnamen)**: historische Auswertung für den angezeigten Ort über 10, 30, 50 oder 85 Jahre (ab 1941) in drei Bereichen: **Klima** – Kennzahlen (Ø Jahrestemperatur und Erwärmung, Hitzetage, Rekorde, stärkste Böe, Niederschlag, Schnee) und Diagramme pro Jahr oder pro Monat: Temperatur (Ø Höchst-, Mittel-, Tiefstwert), Hitzetage (≥ 30 °C), Windspitzen, Niederschlag, Schnee; Tooltip beim Antippen, Tabellenansicht · **Kenntage**: Frost-, Eis-, Sommer- und Starkregentage, Tropennächte, Sturmtage, längste Trocken- und Hitzeperiode, letzter/erster Frost und frostfreie Zeit · **Haus & Garten**: Heizgradtage (G20/15), Niederschlag und Verdunstung, klimatische Wasserbilanz, Vegetationsperiode
- **Was ziehe ich an?** – Outfit-Vorschlag für jeden Tag als Modepuppe (Frau/Mann umschaltbar): berücksichtigt gefühlte Temperatur im Tagesverlauf, Regen, Schnee, Wind, UV sowie die Region (Höhenlage, Alpenraum mit Trachtenjanker, Küste mit Friesennerz, Süden)
- **Bauernregel des Tages**: halbtransparentes Symbol rechts unten öffnet einen augenzwinkernden Wetterspruch (78 Sprüche auf Deutsch und Englisch, passend zu Jahreszeit und Monat, jeder Tag ein anderer; Vortag/Folgetag durchblättern)
- **Niederschlagsradar**: in Deutschland automatisch das DWD-Radar (1 km), weltweit RainViewer – umschaltbar; animierte 2D-Karte (ca. letzte 2 Stunden + Kurzfrist-Prognose, falls verfügbar) mit Markierung der aktuellen Position, Zeitleiste und Play/Pause
- Darstellung angelehnt an klassische Wetterportale: Symbole, rote Höchst-/blaue Tiefstwerte, Temperaturkurven, Regenwahrscheinlichkeit

## Datenquellen (kostenlos & seriös)
| Zweck | Dienst |
|---|---|
| Vorhersage Tag 1–16 | [Open-Meteo](https://open-meteo.com) – Modelle u. a. DWD ICON, ECMWF, NOAA GFS |
| Trend Tag 17–21 | Open-Meteo Ensemble-API, NOAA GEFS (Mittel aus 31 Läufen) |
| Klima-Cockpit | Open-Meteo Historical Weather API (ERA5-Reanalyse, Tageswerte ab 1940) |
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
