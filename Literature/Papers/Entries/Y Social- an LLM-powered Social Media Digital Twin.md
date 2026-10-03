---
title: "Y Social: an LLM-powered Social Media Digital Twin"
tags:
  - model
  - simulation
authors:
  - "[[Literature/Authors/Giulio Rossetti|Giulio Rossetti]]"
  - "[[Literature/Authors/Massimo Stella|Massimo Stella]]"
  - "[[Literature/Authors/Rémy Cazabet|Rémy Cazabet]]"
  - "[[Literature/Authors/Katherine Abramski|Katherine Abramski]]"
  - "[[Literature/Authors/Erica Cau|Erica Cau]]"
  - "[[Literature/Authors/Salvatore Citraro|Salvatore Citraro]]"
  - "[[Literature/Authors/Andrea Failla|Andrea Failla]]"
  - "[[Literature/Authors/Riccardo Improta|Riccardo Improta]]"
  - "[[Literature/Authors/Virginia Morini|Virginia Morini]]"
  - "[[Literature/Authors/Valentina Pansanella|Valentina Pansanella]]"
publication date: 2024-08-01
source: https://arxiv.org/pdf/2408.00818
doi: 10.48550/arXiv.2408.00818
read status: Todo
⚠️:
  - audit failed
---
## Abstract

In this paper we introduce Y, a new-generation digital twin designed to replicate an online social media platform. Digital twins are virtual replicas of physical systems that allow for advanced analyses and experimentation. In the case of social media, a digital twin such as Y provides a powerful tool for researchers to simulate and understand complex online interactions. {\tt Y} leverages state-of-the-art Large Language Models (LLMs) to replicate sophisticated agent behaviors, enabling accurate simulations of user interactions, content dissemination, and network dynamics. By integrating these aspects, Y offers valuable insights into user engagement, information spread, and the impact of platform policies. Moreover, the integration of LLMs allows Y to generate nuanced textual content and predict user responses, facilitating the study of emergent phenomena in online environments. To better characterize the proposed digital twin, in this paper we describe the rationale behind its implementation, provide examples of the analyses that can be performed on the data it enables to be generated, and discuss its relevance for multidisciplinary research.

## Research Questions
> Research Questions extracted via LLM

- How can Y Social provide a configurable, LLM-powered digital twin for controlled simulation and analysis of online social-media interactions?[^r1]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?
Y Social combines a REST platform/data server, an LLM server and one or more synchronized simulation clients to model content and social ties.[^r2]

The state/action types and schedule summarize Figure 2 and Algorithm 1; configurable servers, clients and recommenders are opaque interfaces.[^r2][^r3]

```yml
World:
  users: [User]
  posts: [Post]
  follows: [(UserId, UserId)]
  news: [Article]
  clock: (day: u32, slot: u32)

User:
  profile: # prompted role
    age: u32
    leaning: str
    education: str
    nationality: str
    languages: [str]
    interests: [str]
    big_five: [High | Low] # five dimensions;32 combinations
  llm: ...
  content_recommender: ...
  follow_recommender: ...
  round_actions: u32

Post:
  author: UserId
  parent: PostId?
  text: str
  mentions: [UserId]
  hashtags: [str]
  reactions: [UserId -> Like | Dislike | Neutral]
  emotions: [str]
  created_round: u32
  original_shared_news: PostId?

Article:
  title: str
  summary: str
  source: str

Action: News | Post | Comment | Reply | Share | Read | Search | None | Follow
```

### How does it work?
The workflow follows Algorithm 1; its second follow loop iterates over all agents, while its comment says only a configured fraction of active agents follows. This loop/comment discrepancy is retained rather than silently resolving it.[^r3]

```
sim_loop(mut world: World, config: ...):
  generate/register users; connect platform and LLM servers
  for day in config.days:
    for slot in config.slots:
      h = platform.current_slot() # synchronize each client
      count = int(|world.users| * config.hourly_activity[h])
      active = random_sample_without_replacement(world.users, count)
      for user in active:
        LLM.select_action([News, Post, Comment, Reply, Share,
                           Read, Search, None])
        execute selected action(s) within user's round_actions
      for user in world.users: # literal Algorithm1 follow loop
        select_action([Follow, None])
        # comment: configured daily-follow fraction among active agents
    add config.new_agents_per_iteration users
```

- `Read`: rank a content shortlist, randomly choose one, prompt YES/NO/NEUTRAL, store reaction; then ask whether to follow/unfollow its author. `Post`: generate a new interest-topic discussion. `Comment`: generate a contribution with configured preceding-thread context. `Reply`: target threads recently mentioning the agent; `Search`: filter by hashtags used in its recent posts.[^r4]
- `Follow`: rank candidates, transform scores to probabilities and sample a tie; direct selection is topology-driven, with no LLM prompt. `News`: comment on an RSS article's title/summary; `Share`: repost previously shared news with a new comment and retain origin linkage. Generated text has extracted mentions/hashtags and GoEmotions annotations; role prompts condition on profile and request up to200 characters.[^r4]
- Content recommenders: random, reverse chronology, recent popularity (`likes+dislikes`), follower-based, follower-plus-popularity; each returns `k` recent items and can include a configurable non-follower share. Tie recommenders: random, common-neighbor count, Jaccard, Adamic–Adar and degree-product preferential attachment; optional political homophily bias. Visibility and context windows are configured, rather than universal constants.[^r5]

### What can it answer?
- The political demonstration begins with1000 users, adds10/day for100 days (2400 hourly rounds), and ends with2000. The paper calls its model `llama3-7b`; content uses ReverseChronoFollowersPopularity with60% followed-author exposure, tie suggestions use preferential attachment, visibility is36 rounds, and sources comprise600 curated RSS feeds.[^r6]
- Descriptive analyses cover content/reactions/emotions, networks, topology and controversy; this demonstrates available outputs rather than validates human behavior.[^r6]

The generic configuration example prints `days=365`, although adjacent prose describes100; these are separate/conflicting example settings, so the case-study duration above follows §4.1 explicitly.[^r3][^r6]

### Where does it apply?
- Configure social-media scenarios, distributed clients, mixed LLMs, and changes to curation, profiles, and news.[^r2][^r3][^r6]
- Empirical activity rates initialize hourly activation.[^r2][^r3][^r6]
- Predictive fidelity depends on the scenario; the demonstration does not establish it.[^r2][^r3][^r6]

## Metadata
### References

- [[VoicesOfRapeCognitiveNetworksLinkPassiveVoiceUsageToPsychologicalDistressInOnlineNarratives]]
- [[CognitiveNetworkScienceRevealsBiasInGpt3Gpt35TurboAndGpt4MirroringMathAnxietyInHighSchoolStudents]]
- [[Gpt4TechnicalReport]]
- [[FriendsAndNeighborsOnTheWeb]]
- [[Llama3ModelCard]]
- [[ASystematicReviewOfMachineLearningTechniquesForStanceDetectionAndItsApplications]]
- [[MoreIsDifferentBrokenSymmetryAndTheNatureOfTheHierarchicalStructureOfScience]]
- [[DataMiningForTheSocialSciencesAnIntroduction]]
- [[EffectiveChoiceInThePrisonerSDilemma]]
- [[AgentBasedModelingInEconomicsAndFinancePastPresentAndFuture]]
- [[ScaleFreeNetworksADecadeAndBeyond]]
- [[ScaleFreeNetworks]]
- [[TweetingFromLeftToRightIsOnlinePoliticalCommunicationMoreThanAnEchoChamber]]
- [[ASurveyOnDigitalTwinDefinitionsCharacteristicsApplicationsAndDesignImplications]]
- [[AuditingAlgorithmicBiasOnTwitter]]
- [[ModelingEchoChambersAndPolarizationDynamicsInSocialNetworks]]
- [[SocialMediaUseAndMentalHealthAmongYoungAdults]]
- [[AgentBasedModelsInSociology]]
- [[QuantitativeSocialScienceTheSurvey]]
- [[SocialMediaAndMentalHealth]]
- [[ThePersuasivePowerOfLargeLanguageModels]]
- [[EchoChambersRabbitHolesAndAlgorithmicBiasHowYoutubeRecommendsContentToRealUsers]]
- [[LanguageModelsAreFewShotLearners]]
- [[MultimodalSentimentalAnalysisForSocialMediaApplicationsAComprehensiveReview]]
- [[AnEmpiricalSurveyOfDataAugmentationForLimitedDataLearningInNlp]]
- [[OpinionDynamicsWithBackfireEffectAndBiasedAssimilation]]
- [[DoTheSociallyRichGetRicherANuancedPerspectiveOnSocialNetworkSiteUseAndOnlineSocialCapitalAccrual]]
- [[AnalyzingTheImpactOfFilterBubblesOnSocialNetworkPolarization]]
- [[IntroductionToModernInformationRetrieval]]
- [[SimulatingOpinionDynamicsWithNetworksOfLlmBasedAgents]]
- [[TheEchoChamberEffectOnSocialMedia]]
- [[The Effect of People Recommenders on Echo Chambers and Polarization]]
- [[ManifestoOfComputationalSocialScience]]
- [[TheGameOfLife]]
- [[StsEprModellingIndividualMobilityConsideringTheSpatialTemporalAndSocialDimensionsTogether]]
- [[ADecadeOfSocialBotDetection]]
- [[CooperationBehaviouralSynchronyAndStatusInSocialNetworks]]
- [[ASimulationBasedApproachToAnalyzeTheInformationDiffusionInMicrobloggingOnlineSocialNetwork]]
- [[IntroducingCounsellmeADatasetOfSimulatedMentalHealthDialoguesForComparingLlmsLikeHaikuLlamantinoAndChatgptAgainstHumans]]
- [[EmergenceOfScaleFreeNetworksInSocialInteractionsAmongLargeLanguageModels]]
- [[Mixing beliefs among interacting agents]]
- [[EchoChambersInTheAgeOfMisinformation]]
- [[ModelingConfirmationBiasAndPolarization]]
- [[GoemotionsADatasetOfFineGrainedEmotions]]
- [[ModelingCivilViolenceAnAgentBasedComputationalApproach]]
- [[ExposureInequalityInPeopleRecommenderSystemsTheLongTermEffects]]
- [[IMInTheBlueskyTonightInsightsFromAYearWorthOfSocialData]]
- [[LinkRecommendationsTheirImpactOnNetworkStructureAndMinorities]]
- [[TheRiseOfSocialBots]]
- [[ATheoryOfSocialComparisonProcesses]]
- [[LimitsOfLargeLanguageModelsInDebatingHumans]]
- [[S3SocialNetworkSimulationSystemWithLargeLanguageModelEmpoweredAgents]]
- [[TheRoleOfHomophilyInTheEmergenceOfOpinionControversies]]
- [[QuantifyingControversyOnSocialMedia]]
- [[UsingAgentBasedModellingToEvaluateTheImpactOfAlgorithmicCurationOnSocialMedia]]
- [[UnderstandingEchoChambersInECommerceRecommenderSystems]]
- [[EmergenceInSocialSimulation]]
- [[SimulationForTheSocialScientist]]
- [[TheStrengthOfWeakTies]]
- [[LessThanYouThinkPrevalenceAndPredictorsOfFakeNewsDisseminationOnFacebook]]
- [[InformationDiffusionInOnlineSocialNetworksASurvey]]
- [[ACloserLookAtSkipGramModelling]]
- [[HumanLikeIntuitiveBehaviorAndReasoningBiasesEmergedInLargeLanguageModelsButDisappearedInChatgpt]]
- [[ASurveyOnStanceDetectionForMisAndDisinformationIdentification]]
- [[CommunityCrossInstructUnsupervisedInstructionGenerationForAligningLargeLanguageModelsToOnlineCommunities]]
- [[DisinformationAndMisinformationThroughTheInternetFindingsOfAnExploratoryStudy]]
- [[CommunicatingWithAlgorithmsATransferEntropyAnalysisOfEmotionsBasedEscapesFromOnlineEchoChambers]]
- [[DigitalTwinsInSportConceptsTaxonomiesChallengesAndPracticalPotentials2024]]
- [[WillTheGlobalVillageFractureIntoTribesRecommenderSystemsAndTheirEffectsOnConsumerFragmentation]]
- [[CausallyEstimatingTheEffectOfYoutubeSRecommenderSystemUsingCounterfactualBots]]
- [[MiningTriadicClosurePatternsInSocialNetworks]]
- [[ThePrinciplesOfExperimentalDesignAndTheirApplicationInSociology]]
- [[EvaluatingAndInducingPersonalityInPreTrainedLanguageModels]]
- [[DegenerateFeedbackLoopsInRecommenderSystems]]
- [[OnTheInadequacyOfNominalAssortativityForAssessingHomophilyInNetworks]]
- [[AlgorithmicBiasReviewSynthesisAndFutureResearchDirections]]
- [[ChallengesOfHateSpeechDetectionInSocialMediaDataScarcityAndLeveragingExternalResources]]
- [[ExperimentalEvidenceOfMassiveScaleEmotionalContagionThroughSocialNetworks]]
- [[SentimentAnalysisInTheAgeOfGenerativeAi]]
- [[StanceDetectionASurvey]]
- [[OpenModelsClosedMindsOnAgentsCapabilitiesInMimickingHumanPersonalitiesThroughOpenLargeLanguageModels]]
- [[DoLlmAgentsExhibitSocialBehavior]]
- [[ASurveyOnDeepLearningForNamedEntityRecognition]]
- [[LargeLanguageModelEmpoweredAgentsForSimulatingMacroeconomicActivities]]
- [[TheLinkPredictionProblemForSocialNetworks]]
- [[ArgumentationMiningStateOfTheArtAndEmergingTrends]]
- [[AgentBasedSocialSimulationOfTheCovid19PandemicASystematicReview]]
- [[DividedByTheAlgorithmTheLimitedEffectsOfContentAndSentimentBasedNewsRecommendationOnAffectiveIdeologicalAndPerceivedPolarization]]
- [[AnIntroductionToTheFiveFactorModelAndItsApplications]]
- [[Birds of a Feather- Homophily in Social Networks]]
- [[QuantificationInSocialNetworks]]
- [[StanceAndSentimentInTweets]]
- [[TheLanguageOfOpinionChangeOnSocialMediaUnderTheLensOfCommunicativeAction]]
- [[LearningOpinionDynamicsFromSocialTraces]]
- [[FlamingOnYoutube]]
- [[FromPerilsToPossibilitiesUnderstandingHowHumanAndAiBiasesAffectOnlineFora]]
- [[TowardAStandardApproachForEchoChamberDetectionRedditCaseStudy]]
- [[UnveilingTheTruthAndFacilitatingChangeTowardsAgentBasedLargeScaleSocialMovementSimulation]]
- [[StatisticalMethodsInSocialScienceResearch]]
- [[AnAgentBasedModelOfMessagePropagationInTheFacebookElectronicSocialNetwork]]
- [[ClusteringAndPreferentialAttachmentInGrowingNetworks]]
- [[MixingPatternsInNetworks]]
- [[TheStructureAndFunctionOfComplexNetworks]]
- [[CognitiveIslandsAndRunawayEchoChambersProblemsForEpistemicDependenceOnExperts]]
- [[EchoChambersAndEpistemicBubbles]]
- [[FromMeanFieldToComplexTopologiesNetworkEffectsOnTheAlgorithmicBiasModel]]
- [[ModelingAlgorithmicBiasSimplicialComplexesAndEvolvingNetworkTopologies]]
- [[MassMediaImpactOnOpinionEvolutionInBiasedDigitalEnvironmentsABoundedConfidenceModel]]
- [[NetworkFormationAndDynamicsAmongMultiLlms]]
- [[ASurveyOnTheImpactOfAiBasedRecommendersOnHumanBehavioursMethodologiesOutcomesAndFutureDirections]]
- [[TheFilterBubbleWhatTheInternetIsHidingFromYou]]
- [[GenerativeAgentsInteractiveSimulacraOfHumanBehavior]]
- [[Social Simulacra- Creating Populated Prototypes for Social Computing Systems]]
- [[HumanAiCoevolution]]
- [[FightingMisinformationOnSocialMediaUsingCrowdsourcedJudgmentsOfNewsSourceQuality]]
- [[ThePsychologyOfFakeNews]]
- [[OpinionFormationOnSocialNetworksWithAlgorithmicBiasDynamicsAndBiasImbalance]]
- [[EffectOfAlgorithmicBiasAndNetworkStructureOnCoexistenceConsensusAndPolarizationOfOpinions]]
- [[MultidimensionalPoliticalPolarizationInOnlineSocialNetworks]]
- [[ThisSmartTownAinTBigEnoughSmartSmallTownsAndDigitalTwinsForSustainableUrbanAndRegionalDevelopment]]
- [[ModellingOpinionDynamicsInTheAgeOfAlgorithmicPersonalisation]]
- [[CooperateOrCollapseEmergenceOfSustainabilityBehaviorsInASocietyOfLlmAgents]]
- [[OpinionDynamicsOnInteractingNetworksMediaCompetitionAndSocialInfluence]]
- [[TheAmplificationParadoxInRecommenderSystems]]
- [[FacebookAndTextingMadeMeDoItMediaInducedTaskSwitchingWhileStudying]]
- [[ConformityAPathAwareHomophilyMeasureForNodeAttributedNetworks]]
- [[TheClosedLoopBetweenOpinionFormationAndPersonalizedRecommendations]]
- [[AnalyzingTheChangingLandscapeOfTheCovid19VaccineDebateOnTwitter]]
- [[DynamicModelsOfSegregation]]
- [[ExperimentableDigitalTwinsStreamliningSimulationBasedSystemsEngineeringForIndustry40]]
- [[AnAgentBasedModelOfCollectiveEmotionsInOnlineCommunities]]
- [[ValidatingViralMarketingStrategiesInTwitterViaAgentBasedSocialSimulation]]
- [[QuasiExperimentsInterruptedTimeSeriesDesigns]]
- [[WhenLlmMeetsHypergraphASociologicalAnalysisOnPersonalityViaOnlineSocialNetworks]]
- [[SocialMediaItsImpactWithPositiveAndNegativeAspects]]
- [[AlgorithmicBiasAmplifiesOpinionFragmentationAndPolarizationABoundedConfidenceModel]]
- [[SocialSimulationInTheSocialSciencesABriefOverview]]
- [[InfluenceOfAugmentedHumansInOnlineInteractionsDuringVotingEvents]]
- [[BotsIncreaseExposureToNegativeAndInflammatoryContentInOnlineSocialSystems]]
- [[UsingCognitivePsychologyToUnderstandGptLikeModelsNeedsToExtendBeyondHumanBiases]]
- [[TheOnlineDisinhibitionEffect]]
- [[DigitalTwinInHealthcareRecentUpdatesAndChallenges]]
- [[CognitiveLoadDuringProblemSolvingEffectsOnLearning]]
- [[DigitalTwinInIndustryStateOfTheArt]]
- [[SelfEnhancementThroughOnlineDatingProfilesTheRoleOfAnticipatedFutureInteractionSelfDisclosureAndPerceivedSuccessInMateAttraction]]
- [[EchoChambersAndViralMisinformationModelingFakeNewsAsComplexContagion]]
- [[SimulatingSocialMediaUsingLargeLanguageModelsToEvaluateAlternativeNewsFeedAlgorithms]]
- [[TheDriversOfOnlinePolarizationFittingModelsToData]]
- [[FriendNetworkingSitesAndTheirRelationshipToAdolescentsWellBeingAndSocialSelfEsteem]]
- [[JournalistsOnTwitterSelfBrandingAudiencesAndInvolvementOfBots]]
- [[ModellingDynamicalProcessesInComplexSocioTechnicalSystems]]
- [[SocialComparisonSocialMediaAndSelfEsteem]]
- [[ThatIsYourEvidenceClassifyingStanceInOnlinePoliticalDebate]]
- [[ComputerMediatedCommunicationImpersonalInterpersonalAndHyperpersonalInteraction]]
- [[SocialNetworkAnalysisMethodsAndApplications]]
- [[DigitalTwinOrientedComplexNetworkedSystemsBasedOnHeterogeneousNodeFeaturesAndInteractionRules]]
- [[CanLargeLanguageModelAgentsSimulateHumanTrustBehaviors]]
- [[UrbanGenerativeIntelligenceUgiAFoundationalPlatformForAgentsInEmbodiedCityEnvironment]]
- [[BubblesBurstingInvestigatingAndMeasuringThePersonalisationOfSocialMediaSearches]]
- [[TheSocialDigitalTwinTheSocialTurnInTheFieldOfSmartCities]]
- [[TheImpactOfYoutubeRecommendationSystemOnVideoViews]]


## Audit Log
- Audit invalidated (2026-09-30): auditor admitted incomplete independent checks and premature flag removal. Previous valid audits, if any, remain separate.

- 2026-09-30: Initial/cheap audit failed; stronger source review corrected Algorithm1 exact active-count schedule and follow-loop conflict, state/observations, primitive action mechanisms, recommender scoring and case-study configuration. Independent re-audit pending.

- WITHDRAWN audit claim (2026-09-30): the remaining-audit-c report overstated independent source checks; it does not establish a pass.

## LLM Justification
[^r1]: https://arxiv.org/html/2408.00818; Abstract and Introduction: platform digital-twin aims.
[^r2]: Same source; §3, Figure1 and Figure2: architecture and stored user/content/news/follow/clock state.
[^r3]: Same source; §3.2.2 “Simulation Configuration” and “Simulation workflow,” Algorithm1: fixed-count activity sampling, synchronization, action and second follow loops, daily growth; comment versus loop eligibility discrepancy; example days365 versus adjacent prose100.
[^r4]: Same source; §3.2.1 “Actions and Prompts”: READ selection/reaction, POST, COMMENT/REPLY/SEARCH context/filters, FOLLOW probability sampling, NEWS/SHARE prompts and annotations; profile preprompt and five BigFive dimensions.
[^r5]: Same source; §3.1.1 “Content Recommendations” and “Follows Recommendations”: ranking variants, k, exposure share and homophily bias.
[^r6]: Same source; §4.1 simulation configuration and §4.2 generated-data examples:100days/2400rounds/1000→2000, stated llama3-7b, recommenders,60%,36rounds,600feeds and descriptive scope.
