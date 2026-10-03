---
title: "SARDINE: Simulator for Automated Recommendation in Dynamic and Interactive Environments"
tags:
  - recommender_system
  - simulation
  - "model"
authors:
  - "[[Literature/Authors/Romain Deffayet|Romain Deffayet]]"
  - "[[Literature/Authors/Thibaut Thonet|Thibaut Thonet]]"
  - "[[Literature/Authors/Dongyoon Hwang|Dongyoon Hwang]]"
  - "[[Literature/Authors/Vassilissa Lehoux‐Lebacque|Vassilissa Lehoux‐Lebacque]]"
  - "[[Literature/Authors/Jean-Michel Renders|Jean-Michel Renders]]"
  - "[[Literature/Authors/Maarten de Rijke|Maarten de Rijke]]"
publication date: 2024-04-08 
source: "https://arxiv.org/html/2311.16586"
doi: 10.1145/3656481
read status: Todo
⚠️:
  - audit failed
---

## Abstract

Simulators can provide valuable insights for researchers and practitioners who wish to improve recommender systems, because they allow one to easily tweak the experimental setup in which recommender systems operate, and as a result lower the cost of identifying general trends and uncovering novel findings about the candidate methods. A key requirement to enable this accelerated improvement cycle is that the simulator is able to span the various sources of complexity that can be found in the real recommendation environment that it simulates. With the emergence of interactive and data-driven methods—e.g., reinforcement learning or online and counterfactual learning-to-rank—that aim to achieve user-related goals beyond the traditional accuracy-centric objectives, adequate simulators are needed. In particular, such simulators must model the various mechanisms that render the recommendation environment dynamic and interactive, e.g., the effect of recommendations on the user or the effect of biased data on subsequent iterations of the recommender system. We therefore propose SARDINE, a flexible and interpretable recommendation simulator that can help accelerate research in interactive and data-driven recommender systems. We demonstrate its usefulness by studying existing methods within nine diverse environments derived from SARDINE, and even uncover novel insights about them.

## Research Questions
> Research Questions extracted via LLM
- How can a recommender simulator represent dynamic, interactive effects such as recommendations changing users and feedback changing later data?[^r1]
- How do recommendation methods behave across the nine environments derived from SARDINE?[^r1]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?
- Cold-start sessions over fixed synthetic item/topic embeddings; the agent chooses a slate, the user clicks or skips, and enabled dynamics alter the user vector.[^r3]
- Items cover 2 or 3 topics; users cover 3, 4 or 5. Nonzero components start Uniform(0,1), then the vector is unit-normalized.[^r3]

```yml
World:
  items: [Item]
  user: Vector
  history: [Interaction]
  topic_timeouts: [TopicId -> 0..]

Item:
  embedding: Vector
  main_topic: TopicId

Vector: [0..1]
TopicId: u32

Interaction:
  step: u32
  slate: [ItemId]
  clicks: [bool]

Observation:
  Full:
    user: Vector
    histogram: Vector
    timeouts: Vector
  Partial:
    slate: [ItemId]
    clicks: [bool]
    histogram: Vector
```

### How does it work?
- First slate: random items from the simulator; later slates: the agent's policy. Return reward = click count and continue to session length. The typed rules below use environment settings in CAPS.[^r3]

```
click_probability(
  user: Vector,
  item: Item,
  rank: 1..
) -> 0..1:
  relevance = dot(item.embedding, user)
  attractiveness = ALPHA / (1 + exp(-LAMBDA * (relevance - MU)))
  out = attractiveness * EPSILON^(rank - 1)


clicked_influence(
  user: Vector,
  clicked: [Item]
) -> Vector:
  if clicked.is_empty(): out = user
  else: out = OMEGA * user + (1 - OMEGA) * mean(clicked.embedding)
```

- Clicks are sampled Bernoulli at each rank. Influence is enabled by the chosen environment; `OMEGA` is the old-user weight (1 disables drift). The empty-click guard above is an extraction convention: the printed mean is undefined for zero clicks.[^r3][^r5]
- Boredom uses clicks in the last `T_B` steps, keeping at most the newest `N_B` clicks. A main-topic count **greater than** `TAU_B` triggers boredom.[^r3][^r5]
- Topic-loss zeros that component for `T_B` steps and restores its old value; churn-and-return zeros the entire vector for that duration.[^r3][^r5]
- The paper does not fully specify composition with influence or repeated timer resets.[^r3][^r5]
- Full observation: current user vector, `clip(topic_count / TAU_B, 0, 1)`, and remaining topic timeout divided by `T_B` (inactive topics use `T_B`). Partial: last slate IDs, click flags, same histogram.[^r3]
- Experiments use churn-and-return only. Table 3 varies settings: single/top-K sessions use `L=100`, `N_ITEMS=1000`, `N_TOPICS=10`; reranking uses `L=10`, `N_ITEMS=S=10`. Dynamic settings use `N_B=10`, `T_B=5`, `TAU_B=5`; enabled influence uses `OMEGA=0.95`.[^r4]
- ⚠️ Churn prose claims zero clicks, but the printed sigmoid yields positive click probability at zero relevance. No extra no-click gate is imposed here.[^r5]

### What can it answer?
- Compare methods across nine configurations, measuring cumulative clicks and bored steps; vary bias, uncertainty, state observability and long-term dynamics.[^r4]

### Where does it apply?
- Synthetic interactive recommendation benchmarks. Agent architectures, training settings and remaining per-environment settings are omitted; no real-world behavioral validity is established.[^r4]

## Metadata
### References
- [[BeingAccurateIsNotEnough]]
- [[InteractiveRecommenderSystemsASurveyOfTheStateOfTheArtAndFutureResearchChallengesAndOpportunities]]
- [[ClickModelsForWebSearch]]
- [[UnbiasedLearningToRankWithBiasedFeedback]]
- [[RecommenderSystemsBeyondMatrixCompletion]]
- [[ProceedingsOfThe16thInternationalJointConferenceOnArtificialIntelligenceIjcai99]]
- [[ReinforcementLearningAlgorithmForNonStationaryEnvironments]]
- [[VirtualTaobaoVirtualizingRealWorldOnlineRetailEnvironmentForReinforcementLearning]]
- [[AlgorithmicEffectsOnTheDiversityOfConsumptionOnSpotify]]
- [[KeepingDatasetBiasesOutOfTheSimulation]]
- [[RobustGeneralizationAndSafeQuerySpecializationinCounterfactualLearningToRank]]
- [[UnresolvedReference8384B3EAF42C6CAB]]
- [[LearningRobustRecommendersThroughCrossModelAgreement]]
- [[The Effect of People Recommenders on Echo Chambers and Polarization]]
- [[ProceedingsOfThe15thAcmInternationalConferenceOnInformationAndKnowledgeManagementCikm06]]
- [[MultiArmedBanditsInRecommendationSystemsASurveyOfTheStateOfTheArtAndFutureDirections]]
- [[ActiveLearningInRecommenderSystems]]
- [[RecommenderSystems]]
- [[ProceedingsOfTheInternationalJointConferenceOnNeuralNetworksIjcnn2005]]
- [[EvaluatingRecommenderSystemsSurveyAndFramework]]
- [[ProceedingsOfThe26thInternationalConferenceOnWorldWideWebWww17]]
- [[OfflineEvaluationForReinforcementLearningBasedRecommendation]]
- [[BootstrappedPersonalizedPopularityForColdStartRecommenderSystems]]
- [[2023IeeeInternationalConferenceOnEnablingTechnologiesInfrastructureForCollaborativeEnterprisesWetice]]
- [[UnresolvedReference38CCF27109EFFA10]]
- [[ProceedingsOfThe30thInternationalConferenceOnMachineLearningProceedingsOfMachineLearningResearch]]
- [[ProceedingsOfTheWebConferenceWww20]]
- [[ProceedingsOfThe17thAcmConferenceOnRecommenderSystemsRecsys23]]
- [[IeeeInternationalConferenceOnEnablingTechnologiesInfrastructureForCollaborativeEnterprisesWetice14]]
- [[ProceedingsOfThe13thInternationalConferenceOnWebSearchAndDataMiningWsdm19]]
- [[ProceedingsOfTheInternationalConferenceOnWebSearchAndDataMiningWsdm08]]
- [[ProceedingsOfThe46thInternationalAcmSigirConferenceOnResearchAndDevelopmentInInformationRetrievalSigir23]]
- [[ProceedingsOfThe16thAcmInternationalConferenceOnWebSearchAndDataMiningWsdm23]]
- [[ProceedingsOfTheInternationalConferenceOnMachineLearningIcml18]]
- [[ProceedingsOfThe4thInternationalConferenceOnLearningRepresentationsIclr16]]
- [[ProceedingsOfTheAcmSigirInternationalConferenceSigir22]]
- [[ProceedingsOfThe14thAcmConferenceOnRecommenderSystemsRecsys20]]
- [[ProceedingsOfThe24thInternationalConferenceOnArtificialIntelligenceAndStatisticsProceedingsOfMachineLearningResearch]]
- [[ProceedingsOfThe28thInternationalJointConferenceOnArtificialIntelligenceIjcai19]]
- [[RecSim- A Configurable Simulation Platform for Recommender Systems]]
- [[ProceedingsOfThePerspectivesWorkshopAtRecsys23]]
- [[ProceedingsOfTheInternationalConferenceOnWebSearchAndDataMiningWsdm17]]
- [[UnresolvedReferenceCDBD15A4AFF8CD2A]]
- [[ProceedingsOfTheAcmConferenceOnRecommenderSystemsRecsys23]]
- [[ProceedingsOfThe45thInternationalAcmSigirConferenceOnResearchAndDevelopmentInInformationRetrievalSigir22]]
- [[ProceedingsOfThe19thInternationalConferenceOnWorldWideWebWww10]]
- [[ProceedingsOfTheInternationalConferenceOnWorldWideWebWww23]]
- [[ProceedingsOfTheInternationalJointConferenceOnNeuralNetworksIjcnn17]]
- [[UnresolvedReference0CB7BC1C4EDB0CCA]]
- [[ProceedingsOfTheChi06ExtendedAbstractsOnHumanFactorsInComputingSystemsChiEa06]]
- [[ProceedingsOfThe30thAcmInternationalConferenceOnInformationAndKnowledgeManagementCikm21]]
- [[ProceedingsOfThe44thInternationalAcmSigirConferenceOnResearchAndDevelopmentInInformationRetrievalSigir21]]
- [[ProceedingsOfTheWebConferenceWww21]]
- [[RecogymAReinforcementLearningEnvironmentForTheProblemOfProductRecommendationInOnlineAdvertising]]
- [[ProceedingsOfTheNeuralInformationProcessingSystemsTrackOnDatasetsAndBenchmarks]]
- [[UnresolvedReference758822F73DAAB6DA]]
- [[ProceedingsOfTheInternationalConferenceOnDataMiningWorkshopsIcdmw20]]
- [[ProceedingsOfThe15thAcmConferenceOnRecommenderSystemsRecsys21]]
- [[TheStanfordEncyclopediaOfPhilosophySpring2022Ed]]
- [[ProceedingsOfThe31stInternationalConferenceOnNeuralInformationProcessingSystemsNips17]]
- [[UnresolvedReferenceB31F9560449DA351]]
- [[UnresolvedReference72AA34072D2BAA32]]
- [[ProceedingsOfTheAcmWebConferenceWww22]]

## Audit Log
- Audit invalidated (2026-09-30): auditor admitted clearing flags before completing independent source checks. A new independent audit is required.
- Strong source review (2026-09-30): Fixed influence guard/parameter consistency, explicit click formula and normalized observation definitions; distinguished both boredom variants from churn-only experiments; recorded missing empty-click/composition rules and nonzero sigmoid-at-zero conflict. Independent re-audit pending.
- Initial independent audit: failed on missing model mechanisms, abstract fidelity, or source-access reporting; see `vault/.automation/audit/next-forty-54-66-initial-2026-09-30.json`. Revisions added source-located model detail; independent re-audit remains pending.

- WITHDRAWN audit claim (2026-09-30): previously reported PASS; source claims, current extraction, metadata, references and footnotes checked against the available primary source. See `vault/.automation/audit/remaining-audit-b-2026-09-30.json`.

## LLM Justification
[^r1]: The paper’s abstract, at https://arxiv.org/abs/2311.16586. The questions paraphrase the stated purpose, research scope, and reported approach.
[^r3]: Deffayet et al., §§2–3.5: session sequence, sparse normalized embeddings, Eqs. (1)–(2), position-based Bernoulli clicks; boredom/influence and exact observation vectors. Full text: https://arxiv.org/html/2311.16586.
[^r4]: Deffayet et al., §4.1/Table 2 (nine variants, experiments use churn-and-return), §4.3/Table 3 (environment settings), §4.4 (return/boredom metrics), §1.3 (no human-mind/live-performance guarantee). Full text: https://arxiv.org/html/2311.16586.
[^r5]: Source conflict/underspecification: §3.4 influence divides by the number of clicked items without stating the zero-click case; simultaneous boredom/influence composition and repeated timeout handling are not fully stated. Churn is said to imply no clicks, but §3.3 Eq. (2) and the position-based rule give ALPHA/(1+exp(LAMBDA*MU))*EPSILON^(rank-1)>0 for finite settings. The guard is an explicit extraction convention, not a claimed published equation. Full text: https://arxiv.org/html/2311.16586.
