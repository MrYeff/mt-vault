---

title: "Generative agent-based modeling with actions grounded in physical, social, or digital space using Concordia"
tags: [model, simulation, agent_based_modeling, llm, concordia]
authors:
  - "[[Literature/Authors/Alexander Sasha Vezhnevets|Alexander Sasha Vezhnevets]]"
  - "[[Literature/Authors/John Agapiou|John Agapiou]]"
  - "[[Literature/Authors/Avia Aharon|Avia Aharon]]"
  - "[[Literature/Authors/Ron Ziv|Ron Ziv]]"
  - "[[Literature/Authors/Jayd Matyas|Jayd Matyas]]"
  - "[[Literature/Authors/Edgar A. Duéñez‐Guzmán|Edgar A. Duéñez‐Guzmán]]"
  - "[[Literature/Authors/William A. Cunningham|William A. Cunningham]]"
  - "[[Literature/Authors/Simon Osindero|Simon Osindero]]"
  - "[[Literature/Authors/Danny Karmon|Danny Karmon]]"
  - "[[Literature/Authors/Joel Z. Leibo|Joel Z. Leibo]]"
publication date: 2023-12-06
source: https://arxiv.org/abs/2312.03664
doi: 10.48550/arXiv.2312.03664
read status: Todo
⚠️: []
---

## Abstract

Agent-based modeling has been around for decades, and applied widely across the social and natural sciences. The scope of this research method is now poised to grow dramatically as it absorbs the new affordances provided by Large Language Models (LLM)s. Generative Agent-Based Models (GABM) are not just classic Agent-Based Models (ABM)s where the agents talk to one another. Rather, GABMs are constructed using an LLM to apply common sense to situations, act "reasonably", recall common semantic knowledge, produce API calls to control digital technologies like apps, and communicate both within the simulation and to researchers viewing it from the outside. Here we present Concordia, a library to facilitate constructing and working with GABMs. Concordia makes it easy to construct language-mediated simulations of physically- or digitally-grounded environments. Concordia agents produce their behavior using a flexible component system which mediates between two fundamental operations: LLM calls and associative memory retrieval. A special agent called the Game Master (GM), which was inspired by tabletop role-playing games, is responsible for simulating the environment where the agents interact. Agents take actions by describing what they want to do in natural language. The GM then translates their actions into appropriate implementations. In a simulated physical world, the GM checks the physical plausibility of agent actions and describes their effects. In digital environments simulating technologies such as apps and services, the GM may handle API calls to integrate with external tools such as general AI assistants (e.g., Bard, ChatGPT), and digital apps (e.g., Calendar, Email, Search, etc.). Concordia was designed to support a wide array of applications both in scientific research and for evaluating performance of real digital services by simulating users and/or generating synthetic data.[^r1]

## Research Questions
> Research Questions extracted via LLM
- How does Concordia combine generative agents and a generative environment to model grounded interactions?[^r2]
- How do agent observations, Game Master updates, and configurable turn/clock rules determine the event sequence?[^r2]
- What kinds of research and digital-service evaluations can this framework support?[^r2]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?
- Concordia is a library for constructing generative agent-based models in physical, social, or digital environments; it is a framework, not a single parameterized simulation.[^r3]

### How does it work?
- An agent assembles component states into its prompt context and uses an LLM to produce a natural-language action (Equation 1). Component `.observe()` receives observations as they arrive; `.update()` runs at configured intervals, so multiple observations can arrive before the next action.[^r4]
- In the Appendix A implementation, GM components first update and provide agent-specific `partial_state` observations.[^r5]
- The agent acts; the GM applies `update_before_event`, constructs the event statement from component state, applies `update_after_event`, then checks episode termination.[^r5]
- Player turns use random initiative order.[^r5]
- The builder can advance the clock after each player's action or after all players; the paper describes sequential and quasi-simultaneous modes.[^r5]
- Concurrent turns are optional and potentially inconsistent.[^r5]
- The GM's `partial_state` controls what each player sees, so observations can differ by agent. The builder selects components, LLM, memory embedder, environment, update schedule, and turn/clock mode; these choices define the simulated rules and outputs.[^r6]

### What can it answer?
- Concordia supports experiments with language-mediated behavior, simulated users, and evaluation of digital services; conclusions depend on the specified environment and chosen components/models.[^r7]

### Where does it apply?
- Applications can be grounded in physical, social, or digital spaces. The Game Master maps intended language actions into environment outcomes, including feasibility checks or digital API/tool calls where configured.[^r3]

## Metadata
### References
- [[PeekingInsideTheBlackBoxASurveyOnExplainableArtificialIntelligenceXai]]
- [[DoLargeLanguageModelsUnderstandUs]]
- [[ArtificialGeneralIntelligenceIsAlreadyHere]]
- [[UsingLargeLanguageModelsToSimulateMultipleHumansAndReplicateHumanSubjectStudies]]
- [[TheTheoryOfPlannedBehavior]]
- [[FrameworkBasedQualitativeAnalysisOfFreeResponsesOfLargeLanguageModelsAlgorithmicFidelity]]
- [[Palm2TechnicalReport]]
- [[OutOfOneManyUsingLanguageModelsToSimulateHumanSamples]]
- [[WhichHumans]]
- [[TheEmergenceOfClassesInAMultiAgentBargainingModel]]
- [[WorkingMemory]]
- [[ConstitutionalAiHarmlessnessFromAiFeedback]]
- [[AreEmotionsNaturalKinds]]
- [[TheConceptualActTheoryAPrécis]]
- [[TheArcadeLearningEnvironmentAnEvaluationPlatformForGeneralAgents]]
- [[PowerToThePeopleOpportunitiesAndChallengesForParticipatoryAi]]
- [[SuperintelligencePathsDangersStrategies]]
- [[UsingGptForMarketResearch]]
- [[MachineCulture]]
- [[LargeLanguageModelsCanImplementPolicyIteration]]
- [[LanguageModelsAreFewShotLearners]]
- [[SparksOfArtificialGeneralIntelligenceEarlyExperimentsWithGpt4]]
- [[AreEconomistsDifferentAndIfSoWhy]]
- [[GoalDirectedControlAndItsAntipodes]]
- [[FeudalReinforcementLearning]]
- [[PhilosophyAndSimulationTheEmergenceOfSyntheticReason]]
- [[AssemblageTheory]]
- [[CanAiLanguageModelsReplaceHumanParticipants]]
- [[ASurveyForInContextLearning]]
- [[ASocialPathToHumanLikeArtificialIntelligence]]
- [[MultipleProcessesByWhichAttitudesGuideBehaviorTheModeModelAsAnIntegrativeFramework]]
- [[DoesStudyingEconomicsInhibitCooperation]]
- [[TheAssociativePropositionalEvaluationModelTheoryEvidenceAndOpenQuestions]]
- [[SharedComputationalPrinciplesForLanguageProcessingInHumansAndDeepLanguageModels]]
- [[ImplicitSocialCognitionAttitudesSelfEsteemAndStereotypes]]
- [[AiAndTheTransformationOfSocialScienceResearch]]
- [[TheDungeonMasterGuideNo21002ndEditionAdvancedDungeonsAndDragons]]
- [[LawWithoutTheStateLegalAttributesAndTheCoordinationOfDecentralizedCollectivePunishment]]
- [[TheRoleOfCausalKnowledgeInTheEvolutionOfTraditionalTechnology]]
- [[TheSecretOfOurSuccessHowCultureIsDrivingHumanEvolutionDomesticatingOurSpeciesAndMakingUsSmarter]]
- [[BeyondTheMatrixExperimentalApproachesToStudyingSocialEcologicalSystems]]
- [[CochraneHandbookForSystematicReviewsOfInterventions]]
- [[MetagptMetaProgrammingForMultiAgentCollaborativeFramework]]
- [[LargeLanguageModelsAsSimulatedEconomicAgentsWhatCanWeLearnFromHomoSilicus]]
- [[InnerMonologueEmbodiedReasoningThroughPlanningWithLanguageModels]]
- [[HumanLevelPerformanceIn3dMultiplayerGamesWithPopulationBasedReinforcementLearning]]
- [[EmergentBarteringBehaviourInMultiAgentReinforcementLearning]]
- [[TheArchetypesAndTheCollectiveUnconscious]]
- [[RepresentativenessRevisitedAttributeSubstitutionInIntuitiveJudgment]]
- [[LyfeAgentsGenerativeAgentsForLowCostRealTimeSocialInteractions]]
- [[TheGhostInTheMachine]]
- [[HistoryOfScienceAndItsRationalReconstructions]]
- [[MultiAgentReinforcementLearningInSequentialSocialDilemmas]]
- [[AutocurriculaAndTheEmergenceOfInnovationFromSocialInteractionAManifestoForMultiAgentIntelligenceResearch]]
- [[ScalableEvaluationOfMultiAgentReinforcementLearningWithMeltingPot]]
- [[MultimodalFoundationModelsFromSpecialistsToGeneralPurposeAssistants]]
- [[CamelCommunicativeAgentsForMindExplorationOfLargeLanguageModelSociety]]
- [[SyntacticStructureFromDeepLearning]]
- [[GamesAndDecisionsIntroductionAndCriticalSurvey]]
- [[FromFactorsToActorsComputationalSociologyAndAgentBasedModeling]]
- [[TheLogicOfAppropriateness]]
- [[PlacingLanguageInAnIntegratedUnderstandingSystemNextStepsTowardHumanLevelPerformanceInNeuralLanguageModels]]
- [[TheMediumIsTheMessage]]
- [[TheSocietyOfMind]]
- [[PersonalityWhatMakesYouTheWayYouAre]]
- [[ImplicitAndExplicitMeasuresOfAttitudesThePerspectiveOfTheModeModel]]
- [[WorldOfOurMakingRulesAndRuleInSocialTheoryAndInternationalRelations]]
- [[Gpt4TechnicalReport]]
- [[HabitAndIntentionInEverydayLifeTheMultipleProcessesByWhichPastBehaviorPredictsFutureBehavior]]
- [[GenerativeAgentsInteractiveSimulacraOfHumanBehavior]]
- [[AMultiAgentReinforcementLearningModelOfCommonPoolResourceAppropriation]]
- [[WorkingTogetherCollectiveActionTheCommonsAndMultipleMethodsInPractice]]
- [[PoliticalTheoryOfTheDigitalAgeWhereArtificialIntelligenceMightTakeUs]]
- [[ExpectedUtilitarianism]]
- [[AutomaticBrainsInterpretiveMinds]]
- [[PersonalityTraitsInLargeLanguageModels]]
- [[WhoseOpinionsDoLanguageModelsReflect]]
- [[LargeLanguageModelsCanStrategicallyDeceiveTheirUsersWhenPutUnderPressure]]
- [[ToolformerLanguageModelsCanTeachThemselvesToUseTools]]
- [[AMoreDynamicUnderstandingOfHumanBehaviourForTheAnthropocene]]
- [[ControlledAndAutomaticHumanInformationProcessingIDetectionSearchAndAttention]]
- [[ArtificialNeuralNetworksAccuratelyPredictLanguageProcessingInTheBrain]]
- [[RolePlayWithLargeLanguageModels]]
- [[RewardIsEnough]]
- [[DistributedConnectionistModelsInSocialPsychology]]
- [[LlmPlannerFewShotGroundedPlanningForEmbodiedAgentsWithLargeLanguageModels]]
- [[SocialNormsAndSocialRoles]]
- [[HowChangeHappens]]
- [[BetweenMdpsAndSemiMdpsAFrameworkForTemporalAbstractionInReinforcementLearning]]
- [[AgentBasedComputationalEconomicsOverviewAndBriefHistory]]
- [[Llama2OpenFoundationAndFineTunedChatModels]]
- [[LargeLanguageModelsFailOnTrivialAlterationsToTheoryOfMindTasks]]
- [[Portal2007]]
- [[FeudalNetworksForHierarchicalReinforcementLearning]]
- [[GrandmasterLevelInStarcraftIiUsingMultiAgentReinforcementLearning]]
- [[UnderstandingTheEmergenceOfConventionsInMultiAgentSystems]]
- [[ChainOfThoughtPromptingElicitsReasoningInLargeLanguageModels]]
- [[OrganizingAndTheProcessOfSensemaking]]
- [[EthicalAndSocialRisksOfHarmFromLanguageModels]]
- [[SociotechnicalSafetyEvaluationOfGenerativeAiSystems]]
- [[AnarchyIsWhatStatesMakeOfItTheSocialConstructionOfPowerPolitics]]
- [[TheAgentStructureProblemInInternationalRelationsTheory]]
- [[CyberostracismEffectsOfBeingIgnoredOverTheInternet]]
- [[GeneralizingTheCoreDesignPrinciplesForTheEfficacyOfGroups]]
- [[AModelOfDualAttitudes]]
- [[EmpiricalValidationOfAgentBasedModelsAlternativesAndProspects]]
- [[BloomA176bParameterOpenAccessMultilingualLanguageModel]]
- [[ChatarenaMultiAgentLanguageGameEnvironmentsForLargeLanguageModels2023]]
- [[MitigatingGenerativeAgentSocialDilemmas]]
- [[ASharedLinguisticSpaceForTransmittingOurThoughtsFromBrainToBrainInNaturalConversations]]
- [[LargeLanguageModelsAsCommonsenseKnowledgeForLargeScaleTaskPlanning]]
- [[TheAiEconomistTaxationPolicyDesignViaTwoLevelDeepMultiagentReinforcementLearning]]
- [[SotopiaInteractiveEvaluationForSocialIntelligenceInLanguageAgents]]
- [[ConstructionConcentrationAndDisContinuitiesInSocialValuations]]


Reference list preserved from the prior note in original order; bibliography completeness has not been checked against the primary source.

## Audit Log
- Initial independent audit found Appendix A's update order, player-visible state, and turn/clock options omitted. Added `partial_state` visibility, the GM/player action sequence, random initiative, two clock modes, optional concurrent turns and the separate observation/update timing.[^r4][^r5][^r6]

## LLM Justification
[^r1]: Vezhnevets et al., arXiv v1 Abstract, https://arxiv.org/abs/2312.03664.
[^r2]: Vezhnevets et al., Sections 1–2, https://arxiv.org/pdf/2312.03664.
[^r3]: Vezhnevets et al., Sections 2–3, environment and Game Master description, https://arxiv.org/pdf/2312.03664.
[^r4]: Vezhnevets et al., Appendix A.1, Equation (1), PDF p. 23, https://arxiv.org/pdf/2312.03664.
[^r5]: Vezhnevets et al., Appendix A.3–A.3.1, turn processing and clock options, PDF pp. 24–25, https://arxiv.org/pdf/2312.03664.
[^r6]: Vezhnevets et al., Appendix A.1 and A.3, PDF pp. 23–24, https://arxiv.org/pdf/2312.03664.
[^r7]: Vezhnevets et al., Sections 1 and 4, https://arxiv.org/pdf/2312.03664.
