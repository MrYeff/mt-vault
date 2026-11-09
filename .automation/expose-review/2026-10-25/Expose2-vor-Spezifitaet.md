# Exposé – Stichpunkte

Quelle: `documents/Vorlage – Exposé für Abschlussarbeiten.odt`, Stand 25.10.2026. Inhaltliche Extraktion, keine methodische Überarbeitung. Anleitungstexte der Vorlage stehen separat am Ende.

## Stammdaten

- **Titel**: Seltene Gemeinsamkeiten im Gruppenmatching: Entwicklung und empirische Evaluation zweier **Gewichtungsstrategien**.
- **Art**: Masterarbeit.
- **Verfasser**: Maximilian, Arnold.
- **Studiengang**: Informatik.
- **Beginn**: **01.11.2026**.
- **Sprache**: Deutsch.

## 1. Ausgangssituation und Problemstellung

- **Ausgangspunkt:** *App-Idee* zur Zusammenstellung von *Freizeitgruppen* anhand gemeinsamer Interessen und weiterer *Profilmerkmale*.
- **Gestaltungsproblem**: **Gewichtung** unterschiedlicher Kombinationen gemeinsamer Merkmale.
- **Bei gleicher Gemeinsamkeitenzahl und ähnlicher Gruppenstärke sind unterschiedliche Kombinationen möglich**: eine besonders seltene und ansonsten häufige Gemeinsamkeiten oder mehrere weniger seltene Gemeinsamkeiten.
- **Vélez et al. (2019):** Personen mit einer **seltenen gemeinsamen Präferenz** wurden als potenzielle Gesprächspartner gegenüber Personen mit einer häufigen gemeinsamen Präferenz bevorzugt.
- **Dortige Seltenheitsvergleiche**: **eine beschriebene Präferenz** je potenziellem Partner.
- **Dort nicht untersucht**: Kombinationen unterschiedlich seltener Gemeinsamkeiten und Gruppenauswahl.
- **De Meo et al. (2017)**: Gruppenbildung anhand von **Ähnlichkeit und Vertrauen**.
- **Valcarce et al. (2018)**: Gruppenbildung anhand von **Aktivitätsinteressen und bestehenden Beziehungen**.
- Auch diese Gruppenbildungsansätze **beantworten den vorgesehenen Vergleich nicht**.
- **Ziel**: **Empirische Grundlage** für die bevorzugte Berücksichtigung unterschiedlicher Merkmalskombinationen bei **Freizeitgruppen**.

## 2. Forschungsfrage(n)

- ***TODO aus der Quelle: Selten → Spezifisch.***
- **Hauptfrage**: Werden Gruppenvorschläge mit einer **stark gewichteten seltenen Gemeinsamkeit** oder mit **gleichmäßig gewichteten weniger seltenen Gemeinsamkeiten** bevorzugt?
- **Vergleichsbedingungen**: gleichbleibende Gesamtzahl der Gemeinsamkeiten und vergleichbare Gruppenstärke.
- **Zusatzfrage**: Wird die **besonders seltene Gemeinsamkeit** meistens als **ausschlaggebendes Auswahlkriterium** benannt?
- **Ziel**: Grundlage für einen später um weitere Informationen erweiterten Gruppenmatchingalgorithmus.

## 3. Methodisches Vorgehen

### Ansatz und Verfahrensvarianten

- **Design-Science-Ansatz** nach Peffers et al. (2007).
- **Artefakt**: zwei Varianten eines Gruppenmatchingverfahrens.
- Eine Variante priorisiert eine **besonders seltene Gemeinsamkeit**, auch bei ansonsten häufigen Gemeinsamkeiten.
- Die andere Variante priorisiert **mehrere vergleichsweise seltene Gemeinsamkeiten**.
- **Gemeinsamkeit**: Merkmal **aller Gruppenmitglieder einschließlich der befragten Person**.
- **Gleiche Gruppengröße** und **gleiche Anzahl** verglichener Gemeinsamkeiten.
- **Evaluation**: **Teilnahmepräferenzen** potenzieller Nutzer in einer **zweistufigen Umfrage**.
- **Ziel**: empirisch begründete Entscheidung über die **Gewichtung** unterschiedlich seltener Gemeinsamkeiten.

### Entwicklung und Vorprüfung

- Literatur begründet benötigte **Profilmerkmale**, geeignete **Gruppengröße** und Gestaltung der Varianten.
- Gemeinsame **Thementaxonomie** zur vergleichbaren Erfassung von Interessen.
- Gleiche **Rahmenbedingungen** und Parameter für Zielgruppengröße und **Themenkategorien**.
- Beide Varianten implementieren und mit **synthetischen Profilen** technisch prüfen.
- Insbesondere prüfen, ob sie „**signifikant unterschiedliche Gruppenvorschläge**“ erzeugen.
- **Kleiner Probelauf mit Personen**: **Verständlichkeit** von Darstellung und Fragebogen prüfen.
- Erkannte Probleme **vor der Hauptstudie** beheben.

### Phase 1: Profile und Teilnehmerpool

- Interessen und weitere benötigte **Profilmerkmale** erheben.
- **Rekrutierung** über Hochschulgruppen, persönliche Kontakte und Weiterleitung des Umfragelinks, auch außerhalb der Hochschule.
- Teilnahme **nicht auf Studierende beschränkt**.
- Zusammensetzung der **selbstselektierten Stichprobe** dokumentieren und bei der Interpretation berücksichtigen.
- **Stichprobenumfang** richtet sich nach verfügbaren Rekrutierungsmöglichkeiten.
- **Seltenheit** anhand der **Merkmalsfrequenzen** im erhobenen Teilnehmerpool bestimmen.
- **Vor Phase 2** prüfen, für wie viele Teilnehmende beide Varianten unterschiedliche Vorschläge unter den festgelegten Bedingungen erzeugen.
- Bei **unzureichender Abdeckung** zusätzliche **synthetische Profile** anhand der ursprünglichen Stichprobe erzeugen.
- **Vorgabe für die Synthese**: **Themenverteilung** annähernd erhalten und Probandenprofile **nicht exakt replizieren**.
- **Damit laut Entwurf beabsichtigt**: **Seltenheit** und vorhandene **Teilnehmerzahlen pro Merkmalskombination** nicht verfälschen.
- Beide Varianten verwenden **denselben Teilnehmerpool**, gleiche **Gruppengröße** und **gleiche Anzahl** gemeinsamer Merkmale.

### Phase 2: Vorschläge bewerten

- **Vorschlagspaare** beider Varianten bewerten lassen.
- **Bevorzugte Gruppe** wählen oder **beide ablehnen**.
- Besonders **entscheidungsrelevante Merkmale** angeben.
- **Einheitliche Darstellung**, **zufällige Position** und **verborgene Algorithmuszuordnung**.

### Auswertung und Aussagegrenzen

- Auswahlentscheidungen **quantitativ** auswerten.
- **Mehrere Antworten derselben Person** berücksichtigen.
- Angegebene **Entscheidungsgründe** ergänzend untersuchen.
- Ergebnisse mit dem **Forschungsstand** vergleichen und **Gestaltungsempfehlungen** ableiten.
- Erfasst werden geäußerte **Teilnahmepräferenzen**, **keine tatsächliche Teilnahme** oder spätere **Bindungsentstehung**.

## 4. Erwarteter Mehrwert

- **Wissenschaftlich**: empirischer Vergleich zweier **Gewichtungsstrategien** für gemeinsame Merkmale bei Gruppenempfehlungen.
- **Anschluss an Vélez et al. (2019)**: von seltenen gemeinsamen Präferenzen zur Gruppenauswahl anhand mehrerer unterschiedlich seltener Gemeinsamkeiten.
- Bevorzugte Vorschläge und **selbstberichtete** ausschlaggebende Merkmale identifizieren.
- **Praktische Zielgruppe**: **Entwickler und Betreiber** von Angeboten zur Vermittlung von **Freizeitgruppen**.
- **Praktischer Nutzen**: **Entscheidungshilfe** für die **Gewichtung** gemeinsamer Merkmale.
- Implementierte Varianten als Grundlage für **weitere Auswahlkriterien**.
- Aussagen gelten für die **untersuchte Stichprobe** und geäußerte **Teilnahmepräferenzen**.
- **Kein Nachweis** höherer tatsächlicher Teilnahme oder erfolgreicherer **Bindungsentstehung**.

## 5. Tabellarische Meilensteinplanung

- **01.11.2026**: Bearbeitungsbeginn.
- **01.12.2026**: Umfrage vorbereitet – Umfrage, Algorithmen und Grundliteratur.
- **01.01.2027**: Beide Umfragephasen abgeschlossen.
- **01.02.2027**: Auswertung abgeschlossen.
- **01.03.2027**: Korrekturlesen und Finalisierung der Abschlussarbeit.
- **14.03.2027**: Abgabe.

## Erklärung zur Nutzung generativer KI

- **OpenAI Codex** unterstützt **Literaturrecherche**, **Schärfung der Forschungsfrage** und **Diskussion der Methodik**.
- **Weitere Nutzung**: **Erstellung und Überarbeitung** einzelner Textabschnitte sowie **kritische Prüfung** des Entwurfs.
- Vorgeschlagene Inhalte wurden laut Erklärung **geprüft und überarbeitet**.

## Literaturverzeichnis

- De Meo, P., Messina, F., Rosaci, D., & Sarné, G. M. L. (2017). Forming time-stable homogeneous groups into online social networks. *Information Sciences, 414*, 117–132. https://doi.org/10.1016/j.ins.2017.05.048
- Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. *Journal of Management Information Systems, 24*(3), 45–77. https://doi.org/10.2753/MIS0742-1222240302
- Valcarce, D., Brilhante, I., Macedo, J. A., Nardini, F. M., Perego, R., & Renso, C. (2018). Item-driven group formation. *Online Social Networks and Media, 8*, 17–31. https://doi.org/10.1016/j.osnem.2018.10.002
- **Vélez, N., Bridgers, S., & Gweon, H. (2019). The rare preference effect**: Statistical information influences social affiliation judgments. *Cognition, 192*, Article 103994. https://doi.org/10.1016/j.cognition.2019.06.006

## Vorgaben der Vorlage – getrennt vom eigenen Text

- **Allgemein**: **drei bis fünf Seiten** einschließlich Literaturverzeichnis; Anleitungstexte und Platzhalter ersetzen; nur tatsächlich zitierte Quellen übernehmen.
- **Kapitel 1**: Ausgangssituation und zu lösendes Problem beziehungsweise Beitrag zur Problemlösung beschreiben.
- **Kapitel 2**: möglichst **eine, bei Bedarf zwei** klare Forschungsfragen; Bezug zur Problemlösung erklären und Arbeit daran ausrichten.
- **Kapitel 3**: **Methodenwahl** und wesentliche Schritte erläutern und begründen; etablierte Vorgehensmodelle und methodische Leitlinien nutzen (Recker, 2021).
- **Genannte Methodenoptionen**: Design Science (Gregor & Hevner, 2013; Hevner et al., 2004; Peffers et al., 2007), qualitative empirische Forschung (Myers, 1997), quantitative empirische Forschung, etwa Umfragen (Pinsonneault & Kraemer, 1993), systematische Literaturanalysen (vom Brocke et al., 2009, 2015; Webster & Watson, 2002).
- **Kapitel 4**: **wissenschaftlichen und praktischen Mehrwert**, Anschluss und Erweiterung des Forschungsstands sowie konkrete Nutznießer und Nutzen benennen.
- **Kapitel 5**: wesentliche **Meilensteine** mit realistischen Terminen; Übereinstimmung mit Methodik; ausreichend Zeit für Korrekturlesen und Finalisierung.
- **KI-Erklärung**: Nutzung, Systeme, Aufgaben und Umfang offenlegen.
- **Literatur**: **APA 7**; Zotero empfohlen; Aufbau anhand der Beispiele und Zitationen im Methodikabschnitt.
