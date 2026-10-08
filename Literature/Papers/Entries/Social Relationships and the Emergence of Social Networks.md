---
title: "Social Relationships and the Emergence of Social Networks"
tags:
  - social_network
  - simulation
  - "model"
authors:
  - "[[Literature/Authors/Alistair Sutcliffe|Alistair Sutcliffe]]"
  - "[[Literature/Authors/Di Wang|Di Wang]]"
  - "[[Literature/Authors/Robin Dunbar|Robin Dunbar]]"
publication date: 2012-10-31 
source: "https://www.jasss.org/15/4/3/3.pdf"
doi: 10.18564/jasss.2059
read status: Todo
---

## Abstract

In complex social systems such as those of many mammals, including humans, groups (and hence ego-centric social networks) are commonly structured in discrete layers. We describe a computational model for the development of social relationships based on agents' strategies for social interaction that favour more less-intense, or fewer more-intense partners. A trust-related process controls the formation and decay of relationships as a function of interaction frequency, the history of interaction, and the agents' strategies. A good fit of the observed layers of human social networks was found across a range of model parameter settings. Social interaction strategies which favour interacting with existing strong ties or a time-variant strategy produced more observation-conformant results than strategies favouring more weak relationships. Strong-tie strategies spread in populations under a range of fitness conditions favouring wellbeing, whereas weak-tie strategies spread when fitness favours foraging for food. The implications for modelling the emergence of social relationships in complex structured social networks are discussed.

## Research Questions
> Research Questions extracted via LLM
- Can interaction strategies and trust-related relationship formation reproduce the layered structure observed in human social networks?[^r1]
- Under what fitness conditions do strategies favoring stronger existing ties or weaker ties spread?[^r1]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?
- Agents form directed trusting relationships while allocating turns to foraging or social interaction. Strategy governs partner search; response may cooperate or defect.[^r3]
- The notation covers relationship state and the basic selection experiment; it does not reconstruct unspecified inherited probability functions.[^r3][^r4]

```yml
World:
  agents: [Agent]
  cycle: u32
  generation: u32

Agent:
  strategy: FavourFew | MediumTies | FavourMany | Staged
  trust: [AgentId -> f64]
  successful_contacts: [AgentId -> 0..]
  incoming: 0..
  outgoing: 0..
  forage_turns: 0..
  defects: 0..
```

### How does it work?
- Each cycle gives every agent one turn; `FM` selects foraging (+1 resource) or social contact. Partners are initially random.[^r3]
- Search later favors high-trust, midpoint or low-trust relationships; Staged shifts from high-trust toward weak/unknown partners over the lifetime.[^r3]
- Successful-interaction memory drives search; previous defections are not separately used in partner choice.[^r3]
- Cooperation raises initiator → responder trust; defection lowers it and increments defect count. Prose specifies increasing logarithmic compression, buffering high-trust ties against both signs, and logarithmic decay that weakens stronger ties less.[^r3]
- ⚠️ The printed §2.6 algorithm instead gives increments/decrements `MaxCR - CI * Trust` and `Trust -= W`; it does not define enough detail to identify these with the logarithmic prose.[^r5]
- §4.4 selects log increase/linear decrease. These alternatives are retained as a source conflict; no single exact trust/decay implementation is inferred.[^r5]
- The following fitness equations are transcribed from §4.2. `ties` means the ego's existing relationships; the paper leaves zero-tie/zero-outgoing division unspecified.[^r4]

```
fitness(agent: Agent, ties: [AgentId]) -> (f64, f64):
  n = ties.length()
  wellbeing = sum(agent.trust[ties]) * agent.incoming / agent.outgoing / n
  resource = agent.forage_turns * n
  out = (wellbeing, resource)
```

- Baseline controls vary forage:meeting (FM), resource:wellbeing (R:WB) weight, defect rate, waning and run length; outcomes include strategy frequency and trust-ranked tie layers. The baseline setting uses `N=300`, equal strategy counts, 20 generations, 10% defects, and log increase/linear decrease with `MC=10`, waning `0.08`.[^r6]
- In the kin experiment, parent/sibling kin are seeded as high-trust ties and carried to offspring. Up to five kin replace emerging strong ties without changing layer counts; larger seeds increase strong ties modestly, with the model self-limiting around 8–9.[^r6]
- The evolutionary extension inherits strategy, FM and response-defection rate. The four FM starting settings are `8:1 | 5:1 | 4:1 | 1:1`; defection settings are `0.01, 0.025, 0.05, 0.075`.[^r6]
- For that extension, `N=1000` starts with a balanced hierarchical population; crossover is `0.9`, a random gene is selected per breeding cycle, and mutation is `0.01` over FM and defect ranges divided into 1000 intervals. Across 50-generation runs, wellbeing-favouring settings (notably R:WB≈1:5) more often retain strong/staged strategies and layered ties, while resource-favouring settings favour weak ties and more foraging. These are simulation outcomes, not universal thresholds.[^r6]

### What can it answer?
- Measure trust-ranked ego ties using upper, middle and lower terciles; compare layer counts and strategy survival across wellbeing/resource weights, forage/social time ratios, defections, kin seeding and evolutionary runs. The source reports the best fit near 150 total ties per ego only in particular parameter regions (e.g. FM 1:3 in §4), and notes different outcomes under evolutionary reproduction in §5.[^r4][^r6]

### Where does it apply?
- Mechanism experiments on layered ego networks. Exact inherited search/decay functions and the full simulation code are omitted; unresolved trust rules prevent treating this summary as a complete reproducible simulator.[^r3][^r4][^r5]

## Metadata
### References

- [[Is friendship akin to kinship-|Is friendship akin to kinship?]]
- [[Small groups as complex systems- Formation, coordination, development and adaptation|Small groups as complex systems: Formation, coordination, development and adaptation]]
- [[The need to belong- Desire for interpersonal attachments as a fundamental human motivation|The need to belong: Desire for interpersonal attachments as a fundamental human motivation]]
- [[Spatial behavior in groups- An agent-based approach|Spatial behavior in groups: An agent-based approach]]
- [[The evolution of reciprocity in sizable groups|The evolution of reciprocity in sizable groups]]
- [[Selective investment theory- Recasting the functional significance of close relationships|Selective investment theory: Recasting the functional significance of close relationships]]
- [[Human sympathy groups|Human sympathy groups]]
- [[Coevolution of neocortex size, group size and language in humans|Coevolution of neocortex size, group size and language in humans]]
- [[The Social Brain Hypothesis|The Social Brain Hypothesis]]
- [[Mind the gap- Or why humans aren't just great apes|Mind the gap: Or why humans aren't just great apes]]
- [[Brain and behaviour in primate evolution|Brain and behaviour in primate evolution]]
- [[Understanding primate brain evolution|Understanding primate brain evolution]]
- [[Social networks, support cliques, and kinship|Social networks, support cliques, and kinship]]
- [[Time as an ecological constraint|Time as an ecological constraint]]
- [[The strength of weak ties|The strength of weak ties]]
- [[Economic action and social structure- The problem of embeddedness|Economic action and social structure: The problem of embeddedness]]
- [[The genetical evolution of social behaviour, I and II|The genetical evolution of social behaviour, I and II]]
- [[Nice guys finish first- The competitive altruism hypothesis|Nice guys finish first: The competitive altruism hypothesis]]
- [[The day-to-day functioning of close versus casual friendships|The day-to-day functioning of close versus casual friendships]]
- [[Attitudes and cognitive organization|Attitudes and cognitive organization]]
- [[Social network size in humans|Social network size in humans]]
- [[Network scaling reveals consistent fractal pattern in hierarchical mammalian societies|Network scaling reveals consistent fractal pattern in hierarchical mammalian societies]]
- [[Friendship, cliquishness, and the emergence of cooperation|Friendship, cliquishness, and the emergence of cooperation]]
- [[Effects of trust on complex adaptive supply networks- An agent-based simulation study|Effects of trust on complex adaptive supply networks: An agent-based simulation study]]
- [[Sense and nonsense- Evolutionary perspectives on human behaviour|Sense and nonsense: Evolutionary perspectives on human behaviour]]
- [[Group size, grooming and social cohesion in primates|Group size, grooming and social cohesion in primates]]
- [[Time management in great apes- Implications for gorilla biogeography|Time management in great apes: Implications for gorilla biogeography]]
- [[Size matters- Variation in personal network size, personality and effect on information transmission|Size matters: Variation in personal network size, personality and effect on information transmission]]
- [[The evolution of trust and cooperation between strangers- A computational model|The evolution of trust and cooperation between strangers: A computational model]]
- [[Altruism and kinship- A cross-cultural experimental study|Altruism and kinship: A cross-cultural experimental study]]
- [[Social isolation in America- Changes in core discussion networks over two decades|Social isolation in America: Changes in core discussion networks over two decades]]
- [[Evolution of indirect reciprocity by social information- The role of trust and reputation in evolution of altruism|Evolution of indirect reciprocity by social information: The role of trust and reputation in evolution of altruism]]
- [[Socialization in small groups- Temporal changes in individual-group relations|Socialization in small groups: Temporal changes in individual-group relations]]
- [[Evolution of indirect reciprocity by image scoring|Evolution of indirect reciprocity by image scoring]]
- [[Evolution of indirect reciprocity|Evolution of indirect reciprocity]]
- [[Towards a behavioural theory linking trust, reciprocity and reputation|Towards a behavioural theory linking trust, reciprocity and reputation]]
- [[Friendship maintenance- An analysis of individual and dyad behaviours|Friendship maintenance: An analysis of individual and dyad behaviours]]
- [[How can social networks ever become complex- Modelling the emergence of complex networks from local social exchanges|How can social networks ever become complex? Modelling the emergence of complex networks from local social exchanges]]
- [[A Social Identity Model of Deindividuation Phenomena|A Social Identity Model of Deindividuation Phenomena]]
- [[Trust in close relationships|Trust in close relationships]]
- [[Communication in social networks- Effects of kinship, network size and emotional closeness|Communication in social networks: Effects of kinship, network size and emotional closeness]]
- [[The development of cooperative relationships- An experiment|The development of cooperative relationships: An experiment]]
- [[Exploring variations in active network size- Constraints and ego characteristics|Exploring variations in active network size: Constraints and ego characteristics]]
- [[Evolutionary game theory meets social science- Is there a unifying rule for human cooperation-|Evolutionary game theory meets social science: Is there a unifying rule for human cooperation?]]
- [[Keeping and ending casual, close and best friendships|Keeping and ending casual, close and best friendships]]
- [[A community-level evaluation of the impact of prey behavioural and ecological characteristics on predator diet composition|A community-level evaluation of the impact of prey behavioural and ecological characteristics on predator diet composition]]
- [[Perspective-taking and social network size in humans|Perspective-taking and social network size in humans]]
- [[Computational Modelling of Trust and Social Relationships|Computational modelling of trust and social relationships]]
- [[Relationships and the social brain- Integrating psychological and evolutionary perspectives|Relationships and the social brain: Integrating psychological and evolutionary perspectives]]
- [[An integrative theory of intergroup conflict|An integrative theory of intergroup conflict]]
- [[Evolutionary psychology and the generation of culture, I- Theoretical considerations|Evolutionary psychology and the generation of culture, I: Theoretical considerations]]
- [[Developmental sequence in small groups|Developmental sequence in small groups]]
- [[Different strokes from different folks- Community ties and social support|Different strokes from different folks: Community ties and social support]]
- [[Does the internet increase, decrease, or supplement social capital-|Does the internet increase, decrease, or supplement social capital?]]
- [[Connected lives- The project|Connected lives: The project]]
- [[Culture evolves|Culture evolves]]
- [[A deductive approach to friendship networks|A deductive approach to friendship networks]]
- [[Stability of groups with costly beliefs and practices|Stability of groups with costly beliefs and practices]]
- [[Uncertainty, trust and commitment formation in the United States and Japan|Uncertainty, trust and commitment formation in the United States and Japan]]
- [[Sympathy and punishment- Evolution of cooperation in public goods game|Sympathy and punishment: Evolution of cooperation in public goods game]]
- [[Developing trust in large-scale peer-to-peer systems|Developing trust in large-scale peer-to-peer systems]]
- [[Discrete hierarchical organization of social group sizes|Discrete hierarchical organization of social group sizes]]

## Audit Log
- 2026-10-03: Independent full-source re-audit passed. Full primary source, fitness equations and62references checked; missing footnote and source-bibliography typo corrected and independently re-audited. Inherited-rule gaps/source conflicts remain explicit. `audit failed` removed after the pass.
- Audit invalidated (2026-09-30): auditor admitted clearing flags before completing independent source checks. A new independent audit is required.
- Strong source review (2026-09-30): Corrected date, typed relationship state and added actual wellbeing/resource fitness and selection. Recorded trust prose/control-algorithm conflict; exact inherited partner-search/decay functions remain explicitly unresolved. Independent re-audit pending.
- Initial independent audit: failed on missing model mechanisms, abstract fidelity, or source-access reporting; see `vault/.automation/audit/next-forty-54-66-initial-2026-09-30.json`. Revisions added source-located model detail; independent re-audit remains pending.

- WITHDRAWN audit claim (2026-09-30): previously reported PASS; source claims, current extraction, metadata, references and footnotes checked against the available primary source. See `vault/.automation/audit/remaining-audit-b-2026-09-30.json`.

## LLM Justification
[^r1]: The paper’s abstract, at https://www.jasss.org/15/4/3/3.pdf. The questions paraphrase the stated purpose, research scope, and reported approach.
[^r3]: Sutcliffe, Wang & Dunbar, §§2.1–2.6 (trust, strategies, turn control and inherited formula references), §6.10 (defection memory not used in partner selection; ego-network scope). Full text: https://www.jasss.org/15/4/3.html.
[^r4]: Sutcliffe et al., §§3.1–3.3 (controls and tercile outcomes), §4.2 (wellbeing/resource equations; viewed in full PDF p. 4 because HTML equations are images), §§4.3–4.5 (selection, initial population, cycles, generations and experimental weights), §5 (separate genotype/mutation experiments). Full text: https://www.jasss.org/15/4/3/3.pdf.
[^r5]: Unresolved source conflict: §2.4 specifies a log-ratio rule for positive and negative trust changes; §2.6 printed Model-Control instead uses ±(MaxCR−CI×Trust), then subtracts W, while its notes specify logarithmic waning. §4.4 selects “Log increase/linear decrease.” Exact functions are referred to Sutcliffe & Wang (2012); this summary records the disagreement rather than inventing a resolution. Publication header: 31-Oct-2012. Full text: https://www.jasss.org/15/4/3/3.pdf.
[^r6]: Sutcliffe, Wang & Dunbar, §§3.1–3.3 (baseline and kin experiments, controls and outcomes), §§4.3–4.5 (selection, starting population, cycles, generations and fitness weights), §5 (evolutionary genotype, crossover, mutation, and strategy/tie outcomes). Full source: https://www.jasss.org/15/4/3/3.pdf.
