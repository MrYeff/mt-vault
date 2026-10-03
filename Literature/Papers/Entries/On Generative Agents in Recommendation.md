---
title: "On Generative Agents in Recommendation"
authors:
  - "[[Literature/Authors/An Zhang|An Zhang]]"
  - "[[Literature/Authors/Yuxin Chen|Yuxin Chen]]"
  - "[[Literature/Authors/Leheng Sheng|Leheng Sheng]]"
  - "[[Literature/Authors/Xiang Wang|Xiang Wang]]"
  - "[[Literature/Authors/Tat‐Seng Chua|Tat‐Seng Chua]]"
source: "https://arxiv.org/html/2310.10108"
doi: "10.1145/3626772.3657844"
publication date: "2024-07-10"
tags:
  - "model"
  - "simulation"
  - "recommender_systems"
  - "llm_agents"
read status: Todo
⚠️:
  - audit failed
---

## Abstract

Recommender systems are the cornerstone of today’s information dissemination, yet a disconnect between offline metrics and online performance greatly hinders their development. Addressing this challenge, we envision a recommendation simulator, capitalizing on recent breakthroughs in human-level intelligence exhibited by Large Language Models (LLMs). We propose Agent4Rec, a user simulator in recommendation, leveraging LLM-empowered generative agents equipped with user profile, memory, and actions modules specifically tailored for the recommender system. In particular, these agents’ profile modules are initialized using real-world datasets (e.g., MovieLens, Steam, Amazon-Book), capturing users’ unique tastes and social traits; memory modules log both factual and emotional memories and are integrated with an emotion-driven reflection mechanism; action modules support a wide variety of behaviors, spanning both taste-driven and emotion-driven actions. Each agent interacts with personalized recommender models in a page-by-page manner, relying on a pre-implemented collaborative filtering-based recommendation algorithm. We delve into both the capabilities and limitations of Agent4Rec, aiming to explore an essential research question: “To what extent can LLM-empowered generative agents faithfully simulate the behavior of real, autonomous humans in recommender systems?” Extensive and multi-faceted evaluations of Agent4Rec highlight both the alignment and deviation between agents and user-personalized preferences. Beyond mere performance comparison, we explore insightful experiments, such as emulating the filter bubble effect and discovering the underlying causal relationships in recommendation tasks. Our codes are available at https://github.com/LehengTHU/Agent4Rec.

## Research Questions
> Research Questions extracted via LLM

- To what extent do LLM-powered agents simulate behavior and preferences in recommender systems?[^r1]
- How do agent memory, emotions, and recommender exposure affect simulated preference behavior and filter bubbles?[^r1]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?
- Agent4Rec simulates dataset-initialized users viewing personalized recommendations, with profile, factual/emotional memory, and LLM-driven actions.[^u1]

### How does it work?
The architecture separates user traits, memory, item descriptions, and recommendation policy.[^u1][^u2]

```yml
World:
  agents: [Agent]
  items: [Item]
  recommender: Random | Popularity | MF | LightGCN | MultVAE

Agent:
  tastes: str
  activity: 0..
  conformity: 0..
  diversity: u32
  memory: [Memory]
  reflection_after: u32 # configurable action count

Memory:
  description: str
  embedding: [f64]
  kind: Factual | Emotional

Item:
  quality: f64
  popularity: 0..
  genres: [str]
  summary: str
```

- Profile traits from histories: activity = interacted-item count; conformity = mean squared deviation of personal ratings from item-average ratings; diversity = number of distinct genres seen. Partition each trait into three uneven tiers. Summarize tastes from a random sample of historical items and ratings using ChatGPT.[^u1]
- Store recommended items, view/rating/exit feedback, satisfaction and fatigue as text and embedding memories. Retrieve relevant memories for decisions and append new experience. Reflect on satisfaction/fatigue after a configured action-count threshold; the paper does not give one universal threshold value.[^u3]
- A page shows item descriptions; the LLM chooses watch/skip, gives watched-item ratings and feelings, evaluates satisfaction/fatigue, then chooses continue/exit using emotional memory and activity trait. After exit, interview the agent for system ratings and explanations.[^u4]
- Item quality comes from historical ratings, popularity from review counts; few-shot LLM prompts generate genres and summaries from titles. Remove items with incorrect generated genres. The recommender is a replaceable module; separate experiments retrain with agent feedback between pages.[^u2]

The movie example and strategy evaluation use these fixed settings.[^u1][^u5]

```
AGENTS = 1000
PROFILE_HISTORY_ITEMS = 25
PROFILE_LIKE_MIN_RATING = 3
ITEM_GENRES = 18
ITEMS_PER_PAGE = 4
MAX_PAGES = 5
EVALUATION_LIKE_THRESHOLD = 3 # strict: rating > threshold
```

- The profile labels rating ≥`PROFILE_LIKE_MIN_RATING` as like, while strategy evaluation counts likes only above `EVALUATION_LIKE_THRESHOLD`; preserve this source distinction. Exit is enforced at `MAX_PAGES` in that experiment.[^u1][^u5]
- This extraction omits complete prompt wording, memory-retrieval implementation, and fitted recommendation algorithms. Actions are generated by LLM prompts, not a specified numerical transition law.[^u3][^u4]

### What can it answer?
- It compares ratings and social traits with real-user data, evaluates viewing/likes/exit/satisfaction, and explores feedback training, filter bubbles and causal discovery.[^u5]

### Where does it apply?
- It applies to the paper's recommendation datasets and configured user tasks; reported alignment includes deviations and does not establish universal human fidelity.[^u6]

## Metadata
### References
- [[IncorporatingSocialRoleTheoryIntoTopicModelsForSocialMediaContentAnalysis]]
- [[ANewApproachToEvaluatingNovelRecommendations]]
- [[ImageBasedRecommendationsOnStylesAndSubstitutes]]
- [[CognitiveNeuroscienceOfEmotionalMemory]]
- [[MatrixFactorizationTechniquesForRecommenderSystems]]
- [[CooperativeMultiAgentLearningTheStateOfTheArt]]
- [[ARoadmapOfAgentResearchAndDevelopment]]
- [[DirectlingamADirectMethodForLearningALinearNonGaussianStructuralEquationModel]]
- [[PrivateTraitsAndAttributesArePredictableFromDigitalRecordsOfHumanBehavior]]
- [[TrustworthyOnlineControlledExperiments]]
- [[TheNetflixRecommenderSystem]]
- [[CausalInferenceInStatisticsAPrimer]]
- [[VariationalAutoencodersForCollaborativeFiltering]]
- [[RecommendationSystemBasedOnDeepLearningMethodsASystematicReviewAndNewDirections]]
- [[KeepingDatasetBiasesOutOfTheSimulation]]
- [[BiasAndDebiasInRecommenderSystemASurveyAndFutureDirections]]
- [[UnresolvedReferenceD032E32C1D911CB6]]
- [[DisentanglingUserInterestAndConformityForRecommendationWithCausalEmbedding]]
- [[TopNRecommendationWithCounterfactualUserPreferenceSimulation]]
- [[CausprefCausalPreferenceLearningForOutOfDistributionRecommendation]]
- [[DeepLearningBasedRecommenderSystem]]
- [[ExploringTheFilterBubble]]
- [[InvariantCollaborativeFilteringToPopularityDistributionShift]]
- [[CausalDistillationForAlleviatingPerformanceHeterogeneityInRecommenderSystems]]
- [[SketchfacenerfSketchBasedFacialGenerationAndEditingInNeuralRadianceFields]]
- [[LetMeDoItForYouTowardsLlmEmpoweredRecommendationViaToolLearning]]
- [[LlaraLargeLanguageRecommendationAssistant]]
- [[ToolLearningWithFoundationModels]]
- [[UnresolvedReference29F267FC95E14916]]
- [[UnresolvedReference708AC4FC2600071C]]
- [[UnresolvedReference05982765C2246EED]]
- [[Far]]
- [[UnresolvedReferenceC2E69B3B2913A948]]
- [[ChallengesOfRealWorldReinforcementLearningCorr]]
- [[JenniferDEkstrandOghenemaroAnuyahDavidMcneillAndMariaSoledadPera]]
- [[IsItAnAgentOrJustAProgram]]
- [[2023ASMbox3SocialNetworkSimulationSystemWithLargeLanguageModelEmpoweredAgentsCorr]]
- [[CausalInferenceInRecommenderSystemsASurveyAndFutureDirectionsArxivPreprintArxiv220812397]]
- [[UnresolvedReference72E237DBA27161B3]]
- [[LanguageModelsRepresentSpaceAndTimeCorr]]
- [[TheMovielensDatasets]]
- [[UnresolvedReference3EE758A3AD1FB003]]
- [[RecommenderAiAgentIntegratingLargeLanguageModelsForInteractiveRecommendationsCorr]]
- [[RecSim- A Configurable Simulation Platform for Recommender SystemsCorr]]
- [[Mcauley]]
- [[UnresolvedReference0D5F8272B077456E]]
- [[AgentsimsAnOpenSourceSandboxForLargeLanguageModelEvaluationCorr]]
- [[TrainingSociallyAlignedLanguageModelsInSimulatedHumanSocietyCorr]]
- [[UnresolvedReferenceD4E64B68C0BCA405]]
- [[Lyu]]
- [[RocoDialecticMultiRobotCollaborationWithLargeLanguageModelsCorr]]
- [[UnresolvedReference16B86D16CDD436BD]]
- [[Kording]]
- [[IkramAmousAndFaiezGargouri]]
- [[UnresolvedReference9A037117F3319A9D]]
- [[PercyLiangAndMichaelS]]
- [[CommunicativeAgentsForSoftwareDevelopmentCorr]]
- [[RecogymAReinforcementLearningEnvironmentForTheProblemOfProductRecommendationInOnlineAdvertisingCorr]]
- [[VishakhPadmakumarNitishJoshiSeyedMehranKazemiNajoungKimAndHeHe]]
- [[MariaLomeliLukeZettlemoyerNicolaCanceddaAndThomasScialom]]
- [[AlgorithmOfThoughtsEnhancingExplorationOfIdeasInLargeLanguageModelsCorr]]
- [[VirtualTaobaoVirtualizingRealWorldOnlineRetailEnvironmentForReinforcementLearning]]
- [[UnresolvedReferenceEE0282DBC6535058]]
- [[2023CVoyagerAnOpenEndedEmbodiedAgentWithLargeLanguageModelsCorr]]
- [[ZheweiWeiAndJiRongWen2023BASurveyOnLargeLanguageModelBasedAutonomousAgentsCorr]]
- [[JunXuZhichengDouJunWangAndJiRongWen2023DWhenLargeLanguageModelBasedAgentMeetsUserBehaviorAnalysisANovelUserSimulationParadigmCorr]]
- [[2023ARecmindLargeLanguageModelPoweredAgentForRecommendationCorr]]
- [[QuocVLeAndDennyZhou]]
- [[AutogenEnablingNextGenLlmApplicationsViaMultiAgentConversationFrameworkCorr]]
- [[TheRiseAndPotentialOfLargeLanguageModelBasedAgentsASurveyCorr]]
- [[TowardsAutonomousSystemFlexibleModularProductionSystemEnhancedWithLargeLanguageModelAgentsCorr]]
- [[ExploringLargeLanguageModelsForCommunicationGamesAnEmpiricalStudyOnWerewolfCorr]]
- [[2023BBoostingDifferentiableCausalDiscoveryViaAdaptiveSampleReweightingIclr]]
- [[UnresolvedReference6E92F8F2B59DD67B]]
- [[UnresolvedReference537BE86C09CB74E5]]
- [[2023ACausalDistillationForAlleviatingPerformanceHeterogeneityInRecommenderSystems]]

## Audit Log
- Audit invalidated (2026-09-30): auditor admitted relying on spot checks and previous reports before clearing flags. A full independent audit is still required.
- 2026-09-30: Full-source design audit found previous note falsely claimed source unreadable; profile equations and emotional-memory mechanism omitted; watch/rate/continue/exit procedure omitted; profile/evaluation rating-boundary distinction omitted; strategy-evaluation page cap and outcomes omitted. Corrected against the source passages below; independent re-audit pending.[^design]

- WITHDRAWN audit claim (2026-09-30): incomplete source checks; this audit does not establish a pass.

## LLM Justification
[^r1]: The research questions are a concise transformation of the primary source’s abstract and stated aims. Source location: Section 2 “Agent4Rec” and evaluation sections. Source: [On Generative Agents in Recommendation](https://openreview.net/pdf/7c22be0db1de6ae7283850c35cbae6289e27413f.pdf).


[^u1]: §2.1.1: profile traits and equations, three uneven tiers, 25 sampled items, and like ≥3. Figure 1 and §1 specify 1000 agents and movie/MovieLens-1M example; the architecture also uses Steam and Amazon-Book.

[^u2]: §2.2: quality/popularity from ratings/reviews, eighteen generated genre categories, title-derived summaries and pruning; configurable recommendation algorithms. §3.4 studies retraining between recommendation pages.

[^u3]: §2.1.2: factual/emotional memory, text and vector storage, retrieval/writing/reflection; reflection is triggered after a predefined action count without a universal value stated there.

[^u4]: §2.1.3: taste-driven viewing/rating/feelings, emotional reasoning from page/memory, activity-aware exit, and post-exit interview.

[^u5]: §§3.1–3.5 compare alignment and strategies. §3.3 sets four movies/page, maximum five pages, likes rating >3, and viewing/likes/exit/satisfaction metrics; §4 examines filter bubbles and causal discovery.

[^u6]: §§3 and 6 discuss observed alignment and deviations, simulator limitations and future work.

[^design]: Source audit checked the full text at https://arxiv.org/html/2310.10108. Model footnotes identify the passages supporting the corrections.
