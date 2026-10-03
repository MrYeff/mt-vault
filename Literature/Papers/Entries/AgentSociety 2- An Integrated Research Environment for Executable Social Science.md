---
title: 'AgentSociety 2: An Integrated Research Environment for Executable Social Science'
authors:
- '[[Literature/Authors/Jinghua Piao|Jinghua Piao]]'
- '[[Literature/Authors/Jun Zhang|Jun Zhang]]'
- '[[Literature/Authors/Haoyu Huang|Haoyu Huang]]'
- '[[Literature/Authors/Keming Zhang|Keming Zhang]]'
- '[[Literature/Authors/Jing Yi Wang|Jing Yi Wang]]'
- '[[Literature/Authors/Xinran Zhao|Xinran Zhao]]'
- '[[Literature/Authors/Songwei Li|Songwei Li]]'
- '[[Literature/Authors/Boyuan Sun|Boyuan Sun]]'
- '[[Literature/Authors/Jiayi Chang|Jiayi Chang]]'
- '[[Literature/Authors/Fengli Xu|Fengli Xu]]'
- '[[Literature/Authors/Chunyan Wang|Chunyan Wang]]'
- '[[Literature/Authors/Fang Zhang|Fang Zhang]]'
- '[[Literature/Authors/Ke Rong|Ke Rong]]'
- '[[Literature/Authors/Jun Su|Jun Su]]'
- '[[Literature/Authors/Tianguang Meng|Tianguang Meng]]'
- '[[Literature/Authors/Yi Liu|Yi Liu]]'
- '[[Literature/Authors/Qingguo Meng|Qingguo Meng]]'
- '[[Literature/Authors/Yu Wang|Yu Wang]]'
- '[[Literature/Authors/Yong Li|Yong Li]]'
publication date: 2026-06-11
tags:
- model
- simulation
source: https://arxiv.org/html/2607.11895
doi: 10.48550/arXiv.2607.11895
read status: Todo
---
## Abstract

AI scientist systems are beginning to automate parts of scientific research, but social science poses a distinct challenge: its objects of inquiry are not merely datasets or laboratory protocols, but integrated social processes involving situated participants, interaction contexts, interventions, and outcomes. Yet a critical link is missing: existing systems either assist isolated research tasks or simulate agents as experimental subjects, leaving the research workflow and simulated society decoupled. Here we introduce AgentSociety 2, an Integrated Research Environment for executable social science. It couples two roles of LLM agents in the same runtime: AI social scientists that coordinate literature grounding, hypothesis generation, experiment design, simulation execution, result interpretation, and manuscript drafting; and silicon participants that generate behavioral responses within configurable social environments. This dual-role design turns hypotheses into auditable agent behaviors, environment rules, interventions, and measurements, thereby supporting an end-to-end workflow. Across seven illustrative studies spanning micro-level social-science laboratory experiments, meso-level dynamics in social media, and macro-level urban scenarios, we demonstrate its capacity to support diverse disciplinary questions, reproduce major qualitative patterns from prior studies, identify informative deviations, and enable large-scale simulations through optimized agent-environment interactions. By preserving human researchers' high-level agency while delegating procedural orchestration to agentic systems, it provides a human-in-the-loop and controllable infrastructure for next-generation computational social science, with broader applications in scalable computational social experimentation and AI-enabled social governance platforms.


## Research Questions
> Research Questions extracted via LLM

- How can a research environment connect AI social scientists’ research workflow with LLM-based participants acting in configurable social environments?[^r1]
- Can one platform support social-science experiments across laboratory, social-media, and urban settings while producing traceable behaviors and measurements?[^r1][^r2]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?
AgentSociety² is an integrated research environment that connects a human-steered AI social-science workflow with LLM social participants and configurable executable environments. It is a platform architecture, not a single substantive agent-based model with fixed state-transition rules.[^r1]

### How does it work?
The schema records the platform roles, workspace/tick behavior, and skill-based agent loop described in §§2–3.1 and Figures 4 and 6.[^r3][^r13]
```yml
ResearchEnvironment:
  researcher: Researcher
  scientist: AISocialScientist
  participants: [SocialAgent]
  environment: StudyEnvironment

Researcher:
  approved_artifacts: [KeyArtifact]

AISocialScientist:
  workflow: [WorkflowStage]

WorkflowStage:
  IdeaAndLiterature
  DataPreparation
  Hypothesis
  ExperimentDesign
  Execution
  Analysis
  Manuscript

SocialAgent:
  workspace: Workspace
  skills: [Skill]
  available_actions: [Action]

Skill:
  Observation
  Cognition
  Plan
  Memory

Action:
  DirectAction
  ToolUse
  SkillActivation

Workspace:
  profile: ...
  state: ...
  memory: [...]
  logs: [...]
  checkpoints: [...]

KeyArtifact: ...

StudyEnvironment:
  instruction: NaturalLanguageInstruction
  context: StructuredContext?
  modules: [EnvironmentModule]

NaturalLanguageInstruction: ...
StructuredContext: ...
EnvironmentModule: ...
```

```
agent_step(
  mut agent: SocialAgent,
  context: ...
):

  action = select_action(agent.available_actions, context, agent.workspace)
  result = execute(action, context)
  agent.workspace = update_workspace(agent.workspace, result)
  out = result
```

- **Human control:** researchers approve hypotheses, construct-to-variable mapping, interventions, validity interpretations, and claims. Workspaces retain profile, state, memory, logs, and checkpoints; each tick reads context and writes action results for continuity.[^r3][^r13]
- **Skills:** Observation extracts relevant information; Cognition updates internal state; Plan turns goals/constraints into actions; Memory retains experience. A ReAct-style loop activates, replaces, or composes these skills according to task and feedback; it is not one fixed transition function.[^r13]
- **Environment interface:** modules inherit from `EnvBase`; `@tool()` methods expose observations, statistics, or state-changing/intervention operations. A natural-language instruction with optional structured context returns text and structured output.[^r14]
- **Module integration:** existing simulators can be registered with annotations. Custom modules are generated from a DesignSpec, reviewed, and checked for a unique `EnvBase` export, interface compliance, CodeGenRouter smoke test, and registry visibility.[^r14]
- **CodeGenRouter:** reads registered signatures/types/docs, routes observation requests through a built-in runner, reuses generated/cached code, or asks an LLM to generate ordered environment calls. Generated code runs in a restricted sandbox; pre-generation and semantic caching reduce repeated routing work.[^r14]
- **Scope:** each study supplies its own state variables, transitions, interventions, measurements, and parameters; the schema above summarizes the platform and omits the individual rules of its seven case studies.[^r14]

### What can it answer?
It supports configurable and documented computational social-science studies; the case studies demonstrate varied research workflows and domains rather than one shared prediction.[^r1][^r2]

- In the CodeGenRouter benchmark, the authors report a 60% strict successful-call ratio with Kimi-K2-Instruct, a 31.6% improvement over the best baseline.[^r16]
- In a separate 100-agent, two-round overhead study, pre-generated code handled 74.1% and 70.5% of calls in the two rounds, and first-run code reuse reduced call requirements by 66.5%.[^r16]
- The authors also report that the platform supports simulations involving up to 10,000 agents and 100 million interactions, and reproduces more than 95% of qualitative patterns reported by prior studies.[^r16]

### Where does it apply?
The paper demonstrates laboratory-style experiments, social-media processes, and urban mobility scenarios.[^r2]

## Metadata
### References
- [[Gpt4TechnicalReport]]
- [[UsingLargeLanguageModelsToSimulateMultipleHumansAndReplicateHumanSubjectStudies]]
- [[CellvoyagerAiCompbioAgentGeneratesNewInsightsByAutonomouslyAnalyzingBiologicalData]]
- [[AgentSkills]]
- [[SkillCreator]]
- [[OutOfOneManyUsingLanguageModelsToSimulateHumanSamples]]
- [[EmergentSocialConventionsAndCollectiveBiasInLlmPopulations]]
- [[AnEvolutionaryApproachToNorms]]
- [[AnAiSystemToHelpScientistsWriteExpertLevelEmpiricalSoftware]]
- [[ResearchagentIterativeResearchIdeaGenerationOverScientificLiteratureWithLargeLanguageModels]]
- [[AFoundationModelToPredictAndCaptureHumanCognition]]
- [[UsingCognitivePsychologyToUnderstandGpt3]]
- [[2023SurveyOfHouseholdEconomicsAndDecisionmakingSurveyDataAndCodebook]]
- [[AutonomousChemicalResearchWithLargeLanguageModels]]
- [[CitysimModelingUrbanBehaviorsAndCityDynamicsWithLargeScaleLlmDrivenAgentSimulation]]
- [[ChemcrowAugmentingLargeLanguageModelsWithChemistryTools]]
- [[ToolreagtToolRetrievalForLlmBasedComplexTaskSolutionViaRetrievalAugmentedGeneration]]
- [[LanguageModelsAreFewShotLearners]]
- [[EvaluatingLargeLanguageModelsTrainedOnCode]]
- [[AgentverseFacilitatingMultiAgentCollaborationAndExploringEmergentBehaviors]]
- [[OpenlensAiFullyAutonomousResearchAgentForHealthInfomatics]]
- [[ÉsJFreireReprozipUsingProvenanceToSupportComputationalReproducibility]]
- [[ScientificWorkflowsForComputationalReproducibilityInTheLifeSciencesStatusChallengesAndOpportunities]]
- [[Gemini25PushingTheFrontierWithAdvancedReasoningMultimodalityLongContextAndNextGenerationAgenticCapabilities]]
- [[UsingLargeLanguageModelsInPsychology]]
- [[Mind2webTowardsAGeneralistAgentForTheWeb]]
- [[CanAiLanguageModelsReplaceHumanParticipants]]
- [[CognitiveBiasInDecisionMakingWithLlms]]
- [[GenerativeSocialScienceStudiesInAgentBasedComputationalModeling]]
- [[FactsetOwnership]]
- [[PredictingHumanMobilityWithSemanticMotivationViaDeepGenerativeModel]]
- [[Internagent15AUnifiedAgenticFrameworkForLongHorizonAutonomousScientificDiscovery]]
- [[CompanyNewsApi]]
- [[StockCandlesApi]]
- [[SocialPreferencesBeliefsAndTheDynamicsOfFreeRidingInPublicGoodsExperiments]]
- [[LargeLanguageModelsEmpoweredAgentBasedModelingAndSimulationASurveyAndPerspectives]]
- [[AgentscopeAFlexibleYetRobustMultiAgentPlatform]]
- [[DemocratizingAiScientistsUsingTooluniverse]]
- [[AMultiAgentSystemForAutomatingScientificDiscovery]]
- [[QuantifyingGithubCopilotSImpactOnDeveloperProductivityAndHappiness]]
- [[ChatglmAFamilyOfLargeLanguageModelsFromGlm130bToGlm4AllTools]]
- [[AcceleratingScientificDiscoveryWithCoScientist]]
- [[UsingTheImplicitAssociationTestToMeasureSelfEsteemAndSelfConcept]]
- [[AiAndTheTransformationOfSocialScienceResearch]]
- [[RepresentingAndInterveningIntroductoryTopicsInThePhilosophyOfNaturalScience]]
- [[HumanLikeIntuitiveBehaviorAndReasoningBiasesEmergedInLargeLanguageModelsButDisappearedInChatgpt]]
- [[IsThereAUniversalNeedForPositiveSelfRegard]]
- [[TheFourthParadigmDataIntensiveScientificDiscovery]]
- [[LargeLanguageModelsAsSimulatedEconomicAgentsWhatCanWeLearnFromHomoSilicus]]
- [[TimegeoModelingFrameworkForUrbanMobilityWithoutTrackingData]]
- [[LongContextLlmsMeetRagOvercomingChallengesForLongInputsInRag]]
- [[ExperimentalTestsOfTheEndowmentEffectAndTheCoaseTheorem]]
- [[TheoryOfMindMayHaveSpontaneouslyEmergedInLargeLanguageModels]]
- [[TheStructureOfScientificRevolutions]]
- [[ComputationalSocialScience]]
- [[TheComplexitiesOfAgentBasedModelingOutputAnalysis]]
- [[SocialMediaNewsConsumptionAndPolarizationEvidenceFromAFieldExperiment]]
- [[AutosotaAnEndToEndAutomatedResearchSystemForStateOfTheArtAiModelDiscovery]]
- [[LostInTheMiddleHowLanguageModelsUseLongContexts]]
- [[LonggenbenchLongContextGenerationBenchmark]]
- [[TheAiScientistTowardsFullyAutomatedOpenEndedScientificDiscovery]]
- [[TowardsEndToEndAutomationOfAiResearch]]
- [[TutorialOnAgentBasedModelingAndSimulation]]
- [[FromFactorsToActorsComputationalSociologyAndAgentBasedModeling]]
- [[AgentKernelAMicrokernelMultiAgentSystemFrameworkForAdaptiveSocialSimulationPoweredByLlms]]
- [[From Individual to Society- A Survey on Social Simulation Driven by Large Language Model-based Agents]]
- [[PanelStudyOfIncomeDynamics2023FamilySurveyPublicUseDataset]]
- [[GenerativeAgentsInteractiveSimulacraOfHumanBehavior]]
- [[TheBerkeleyFunctionCallingLeaderboardBfclFromToolUseToAgenticEvaluationOfLargeLanguageModels]]
- [[EmergenceOfHumanLikePolarizationAmongLargeLanguageModelAgents]]
- [[AgentSociety- Large-Scale Simulation of LLM-Driven Generative Agents Advances Understanding of Human Behaviors and Society]]
- [[AComprehensiveDatasetForInvestigatingTheStructureOfSelfBias]]
- [[SelfReferenceAndTheEncodingOfPersonalInformation]]
- [[SafegraphCorePlacesAndPatternsData]]
- [[BitByBitSocialResearchInTheDigitalAge]]
- [[AgentLaboratoryUsingLlmAgentsAsResearchAssistants]]
- [[ALargeScaleDatasetWithBehaviorAttributesAndContentOfMobileShortVideoPlatform]]
- [[OmniscientistTowardACoEvolvingEcosystemOfHumanAndAiScientists]]
- [[ChainOfPlannedBehaviourWorkflowElicitsFewShotMobilityGenerationInLlms]]
- [[NaturalLanguageToCodeTranslationWithExecution]]
- [[ArtificialIntelligencePoweredMetaverseAnalysisChallengesAndFuturePerspectives]]
- [[LimitsOfPredictabilityInHumanMobility]]
- [[OpenclawPersonalAiAssistant]]
- [[TheVirtualLabOfAiAgentsDesignsNewSarsCov2Nanobodies]]
- [[AiResearcherAutonomousScientificInnovation]]
- [[GensimAGeneralSocialSimulationPlatformWithLargeLanguageModelBasedAgents]]
- [[MetaverseAndDigitalTwinsInTheAgeOfAiAndExtendedReality]]
- [[IllusionAndWellBeingASocialPsychologicalPerspectiveOnMentalHealth]]
- [[KimiK2OpenAgenticIntelligence]]
- [[ConsumerExpenditureSurveysPublicUseMicrodata2023]]
- [[AmericanCommunitySurvey5YearData2019]]
- [[AmericanCommunitySurvey5YearEstimates20152019]]
- [[2023AmericanCommunitySurvey1YearEstimatesPublicUseMicrodataSample]]
- [[2023SurveyOfIncomeAndProgramParticipation]]
- [[ASurveyOnHumanCentricLlms]]
- [[YulanOnesimTowardsTheNextGenerationOfSocialSimulatorWithLargeLanguageModels]]
- [[PlanAndSolvePromptingImprovingZeroShotChainOfThoughtReasoningByLargeLanguageModels]]
- [[EmergentAnalogicalReasoningInLargeLanguageModels]]
- [[ChainOfThoughtPromptingElicitsReasoningInLargeLanguageModels]]
- [[DeepscientistAdvancingFrontierPushingScientificFindingsProgressively]]
- [[ScienceInTheAgeOfComputerSimulation]]
- [[Qwen3TechnicalReport]]
- [[OASIS- Open Agent Social Interaction Simulations with One Million Agents]]
- [[ReactSynergizingReasoningAndActingInLanguageModels]]
- [[EquippingAgentsForTheRealWorldWithAgentSkillsOctober2025]]
- [[SocioverseAWorldModelForSocialSimulationPoweredByLlmAgentsAndAPoolOf10MillionRealWorldUsers]]
- [[CompeteaiUnderstandingTheCompetitionDynamicsInLargeLanguageModelBasedAgents]]
- [[Act2locAGenerativeFrameworkForMicroscopicHumanMobilitySimulationWithActivityDrivenMotivations]]
- [[AutonomousAgentsForScientificDiscoveryOrchestratingScientistsLanguageCodeAndPhysics]]
- [[DifftrajANovelApproachForTrajectoryGenerationUsingDiffusionModels]]
- [[CanLargeLanguageModelsTransformComputationalSocialScience]]

## Audit Log
- Initial audit found the empty schema uninformative and omitted human approval gates and environment architecture. Revision added the Observation/Cognition/Plan/Memory loop, EnvBase and CodeGenRouter module lifecycle, routing, validation, caching, and reported performance results. Independent re-audit checked these claims and the research questions against the full source and found them supported; experiment-specific rules remain correctly identified as study-specific. Audit passed.[^r15]

## LLM Justification
[^r1]: Piao et al., “AgentSociety 2,” Abstract and §3, especially §§3.1–3.2 (participants and agentic environments): https://arxiv.org/html/2607.11895
[^r2]: Ibid., §7 “Multi-Scale Social Science Studies” and §§7.1–7.7 (seven examples and application domains).
[^r3]: Ibid., Figure 6 and §3.1.1 (workspace/tick behavior); §§4.1–4.7 (AI social-scientist workflow).
[^r13]: Piao et al., “AgentSociety 2,” §2.2 (human approval gates); §§3.1.1–3.1.5 and Figure 6 (workspace/tick behavior, skill activation, and the four built-in skills); §§4.1–4.7 (AI social-scientist workflow); https://arxiv.org/html/2607.11895.
[^r14]: Ibid., §§3.2.1–3.2.5 and Figures 7–8 (environment interfaces, module integration and validation, CodeGenRouter routing/security, pre-generation and caching); §§4.4–4.5 (study-specific design and execution); §§7.1–7.7 (illustrative studies); same URL.
[^r15]: Audit log basis: source §§2–4, 6, and 7, https://arxiv.org/html/2607.11895.
[^r16]: Ibid., Abstract and §1 (scale and qualitative-pattern reproduction); §6.2 and Table 6 (CodeGenRouter benchmark); §6.3 (100-agent overhead study and call/cache results); same URL.
