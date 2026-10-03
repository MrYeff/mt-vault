---
title: "Reliable and Efficient Agent-Based Modeling and Simulation"
tags:
  - agent_based_model
  - simulation_framework
authors:
  - "[[Literature/Authors/Alessia Antelmi|Alessia Antelmi]]"
  - "[[Literature/Authors/Pasquale Caramante|Pasquale Caramante]]"
  - "[[Literature/Authors/Gennaro Cordasco|Gennaro Cordasco]]"
  - "[[Literature/Authors/Giuseppe D’Ambrosio|Giuseppe D’Ambrosio]]"
  - "[[Literature/Authors/Daniele De Vinco|Daniele De Vinco]]"
  - "[[Literature/Authors/Francesco Foglia|Francesco Foglia]]"
  - "[[Literature/Authors/Luca Postiglione|Luca Postiglione]]"
  - "[[Literature/Authors/Carmine Spagnuolo|Carmine Spagnuolo]]"
publication date: 2024-03-31 
source: "https://www.jasss.org/27/2/4.html"
doi: 10.18564/jasss.5300
read status: Todo
⚠️:
  - audit failed
---

## Abstract

Agent-based models represent a primary methodology to untangle and study complex systems. Over the last decade, the need for more elaborate computing-demanding models gave rise to many frameworks and tools to run ABM simulations. Current state-of-the-art ABM tools either focus on ease of use, performance, or a trade-off between these two elements. Still, efficiency-oriented solutions (required for both large and small-scale simulations) are vulnerable to memory flaws which could invalidate the experiment results. This work aims to merge efficiency, reliability, and safeness under an innovative ABM software framework based on the Rust programming language. Our framework, krABMaga, is an open-source library that offers a high-level environment by exploiting metaprogramming and expandable visualization features. We equipped our library with a dynamic simulation monitoring system and model exploration and optimization capabilities over parallel, distributed, and cloud architectures. After having presented the overall architecture and functionalities of krABMaga, we discuss a performance comparison of our framework against the mostly adopted ABM software and the scalability potential of our simulation engine on a model calibration experiment running over an AWS EC2 virtual cluster machine. All code and examples models are available on GitHub.

## Research Questions
> Research Questions extracted via LLM
- Can krABMaga combine runtime efficiency with reliability and safety for agent-based simulation?[^r1]
- How does its simulation performance and scalability compare with established ABM tools and a distributed calibration experiment?[^r1]

## Study Design
> Study design extracted via LLM

This is a software-framework and performance study, not a substantive behavioral model. The authors compare krABMaga with established ABM tools and report scalability testing in a model-calibration experiment on an AWS EC2 cluster.[^r3]

## Metadata
### References
- [[EfficientGlobalOptimizationOfExpensiveBlackBoxFunctions]]
- [[GeomasonGeospatialSupportForMason]]
- [[FindingFormsOfFlockingEvolutionarySearchInAbmParameterSpaces]]
- [[SoftwareReviewTheEcjToolkit]]
- [[DistributedSimulationOfHybridSystemsWithAnylogicAndHla]]
- [[OpenmoleAWorkflowEngineSpecificallyTailoredForTheDistributedExplorationOfSimulationModels]]
- [[TheExplicitRepresentationOfContextInAgentBasedModelsOfComplexAdaptiveSpatialSystems]]
- [[AnAgentBasedModelingApproachAppliedToTheSpreadOfCholera]]
- [[ParallelAgentBasedSimulationWithRepastForHighPerformanceComputing]]
- [[ThinkingLikeAWolfASheepOrAFireflyLearningBiologyThroughConstructingAndTestingComputationalTheoriesAnEmbodiedModelingApproach]]
- [[TheNetlogoBasedDynamicModelForTheTeaching]]
- [[SafeSimulationAutomationFrameworkForExperiments]]
- [[MasonAMultiagentSimulationEnvironment]]
- [[DesignGuidelinesForAgentBasedModelVisualization]]
- [[ComplexAdaptiveSystemsModelingWithRepastSimphony]]
- [[ASurveyOnParallelAndDistributedMultiAgentSystemsForHighPerformanceComputingSimulations]]
- [[AgentBasedModellingAndSimulationToolsAReviewOfTheStateOfArtSoftware]]
- [[ConnectedscienceLearningBiologyThroughConstructingAndTestingComputationalTheoriesAnEmbodiedModelingApproach]]
- [[FlameGpuComplexSystemSimulationFramework]]
- [[RustbeltSecuringTheFoundationsOfTheRustProgrammingLanguage]]
- [[PynetlogoLinkingNetlogoWithPython]]
- [[DistributedMasonAScalableDistributedMultiAgentSimulationEnvironment]]
- [[AStochasticAgentBasedModelOfTheSarsCov2EpidemicInFrance]]
- [[AnIntroductionToComplexSystemsScienceAndItsApplications]]
- [[UtilizingPythonForAgentBasedModelingTheMesaFramework]]
- [[ExperiencesInDevelopingADistributedAgentBasedModelingToolkitWithPython]]
- [[ReplicationOfAnAgentBasedModelUsingTheReplicationStandard]]
- [[AStudyOfCCCodeWeaknessesOnStackOverflow]]
- [[NoFreeLunchWhenEstimatingSimulationParameters]]
- [[ALightweightFormalismForReferenceLifetimesAndBorrowingInRust]]
- [[Policyspace2ModelingMarketsAndEndogenousPublicPolicies]]
- [[PylogoAPythonReimplementationOfMuchOfNetlogo]]
- [[ChallengesTasksAndOpportunitiesInModelingAgentBasedComplexSystems]]
- [[AgentsJlAPerformantAndFeatureFullAgentBasedModelingSoftwareOfMinimalCodeComplexity]]
- [[RustLanguageForSupercomputingApplications]]
- [[FearBehaviourAndTheCovid19PandemicACityScaleAgentBasedModelUsingSocioDemographicAndSpatialMapData]]
- [[ExperimentingWithAgentBasedModelSimulationTools]]
- [[AgentBasedModelForUrbanAdministrationACaseStudyOfBridgeConstructionAndItsTrafficDispersionEffect]]
- [[AdvancedTutorialParallelAndDistributedMethodsForScalableDiscreteSimulation]]
- [[Reliable and Efficient Agent-Based Modeling and Simulation]]
- [[UnresolvedReference519719E1A303EA73]]
- [[UnresolvedReferenceB24DA3BA975546AC]]
- [[UnresolvedReferenceBF5490EAA1BA78E2]]
- [[UnresolvedReferenceCE792AAAC5CACBC3]]
- [[UnresolvedReference7E99DBE33CD313E6]]
- [[UnresolvedReference05220F89B177FF9E]]
- [[UnresolvedReference0BF12E73B26815E2]]
- [[UnresolvedReference6AB9AF9EE6C6BB0E]]
- [[UnresolvedReference114FA4BA40626BBC]]
- [[UnresolvedReferenceD292E24B59882FAD]]
- [[UnresolvedReference217E84391C3D9D45]]

## Audit Log
- Audit invalidated (2026-09-30): auditor admitted clearing flags before completing independent source checks. A new independent audit is required.
- Strong source review (2026-09-30): Verified full published article; copied abstract from the inspected publisher HTML (which differs slightly from PDF phrasing) and confirmed 31 March 2024 date. Independent re-audit pending.
- Initial independent audit: failed on abstract fidelity or incomplete source verification; revisions made. Independent re-audit remains pending. See `vault/.automation/audit/next-forty-54-66-initial-2026-09-30.json`.

- WITHDRAWN audit claim (2026-09-30): previously reported PASS; source claims, current extraction, metadata, references and footnotes checked against the available primary source. See `vault/.automation/audit/remaining-audit-b-2026-09-30.json`.

## LLM Justification
[^r1]: The paper’s abstract, at https://www.jasss.org/27/2/4.html. The questions paraphrase the stated purpose, research scope, and reported approach.
[^r3]: Antelmi et al., §3 (krABMaga framework), §4 (performance comparison of simulation engines and distributed model exploration/calibration on AWS EC2). Full published text: https://www.jasss.org/27/2/4.html.
