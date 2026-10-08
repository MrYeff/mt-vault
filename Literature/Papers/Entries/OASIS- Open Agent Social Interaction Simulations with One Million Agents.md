---
title: "OASIS: Open Agent Social Interaction Simulations with One Million Agents"
authors:
  - "[[Literature/Authors/Ziyi Yang|Ziyi Yang]]"
  - "[[Literature/Authors/Zaibin Zhang|Zaibin Zhang]]"
  - "[[Literature/Authors/Zirui Zheng|Zirui Zheng]]"
  - "[[Literature/Authors/Jiang, Yuxian|Jiang, Yuxian]]"
  - "[[Literature/Authors/Gan, Ziyue|Gan, Ziyue]]"
  - "[[Literature/Authors/Zhiyu Wang|Zhiyu Wang]]"
  - "[[Literature/Authors/Ling, Zijian|Ling, Zijian]]"
  - "[[Literature/Authors/Jinsong Chen|Jinsong Chen]]"
  - "[[Literature/Authors/Martz Ma|Martz Ma]]"
  - "[[Literature/Authors/Bowen Dong|Bowen Dong]]"
  - "[[Literature/Authors/Gupta, Prateek|Gupta, Prateek]]"
  - "[[Literature/Authors/Shanshan Hu|Shanshan Hu]]"
  - "[[Literature/Authors/Zhenfei Yin|Zhenfei Yin]]"
  - "[[Literature/Authors/Guohao Li|Guohao Li]]"
  - "[[Literature/Authors/Jia Yue Xu|Jia Yue Xu]]"
  - "[[Literature/Authors/Lijun Wang|Lijun Wang]]"
  - "[[Literature/Authors/Bernard Ghanem|Bernard Ghanem]]"
  - "[[Literature/Authors/Huchuan Lu|Huchuan Lu]]"
  - "[[Literature/Authors/Lu, Chaochao|Lu, Chaochao]]"
  - "[[Literature/Authors/Wanli Ouyang|Wanli Ouyang]]"
  - "[[Literature/Authors/Yushan Qiao|Yushan Qiao]]"
  - "[[Literature/Authors/Philip H. S. Torr|Philip H. S. Torr]]"
  - "[[Literature/Authors/Jing Fan Shao|Jing Fan Shao]]"
source: "https://arxiv.org/html/2411.11581"
doi: "10.48550/arXiv.2411.11581"
publication date: "2024-11-18"
tags:
  - "model"
  - "simulation"
  - "social_media"
  - "llm_agents"
read status: Todo
---

## Abstract

There has been a growing interest in enhancing rule-based agent-based models (ABMs) for social media platforms (i.e., X, Reddit) with more realistic large language model (LLM) agents, thereby allowing for a more nuanced study of complex systems. As a result, several LLM-based ABMs have been proposed in the past year. While they hold promise, each simulator is specifically designed to study a particular scenario, making it time-consuming and resource-intensive to explore other phenomena using the same ABM. Additionally, these models simulate only a limited number of agents, whereas real-world social media platforms involve millions of users. To this end, we propose OASIS, a generalizable and scalable social media simulator. OASIS is designed based on real-world social media platforms, incorporating dynamically updated environments (i.e., dynamic social networks and post information), diverse action spaces (i.e., following, commenting), and recommendation systems (i.e., interest-based and hot-score-based). Additionally, OASIS supports large-scale user simulations, capable of modeling up to one million users. With these features, OASIS can be easily extended to different social media platforms to study large-scale group phenomena and behaviors. We replicate various social phenomena, including information spreading, group polarization, and herd effects across X and Reddit platforms. Moreover, we provide observations of social phenomena at different agent group scales. We observe that the larger agent group scale leads to more enhanced group dynamics and more diverse and helpful agents’ opinions. These findings demonstrate OASIS’s potential as a powerful tool for studying complex systems in digital environments.

## Research Questions
> Research Questions extracted via LLM

- Can a general social-media simulation framework support multiple platform behaviors and large populations?[^r1]
- How do platform mechanisms and population scale affect diffusion and collective phenomena in the evaluated scenarios?[^r1]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?
- OASIS is a configurable X/Reddit-like social-media environment with LLM user agents, changing posts, interactions, and follow networks.[^o1]

### How does it work?
- Registration provides user profile/history, character description, and platform action description. The Environment Server stores users, posts, comments, relationships, action traces, and recommendations.[^o1]
- Each agent has hourly activation probabilities and memory of encountered content, engagement counts, its previous actions, and rationales. The Time Engine activates agents probabilistically; RecSys supplies visible posts; an LLM chooses permitted actions and rationale; actions update the database and social network.[^o2]

These constants describe the paper's timing, capabilities and Reddit score.[^o2][^o3]

```
HOURS_PER_DAY = 24
STEP_MINUTES = 3
ACTION_SPACE_SIZE = 21
MAX_AGENTS = 1000000
REDDIT_EPOCH = 1134028003
HOT_TIME_SCALE = 45000
HOT_MIN_COUNT = 1
```

- Supported actions include registration, refresh/trends/search, post/repost/comment, follow/unfollow, mute/unmute, like/unlike, dislike/undo, corresponding comment votes, and doing nothing. Scenarios select subsets rather than making every action mandatory.[^o3]
- **X feed:** rank followed users' posts by likes; score out-of-network posts by `recency * follower_score * similarity`. Similarity is TwHIN-BERT cosine similarity between post and user profile/recent-content embeddings; follower score is `max(1,log_1000(followers+1))`. Appendix D.3 defines recency as `ln((271.8-(current-created))/100)`; its time-unit/cutoff treatment is not specified in that formula.[^o4]
- **Reddit feed:** with `votes=upvotes-downvotes`, Eq. (1) uses `log10(max(abs(votes),HOT_MIN_COUNT)) + sign(votes)*(created-REDDIT_EPOCH)/HOT_TIME_SCALE`. Rank by this score and retain top-k, with k chosen per experiment.[^o4]
- RecSys stores a ranked recommendation pool; refresh samples a subset to display. LLM decisions depend on persona, visible posts, memory and prompts; no fixed numerical human-response probability is asserted.[^o4][^o2]
- **X information propagation:** 198 Twitter15/Twitter16 rumor cascades (100–700 users each) use the actions like, repost, follow, and do nothing for up to 50 three-minute steps. Compare propagation scale, depth, and maximum breadth with real cascades using normalized RMSE; reported average error is about 30%, with simulated depth below the observed trend.[^o5]
- **X group polarization:** 196 real users form the core group. In the dilemma scenario, collect advice every 10 steps across 80 steps and compare extremity with GPT-4o-mini for uncensored versus aligned Llama-3-8B. A separate 30-step scale study compares populations of 196, 10,196, and 100,196 while reusing the same core users; larger populations yield more diverse and rated-helpful opinions.[^o5]
- **Reddit herd effects:** the human-comparison experiment uses 116,932 comments across seven topics, 3,600 generated agents, and 40 steps; a controlled poster adds 200 posts per step, each agent activates with probability 0.1, and the RecSys caches the top 300. For counterfactuals, use 21,919 items and 30 steps; the scale comparison uses 100/1,000/10,000 agents, activation 0.1, five sampled posts per active agent, and cache sizes 50/500/5,000. Both assign up-treated (one initial like), down-treated (one initial dislike), and untreated controls; larger groups show clearer herd effects, especially following initial dislikes.[^o5]
- This compact extraction omits database schema details, full prompt templates, profile-generation sampling, and scenario-specific action subsets. Platform choice, LLM, activation vectors, recommendations and prompts are experiment inputs.[^o6]

### What can it answer?
- It tests information diffusion, polarization and voting herd effects under specified platform/agent configurations and population scales.[^o5]

### Where does it apply?
- It supports configurable social-media experiments; fidelity depends on the chosen scenario and is assessed against the paper's empirical comparisons.[^o5][^o6]

## Metadata
### References
- [[EmergenceOfScalingInRandomNetworks]]
- [[CombatingMisinformationInTheAgeOfLlmsOpportunitiesAndChallenges]]
- [[UsingNeuralNetworksToCalibrateAgentBasedModelsEnablesImprovedRegionalEvidenceForVaccineStrategyAndPolicy]]
- [[OnTheLimitsOfAgencyInAgentBasedModels]]
- [[SingleDocumentAutomaticTextSummarizationUsingTermFrequencyInverseDocumentFrequencyTfIdf]]
- [[SafeRlhfSafeReinforcementLearningFromHumanFeedback]]
- [[BertPreTrainingOfDeepBidirectionalTransformersForLanguageUnderstanding]]
- [[RedditUserAgeGenderDemographics2024]]
- [[S3SocialNetworkSimulationSystemWithLargeLanguageModelEmpoweredAgents]]
- [[AgentscopeAFlexibleYetRobustMultiAgentPlatform]]
- [[UsingAgentBasedModellingToEvaluateTheImpactOfAlgorithmicCurationOnSocialMedia]]
- [[AgentBasedModels]]
- [[First100DaysOfPandemicAnInterplayOfPharmaceuticalBehavioralAndDigitalInterventionsAStudyUsingAgentBasedModeling]]
- [[HowFarAreWeOnTheDecisionMakingOfLlmsEvaluatingLlmsGamingAbilityInMultiAgentEnvironments]]
- [[TheImpactOfGroupPolarizationOnTheQualityOfOnlineDebateInSocialMediaASystematicLiteratureReview]]
- [[GroupPolarizationACriticalReviewAndMetaAnalysis]]
- [[ScalingLawsForNeuralLanguageModels]]
- [[AdvancesInSocialMediaResearchPastPresentAndFuture]]
- [[WhatIsAComplexSystem]]
- [[HeterogeneousExpectationsLeadingToBubblesAndCrashesInAssetMarketsTippingPointHerdingBehaviorAndGroupEffectInAnAgentBasedModel]]
- [[CamelCommunicativeAgentsForMindExplorationOfLargeLanguageModelSociety]]
- [[SocialPsychology]]
- [[TrainingSociallyAlignedLanguageModelsOnSimulatedSocialInteractions]]
- [[RealTimeRumorDebunkingOnTwitter]]
- [[DetectingRumorsFromMicroblogsWithRecurrentNeuralNetworks]]
- [[ChisimAnAgentBasedSimulationModelOfSocialInteractionsInALargeUrbanArea]]
- [[LocatingAndEditingFactualAssociationsInGpt]]
- [[EthicsOfSocialMediaResearchCommonConcernsAndPracticalConsiderations]]
- [[CanLlmAugmentedAutonomousAgentsCooperateAnEvaluationOfTheirCooperativeCapabilitiesThroughMeltingPot]]
- [[UnveilingTheTruthAndFacilitatingChangeTowardsAgentBasedLargeScaleSocialMovementSimulation]]
- [[SocialInfluenceBiasARandomizedExperiment]]
- [[SocialMediaNeedsScienceBasedGuidelines]]
- [[Nomic]]
- [[TheGreatRewiringIsSocialMediaReallyBehindAnEpidemicOfTeenageMentalIllness]]
- [[Social Simulacra- Creating Populated Prototypes for Social Computing Systems]]
- [[GenerativeAgentsInteractiveSimulacraOfHumanBehavior]]
- [[GenerativeAgentSimulationsOf1000People]]
- [[PushshiftReddit202303]]
- [[CommunicativeAgentsForSoftwareDevelopment]]
- [[ToolllmFacilitatingLargeLanguageModelsToMaster16000RealWorldApis]]
- [[SentenceBertSentenceEmbeddingsUsingSiameseBertNetworks]]
- [[EmergenceOfSocialNormsInLargeLanguageModelBasedAgentSocieties]]
- [[HowRedditRankingAlgorithmsWorkDec2015]]
- [[ModelsOfSegregation]]
- [[DynamicSpiralsPutToTestAnAgentBasedModelOfReinforcingSpiralsBetweenSelectiveExposureInterpersonalNetworksAndAttitudePolarization]]
- [[TheAlgorithm]]
- [[TheSpreadOfTrueAndFalseNewsOnline]]
- [[HowToMitigateMisinformation]]
- [[User Behavior Simulation with Large Language Model based Agents]]
- [[SibylSimpleYetEffectiveAgentFrameworkForComplexRealWorldReasoning]]
- [[ChainOfThoughtPromptingElicitsReasoningInLargeLanguageModels]]
- [[MostUsersDoNotFollowPoliticalElitesOnTwitterThoseWhoDoShowOverwhelmingPreferencesForIdeologicalCongruity]]
- [[MinelandSimulatingLargeScaleMultiAgentInteractionsWithLimitedMultimodalSensesAndPhysicalNeeds]]
- [[ScalingVisionTransformers]]
- [[On Generative Agents in Recommendation]]
- [[TwhinBertASociallyEnrichedPreTrainedLanguageModelForMultilingualTweetRepresentationsAtTwitter]]
- [[ExpelLlmAgentsAreExperientialLearners]]
- [[WebarenaARealisticWebEnvironmentForBuildingAutonomousAgents]]
- [[SotopiaInteractiveEvaluationForSocialIntelligenceInLanguageAgents]]

## Audit Log
- 2026-10-03: Independent full-source re-audit passed. Full arXiv v5 body, appendices A–I, scenario controls/outcomes and all 59 references independently checked. `audit failed` removed after the pass.
- Audit invalidated (2026-09-30): auditor admitted relying on spot checks and previous reports before clearing flags. A full independent audit is still required.
- 2026-09-30: Full-source design audit found missing recommendation ranking mechanics; omitted feed refresh sampling and activation timing; unexplained scenario control conditions; configurable framework scope insufficiently exposed. Corrected against the source passages below; independent re-audit pending.[^design]
- Independent source audit found the architecture, information flow, observation/action process, and experiment setup too generic. The note now names the five components and their roles and clarifies the platform interaction loop and study-specific setup. At that stage, independent re-audit remained pending.

- WITHDRAWN audit claim (2026-09-30): incomplete source checks; this audit does not establish a pass.

## LLM Justification
[^r1]: The research questions are a concise transformation of the primary source’s abstract and stated aims. Source location: Framework/agent design and evaluation sections. Source: [OASIS: Open Agent Social Interaction Simulations with One Million Agents](https://arxiv.org/abs/2411.11581).


[^o1]: §§2.1–2.2 and Figure 2: registration and simulation workflow; Environment Server tables and dynamic updates.

[^o2]: §§2.1, 2.4–2.5: memory/action modules, LLM action/rationale generation, 24-dimensional activation vector, three-minute step, and optional real-time scaling.

[^o3]: §2.4 lists 21 actions; Table 1 lists maximum 1M population; §3.2 and Appendix F.1 explain scenario action restrictions.

[^o4]: §2.3 Eq. (1) supplies the exact Reddit hot-score expression. Appendix D.3 Eqs. (2)–(5) supplies X multiplicative score and recency/fan/embedding components, and describes recommendation-table subset sampling on refresh. The hot-score formula is transcribed from this paper, not replaced with another implementation.

[^o5]: §§3.1–3.5 and §3.2 settings; Appendix E.1–E.3 and F.1–F.4: 198 cascades, group-polarization and herd sample sizes, time steps, action subsets, activation and feed-cache controls, vote treatments, normalized RMSE and extremity/helpfulness measures.

[^o6]: Appendices D–F contain platform, generation, prompt and experiment details; §§2–3 make scenario configurability explicit.

[^design]: Source audit checked the full text at https://arxiv.org/html/2411.11581. Model footnotes identify the passages supporting the corrections.
