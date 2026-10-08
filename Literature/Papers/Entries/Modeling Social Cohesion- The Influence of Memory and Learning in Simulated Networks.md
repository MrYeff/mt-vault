---
title: "Modeling Social Cohesion: The Influence of Memory and Learning in Simulated Networks"
authors:
  - "[[Literature/Authors/Yara Khaluf|Yara Khaluf]]"
  - "[[Literature/Authors/Bernd Wurpts|Bernd Wurpts]]"
  - "[[Literature/Authors/Till Hovestadt|Till Hovestadt]]"
  - "[[Literature/Authors/Nikolas Zöller|Nikolas Zöller]]"
  - "[[Literature/Authors/Gert Jan Hofstede|Gert Jan Hofstede]]"
source: "https://link.springer.com/chapter/10.1007/978-3-032-01373-6_11"
doi: "10.1007/978-3-032-01373-6_11"
publication date: "2026-02-08"
tags:
  - "model"
  - "simulation"
  - "social_cohesion"
read status: Todo
---

## Abstract

This study explores group cohesion on the base of social exchange theory, focusing on the dynamics within groups as influenced by memory and learning mechanisms. Using agent-based modeling, we examine how these factors affect individual and group-level cohesion. Specifically, we model the average time agents spend in groups (duration of individual membership), the duration of group existence (aggregate cohesion), and overall agent satisfaction under three conditions: No Memory, Memory, and Memory+Learning, across two network structures: Fully Connected (FC) and Preferential Attachment (PA). Our model incorporates dynamic cultural adaptation and reciprocal exchanges to simulate realistic social dynamics. Dynamic cultural adaptation in our model refers to the evolving behaviors of agents as they adjust their individualism and preferences based on past interactions and group experiences. We find that memory of past interactions enhances group cohesion and stability, while learning introduces new dynamics that influence group persistence.

## Research Questions
> Research Questions extracted via LLM

- How do memory and learning affect individual membership, group duration, and satisfaction?[^r1]
- Do these effects differ between fully connected and preferential-attachment networks?[^r1]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?
- Agents exchange status within changing groups; satisfaction, memory, and individualism influence membership and group persistence.[^c1]

### How does it work?
The state and initial settings come from §11.3 and Table 11.1.[^c2]

```yml
World:
  agents: [Agent]
  groups: [Group]
  network: FullyConnected | PreferentialAttachment
  condition: NoMemory | Memory | MemoryLearning
  reset_memory: bool

Group:
  members: [AgentId]
  status: 0..1 # mean member status

FeedbackRecord:
  value: -1 | 1
  time_step: u32

Agent:
  group: GroupId
  status: 0..1
  individualism: 0..1
  feedback_memory: [FeedbackRecord] # signed feedback retained with its time step
  memory_length: 1..10 # number of time steps remembered; initialized to 5
  satisfaction: -1..1
  leave: bool # initialized to false
```

```
INITIAL_MEAN = 0.5
INITIAL_STD = 0.1
MEMORY_LENGTH_RANGE = 1..10
INITIAL_MEMORY_LENGTH = 5
INITIAL_GROUP_SIZE_RANGE = 1..100 # initial group size is randomly assigned within range
PA_LINK_DENSITY = 0.15
```

- Initially assign groups randomly; initial group size is randomly assigned in the range 1–100. This is an initial setting, not a bound on later group membership. Status and individualism have normal initial draws with `INITIAL_MEAN` and `INITIAL_STD`. Table 11.1 declares `[0,1]` ranges without specifying how out-of-range draws are handled. Memory length is the number of time steps remembered (range 1–10, initial value 5); the retained history therefore needs time-step indexing, rather than treating the parameter as a count of feedback events. The leave-group flag starts false.[^c2]
- Each tick resets interaction state, finds neighboring mates within groups, interacts, computes satisfaction, decides exits, restructures groups, and records outcomes. An isolated agent with no mate is flagged to leave and seek/form a group.[^c3]
- Sender conferral combines receiver status and mean group status: individualism favors personal status, collectivism group status; add a small random component. The receiver compares actual conferral with its expectation; below expectation beyond tolerance gives −1, otherwise +1. Store this feedback in the **sender's** memory.[^c1]
- Satisfaction uses linearly increasing recency weights on positive feedback, divided by a normalization factor. Memory may persist or reset after group changes. Learning adapts individualism to the current group, changing conferral and feedback expectations; group exit is probabilistic in satisfaction and individualism.[^c4]
- Compare NoMemory, Memory, and MemoryLearning in FullyConnected and Barabási–Albert PreferentialAttachment networks. NoMemory responds to immediate feedback; memory conditions accumulate prior feedback.[^c4]
- Reporting limits: Table 11.1 permits satisfaction −1..1, while §11.3's positive-feedback normalization describes a nonnegative score. The chapter gives no exact conferral formula, tolerance value, individualism-learning update, exit probability, or normalization factor; this extraction does not invent them.[^c5]

### What can it answer?
- It measures membership duration, group lifespan (until its last member leaves), and average satisfaction. Memory improves membership duration, while group-lifespan effects depend on network and learning condition.[^c6]

### Where does it apply?
- It applies to the chapter's stylized status exchanges and two network settings; model extensions require additional behavioral specification.[^c1][^c5]

## Metadata
### References

- [[Network Science]]
- [[EmergenceOfScalingInRandomNetworks]]
- [[HandbookOfSocialPsychology|Social exchange theory]]
- [[Exchange theory, part I- A psychological basis for social exchange|Exchange theory, part I: A psychological basis for social exchange]]
- [[Exchange theory, part II- Exchange relations and networks|Exchange theory, part II: Exchange relations and networks]]
- [[GrowingArtificialSocieties]]
- [[SimulationForTheSocialScientist]]
- [[ToStayOrNotToStayArtificialSocialityInGraspWorld]]
- [[Stimulating diffusion of technological innovations]]
- [[A Social Interactional Theory of Emotions]]
- [[Emotion and group cohesion in productive exchange]]
- [[PowerAndTheEmergenceOfCommitmentBehaviorInNegotiatedExchange]]
- [[CommitmentInExchangeRelationsTestOfATheoryOfRelationalCohesion]]
- [[NetworkStructureAndEmotionInExchangeRelations]]
- [[A new theory of group solidarity]]
- [[DependenceAndRiskTransformingTheStructureOfSocialExchange]]
- [[CoercivePowerInSocialExchange]]
- [[SocialExchangeNetworksAReviewOfExperimentalStudies]]
- [[Emotionssoziologie]]
- [[TheLargeScaleStructureOfSemanticNetworksStatisticalAnalysesAndAModelOfSemanticGrowth]]

## Audit Log
- 2026-10-03: Independent full-source re-audit passed. Memory state, initial settings, update sequence and all 20 references checked against the corrected publisher chapter and tables. `audit failed` removed after the pass.
- Audit invalidated (2026-09-30): auditor admitted relying on spot checks and previous reports before clearing flags. A full independent audit is still required.
- 2026-09-30: Full-source design audit found missing parameter and scheduling tables; recency weighting insufficiently specified; satisfaction range/positive-feedback reporting tension unflagged; omitted numerical transition rules not disclosed. Corrected against the source passages below; independent re-audit pending.[^design]
- Independent source audit found the earlier account blurred the model into reciprocal exchange and omitted update/tick mechanics. It now specifies one-sided status conferral, receiver feedback, recency-weighted memory, optional reset, individualism learning, probabilistic exit, network initialization, and measured outcomes. At that stage, independent re-audit remained pending.

- WITHDRAWN audit claim (2026-09-30): incomplete source checks; this audit does not establish a pass.

## LLM Justification
[^r1]: The research questions are a concise transformation of the primary source’s abstract and stated aims. Source location: Model and Results sections. Source: [Modeling Social Cohesion: The Influence of Memory and Learning in Simulated Networks](https://link.springer.com/chapter/10.1007/978-3-032-01373-6_11).


[^c1]: §11.3 Model: sender/receiver status exchange, actual-versus-expected comparison, feedback signs and memory direction.

[^c2]: Table 11.1 at /chapter/10.1007/978-3-032-01373-6_11/tables/1: individualism/status range 0–1 and Normal(0.5,0.1), memory range 1–10 initialized 5, random groups, satisfaction −1..1. §11.3 specifies PA density 0.15.

[^c3]: §11.3, Figure 11.1 and Table 11.2 at /chapter/10.1007/978-3-032-01373-6_11/tables/2: initialization, interaction, satisfaction, decision, restructuring, recording; text flags agents with no mate for exit.

[^c4]: §11.3 memory, reset, learning, exit and network paragraphs: recency weights increase linearly; learning adjusts individualism; exit is probabilistic; three conditions crossed with two networks.

[^c5]: Full §11.3 and Tables 11.1–11.2 were checked. Exact numerical transition functions are not supplied there. Table 11.1 satisfaction range includes negative values; text describes weighted positive-feedback normalization. The omitted details cannot be reconstructed faithfully from this chapter alone.

[^c6]: §11.4 defines membership time, group existence until empty, and rolling satisfaction; Figures 11.2–11.7 and Table 11.3 compare conditions by network.

[^design]: Source audit checked the full text at https://link.springer.com/chapter/10.1007/978-3-032-01373-6_11. Model footnotes identify the passages supporting the corrections.
