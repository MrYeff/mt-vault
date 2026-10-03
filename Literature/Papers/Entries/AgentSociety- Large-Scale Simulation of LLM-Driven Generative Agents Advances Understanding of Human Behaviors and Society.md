---
title: 'AgentSociety: Large-Scale Simulation of LLM-Driven Generative Agents Advances Understanding of Human Behaviors and Society'
authors:
- '[[Literature/Authors/Jinghua Piao|Jinghua Piao]]'
- '[[Literature/Authors/Yuwei Yan|Yuwei Yan]]'
- '[[Literature/Authors/Jun Zhang|Jun Zhang]]'
- '[[Literature/Authors/Nian Li|Nian Li]]'
- '[[Literature/Authors/Junbo Yan|Junbo Yan]]'
- '[[Literature/Authors/Xiaochong Lan|Xiaochong Lan]]'
- '[[Literature/Authors/Zhihong Lu|Zhihong Lu]]'
- '[[Literature/Authors/Zhiheng Zheng|Zhiheng Zheng]]'
- '[[Literature/Authors/Jing Yi Wang|Jing Yi Wang]]'
- '[[Literature/Authors/Di Zhou|Di Zhou]]'
- '[[Literature/Authors/Chen Gao|Chen Gao]]'
- '[[Literature/Authors/Fengli Xu|Fengli Xu]]'
- '[[Literature/Authors/Fang Zhang|Fang Zhang]]'
- '[[Literature/Authors/Ke Rong|Ke Rong]]'
- '[[Literature/Authors/Jun Su|Jun Su]]'
- '[[Literature/Authors/Yong Li|Yong Li]]'
publication date: 2025-02-12
tags:
- model
- simulation
source: https://arxiv.org/html/2502.08691
doi: 10.48550/arXiv.2502.08691
read status: Todo
---
## Abstract

Understanding human behavior and society is a central focus in social sciences, with the rise of generative social science marking a significant paradigmatic shift. By leveraging bottom-up simulations, it replaces costly and logistically challenging traditional experiments with scalable, replicable, and systematic computational approaches for studying complex social dynamics. Recent advances in large language models (LLMs) have further transformed this research paradigm, enabling the creation of human-like generative social agents and realistic simulacra of society. In this paper, we propose AgentSociety, a large-scale social simulator that integrates LLM-driven agents, a realistic societal environment, and a powerful large-scale simulation engine. Based on the proposed simulator, we generate social lives for over 10k agents, simulating their 5 million interactions both among agents and between agents and their environment. Furthermore, we explore the potential of AgentSociety as a testbed for computational social experiments, focusing on five key social issues: polarization, the spread of inflammatory messages, the effects of universal basic income policies, the impact of external shocks such as hurricanes, and urban sustainability. These five issues serve as valuable cases for assessing AgentSociety's support for typical research methods -- such as surveys, interviews, and interventions -- as well as for investigating the patterns, causes, and underlying mechanisms of social issues. The alignment between AgentSociety's outcomes and real-world experimental results not only demonstrates its ability to capture human behaviors and their underlying mechanisms, but also underscores its potential as an important platform for social scientists and policymakers.


## Research Questions
> Research Questions extracted via LLM

- How does AgentSociety combine LLM-driven agents, a modeled societal environment, and a large-scale engine to simulate social life?[^r1]
- How can the simulator be used to run social experiments on polarization, inflammatory-message spread, universal basic income, hurricanes, and urban sustainability?[^r2]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?

- AgentSociety couples LLM-driven agents, an urban/social/economic environment, and a distributed simulation engine.[^r1]
- The paper reports simulations of over 10,000 agents and five million interactions; its introduction also describes a 10,000-agent capacity and about 500 interactions per agent per day.[^r1]

### How does it work?

- Agent profiles and dynamic status include mental state, economic status, and relationships.[^r1][^r3]
- Emotions, needs, and cognition guide behavior; needs form a hierarchy, with a need prompting a plan and a plan decomposed into actions such as choosing a place and moving there.[^r1][^r3]
- The compact types below capture the platform components and specified agent fields.[^r1][^r3]

```yml
World:
  agents: [Agent]
  environment: SocietalEnvironment
  engine: SimulationEngine

Agent:
  profile: Profile
  status: Status
  mind: Mind
  relationships: [Relationship]

Mind:
  emotion: Emotion
  needs: [Need]
  cognition: ...

Emotion:
  keyword: ...
  thought: ...
  sadness: 0..10
  joy: 0..10
  fear: 0..10
  disgust: 0..10
  anger: 0..10
  surprise: 0..10

Relationship:
  kind: Family | Friendship | Colleague
  strength: 0..100

SocietalEnvironment: ...
SimulationEngine: ...
Profile: ...
Status: ...
Need: ...
Plan: ...
Event: ...
Perception: ...
```

- **Agent loop:** choose an action from status and emotional/cognitive evaluations; receive environmental or social feedback; append an Event Flow memory item; link it to Perception Flow thoughts/attitudes; analyze it to update emotion and cognition. Memory also stores a static Profile and dynamic key-value Status.[^r3]
- **Mobility:** infer intention from needs, choose a matching place type and feasible radius, then sample a destination by gravity probability \(P_{ij}=(S_j/D_{ij}^{\beta})/\sum_k(S_k/D_{ik}^{\beta})\).[^r4]
- **Social interaction:** use family, friendship, and colleague ties; partner choice depends on tie type/strength and recipient profile; messages and responses depend on needs, beliefs, emotion, and interaction history.[^r4]
- **Employment and consumption:** propensity sets work hours/income and a consumption budget; allocation responds to prior consumption, prices, and taxes. Simple actions such as sleeping are handled directly by the LLM.[^r4]
- **Runtime:** agents execute asynchronously in concurrent Ray processes; asyncio handles I/O, MQTT carries inter-agent messages, and PostgreSQL stores results.[^r5]

- **Omitted here:** detailed prompts, individual parameters, experimental treatments, and low-level scheduling settings.[^r3][^r4][^r5]
- **Future work:** job changes, debt, investment, and detailed offline agent interactions.[^r4]

### What can it answer?

- The platform supports surveys, interviews, and interventions across five case studies.[^r2][^r6]
- Reported results include 52% of agents becoming more polarized in a gun-control homophilic treatment versus 89% becoming more moderate under opposing content.[^r2][^r6]
- In the Hurricane Dorian case, modeled travel fell from 70–90% before landfall to about 30% during the hurricane, then recovered.[^r2][^r6]
- These are the authors’ simulation results, not an independent external-validity assessment.[^r2][^r6]

### Where does it apply?

- The environment includes urban mobility and online/offline social spaces, while agent interaction behavior is primarily online; offline interaction remains future work.[^r2][^r4]
- Case studies cover polarization, inflammatory-message spread, universal basic income, hurricane shocks, and urban sustainability.[^r2][^r4]

## Metadata
### References
- [[Chapter32OutOfEquilibriumEconomicsAndAgentBasedModeling]]
- [[CongestedTrafficStatesInEmpiricalObservationsAndMicroscopicSimulations]]
- [[HowToBuildAndUseAgentBasedModelsInSocialScience]]
- [[ComputationalModelsOfCollectiveBehavior]]
- [[AdaptiveAgentsIntelligenceAndEmergentHumanOrganizationCapturingComplexityThroughAgentBasedModeling]]
- [[GeneralLaneChangingModelMobilForCarFollowingModels]]
- [[WhatIsAComplexSystem]]
- [[TheUseOfTheCenterForEpidemiologicStudiesDepressionScaleInAdolescentsAndYoungAdults]]
- [[LinkingAgentBasedModelsAndStochasticModelsOfFinancialMarkets]]
- [[AMultiAgentModelOfSeveralEconomicRegions]]
- [[AgentBasedEconomicModelsAndEconometrics]]
- [[AgentBasedComputationalModelsAndGenerativeSocialScience]]
- [[AgentBasedModels]]
- [[DifferencesInTheMechanicsOfInformationDiffusionAcrossTopics]]
- [[CausalMechanismsInTheSocialSciences]]
- [[HumanAgencyInSocialCognitiveTheory]]
- [[SocialForceModelForPedestrianDynamics]]
- [[APersonalisticAppraisalOfMaslowSNeedsTheoryOfMotivationFromHumanisticPsychologyToIntegralHumanism]]
- [[ReconstructingEconomics]]
- [[TheP1P2DHypothesisOnTheIntercityMovementOfPersons]]
- [[AgentBasedModelingAndNetworkDynamics]]
- [[EmotivationalPsychologyHowDistinctEmotionsFacilitateFundamentalMotives]]
- [[EmotionShapesTheDiffusionOfMoralizedContentInSocialNetworks]]
- [[GrowingArtificialSocieties]]
- [[CityflowAMultiAgentReinforcementLearningEnvironmentForLargeScaleCityTrafficScenario]]
- [[AnInterdependentModelOfPersonalityMotivationEmotionAndMoodForIntelligentVirtualAgents]]
- [[EmergenceOfPolarizedIdeologicalOpinionsInMultidimensionalTopicSpaces]]
- [[NominalRigiditiesAndTheDynamicEffectsOfAShockToMonetaryPolicy]]
- [[EmpiricalEvidenceUsingMicrosimulationModelsInTheSocialSciences]]
- [[IntegratingExplanationAndPredictionInComputationalSocialScience]]
- [[WhyStockMarketsCrashCriticalEventsInComplexFinancialSystems]]
- [[SocialEmergence]]
- [[SocialScienceMicrosimulation]]
- [[CognitivePsychology]]
- [[OutOfOneManyUsingLanguageModelsToSimulateHumanSamples]]
- [[ChatgptAndTheRiseOfSemiHumans]]
- [[EfficientMemoryManagementForLargeLanguageModelServingWithPagedattention]]
- [[HumanAiAdaptiveDynamicsDrivesTheEmergenceOfInformationCocoons]]
- [[LargeLanguageModelsShowHumanLikeContentBiasesInTransmissionChainExperiments]]
- [[AutonomousChemicalResearchWithLargeLanguageModels]]
- [[UsingLargeLanguageModelsToGenerateSiliconSamplesInConsumerAndMarketingResearchChallengesOpportunitiesAndGuidelines]]
- [[ASurveyOnLargeLanguageModelBasedAutonomousAgents]]
- [[PerilsAndOpportunitiesInUsingLargeLanguageModelsInPsychologicalResearch]]
- [[LanguageModelsLikeHumansShowContentEffectsOnReasoningTasks]]
- [[EconagentLargeLanguageModelEmpoweredAgentsForSimulatingMacroeconomicActivities]]
- [[ChatdevCommunicativeAgentsForSoftwareDevelopment]]
- [[EvaluatingLargeLanguageModelsInTheoryOfMindTasks]]
- [[UnresolvedReference24F3B63196495076]]
- [[UnresolvedReference15EAD20F405CFD42]]
- [[UnresolvedReference6B77254A96CE3E0F]]
- [[UnresolvedReference4CE1581D99031881]]
- [[TutorialOnAgentBasedModelingAndSimulation]]
- [[UnresolvedReference6EA5D79DC83FDFF4]]
- [[UnresolvedReference4CF0ECCFE2C34736]]
- [[UnresolvedReferenceA92D55B1A7476FC1]]
- [[ChallengesTasksAndOpportunitiesInModelingAgentBasedComplexSystems]]
- [[LargeLanguageModelsEmpoweredAgentBasedModelingAndSimulationASurveyAndPerspectives]]
- [[UnresolvedReference390424F59D662F1E]]
- [[TheAiEconomistTaxationPolicyDesignViaTwoLevelDeepMultiagentReinforcementLearning]]
- [[UnresolvedReference940C48C1B85A4CB4]]
- [[TestingTheoryOfMindInLargeLanguageModelsAndHumans]]
- [[CamelCommunicativeAgentsForMindExplorationOfLargeLanguageModelSociety]]
- [[ChainOfThoughtPromptingElicitsReasoningInLargeLanguageModels]]
- [[UnresolvedReference5CD7B42755489CBA]]
- [[UnresolvedReference157C3C2C49511B07]]
- [[UnresolvedReferenceD17455A686F13F20]]
- [[UnresolvedReference20341A8A5A831E3C]]
- [[GenerativeAgentsInteractiveSimulacraOfHumanBehavior]]
- [[UnresolvedReference85F7AF1F12155C83]]
- [[BuildingLifelongAnalyticalAgentsWithRealWorldTextAndTimeSeries]]
- [[UnresolvedReference366A8544E39F55C5]]
- [[UnresolvedReference383B170442D07168]]
- [[UnresolvedReference7D0812A3783AB755]]
- [[UnresolvedReferenceFECC502F6C25F225]]
- [[ATheoryOfHumanMotivation]]
- [[TheTheoryOfPlannedBehavior]]
- [[UnresolvedReference44BA47B6D3A0BCF8]]
- [[SelfAlignmentOfLargeLanguageModelsViaMonopolylogueBasedSocialSceneSimulation]]
- [[UnresolvedReference8CBA3A2D861FC0A6]]
- [[UnresolvedReference32FF6320E04B1151]]
- [[On Generative Agents in Recommendation]]
- [[UnresolvedReferenceA352B47E8E52B3AC]]
- [[UnresolvedReference54325AA600F04F93]]
- [[UnresolvedReferenceD78238F090EB7B1C]]
- [[User Behavior Simulation with Large Language Model based AgentsForRecommenderSystems]]
- [[UnresolvedReference3534D3C3B84A90C9]]
- [[UnresolvedReferenceB6B65092D101902A]]
- [[MaslowSHierarchyOfNeeds]]
- [[EmotionModelingInSocialSimulationASurvey]]
- [[PersonalizingHumanAgentInteractionThroughCognitiveModels]]
- [[UnresolvedReference54EF5959C8DAA95D]]
- [[ASurveyOnHallucinationInLargeLanguageModelsPrinciplesTaxonomyChallengesAndOpenQuestions]]
- [[SumoSimulationOfUrbanMobilityAnOverview]]
- [[IntelligentDrivingIntelligenceTestForAutonomousVehiclesWithNaturalisticAndAdversarialEnvironment]]
- [[UnresolvedReferenceCDE028CF9EB16279]]
- [[UnresolvedReference46C6E3124F25B5A3]]
- [[RayADistributedFrameworkForEmergingAiApplications]]
- [[UnresolvedReference8AF678E27B4E67F9]]
- [[DifferencesInTheMechanicsOfInformationDiffusionAcrossTopicsIdiomsPoliticalHashtagsAndComplexContagionOnTwitter]]
- [[UnresolvedReferenceA3293F779BAD3C6F]]
- [[UnresolvedReference044B8215C1FD31DE]]
- [[TptuTaskPlanningAndToolUsageOfLargeLanguageModelBasedAiAgents]]
- [[UnresolvedReferenceBD398BAEF80D697A]]
- [[UnresolvedReference07A260F8EABFF736]]
- [[UnresolvedReferenceBCF2ABB92ADCD827]]
- [[UnresolvedReference2841E6374E2C884C]]
- [[SelfalignmentOfLargeLanguageModelsViaMultiAgentSocialSimulation]]
- [[UnresolvedReference7DBC035F93573E3C]]
- [[CellularAutomata]]
- [[TheGameOfLife]]
- [[ReconstructingEconomicsAgentBasedModelsAndComplexity]]
- [[AgentBasedModelingInEconomicsAndFinancePastPresentAndFuture]]
- [[UnresolvedReference61FD47BA38D8EA49]]
- [[BigDataAgentsAndMachineLearningTowardsADataDrivenAgentBasedModelingApproach]]
- [[HumanLikeProblemsolvingAbilitiesInLargeLanguageModelsUsingChatgpt]]
- [[UnresolvedReference1230F56718C59C7E]]
- [[UsingLargeLanguageModelsToSimulateMultipleHumansAndReplicateHumanSubjectStudies]]
- [[PredictingResultsOfSocialScienceExperimentsUsingLargeLanguageModels]]
- [[UnresolvedReferenceFACD6FE09E659BAD]]
- [[UsingLargeLanguageModelsInPsychology]]

## Audit Log
- An earlier independent audit failed because the note underspecified agent mechanics and implied empty state variables. The revision added the specified mental-state, mobility, social, economic, memory, engine, and case-result details.[^r8]
- The current independent audit found the earlier prose summary too dense and asked for compact model notation. The architecture is now represented with concise types and a workflow while preserving source-grounded behavior details and the distinction between available environment spaces and still-unspecified offline agent transitions. This note remains audit failed pending re-audit.[^r8]

## LLM Justification
[^r1]: Piao et al., “AgentSociety,” Abstract and §1 (three components; reported scale and interaction counts): https://arxiv.org/html/2502.08691
[^r2]: Ibid., Abstract, §1, and §7.2–7.6 (methods, five case studies, and authors’ reported comparison/reproduction claims).
[^r3]: Ibid., §§3.1–3.2 and §3.6 (agent profile/status and mental processes; emotion ratings in §3.2; need-plan-behavior chain in §3.2; memory components and workflow in §3.6).
[^r4]: Ibid., §§3.3–3.5 (mobility sequence and gravity equation in §3.3; social relationships/interactions in §3.4; employment and consumption in §3.5); §§4.1–4.4 for environment description.
[^r5]: Piao et al., “AgentSociety,” §§5.2–5.4 (Ray agent groups, asynchronous execution, MQTT messaging, and PostgreSQL result storage): https://arxiv.org/html/2502.08691.
[^r6]: Ibid., §§7.2 and 7.5 (polarization percentages and Hurricane Dorian activity-level results): same URL.
[^r8]: Audit and revision basis: source §§3.1–3.6, 4.1–4.4, 5.2–5.4, and 7.2–7.6; https://arxiv.org/html/2502.08691.
