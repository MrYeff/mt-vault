---
title: "Construct User Guide"
tags:
  - guide
  - software
authors:
  - "[[Literature/Authors/Stephen Dipple|Stephen Dipple]]"
  - "[[Literature/Authors/Isabel Murdock|Isabel Murdock]]"
  - "[[Literature/Authors/Kathleen M. Carley|Kathleen M. Carley]]"
publication date: 2024-06
source: https://www.cmu.edu/casos-center/publications/cmu-s3d-24-105.pdf
doi:
read status: Todo
⚠️: []
---

## Abstract

This technical report provides users and researchers information on the configuration and use of Construct version 5.4.4 or later versions. Construct is the CASOS’s agent-based simulation software for dynamic network and information diffusion in complex socio-technical systems. The report provides a quick start guide to Construct, a detailed discussion of its configuration, and use through a sample problem and virtual experiment configuration exemplar, and a set of appendices with additional useful information. This document is both an introduction to Construct for casual modelers as well as a reference guide for researchers, modelers, and simulationists.[^r1]

## Research Questions
> Research Questions extracted via LLM

- What does the guide document about configuring and running Construct simulations?[^r1]
- How does Construct sequence model actions and messages during each simulated time period?[^r1]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?

- Construct is a configurable agent-based simulation framework.[^r2]
- Its Standard Interaction Model uses a knowledge network to represent which knowledge each agent has, an interaction sphere network to represent which agents an agent knows and may initiate with, and a separate interaction network to record realized interactions.[^r2]

### How does it work?

- The guide describes one-time initialization, then five synchronous phases across models: Think creates messages; Update modifies messages; Intercept lets models modify items created by other models; Communicate parses messages; and Clean Up updates strategies or characteristics for the next period.[^r3]
- Every model completes a phase before any model advances to the next.[^r3]

- In the Standard Interaction Model, agents initiate only to agents in their directed interaction sphere.[^r4]
- Weighted partner selection combines physical, social, and sociodemographic proximity with knowledge similarity and expertise.[^r4]
- Agent activity, initiation/reception limits, and access to a shared communication medium constrain which pairs are eligible; interactions are formed dynamically until no initiators remain.[^r4]
- This is a summary of the Standard Interaction Model, not every optional Construct model or parameter.[^r4]

### What can it answer?

A configured simulation can examine outcomes implied by its selected interaction models, network inputs, and outputs. The manual does not report one standardized experiment or empirical result.[^r1]

### Where does it apply?

The guide presents Construct for agent-based modeling of dynamic networks and information diffusion in socio-technical systems; results depend on the user’s configured scenario and model choices.[^r1]

## Metadata
### References

- "[[RulesOfMind]]"
- "[[MapreduceTutorial]]"
- "[[AnApproachForRelatingSocialStructureToCognitiveStructure]]"
- "[[GroupStabilityASocioCognitiveApproach]]"
- "[[ATheoryOfGroupStability]]"
- "[[CommunicationTechnologiesAndTheirEffectOnCulturalHomogeneityConsensusAndTheDiffusionOfNewIdeas]]"
- "[[ComputationalOrganizationScienceANewFrontier]]"
- "[[ADynamicNetworkApproachToTheAssessmentOfTerroristGroupsAndTheImpactOfAlternativeCoursesOfAction]]"
- "[[TheEtiologyOfSocialChangeTopicsInCognitiveScience14621650]]"
- "[[UnderstandingTaxpayerBehaviorAndAssessingPotentialIrsInterventionsUsingMultiagentDynamicNetworkSimulations]]"
- "[[TheNatureOfTheSocialAgent]]"
- "[[OraOrganizationRiskAnalyzer]]"
- "[[PredictingIntentionalAndInadvertentNonCompliance]]"
- "[[GrowingArtificialSocietiesSocialScienceFromTheBottomUp]]"
- "[[ATheoryOfSocialComparisonProcessesHumanRelations72117140]]"
- "[[ATheoryOfCognitiveDissonance]]"
- "[[AStructuralTheoryOfSocialInfluenceCambridgeUniversityPress]]"
- "[[MathematicalGamesTheFantasticCombinationsOfJohnConwaySNewSolitaireGameLife]]"
- "[[TheConstitutionOfSocietyOutlineOfTheTheoryOfStructuration]]"
- "[[TheImpactOfEducationalInterventionsOnRealStylizedCities]]"
- "[[LoadingNetworksInConstruct]]"
- "[[SpecifyingAgentsInConstruct]]"
- "[[ArabSpringFromNewspaper]]"
- "[[OnTheCoevolutionOfStereotypeCultureAndSocialRelationshipsAnAgentBasedModel]]"
- "[[SocialConstructivism]]"
- "[[AnalyzingJobMachineMatchesUsingCondorQAnalyzePowerpointSlides]]"
- "[[APcansModelOfStructureInOrganizations]]"
- "[[MoreOfAReceiverThanAGiverWhyDoPeopleUnfollowInFacebook]]"
- "[[SoarCognitiveArchitecture]]"
- "[[SymbolicInteractionAReaderInSocialPsychology]]"
- "[[InWikipedia]]"
- "[[ModelingAndSimulationOfTerroristNetworksInSocialAndGeospatialDimensionsIeeeIntelligentSystems2254049]]"
- "[[AnAgentBasedModelOfRedditInteractionsAndModeration]]"
- "[[SimulationToolsForSocialScientistsBuildingAgentBasedModelsWithSwarm]]"
- "[[TheContingentEffectsOfTransactiveMemoryWhenIsItMoreBeneficialToKnowWhatOthersKnowManagementScience525671682]]"
- "[[ASocialInformationProcessingApproachToJobAttitudesAndTaskDesign]]"
- "[[HowRedditRankingAlgorithmsWork]]"
- "[[MicromotivesAndMacrobehaviorNorton]]"
- "[[DynamicModelsOfSegregation]]"
- "[[SorascsACaseStudyInSoaBasedPlatformDesignForSocioCulturalAnalysis]]"
- "[[TheImpactOfDatabasesOnKnowledgeTransferSimulationProvidingTheory]]"
- "[[AgentInteractionsInConstructAnEmpiricalValidationUsingCalibratedGrounding]]"
- "[[ConstructAMultiAgentNetworkModelForTheCoEvolutionOfAgentsAndSocioCulturalEnvironments]]"
- "[[AdministrativeBehaviorAStudyOfDecisionMakingProcessesInAdministrativeOrganization2ndEd]]"
- "[[SymbolicInteractionismASocialStructuralVersion]]"
- "[[ModelingComplexSocioTechnicalSystemsUsingMultiAgentSimulationMethods]]"
- "[[TransactiveMemoryAContemporaryAnalysisOfTheGroupMind]]"



## Audit Log
- 2026-09-29 initial independent audit failed: the phase list omitted Intercept and the network terminology conflated the interaction sphere with realized interactions. Corrected the phase sequence and network roles; added the essential partner-selection and eligibility mechanics with source locations. Status remains `not audited` pending independent re-audit.
- 2026-09-29 independent re-audit found that the 47 imported reference links lacked a bibliography caveat and had not been reconciled item by item. Added the caveat; references and order were not changed. Awaiting final audit.

- Independent final check passed after correction; bibliography mapping remains unverified as stated above.

## LLM Justification
[^r1]: Construct User Guide, abstract and “Introduction to the Report” (PDF pp. 2, 12–14): identifies Construct as simulation software for dynamic networks and information diffusion, and describes the report as a user guide and reference. https://www.cmu.edu/casos-center/publications/cmu-s3d-24-105.pdf
[^r2]: Construct User Guide, “The Knowledge Network,” “The Interaction Sphere,” and “Models” (PDF pp. 20, 24–25): defines the two networks and characterizes the Standard Interaction Model. https://www.cmu.edu/casos-center/publications/cmu-s3d-24-105.pdf
[^r3]: Construct User Guide, “Models and Construct Program Flow,” “Think Function,” “Update Function,” “Intercept Function,” “Communicate Function,” and “Clean Up Function” (PDF pp. 22–24): documents the execution ordering and phase purposes, including Intercept’s role in modifying items created by other models. https://www.cmu.edu/casos-center/publications/cmu-s3d-24-105.pdf
[^r4]: Construct User Guide, “Standard Interaction Model” (PDF pp. 50–52): defines the knowledge and interaction-sphere networks, weighted interaction probability factors, eligibility constraints, and dynamic interaction-pair formation. https://www.cmu.edu/casos-center/publications/cmu-s3d-24-105.pdf
