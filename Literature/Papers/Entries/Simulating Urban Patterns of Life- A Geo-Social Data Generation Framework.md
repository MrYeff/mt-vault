---
title: "Simulating Urban Patterns of Life: A Geo-Social Data Generation Framework"
tags:
  - urban_simulation
  - synthetic_data
  - model
  - simulation
authors:
  - "[[Literature/Authors/Joon-Seok Kim|Joon-Seok Kim]]"
  - "[[Literature/Authors/Hamdi Kavak|Hamdi Kavak]]"
  - "[[Literature/Authors/Umar Manzoor|Umar Manzoor]]"
  - "[[Literature/Authors/Andrew Crooks|Andrew Crooks]]"
  - "[[Literature/Authors/Dieter Pfoser|Dieter Pfoser]]"
  - "[[Literature/Authors/Carola Wenk|Carola Wenk]]"
  - "[[Literature/Authors/Andreas Züfle|Andreas Züfle]]"
publication date: 2019-11
source: "https://par.nsf.gov/servlets/purl/10187146"
doi: 10.1145/3347146.3359106
read status: Todo
---

## Abstract

Data generators have been heavily used in creating massive trajectory datasets to address common challenges of real-world datasets, including privacy, cost of data collection, and data quality. However, such generators often overlook social and physiological characteristics of individuals and as such their results are often limited to simple movement patterns. To address these shortcomings, we propose an agent-based simulation framework that facilitates the development of behavioral models in which agents correspond to individuals that act based on personal preferences, goals, and needs within a realistic geographical environment. Researchers can use a drag-and-drop interface to design and control their own world including the geospatial and social (i.e. geo-social) properties. The framework is capable of generating and streaming very large data that captures the basic patterns of life in urban areas. Streaming data from the simulation can be accessed in real time through a dedicated API.

## Research Questions
> Research Questions extracted via LLM
- How can an agent-based framework generate large urban trajectory data while representing individual preferences, goals, needs, and geo-social context?[^r1]
- How can researchers configure a geographical world and stream generated data for downstream use?[^r1]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?
- A configurable geo-social data generator: modelers assemble trigger → behavior → action → goal components in a geographical environment.[^r3]
- These are component interfaces; action logic and competing-behavior priorities belong to the selected model.[^r3]

```yml
World:
  agents: [Agent]
  environment: GeoSocialEnvironment
  output: File | Stream

Agent:
  needs: [()]
  beliefs: [()]
  characteristics: [()]
  location: ()
  behaviors: [Behavior]

Behavior:
  trigger: ()
  actions: [Action]
  priority: ModelerDefinedOrder # no numeric priority scale specified

Action:
  steps: ()
  goal: () # action's termination condition

GeoSocialEnvironment: ()
```

### How does it work?
- A trigger responds to a change or event in an internal factor (need, belief, characteristic) or an external factor (environment or another individual). It initiates a behavior, which can contain multiple actions; each action can have one or more steps, emits an output, and continues until its explicit goal is met. An action output can feed the next action.[^r3]
- Agents may have competing behaviors. The modeler specifies their execution priority; the paper offers Maslow’s hierarchy only as one possible hypothesis and gives no universal priority rule or numeric scale.[^r3]
- Architecture has three parts: a shared library of function-block components; a drag-and-drop Model Builder whose encoder saves model files; and a Simulator whose decoder loads those files, instantiates agents, and writes check-ins, transactions, or meetings to a file or stream. The demonstration’s builder uses Java/JGraphX.[^r3][^r4]
- Demonstration only: the sample model has food and sleep triggers, eight listed properties (money, wage, workHour, buildings, homeLocation, workLocation, destination, currentLocation), and eating/sleeping/working/doNothing behaviors. Food need strength above 50 triggers restaurant choice, shortest-path travel, eating to the `untilFULL` goal (100% food level), and bill payment from money.[^r4]
- MASON/GeoMASON runs 10,000 agents on synthetic spatial data containing 14,181 road segments. The displayed daily routine (home around 6 a.m., rush hour around 7 a.m., work around 8:30 a.m., lunch at noon) is visual demonstration; the authors say trace-based empirical validation is possible, so screenshots alone do not establish empirical validity.[^r4]
- The stream reports agent ID, simulation timestamp and tick, current location and status; the implementation uses the ZeroMQ client library. The demonstration connects this stream to Zeppelin and Spark Streaming for analysis.[^r4]

### What can it answer?
- Generate and stream trajectories and associated geo-social events under user-defined behavior rules; explore a configurable model's mobility consequences.[^r4]

### Where does it apply?
- Urban data generation. The demonstration is highly stylized, and the conclusion describes a plausible pattern-of-life model as future work. The paper does not supply a universal restaurant-choice function or report completed empirical trace validation.[^r3][^r4]

## Metadata
### References

- [[Apple privacy policy]]
- [[JGraphX]]
- [[New York City Taxi and Limousine Commission trip record data]]
- [[An empirical test of a new theory of human needs]]
- [[A Framework for Generating Network-Based Moving Objects]]
- [[Agent-Based Modelling and Geographical Information Systems- A Practical Primer|Agent-Based Modelling and Geographical Information Systems: A Practical Primer]]
- [[Unique in the crowd- The privacy bounds of human mobility|Unique in the crowd: The privacy bounds of human mobility]]
- [[Intrinsic motivation and self-determination in human behavior]]
- [[Applying statistical debugging for enhanced trace validation of agent-based models]]
- [[Location-based social simulation]]
- [[Procedural city generation beyond game development]]
- [[Discovering spatio-temporal causal interactions in traffic data streams]]
- [[MASON- A multiagent simulation environment|MASON: A multiagent simulation environment]]
- [[The image of the city]]
- [[A theory of human motivation]]
- [[The achievement motive]]
- [[MNTG- An extensible web-based traffic generator|MNTG: An extensible web-based traffic generator]]
- [[Protecting user privacy- Obfuscating discriminative spatio-temporal footprints|Protecting user privacy: Obfuscating discriminative spatio-temporal footprints]]
- [[Generating semantics-based trajectories of moving objects]]
- [[SMARTS- Scalable microscopic adaptive road traffic simulator|SMARTS: Scalable microscopic adaptive road traffic simulator]]
- [[Predicting disease transmission from geo-tagged micro-blog data]]
- [[GeoMASON- Geospatial support for MASON|GeoMASON: Geospatial support for MASON]]
- [[Constructing popular routes from uncertain trajectories]]
- [[Destination prediction by sub-trajectory synthesis and privacy protection against such prediction]]
- [[T-Drive- Driving directions based on taxi trajectories|T-Drive: Driving directions based on taxi trajectories]]
- [[Where to find my next passenger]]

## Audit Log
- 2026-10-03: Independent full-source re-audit passed. Full four-page primary paper, demonstration rules and 26 references checked; filename-safe target changes independently rechecked and demonstration separated from empirical validation. `audit failed` removed after the pass.
- Audit invalidated (2026-09-30): auditor admitted clearing flags before completing independent source checks. A new independent audit is required.
- Strong source review (2026-09-30): Verified NSF full paper is four pages; retained all 26 ordered bibliography links and clarified component interfaces, goal ownership and demonstration scope. Independent re-audit pending.
- Initial independent audit: failed on missing model mechanisms, abstract fidelity, or source-access reporting; see `vault/.automation/audit/next-forty-54-66-initial-2026-09-30.json`. Revisions added source-located model detail; independent re-audit remains pending.
- 2026-09-30: Added all 26 bibliography entries in source order from the NSF Public Access Repository copy (printed pp. 3–4; references [1]–[26]). The original captured import had no bibliography metadata. Corrected malformed YAML tags into separate `model` and `simulation` list items; audit remains pending.

- WITHDRAWN audit claim (2026-09-30): previously reported PASS; source claims, current extraction, metadata, references and footnotes checked against the available primary source. See `vault/.automation/audit/remaining-audit-b-2026-09-30.json`.

## LLM Justification
[^r1]: https://par.nsf.gov/servlets/purl/10187146; abstract, which states the framework purpose, researcher-configurable geo-social world, and streaming outputs.
[^r3]: Kim et al., §2 “Concepts and Architecture,” pp. 2–3: trigger/behavior/action/goal definitions; modeler-selected priorities; Fig. 2 and builder/library/simulator descriptions. Full four-page paper: https://par.nsf.gov/servlets/purl/10187146.
[^r4]: Kim et al., §3 “Demonstration,” pp. 3–4: HUNGRY example, MASON/GeoMASON, agent and road counts, file/stream interfaces; §4: future development of a plausible pattern-of-life model. Full paper: https://par.nsf.gov/servlets/purl/10187146.
