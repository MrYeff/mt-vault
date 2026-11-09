# Matching über seltene Gemeinsamkeiten

Ausgangspunkt: [[2026-10-16]]. Exposé-Entwurf; Forschungsstand geprüft am 17.10.2026.

- **Ausgangssituation und Problemstellung**
  - Seltene gemeinsame Interessen erhöhen in Experimenten die zwischenmenschliche Attraktivität und die Bereitschaft zur Interaktion.[^alves][^velez]
  - Daraus folgt nicht, dass ein Matching nach seltenen Interessen insgesamt mehr dauerhafte Beziehungen erzeugt: Geeignete Partner sind seltener; Zeit und Beziehungskapazität sind begrenzt.
  - Zu untersuchen ist der Zielkonflikt zwischen höherer Attraktivität einzelner Vorschläge und der Versorgung aller Nutzer mit passenden Kontakten.
- **Forschungsfrage**
  - Unter welchen Bedingungen erzeugt Matching nach seltenen gemeinsamen Interessen mehr dauerhafte, gegenseitige Beziehungen als Matching nach der Anzahl gemeinsamer Interessen?
- **Methodik**
  - Agentenbasiertes Modell einer begrenzten Nutzerpopulation mit Interessen, beobachtbaren Profilen und begrenzter Kontaktzeit.
  - Drei Matching-Regeln: zufällige Vorschläge; Anzahl gemeinsamer Interessen; nach Seltenheit gewichtete Gemeinsamkeiten.
  - Gleiche Ausgangspopulation, gleiche Vorschlagszahl und gleicher Zeitrahmen für alle Regeln; Annahme und Ablehnung durch beide Seiten möglich.
  - Seltenheit für den Algorithmus aus der Population berechnen; wahrgenommene Seltenheit für Agenten getrennt modellieren.
  - Kontaktbildung und Beziehungserhalt als getrennte Prozesse; einen Kontakt erst nach wiederholten gegenseitigen Interaktionen als dauerhafte Beziehung zählen.
  - Stärke des Seltenheitseffekts, Interessenhäufigkeiten, Profilvollständigkeit und Kontaktkapazität variieren; auch ohne Seltenheitseffekt rechnen.
  - Messen: dauerhafte Beziehungen pro Agent, Anteil ohne Beziehung, Beziehungsdauer und Konzentration der Kontakte auf wenige Agenten.
  - Mehrere Zufallsstarts und Unsicherheitsintervalle; Regeln zunächst an den experimentellen Befunden prüfen. Langfristige Beziehungen bleiben ohne passende Verlaufsdaten eine Modellannahme.
- **Mehrwert für Forschung und Praxis**
  - Forschung: Bedingungen bestimmen, unter denen ein bekannter Effekt auf Personenebene einen Vorteil für das gesamte Netzwerk ergibt oder verfehlt.
  - Praxis: Vergleich einer leicht nachvollziehbaren Matching-Regel mit einfachen Alternativen; Nachteile für schwer vermittelbare Nutzer sichtbar machen.
  - Aussagegrenze: bedingte Simulationsergebnisse, kein Nachweis tatsächlicher Freundschaftsbildung durch eine App.

**Forschungsstand / Abgrenzung**

- Grundlage: gezielte Suche nach empirischen Seltenheitseffekten, Matching-Verfahren und Netzwerkmodellen; keine vollständige systematische Literaturübersicht. Literaturbefunde und vorgeschlagene Modellregeln sind getrennt dargestellt.
- **Grundeffekt bereits direkt erforscht:** Die Frage „Wirken seltene Gemeinsamkeiten anziehender?“ ist als alleiniger Beitrag zu schwach.[^alves][^velez]
- **Auch die algorithmische Gewichtung ist keine sichere Neuheit:** Ein aktuelles Reisepartner-Matching berücksichtigt bereits seltene Interessen.[^matching]
- **Tragfähigerer Fokus:** langfristiger Vergleich der Netzwerkfolgen unter knapper Kontaktzeit und ungleicher Verteilung von Interessen. Dass genau dieser Vergleich noch fehlt, ist vor einer Neuheitsbehauptung weiter zu prüfen.
- **Wichtig:** Ein eingebauter Seltenheitsbonus darf nicht als Ergebnis „entdeckt“ werden. Das Ergebnis ist, ob sein Vorteil unter Kapazitätsgrenzen, Konkurrenz und Beziehungserhalt bestehen bleibt.

**Literatur**

[^alves]: Alves (2018), [Sharing Rare Attitudes Attracts](https://doi.org/10.1177/0146167218766861). Fünf Studien zu seltenen gemeinsamen Interessen und Attraktivität; kein Langzeittest eines Freundschaftsnetzwerks.
[^velez]: Vélez, Bridgers & Gweon (2019), [The rare preference effect: Statistical information influences social affiliation judgments](https://doi.org/10.1016/j.cognition.2019.06.006). Experimentelle Befunde zu Seltenheit, gemeinsamem Wissen und Interaktionsentscheidungen; [Volltext](https://sll.stanford.edu/docs/2019_Velez_Bridgers_Gweon_Cognition.pdf).
[^matching]: [A Safety-Enhanced and Trust-Aware Recommendation Framework for Travel Companion Matching](https://www.mdpi.com/2078-2489/17/5/406) (2026). Nahe algorithmische Vorarbeit: Seltenheitsgewichtung im Reisepartner-Matching. Für die Abgrenzung berücksichtigt; keine Gleichsetzung mit langfristiger Freundschaftsbildung.
