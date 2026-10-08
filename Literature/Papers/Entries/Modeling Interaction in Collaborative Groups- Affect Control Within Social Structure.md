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
  group_actions_enabled: bool
  group_action_rate: 0..1 # used when group actions are enabled
  reciprocity_rate: 0..1
  data_model: USUnisex | USMale | USFemale | CanadaUnisex | CanadaMale | CanadaFemale | ChinaUnisex | GermanyUnisex
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
  actor_rule: code? # optional task-specific override
  settings: ... # parameter values for this protocol segment
  before_after_code: (str, str)?
```

- At each step, a reciprocal action occurs with `reciprocity_rate`; the prior object then becomes the actor. Otherwise, the agent with greatest deflection acts. Protocol segments may replace actor selection. The schedule advances, the actor chooses an eligible object/behavior, and involved transient identities and deflections are updated.[^a2]
- For each eligible object, optimize behavior EPA to minimize event deflection. With discrete behaviors, restrict optimization to the supplied list. The network permits only directed actor→object edges; a group object can receive actions but cannot act.[^a3]
- Impression formation expands the nine pre-event actor/behavior/object EPA components into polynomial feature vector `t` with a constant, main terms, and all products up to first order in each component. A survey-estimated coefficient matrix `M` gives `transient_after = M*t`; event deflection is the sum of squared differences between the nine fundamental and predicted transient EPA values. For continuous behavior, solve `∂D/∂B_i=0` for evaluation, potency, and activity; discrete behavior chooses among the supplied EPA vectors.[^a4]
- `MinEvent` selects the object with least after-event deflection for the actor/object/behavior triple; `MaxReduction` selects the greatest decrease in overall group deflection; `Random` samples an eligible object. The network restricts actor→object pathways. A group-directed action updates every member except the actor as though each were the object.[^a3]

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

- The jury replication uses 12 jurors (8 male, 4 female), the cited male/female EPA identities, a group identity initialized to member means, individuality and initial tension 1.0, group-action rate .4, reciprocity .8, 500 replications and 1,000 turns. It crosses three object rules with continuous/discrete behavior against IPA annotations from 29 juries; the discrete/MaxReduction condition has the highest behavior-distribution correlation (0.96; gender-difference correlation 0.90). Discrete actions improve correlations under each rule, while MaxReduction notably lowers deflection.[^a5]
- Initialization draws each agent’s fundamental EPA from a clipped normal around its target mean with standard deviation `individuality`; initial transient EPA is clipped normal around the fundamental with standard deviation `initial_tension`. The optional group identity defaults to the member mean. The ACT coefficient matrix and application-specific role/action EPA ratings remain inputs.[^a4][^a7]
- In four three-agent toy network topologies, all agents share female-centered EPA [1.78, 0.83, 0.84], individuality and initial tension 1.0; no group object is used and results average 2,000 runs. Symmetric networks produce equal mean transients; asymmetric positions change potency and deflection, with greater action opportunity yielding lower deflection in the hierarchical topology.[^a6]
- In the expectation-states experiment, a three-agent hierarchy crosses four male/female leader and group-composition settings using EPA [1.78, 0.83, 0.84] (female) and [1.07, 2.01, 1.05] (male), over 2,000 runs. Male-majority groups have greater overall deflection; at equal role composition, a female leader produces significantly greater deflection than a male leader in the model.[^a6]
- The GitHub illustration reverses accepted-PR network edges to represent actions toward submitters, uses a group object, ignores self-loops, and cycles through submit, 0–10 discussion actions, then accept/reject by a merge-authorized candidate. A 17-user mini-survey supplies EPA ratings; 5,000 runs compare four experienced/novice assignments in each of two networks. Assigning experienced developers to high-status positions lowers group mean deflection versus random assignment.[^a6]
- These are model demonstrations, not direct empirical validation of group-level ACT. Agents are assumed to share full information about one another’s transient identities/deflection; learning and long-term career goals are not modeled. ACT’s impression equations were estimated from dyadic vignettes, and turn-taking mechanisms remain a limitation.[^a6]

### What can it answer?
- It tests how role identities, interaction opportunities, object selection, and task protocols affect status and affective deflection.[^a6]

### Where does it apply?
- It applies to specified task groups with cultural EPA ratings, interaction pathways, and optional protocols; examples include juries, toy networks, expectation-state experiments, and software-development teams. Group-level inference is idealized, not empirically validated by this paper.[^a6]

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
- 2026-10-03: Full publisher-source review expanded the state/control schema, initialization, and source-reported jury, toy-network, expectation-states and GitHub experiment settings/outcomes and limitations. References were checked against all 74 publisher entries and retained. Warning remains unchanged; independent re-audit pending.[^design]
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

[^a6]: Simulations → restricted toy networks, expectation states theory, and GitHub collaboration; see Figures 3–12, Table 4 and protocol description for settings, replications, outcomes, and source limits.

[^a7]: Appendix ODD → Initialization: clipped-normal initialization for fundamental/transient EPA and group identity mean default.

[^design]: Source audit checked the complete publisher text and appendix at https://www.jasss.org/24/4/6.html. Model footnotes identify the passages supporting the extraction.
