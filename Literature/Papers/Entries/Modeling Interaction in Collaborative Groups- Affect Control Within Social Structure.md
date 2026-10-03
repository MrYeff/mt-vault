---
title: "Modeling Interaction in Collaborative Groups: Affect Control Within Social Structure"
authors:
  - "[[Literature/Authors/Nikolas Zöller|Nikolas Zöller]]"
  - "[[Literature/Authors/Jonathan Howard Morgan|Jonathan Howard Morgan]]"
  - "[[Literature/Authors/Tobias Schröder|Tobias Schröder]]"
source: "https://www.jasss.org/24/4/6.html"
doi: "10.18564/jasss.4699"
publication date: "2021-10-31"
tags:
  - "model"
  - "simulation"
read status: Todo
⚠️:
  - audit failed
---

## Abstract

This paper studies the dynamics of identity and status management within groups in collaborative settings. We present an agent-based simulation model for group interaction rooted in social psychological theory. The model integrates affect control theory with networked interaction structures and sequential behavior protocols as they are often encountered in task groups. By expressing status hierarchy through network structure, we build a bridge between expectation states theory and affect control theory, and are able to reproduce central results from the expectation states research program in sociological social psychology. Furthermore, we demonstrate how the model can be applied to analyze specialized task groups or sub-cultural domains by combining it with empirical data sources. As an example, we simulate groups of open-source software developers and analyze how cultural expectations influence the occupancy of high status positions in these groups.

## Research Questions
> Research Questions extracted via LLM

- How do role identities and group interaction structures shape status positions in task groups?[^r1]
- Can ACT-driven behavior reproduce expectation-states patterns when status hierarchy is expressed as a network?[^r1]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?
- ACTING represents task-group members' fixed cultural identities and changing impressions in evaluation, potency, and activity (EPA) space.[^a1]

### How does it work?
The state records the model's actor/object constraints, reciprocal actions, optional group identity, and protocol-dependent action sets.[^a1]

```yml
World:
  agents: [Agent]
  group: Agent?
  network: [AgentId -> [AgentId]]
  behaviors: Continuous | [EPA]
  object_rule: MinEvent | MaxReduction | Random
  reciprocity: 0..1
  group_action_rate: 0..1
  previous: Event?
  protocol: [Part]?

Agent:
  fundamental: EPA
  transient: EPA

EPA:
  evaluation: f64
  potency: f64
  activity: f64

Event:
  actor: AgentId
  behavior: EPA
  object: AgentId | Group

Part:
  turns: u32
  behaviors: Continuous | [EPA]
  actor_rule: ... # optional task-specific override
  settings: ... # optional changes and before/after code
```

- Each turn normally selects the member maximizing `sum((fundamental-transient)^2)`; a reciprocal turn instead reverses the preceding actor/object roles. Protocols can override actor selection.[^a2]
- For each eligible object, optimize behavior EPA to minimize event deflection. With discrete behaviors, restrict optimization to the supplied list. The network permits only directed actor→object edges; a group object can receive actions but cannot act.[^a3]
- Impression formation expands the nine pre-event actor/behavior/object EPA components into a polynomial feature vector `t` containing a constant, main terms and cross-products up to first order in each event element. A survey-estimated matrix `M` gives `transient_after = M*t`; the objective is `D=sum((F-M*t)^2)` over the actor/behavior/object fundamental EPA vector. Continuous behavior solves `∂D/∂B_i=0` for the three behavior dimensions.[^a4]
- `MinEvent` selects the object with least hypothetical event deflection; `MaxReduction` selects the greatest decrease from overall pre-event deflection; `Random` samples an eligible object. Perform the chosen event and update affected transient identities. In a group-directed action, every member except the actor experiences the object role.[^a3]

The jury replication fixes these experiment constants; they are not universal model defaults.[^a5]

```
JURY_SIZE = 12
MALE_JURORS = 8
FEMALE_JURORS = 4
MALE_EPA = (0.8, 1.6, -0.5)
FEMALE_EPA = (1.2, 0.7, 0.0)
INDIVIDUALITY = 1.0
INITIAL_TENSION = 1.0
GROUP_ACTION_RATE = 0.4
RECIPROCITY_RATE = 0.8
REPLICATIONS = 500
TURNS = 1000
```

- The jury study crosses three object rules with continuous/discrete behavior; the group identity starts at members' mean identity. Measured IPA behavior distributions and gender differences are compared with observed jury data.[^a5]
- This compact extraction omits the numerical survey coefficient matrix, the twelve IPA EPA entries, and complete software-developer protocols; these remain application inputs in the source.[^a4][^a5][^a6]

### What can it answer?
- It tests how role identities, interaction opportunities, object selection, and task protocols affect status and affective deflection.[^a6]

### Where does it apply?
- It applies to specified task groups with cultural EPA ratings; examples include juries, toy networks, expectation-state experiments, and software-development teams.[^a6]

## Metadata
### References
- [[ConsensusAndStratificationInTheAffectiveMeaningOfHumanSociality]]
- [[ModifiedSocialIdentitiesAmalgamationsAttributionsAndEmotions]]
- [[InteractionProcessAnalysisAMethodForTheStudyOfSmallGroups]]
- [[TheEquilibriumProblemInSmallGroupsWorkingPapersInTheTheoryOfAction]]
- [[RoleDifferentiationInSmallDecisionMakingGroupsInRBalesTParsonsEds]]
- [[PhasesInGroupProblemSolving]]
- [[StatusCharacteristicsAndSocialInteraction]]
- [[TheOrganizationalSelectionOfStatusCharacteristicsStatusEvaluationsInAnOpenSourceCommunity]]
- [[InteractionInSmallGroupsInJDelamaterEd]]
- [[TowardAStructuralTheoryOfActionNetworkModelsOfSocialStructurePerceptionAndAction]]
- [[StructuralChangeAndLearningWithinOrganizationsInALomiERLarsenEds]]
- [[AGarbageCanModelOfOrganizationalChoice]]
- [[LossOfPower]]
- [[WarmthAndCompetenceAFeministLookAtPowerAndNegotiationInCBTravisJWWhiteARutherfordWSWilliamsSLCookKFWycheEds]]
- [[ComplexSocialStructureAllianceStabilityAndMatingAccessInABottlenoseDolphinSuperAlliance]]
- [[PowerEquityAndCommitmentInExchangeNetworks]]
- [[ExpectationStatesTheoryInJDelamaterEd]]
- [[ICompagniUnderstandingChildrenSTransitionFromPreschoolToElementarySchool]]
- [[TaemsAFrameworkForEnvironmentCenteredAnalysisDesignOfCoordinationMechanisms]]
- [[OriginsOfTheModernMindThreeStagesInTheEvolutionOfCultureAndCognition]]
- [[TheSocialBrainHypothesisAndItsImplicationsForSocialEvolution]]
- [[TheMeritsOfAMeritocracyInOpenSourceSoftwareEcosystemsAcmInternationalConferenceProceedingSeriesDoi10114526428032642810]]
- [[EStateStructuralismATheoreticalMethod]]
- [[WhatSSoSpecialAboutSexGenderStereotypingAndDiscriminationInSOskampMCostanzoEds]]
- [[SocialDynamicsFromTheBottomUpAgentBasedModelsOfSocialInteractionInPBearmanPHedströmEds]]
- [[CentralityInSocialNetworksConceptualClarification]]
- [[TheoreticalFoundationsForCentralityMeasures]]
- [[ThePresentationOfSelfInEverydayLife]]
- [[TheSubjectVerbObjectApproachToSocialCognition]]
- [[The ODD Protocol for Describing Agent-Based and Other Simulation Models- A Second Update to Improve Clarity- Replication- and Structural Realism]]
- [[AgentBasedComputationalModelsOfReputationAndStatusDynamicsInFGiardiniRWittekEds]]
- [[ExpressiveOrderConfirmingSentimentsInSocialActions]]
- [[MeasurementReliabilityInDRHeiseEd]]
- [[ModelingInteractionsInSmallGroups]]
- [[SocialNetworkAnalysisShowsDirectEvidenceForSocialTransmissionOfToolUseInWildChimpanzees]]
- [[DenotativeAndConnotativeManagementOfUncertaintyAComputationalDualProcessModel]]
- [[AnInputOutputApproachToCliqueIdentification]]
- [[ConvergenceAndDivergenceInPrimateSocialSystemsInJGFleagleEd]]
- [[NetworkTheoryAndSmallGroups]]
- [[EmotionAndGroupCohesionInProductiveExchange]]
- [[GroundingGroupsInTheoryFunctionalCognitiveAndStructuralInterdependencies]]
- [[SociologyOfGroupsInJDWrightEd]]
- [[ASociologicalDeConstructionOfTheRelationshipBetweenStatusAndQuality]]
- [[WhyDoNominalCharacteristicsAcquireStatusValueAMinimalExplanationForStatusConstruction]]
- [[ANewTheoryOfGroupSolidarityAvailableAtHttpsEcommonsCornellEduHandle181374893]]
- [[TheSeedsOfWeakPowerAnExtensionOfNetworkExchangeTheory]]
- [[MesaAnAgentBasedModelingFrameworkAvailableAtHttpsMesaReadthedocsIoEnStableDoi1025080Majora7b98e3ed009]]
- [[TheRoleSetProblemsInSociologicalTheory]]
- [[SocialTheoryAndSocialStructure]]
- [[PowerInNegotiatedAndReciprocalExchange]]
- [[DistinguishingNormativeProcessesFromNoiseAComparisonOfFourApproachesToModelingImpressionsOfSocialEvents]]
- [[WhenMenBreakTheGenderRulesStatusIncongruityAndBacklashAgainstModestMen]]
- [[CrossCulturalUniversalsOfAffectiveMeaning]]
- [[ThreeFacesOfIdentity]]
- [[ProblemsOfEquilibrationInMAppelEd]]
- [[BehaviorTheControlOfPerception]]
- [[ComputationalOrganizationTheoryAutonomousAgentsAndEmergentBehavior]]
- [[TheSocialConstructionOfStatusValueGenderAndOtherNominalCharacteristics]]
- [[StatusWhyIsItEverywhereWhyDoesItMatter]]
- [[GenderAsStatusAnExpectationStatesTheoryApproachInAHEaglyAEBeallRJSternbergEds]]
- [[TheGenderSystemAndInteractions]]
- [[SelfPromotionAsARiskFactorForWomen]]
- [[FreeOpenSourceSoftwareDevelopmentRecentResearchResultsAndEmergingOpportunitiesEsecFse076thJointMeetingOfTheEuropeanSoftwareEngineeringConferenceAndTheAcmsigsoftSymposiumOnTheFoundationsOfSoftwareEngineeringCompanionPapersDoi10114512950141295019]]
- [[MakingSenseOfSocialInteractionEmotionalCoherenceDrivesSemanticIntegrationAsAssessedByEventRelatedPotentials]]
- [[ModelingDynamicIdentitiesAndUncertaintyInSocialInteractionsBayesianAffectControlTheory]]
- [[AffectiveDynamicsOfLeadershipAnExperimentalTestOfAffectControlTheory]]
- [[SocialStructureNetworksAndEStateStructuralismModels]]
- [[MeanAffectiveRatingsOf2106ConceptsByUniversityOfNorthCarolinaUndergraduatesIn1978]]
- [[SexRoleDifferentiationInJuryDeliberations]]
- [[GenderDifferencesAndBiasInOpenSourcePullRequestAcceptanceOfWomenVersusMen]]
- [[HowToMakeDecisionsCoherenceEmotionAndPracticalInferenceInEMillgramEd]]
- [[GenderedBehaviorAsADisadvantageInOpenSourceSoftwareDevelopment]]
- [[CollectiveIntelligenceAndGroupPerformance]]
- [[ATopologyOfGroupsWhatGithubCanTellUsAboutOnlineCollaboration]]

## Audit Log
- Audit invalidated (2026-09-30): auditor admitted relying on spot checks and previous reports before clearing flags. A full independent audit is still required.
- 2026-09-30: Full-source design audit found missing reciprocal actor selection and group-directed actions; unexplained ACT minimizer concealed polynomial and objective; missing network eligibility and protocol constraints; incomplete jury control settings. Corrected against the source passages below; independent re-audit pending.[^design]
- Independent audit found the publication date and actor/object/action selection mechanisms incomplete. The note now gives the article date, EPA event/deflection basis, three object-selection rules, discrete action-space option, and jury replication setup from the full text. At that stage, independent re-audit remained pending.

- WITHDRAWN audit claim (2026-09-30): incomplete source checks; this audit does not establish a pass.

## LLM Justification
[^r1]: The research questions are a concise transformation of the primary source’s abstract and stated aims. Source location: ACTING Model, Entities/state variables, Process overview and scheduling, Basic principles, Objectives, and Interaction. Source: [Modeling Interaction in Collaborative Groups: Affect Control Within Social Structure](https://www.jasss.org/24/4/6.html).


[^a1]: Model → Entities, state variables, and scales, Table 1: group members, optional group object, GroupModel and ProtocolGroupModel attributes; fundamental identity is fixed and transient identity changes.

[^a2]: Model → Process overview and scheduling and Interaction → Actor and object selection; Table 1 defines reciprocal probability and protocol select_actor override.

[^a3]: Model → Interaction: object-selection criteria, action space, interaction structure, protocols; Process overview explains group actions affecting all non-actors.

[^a4]: Model → Basic principles, Eqs. (1)–(3), and Objectives, Eqs. (4)–(5). Coefficients come from a 1978 North Carolina undergraduate survey, as used by Heise (2013). The source refers to Heise (2007) for the full continuous optimum derivation.

[^a5]: Simulations → Application: Jury deliberations, Table 2 and experiment paragraphs specify all constants and the six crossed conditions; continuous actions are assigned to nearest IPA category by Euclidean distance.

[^a6]: Simulations → restricted toy networks, expectation states theory, and open-source software teams; model purpose is role/status and network interplay.

[^design]: Source audit checked the full text at https://www.jasss.org/24/4/6.html. Model footnotes identify the passages supporting the corrections.
