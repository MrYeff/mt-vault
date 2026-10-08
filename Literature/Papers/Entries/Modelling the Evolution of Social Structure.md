---
title: "Modelling the Evolution of Social Structure"
authors:
  - "[[Literature/Authors/Alistair Sutcliffe|Alistair Sutcliffe]]"
  - "[[Literature/Authors/Robin Dunbar|Robin Dunbar]]"
  - "[[Literature/Authors/D. Wang|D. Wang]]"
source: "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0158605"
doi: "10.1371/journal.pone.0158605"
publication date: "2016-07-18"
tags:
  - "model"
  - "simulation"
  - "social_structure"
read status: Todo
---

## Abstract

Although simple social structures are more common in animal societies, some taxa (mainly mammals) have complex, multi-level social systems, in which the levels reflect differential association. We develop a simulation model to explore the conditions under which multi-level social systems of this kind evolve. Our model focuses on the evolutionary trade-offs between foraging and social interaction, and explores the impact of alternative strategies for distributing social interaction, with fitness criteria for wellbeing, alliance formation, risk, stress and access to food resources that reward social strategies differentially. The results suggest that multi-level social structures characterised by a few strong relationships, more medium ties and large numbers of weak ties emerge only in a small part of the overall fitness landscape, namely where there are significant fitness benefits from wellbeing and alliance formation and there are high levels of social interaction. In contrast, ‘favour-the-few’ strategies are more competitive under a wide range of fitness conditions, including those producing homogeneous, single-level societies of the kind found in many birds and mammals. The simulations suggest that the development of complex, multi-level social structures of the kind found in many primates (including humans) depends on a capacity for high investment in social time, preferential social interaction strategies, high mortality risk and/or differential reproduction. These conditions are characteristic of only a few mammalian taxa.

## Research Questions
> Research Questions extracted via LLM

- Under which fitness conditions do multi-level social systems emerge?[^r1]
- How do alternative strategies for allocating social time compare across generations?[^r1]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?
- Social ties emerge from repeated cooperative interaction; evolutionary selection rewards trade-offs between foraging, relationship benefits, risk, and stress.[^e1]

### How does it work?
- Each cycle gives every agent a turn: forage according to its forage:social propensity, or choose a partner. Initial partner choice is random; later choices use remembered directed trust.[^e2]
- FtF favors strong ties, FtW weak ties, FtM middle ties; Staged progressively shifts from strong toward weak ties. New partners remain possible. For `n` existing ties in descending trust order with total `T`, FtF uses `p_j=t_j/T`, FtW uses `p_j=t_(n-j+1)/T`; select a new partner with probability `1-n/P`, otherwise apply the existing-tie rule. Staged uses `p_j=(t_j-(t_j-t_(n-j+1))/RC)/T`, with `RC` remaining cycles. The FtM formula/prose conflict is recorded below.[^e3]
- Cooperation adds `MAX_COMPRESSION-CI*trust`; rejection subtracts it, with `CI=(MAX_COMPRESSION-MIN_COMPRESSION)/MAX_TRUST`. Appendix Eq. (7) waning is `next=max(0,trust-MIN_WANING*(1+WANING_RATE-previous_trust/MAX_TRUST))`. `MIN_WANING` is an input without a reported value; the equation explicitly uses lagged `previous_trust`.[^e2]

The appendix's named objective functions expose the fitness mechanism; `mean_trust`, `ties`, `incoming`, `outgoing`, and `forage_turns` refer to an agent's lifetime history.[^e4]

```
AGENTS = 300
CYCLES_PER_GENERATION = 2000
GENERATIONS = 50
REPLACEMENT_SHARE = 0.20
ALLIANCE_COEFFICIENT = 0.05
RISK_COEFFICIENT = 0.005
MAX_TRUST = 100
MAX_COMPRESSION = 10
MIN_COMPRESSION = 0
WANING_RATE = 0.08
INITIAL_FORAGE_SOCIAL_RATIO = 1:8
REJECTION_RATE_RANGE = 0..10%
FITNESS_WEIGHT_RANGE = 1..5 # 1..10 in N=500 sensitivity run
FITNESS_LANDSCAPE_RUNS = 3125

objectives(
  agent: Agent
):
  wellbeing = mean_trust * incoming/outgoing
  resource = forage_turns * ties
  alliance = mean_trust * ALLIANCE_COEFFICIENT * ties
  risk = mean_trust / (RISK_COEFFICIENT*(incoming+outgoing))
  stress = ties
  out = (wellbeing, resource, alliance, risk, stress)
```

- Rank-normalize each criterion across agents, apply run-specific weights, sum wellbeing/resource/alliance and subtract risk/stress. Replace the bottom `REPLACEMENT_SHARE` with offspring of the top share; inherit social strategy, without inheriting relationships. The experiments vary weights from 1 to 5, strategies, foraging/social propensity and rejection.[^e1][^e4]
- Source conflicts: main text labels resource `RS` and risk `R`, then writes `(R+WB+AL)-(RS+ST)`; appendix calls resource `R` and risk `RS`. Main prose calls stress a decreasing function of ties, but appendix defines `ST=ties`, a rising cost. Risk prose says more interactions raise risk, but its appendix ratio decreases with interaction count at fixed trust. These contradictions remain unresolved.[^e5]
- Appendix FtM formulas apply direct trust weights to the top half and reversed weights to the bottom half; the next page's prose says the reverse. The waning section's Eq. (7) depends on lagged trust, while the parameter summary calls decrease linear/8% per cycle. These additional conflicts require an explicit implementation choice.[^e7]
- The parameter summary reports an initial forage:social ratio of 1:8 for its baseline configuration. The separate strategy-competition design tests 8:1, 5:1, 4:1 and 1:1; these are distinct experiment settings, not a source contradiction. That design also tests selection rates of 5%, 10% and 20%, with forage:social and rejection ratios mutated by ±1.[^e9]
- Initial fitness-landscape results: all 3,125 combinations of five criterion weights (1–5) were clustered with k-means (k=1..7). The reported outcomes were approximately 80% small-core, 14% no-layers, 5% large-core and 1% structure-compliant; the structure-compliant pattern averaged about 5 strong, 9 medium and 133 weak ties (total network size 147).[^e8]
- In the strategy-competition and sensitivity experiments, outputs include surviving strategy frequencies by generation, final mean tie strength, and forage:social and cooperate:reject ratios. FtF and Staged often spread, and structure-compliant outcomes remained sensitive to fitness weights, population size and selection rate.[^e8]
- The extraction leaves zero-denominator handling unspecified for `incoming/outgoing` and `incoming+outgoing`; the source gives no fallback rule. Mutation details are summarized above. Trust and search equations are transcribed from the appendix; only the explicitly conflicting definitions remain unresolved.[^e2][^e3][^e4]

### What can it answer?
- It tests which preference strategies and fitness regimes yield many weak ties plus small stronger layers, and which strategies survive evolutionary competition.[^e6]

### Where does it apply?
- It is a functional model of animal/human social organization; it does not specify physiological or psychological mechanisms underlying relationships.[^e6]

## Metadata
### References
- [[Community structure in social and biological networks]]
- [[Natural and sexual selection and the evolution of multi-level societies- insights from zebras with comparisons to primates|Natural and sexual selection and the evolution of multi-level societies: insights from zebras with comparisons to primates]]
- [[Network scaling reveals consistent fractal pattern in hierarchical mammalian societies]]
- [[Evolutionary determinants of modular societies in colobines]]
- [[The ‘F’-word in primatology]]
- [[Bondedness and sociality]]
- [[Encephalisation is not a universal macroevolutionary phenomenon in mammals but is associated with sociality]]
- [[Close social associations in animals and humans- functions and mechanisms of friendship|Close social associations in animals and humans: functions and mechanisms of friendship]]
- [[The strength of weak ties]]
- [[Reproductive Decisions- An Economic Analysis of Gelada Baboon Social Strategies|Reproductive Decisions: An Economic Analysis of Gelada Baboon Social Strategies]]
- [[The costs of family and friends- an 18-month longitudinal study of relationship maintenance and decay|The costs of family and friends: an 18-month longitudinal study of relationship maintenance and decay]]
- [[Managing relationship decay- network, gender and contextual effects|Managing relationship decay: network, gender and contextual effects]]
- [[Strategic use of allopreening in family-living wrens]]
- [[Time as a limited resource- communication strategy in mobile phone networks|Time as a limited resource: communication strategy in mobile phone networks]]
- [[Limited communication capacity unveils strategies for human interaction]]
- [[The persistence of social signatures in human communication]]
- [[Neocortex size and social network size in primates]]
- [[Living in Groups]]
- [[Relationships and the social brain- integrating psychological and evolutionary perspectives|Relationships and the social brain: integrating psychological and evolutionary perspectives]]
- [[Determinants and evolutionary consequences of dominance among female gelada baboons]]
- [[Social stressors and coping mechanisms in wild female baboons (Papio hamadryas ursinus)]]
- [[Social bonds of female baboons enhance infant survival]]
- [[The benefits of social capital- Close social bonds among female baboons enhance offspring survival|The benefits of social capital: Close social bonds among female baboons enhance offspring survival]]
- [[Strong and consistent social bonds enhance the longevity of female baboons]]
- [[Why are diurnal primates living in groups-|Why are diurnal primates living in groups?]]
- [[Primate Social Systems]]
- [[A community-level evaluation of the impact of prey behavioural and ecological characteristics on predator diet composition]]
- [[Predator diet choices are associated with prey life history and behavioural characteristics in terrestrial mammal communities]]
- [[Deacon’s dilemma- the problem of pairbonding in human evolution|Deacon’s dilemma: the problem of pairbonding in human evolution]]
- [[Unravelling the evolutionary function of communities]]
- [[Discrete hierarchical organization of social group sizes]]
- [[The complex structure of hunter-gatherer social networks]]
- [[The structure of online social networks mirrors those in the offline world]]
- [[Do online social media cut through the constraints that limit the size of offline social networks-|Do online social media cut through the constraints that limit the size of offline social networks?]]
- [[Social network size in humans]]
- [[Social networks, support cliques, and kinship]]
- [[Perspective-taking and social network size in humans]]
- [[Human sympathy groups]]
- [[Economic action and social structure- The problem of embeddedness|Economic action and social structure: The problem of embeddedness]]
- [[The day-to-day functioning of close versus casual friendships]]
- [[Different strokes from different folks- Community ties and social support|Different strokes from different folks: Community ties and social support]]
- [[The need to belong- Desire for interpersonal attachments as a fundamental human motivation|The need to belong: Desire for interpersonal attachments as a fundamental human motivation]]
- [[Social isolation in America- Changes in core discussion networks over two decades|Social isolation in America: Changes in core discussion networks over two decades]]
- [[Selective investment theory- Recasting the functional significance of close relationships|Selective investment theory: Recasting the functional significance of close relationships]]
- [[Evolutionary significance of the role of family units in a broader social system]]
- [[Social networks in primates- smart and tolerant species have more efficient networks|Social networks in primates: smart and tolerant species have more efficient networks]]
- [[Focused grooming networks and stress alleviation in wild female baboons]]
- [[The spread of obesity in a large social network over 32 years]]
- [[Dynamic spread of happiness in a large social network- longitudinal analysis over 20 years in the Framingham Heart Study|Dynamic spread of happiness in a large social network: longitudinal analysis over 20 years in the Framingham Heart Study]]
- [[Social networks and health]]
- [[Social network determinants of depression]]
- [[Motivation losses in small groups- a social dilemma analysis|Motivation losses in small groups: a social dilemma analysis]]
- [[Extraverts have larger social network layers but do not feel emotionally closer to individuals at any layer]]
- [[Time as an ecological constraint]]
- [[Cooperation, behavioural synchrony and status in social networks]]
- [[Connected lives- the project|Connected lives: the project]]
- [[Computational modelling of trust and social relationships]]
- [[Mortality in traditional hunter-gatherer, pastoralist and agriculturalist communities- the validity of longevity studies based on mobility and subsistence strategies|Mortality in traditional hunter-gatherer, pastoralist and agriculturalist communities: the validity of longevity studies based on mobility and subsistence strategies]]
- [[Evolution of indirect reciprocity by image scoring]]
- [[Evolution of indirect reciprocity]]
- [[The development of cooperative relationships- an experiment|The development of cooperative relationships: an experiment]]
- [[Uncertainty, trust and commitment formation in the United States and Japan]]
- [[Evolutionary game theory meets social science- is there a unifying rule for human cooperation|Evolutionary game theory meets social science: is there a unifying rule for human cooperation]]
- [[Friendship maintenance- An analysis of individual and dyad behaviours|Friendship maintenance: An analysis of individual and dyad behaviours]]
- [[Nice guys finish first- The competitive altruism hypothesis|Nice guys finish first: The competitive altruism hypothesis]]
- [[On the aims and methods of Ethology]]
- [[The socioecology of elephants- analysis of the processes creating multitiered social structures|The socioecology of elephants: analysis of the processes creating multitiered social structures]]
- [[Attitudes and cognitive organization]]
- [[Friendship, cliquishness, and the emergence of cooperation]]
- [[Predation risk as an influence on group size in cercopithecoid primates- implications for social structure|Predation risk as an influence on group size in cercopithecoid primates: implications for social structure]]
- [[The evolution of female social relationships in nonhuman primates]]
- [[Infanticide risk and the evolution of male-female association in primates]]
- [[Stepwise evolution of stable sociality in primates]]
- [[An evaluation of the roles of predation rate and predation risk as selective pressures on primate grouping behaviour]]
- [[Infanticide still drives primate monogamy]]
- [[Social suppression of reproduction in subordinate talapoin monkeys, Miopithecus talapoin]]
- [[Habitat quality, population dynamics and group composition in colobus monkeys (Colobus guereza)]]
- [[Ecological determinants of birth intervals baboons]]

## Audit Log
- 2026-10-03: Independent full-source re-audit passed. Full primary article, S1 appendix and 78 references checked; embedded trust/search equations independently read visually, with an additional focused review. Source conflicts and missing values remain explicit. `audit failed` removed after the pass.
- 2026-10-03: Rebuilt Metadata/References from the complete publisher bibliography: 78 numbered PLOS references now appear in source order as title-bearing links. Removed all six opaque targets and surplus imported entries outside the publisher bibliography. Expanded the model extraction with the exhaustive weight-space design, tie outcomes, and parameter variations; published abstract and YAML warning retained. Independent re-audit pending.[^e8][^e9]

- Audit invalidated (2026-09-30): auditor admitted relying on spot checks and previous reports before clearing flags. A full independent audit is still required.
- 2026-09-30: Full-source design audit found opaque fitness omitted objective functions; appendix not examined by prior extraction; resource/risk symbol contradiction hidden; stress and risk direction conflicts hidden. Corrected against the source passages below; independent re-audit pending.[^design]
- Independent audit found the agent count, four strategies, lifetime/generation schedule, fitness formula, criterion weights, selection, and resource competition omitted. These are now stated with source locators; the note identifies this as an evolutionary simulation rather than an empirical fit. At that stage, independent re-audit remained pending.

- WITHDRAWN audit claim (2026-09-30): incomplete source checks; this audit does not establish a pass.

## LLM Justification
[^r1]: The research questions are a concise transformation of the primary source’s abstract and stated aims. Source location: Methods/model description and Results. Source: [Modelling the Evolution of Social Structure](https://pmc.ncbi.nlm.nih.gov/articles/PMC4948869/).


[^e1]: Main text → Social Simulation Model: turns, 300 agents, four strategies, 2000 cycles/generation, 50 generations, ranked fitness, replacement of 20%, and no inherited relationships; Experimental Design varies five objective weights.

[^e2]: S1 Appendix pp.2–3, Eqs. (1)–(7), and Model Control Process: directed trust, compressed signed increments, and waning with lagged trust. Embedded equation images were visually checked in the rendered original DOCX. Summary of Parameters sets WaningR=0.08 but gives no MinWaning value.

[^e3]: S1 Appendix → Agent strategies and Interaction Process and Relationship Formation: new/existing partners, ranked trust selection, FtF/FtW/FtM probabilities and Staged shift. Embedded search formulas were visually checked on Appendix pp.4–5; Eqs. (8)–(10) give new/existing probability and total trust; Staged uses remaining cycles RC.

[^e4]: S1 Appendix → Objective Functions and Summary of Parameters: WB=mR*(Iin/Iout); resource R=Fr*N; AL=mR*(0.05*N); risk RS=mR/(0.005*Itot); ST=N; positive versus negative fitness terms. Main text explains rank normalization and run-specific weighting.

[^e5]: Main Social Simulation Model prose and fitness formula conflict in R/RS meanings and stress direction with S1 Objective Functions. Appendix Risk prose says increasing interactions incurs more risk, despite RS=mR/(b*Itot). Both descriptions are preserved without silently resolving them.

[^e6]: Main Results, sensitivity analyses, and Discussion: rarity of layered structures, competitive strategies, and explicit functional rather than mechanism-level explanation.

[^design]: Source audit checked the full text at https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0158605. Model footnotes identify the passages supporting the corrections.


[^e7]: S1 Appendix p.4 FtM formula paragraph (c) conflicts with p.5 explanation; p.3 Eq. (7) uses trust_(t-1), whereas Summary of Parameters describes linear/8% decay. These embedded formulas were checked visually.

[^e8]: Main text, Experimental Design, Results and sensitivity analyses: all 3,125 weight combinations, five objective weights in the 1–5 range, k-means clustering across k=1–7, tie-category outcomes and strategy survival. S1 Appendix, Experimental Design: average tie strength by tercile, survivorship and final-population outputs.

[^e9]: S1 Appendix, Model Control Process and Summary of Parameters: initial 1:8 F:S setting, 0–10% reject range, ±1 mutation of F:S and rejection settings, selection/breeding rate 20% (also 5% and 10%), 2,000 cycles, 50 generations, N=300 (with N=200 and 500 sensitivity runs).
