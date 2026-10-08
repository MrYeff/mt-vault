---
title: "Massive Multi-agent Data-Driven Simulations of the GitHub Ecosystem"
authors:
  - "[[Literature/Authors/Jim Blythe|Jim Blythe]]"
  - "[[Literature/Authors/John Bollenbacher|John Bollenbacher]]"
  - "[[Literature/Authors/Di Huang|Di Huang]]"
  - "[[Literature/Authors/Pik-Mai Hui|Pik-Mai Hui]]"
  - "[[Literature/Authors/Rachel Krohn|Rachel Krohn]]"
  - "[[Literature/Authors/Diogo Pacheco|Diogo Pacheco]]"
  - "[[Literature/Authors/Goran Muric|Goran Muric]]"
  - "[[Literature/Authors/Anna Sapienza|Anna Sapienza]]"
  - "[[Literature/Authors/Alexey Tregubov|Alexey Tregubov]]"
  - "[[Literature/Authors/Yong-Yeol Ahn|Yong-Yeol Ahn]]"
  - "[[Literature/Authors/Alessandro Flammini|Alessandro Flammini]]"
  - "[[Literature/Authors/Kristina Lerman|Kristina Lerman]]"
  - "[[Literature/Authors/Filippo Menczer|Filippo Menczer]]"
  - "[[Literature/Authors/Tim Weninger|Tim Weninger]]"
  - "[[Literature/Authors/Emilio Ferrara|Emilio Ferrara]]"
source: "https://arxiv.org/html/1908.05437"
doi: "10.1007/978-3-030-24209-1_1"
publication date: "2019-06-26"
tags:
  - "model"
  - "simulation"
read status: Todo
---

## Abstract

Simulating and predicting planetary-scale techno-social systems poses heavy computational and modeling challenges. The DARPA SocialSim program set the challenge to model the evolution of GitHub, a large collaborative software-development ecosystem, using massive multi-agent simulations. We describe our best performing models and our agent-based simulation framework, which we are currently extending to allow simulating other planetary-scale techno-social systems. The challenge problem measured participant’s ability, given 30 months of meta-data on user activity on GitHub, to predict the next months’ activity as measured by a broad range of metrics applied to ground truth, using agent-based simulation. The challenge required scaling to a simulation of roughly 3 million agents producing a combined 30 million actions, acting on 6 million repositories with commodity hardware. It was also important to use the data optimally to predict the agent’s next moves. We describe the agent framework and the data analysis employed by one of the winning teams in the challenge. Six different agent models were tested based on a variety of machine learning and statistical methods. While no single method proved the most accurate on every metric, the broadly most successful sampled from a stationary probability distribution of actions and repositories for each agent. Two reasons for the success of these agents were their use of a distinct characterization of each agent, and that GitHub users change their behavior relatively slowly.

## Research Questions
> Research Questions extracted via LLM

- What agent models best predict future GitHub activity at planetary scale?[^r1]
- How do agent-specific action and repository distributions support next-period activity prediction?[^r1]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?
- GitHub users act on repositories; output events contain time, event type, user ID, and repository ID.[^g1]

The shared state below records users, repositories and timestamped actions. Fitted model internals are left opaque; the candidate rules are listed below.[^g1][^g2]

```yml
World:
  users: [User]
  repositories: [Repository]
  events: [Event]
  model: Null | Baseline | GroundEvent | PreferentialAttachment | LinkPrediction | Bayesian

User:
  profile: ... # historical activity and metadata

Repository:
  state: ... # maintained by repository hubs

Event:
  time: Timestamp
  event_type: str # source event-count conflict retained below
  user: UserId
  repository: RepositoryId
```

### How does it work?
- FARM/DASH user agents communicate through repository-state hubs. The challenge predicts February 2018 from historical events and metadata, including profiles created during the training gap.[^g1]
- Six candidates were tested: Null, Baseline, GroundEvent, PreferentialAttachment, LinkPrediction, and Bayesian. The separately described S3D extension is not a seventh tested candidate.[^g2]

The constants are source-specific experiment and model settings.[^g1][^g2][^g3][^g4]

```
NULL_SHIFT_WEEKS = 2
ACTIVITY_HALF_LIFE_DAYS = 30
WALK_MEAN_LENGTH = 2
LPE_REPOSITORY_LIMIT = 100
S3D_FEATURE_COUNT = 124
USER_COUNT_APPROX = 3000000
EVENT_COUNT_APPROX = 30000000
REPOSITORY_COUNT_APPROX = 6000000
```

- **Null:** replay the two weeks immediately before the test period with dates shifted forward.[^g2]
- **Baseline:** each user keeps its historical event rate; sample event type and repository independently from that user's frequency distributions. **GroundEvent:** sample an event–repository pair from the user's joint historical distribution.[^g3]
- **PreferentialAttachment:** extend Baseline for watch/fork. Select a neighboring user who interacted with a repository the focal user used, then one of that neighbor's repositories; both selections depend on popularity.[^g3]
- **LinkPrediction:** event-specific weighted user–repository networks predict links by embeddings. Graph Factorization was selected for performance/scalability; repository-choice tails were truncated to `LPE_REPOSITORY_LIMIT` per user. This case excludes previously absent users/repositories.[^g4]
- **Bayesian:** choose new/existing user, event category, then repository/action using data-inferred branch probabilities. Existing-user activity ranks decay with `ACTIVITY_HALF_LIFE_DAYS`. Distinguish one-time events from repeat events; watch/fork use separate repository rank models. For repeats, choose own/other repositories: own repositories weighted by prior activity; others through a geometric-length random walk of mean `WALK_MEAN_LENGTH` through the user's social vicinity.[^g5]
- **S3D extension:** for user–repository pairs lacking joint history, iteratively select features explaining the largest remaining variation in event count, with regularization parameter λ; examples include ownership, age, and shared programming language. Latent features of creators/new entities are discussed as ongoing work.[^g6]
- Source conflict: §2 says ten event types; §4.2 uses twelve networks excluding create/delete, and §4.4 says fourteen event-count models. The extraction retains these descriptions without assigning a single event count.[^g7]
- This comparison omits full branch-probability tables, fitted embeddings, and S3D predictors; these are learned from data. It does not supply one universal behavioral transition for all six candidates.[^g3][^g4][^g5][^g6]

### What can it answer?
- It compares forecasts of popularity, issue counts, contributors, and community participation at node, community, and population levels; no candidate dominates every metric.[^g2]

### Where does it apply?
- It applies to the GitHub challenge and comparable data-rich platforms after fitting new agent distributions and domain rules.[^g8]

## Metadata
### References

- [[CoEvolutionOfProjectDocumentationAndPopularityWithinGithub]]
- [[TheEffectOfRecencyToHumanMobility]]
- [[PopularityInteroperabilityAndImpactOfProgrammingLanguagesIn100000OpenSourceProjects]]
- [[ADualProcessCognitiveModelForTestingResilientControlSystems]]
- [[FarmArchitectureForDistributedAgentBasedSocialSimulations]]
- [[PredictingThePopularityOfGithubRepositories]]
- [[ParallelAgentBasedSimulationWithRepastForHighPerformanceComputing]]
- [[DistributedLoadBalancingForParallelAgentBasedSimulations]]
- [[SocialCodingInGithub]]
- [[Predicting and Explaining Behavioral Data with Structured Feature Space Decomposition]]
- [[ScaleFreeNetworkGrowthByRanking]]
- [[GhtorrentGithubSDataFromAFirehose]]
- [[TheGhtorentDatasetAndToolSuite]]
- [[UnderstandingTheGroupDynamicsAndSuccessOfTeams]]
- [[Coding together at scale- Github as a collaborative social network]]
- [[MultiAgentSocialSimulationForSocialServiceDesign]]
- [[DistributedPlatformForLargeScaleAgentBasedSimulations]]
- [[HowMuchIsTheWholeReallyMoreThanTheSumOfItsParts1125SuperlinearProductivityInCollectiveGroupActions]]
- [[NetworkStructureOfSocialCodingInGithub]]
- [[DistributedAgentBasedAirTrafficFlowManagement]]
- [[ASimilarityMeasureForIndefiniteRankings]]
- [[PatternsOfFolderUseAndProjectPopularity]]

## Audit Log
- 2026-10-03: Independent full-source re-audit passed. Six tested candidate models, shared state, S3D distinction, source conflicts, all 22 references and publisher publication date independently checked. `audit failed` removed after the pass.
- Audit invalidated (2026-09-30): auditor admitted relying on spot checks and previous reports before clearing flags. A full independent audit is still required.
- 2026-09-30: Full-source design audit found S3D incorrectly grouped with six evaluated candidates; neighbor popularity omitted; embedding truncation and prospective latent-feature scope omitted; event-type count source conflict unreported. Corrected against the source passages below; independent re-audit pending.[^design]
- Independent source audit found the earlier model account omitted the six candidate models and their defining data-derived behavior. The revision states the action tuple, three stationary variants, link-prediction and Bayesian mechanisms, new-user/repository feature model, and evaluation scope with section locators. At that stage, independent re-audit remained pending.

- WITHDRAWN audit claim (2026-09-30): incomplete source checks; this audit does not establish a pass.

## LLM Justification
[^r1]: The research questions are a concise transformation of the primary source’s abstract and stated aims. Source location: Challenge setup and Agent models/Results. Source: [Massive Multi-agent Data-Driven Simulations of the GitHub Ecosystem](https://arxiv.org/abs/1908.05437).


[^g1]: §§1–3: challenge scope, February 2018 output, training gap, FARM/DASH hubs, and approximate scale.

[^g2]: §5 lists exactly six tested candidates, defines Null, and describes prediction metrics; §7 compares strengths across metrics.

[^g3]: §4.1 defines user-specific constant rates, independent/joint sampling, and popularity-weighted neighbor/repository selection for the preferential-attachment variant.

[^g4]: §4.2 gives event-specific weighted bipartite networks and selection of Graph Factorization; §5 gives the 100-repository truncation.

[^g5]: §4.3 and Figure 1 describe generation order, 30-day half-life ranks, one-/multiple-time split, two watch/fork rank models, ownership branch, and geometric random walk with mean 2.

[^g6]: §4.4 describes 124 candidate features, sequential S3D selection, λ regularization and fourteen event-count models; §7 discusses latent features and continued work on new entities.

[^g7]: §2 explicitly states ten event types; §4.2 states twelve networks except create/delete; §4.4 states fourteen models. These are retained as a source inconsistency.

[^g8]: §7 describes a general simulation comparison framework already adapted to Twitter/Reddit and domain-dependent training windows.

[^design]: Source audit checked the full text at https://arxiv.org/html/1908.05437. Model footnotes identify the passages supporting the corrections.
