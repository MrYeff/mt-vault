Social Media Platformen bilden ein zentrales Element Sozialer und Informations Infrastruktur. Wärend kleinere Message boards damit auskommen alle bestehenden Inhalte als liste zu präsentieren, verlangen größere Platformen Algorithmen zur priorisierung der den Nutzern angezeigten Informationen. Im Bereich dieser Algorithmen - Gennant recomender Algorithmen - gibt es signifikante unterschiede , basierend darauf welche Inhalte (z.b. Nutzer, Videos, ...) verwaltet werden und nach welchen kritierien sie vorgeschlagen werden (z.b. Gemeinsamkeiten, Frühere Annahme-Rate, ...). 
In dieser Arbeit soll es um das Vorschlagen von Gruppen anhand geteilter Kriteria der potenziellen Gruppenteilnehmer gehen. Insbesondere wird untersucht, ob Nutzer Gruppenvorschläge mit wenigen seltenen gemeinsamen Eigenschaft gegenüber Vorschlägen mit mehreren aber häufigeren Gemeinsamkeiten bevorzugen. 
Um dies  Frage zu beantworten werden zwei Gruppen-Vorschlags-Algorithmen implementier und getestet in einer Umfrage. Die Umfrage beinhaltet zwei Phasen.
Phase 1 besteht aus der Erfassung der Eigenschaften der Probanden. In Phase 2 werden Vorschläge der obrigen Algorithmen auf Basis des in Phase 1 erfassten Korpuses entgegengestelt und durch die Probanden bewertet.
Auf Basis der gesammelten Datenpunkte soll bestimmt werden unter welchen Umständen die Empfehlung welcher Algorithmen bevorzugt wird.

## Notes

1. **Problem bestimmen:**  Bei der Bildung interessenbasierter Freizeitgruppen ist unklar, ob Gruppen mit einer selten auftretenden Gemeinsamkeit oder Gruppen mit mehreren aber häufiger auftretenden Gemeinsamkeiten von Nutzern beforzugt werden. Diese Entscheidung bestimmt, welche Gruppen ein Matchingverfahren vorschlägt. Ihre Untersuchung soll eine empirische Grundlage für die Gewichtung gemeinsamer Interessen schaffen.
2. **Ziele festlegen:** Gruppenvorschläge erzeugen, denen Nutzer eher beitreten möchten.
3. **Lösung entwickeln:** Zwei Matchingvarianten entwickeln: Eine gewichtet seltene Gemeinsamkeiten stärker, die andere mehrere häufigere Gemeinsamkeiten.
4. **Anwendung demonstrieren:** Mit erhobenen Interessenprofilen konkrete Gruppenvorschläge für die Teilnehmenden erzeugen.
5. **Evaluieren:** Teilnehmende wählen zwischen Vorschlägen beider Varianten oder lehnen beide ab. Auswahlanteile und Entscheidungsgründe vergleichen.
6. **Erkenntnisse vermitteln:** Beschreiben, welche Gewichtungsstrategie im untersuchten Kontext bevorzugte Vorschläge erzeugt und welche Grenzen die Übertragung auf andere Kontexte hat.