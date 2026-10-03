---
title: "Modelling Agents Endowed with Social Practices: Static Aspects"
authors:
  - "[[Literature/Authors/Rijk Mercuur|Rijk Mercuur]]"
  - "[[Literature/Authors/Virginia Dignum|Virginia Dignum]]"
  - "[[Literature/Authors/Catholijn M. Jonker|Catholijn M. Jonker]]"
source: "https://arxiv.org/html/1811.10981v1"
doi: "10.48550/arXiv.1811.10981"
publication date: "2018-11-27"
tags:
  - "model"
  - "social_practice"
read status: Todo
⚠️:
  - audit failed
---

## Abstract

To understand societal phenomena through simulation, we need computational variants of socio-cognitive theories. Social Practice Theory has provided a unique understanding of social phenomena regarding the routinized, social and interconnected aspects of behaviour. This paper provides the Social Practice Agent (SoPrA) model that enables the use of Social Practice Theory (SPT) for agent-based simulations. We extract requirements from SPT, construct a computational model in the Unified Modelling Language, verify its implementation in Netlogo and Protégé and show how SoPrA maps on a use case of commuting. The next step is to model the dynamic aspect of SPT and validate SoPrA’s ability to provide understanding in different scenario’s. This paper provides the groundwork with a computational model that is a correct depiction of SPT, computational feasible and can be directly mapped to the habitual, social and interconnected aspects of a target scenario.

## Research Questions
> Research Questions extracted via LLM

- How can static elements of Social Practice Theory be represented computationally for agent-based simulation?[^r1]
- How does SoPrA map habitual, social, and interconnected practice aspects onto commuting?[^r1]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?
- SoPrA is a static representation of habitual, social, and interconnected activities; it provides structures for future agent decision models.[^s1]

### How does it work?
The schema preserves the UML's association strengths and separate personal/shared beliefs; each activity instance is one view of a bodily movement.[^s2]

```yml
World:
  agents: [Agent]
  activities: [Activity]
  cues: [Cue]
  values: [Value]
  implementation: [Implementation]
  triggers: [Trigger]
  meanings: [Meaning]
  beliefs: [Belief]
  adherence: [Adherence]
  same: [ActivityId -> [ActivityId]]

Cue:
  name: str
  kind: Object | Location | Agent | Activity

Agent: Cue
  habit_rate: f64

Activity: Cue
  level: Action | AbstractAction | TopAction

Value:
  name: str

Implementation:
  child: ActivityId
  parent: ActivityId
  kind: AllOf | PartOf

Trigger:
  activity: ActivityId
  cue: CueId
  strength: f64

Meaning:
  activity: ActivityId
  value: ValueId
  strength: f64

Belief:
  agent: AgentId
  activity: ActivityId
  personal_strength: f64
  shared_strength: f64

Adherence:
  agent: AgentId
  value: ValueId
  strength: f64
```

- `AllOf` represents generalization; `PartOf` requires completion of all component activities. The hierarchy does **not** specify their order or concurrency and does **not** model overlapping activities.[^s3]
- Trigger strength links an activity to a cue; meaning strength links it to a value. Belief strengths distinguish an agent's agreement from its belief about others' agreement. Adherence measures how much the agent values a value; habit rate represents individual differences in habit acquisition.[^s2]
- Formal constraints: the implementation graph is a directed tree with one root; actions are leaves, abstract actions intermediate nodes, and the top action the root. Every `PartOf` child has at least one sibling that is also `PartOf`.[^s4]
- A parent inherits each value's mean association strength across its children; leaf strengths are supplied by the application. Habit strengths need not be inherited. `same` is reflexive, symmetric, and transitive.[^s4]
- This extraction omits UML drawing details. The paper supplies no complete simulation loop, learning update, or action-selection rule; time cues and dynamic habit learning are deferred.[^s5]

### What can it answer?
- It checks whether a static practice representation captures the proposed requirements and maps them onto a commuting scenario; it does not test behavioral prediction.[^s6]

### Where does it apply?
- It provides a representation for practice-based agent models, verified in NetLogo and Protégé and illustrated with commuting.[^s6]

## Metadata
### References
- [[TheStructuralOrganizationOfHumanValuesEvidenceFromThreeRoundsOfTheEuropeanSocialSurveyEss|The Structural Organization of Human Values-Evidence from Three Rounds of the European Social Survey (ESS)]]
- [[OutlineOfATheoryOfPractice|Outline of a theory of practice]]
- [[CommutingPracticesNewInsightsIntoModalShiftFromTheoriesOfSocialPractice|Commuting practices: New insights into modal shift from theories of social practice]]
- [[ModelingSocialActionForAIAgents|Modeling social action for AI agents]]
- [[AKnowledgeDrivenApproachToActivityRecognitionInSmartHomes|A Knowledge-Driven Approach to Activity Recognition in Smart Homes]]
- [[BringingValuesBackInTheAdequacyOfTheEuropeanSocialSurveyToMeasureValuesIn20Countries|Bringing values back in: The adequacy of the European social survey to measure values in 20 countries]]
- [[NoSmokingHereValuesNormsAndCultureInMultiAgentSystems|No Smoking Here: Values, Norms and Culture in Multi-Agent Systems]]
- [[AModelForOrganizationalInteractionBasedOnAgentsFoundedInLogic|A model for organizational interaction: based on agents, founded in logic]]
- [[AutonomousAgentsWithNorms|Autonomous agents with norms]]
- [[TowardsSociallySophisticatedBDIAgents|Towards socially sophisticated BDI agents]]
- [[FromAutisticToSocialAgents|From Autistic to Social Agents]]
- [[ContextualizedPlanningUsingSocialPractices|Contextualized Planning Using Social Practices]]
- [[ArtificialSocialReasoningComputationalMechanismsForReasoningAboutOthers|Artificial social reasoning: Computational mechanisms for reasoning about others]]
- [[StructuralEquivalenceOfTheValuesDomainAcrossCulturesDistinguishingSamplingFluctuationsFromMeaningfulVariation|Structural Equivalence of the Values Domain Across Cultures: Distinguishing Sampling Fluctuations From Meaningful Variation]]
- [[ASystematicReviewAndMetaAnalysisOfApplicationsOfTheSelfReportHabitIndexToNutritionAndPhysicalActivityBehaviours|A systematic review and meta-analysis of applications of the self-report habit index to nutrition and physical activity behaviours]]
- [[TheConstitutionOfSocietyOutlineOfTheTheoryOfStructuration|The constitution of society: Outline of the theory of structuration]]
- [[SocialIntelligence|Social Intelligence]]
- [[HowToRelateModelsToRealityAnEpistemologicalFrameworkForTheValidationAndVerificationOfComputationalModels|How to Relate Models to Reality? An Epistemological Framework for the Validation and Verification of Computational Models]]
- [[WhatCognitiveMechanismsPredictTravelModeChoiceASystematicReviewWithMetaAnalysis|What cognitive mechanisms predict travel mode choice? A systematic review with meta-analysis]]
- [[GRASPAgentsSocialFirstIntelligentLater|GRASP agents: social first, intelligent later]]
- [[GeneratingSocialPractices|Generating Social Practices]]
- [[DescriptionLogicAFormalFoundationForOntologyLanguagesAndTools|Description Logic : A Formal Foundation for Ontology Languages and Tools]]
- [[BehaviourInCommonsDilemmasHomoEconomicusAndHomoPsychologicusInAnEcologicalEconomicModel|Behaviour in commons dilemmas: Homo economicus and Homo psychologicus in an ecological-economic model]]
- [[FormalAnalysisOfModelsForTheDynamicsOfTrustBasedOnExperiences|Formal Analysis of Models for the Dynamics of Trust based on Experiences]]
- [[TowardAFormalismForConversationProtocolsUsingJointIntentionTheory|Toward a formalism for conversation protocols using joint intention theory]]
- [[HabitualBehaviorsOrPatternsOfPracticeExplainingAndChangingRepetitiveClimaterelevantActions|Habitual behaviors or patterns of practice? Explaining and changing repetitive climate‐relevant actions]]
- [[HowAreHabitsFormedModellingHabitFormationInTheRealWorld|How are habits formed: Modelling habit formation in the real world]]
- [[OnActorNetworkTheoryAFewClarifications|On actor-network theory: A few clarifications]]
- [[InterventionsOnContextualizedDecisionMakingAnAgentBasedSimulationStudy|Interventions on Contextualized Decision Making : an Agent-Based Simulation Study]]
- [[ModelingSocialPreferencesWithValues|Modeling Social Preferences with Values]]
- [[ModellingTheSocialPracticesOfAnEmergencyRoomToEnsureStaffAndPatientWellbeing|Modelling the Social Practices of an Emergency Room to Ensure Staff and Patient Wellbeing]]
- [[TheEmergenceOfASharedActionOntologyBuildingBlocksForATheory|The emergence of a shared action ontology: Building blocks for a theory]]
- [[AutomaticityATheoreticalAndConceptualAnalysis|Automaticity: a theoretical and conceptual analysis]]
- [[TheProtegeProjectALookBackAndALookForward|The protégé project: a look back and a look forward]]
- [[UsingABMToClarifyAndRefineSocialPracticeTheory|Using ABM to Clarify and Refine Social Practice Theory]]
- [[CombiningOntologicalAndTemporalFormalismsForCompositeActivityModellingAndRecognitionInSmartHomes|Combining ontological and temporal formalisms for composite activity modelling and recognition in smart homes]]
- [[ExtractingOwlOntologiesFromAgentBasedModelsANetlogoExtension|Extracting OWL Ontologies from Agent-Based Models: A Netlogo Extension]]
- [[TowardATheoryOfSocialPracticesADevelopmentInCulturalistTheorizing|Toward a theory of social practices: A development in culturalist theorizing]]
- [[SocialPracticesAWittgensteinianApproachToHumanActivityAndTheSocial|Social Practices. A Wittgensteinian approach to human activity and the social]]
- [[AgentBasedModellingOfSocialEcologicalSystemsAchievementsChallengesAndAWayForward|Agent-based modelling of social-ecological systems: Achievements, challenges, and a way forward]]
- [[AnOverviewOfTheSchwartzTheoryOfBasicValues|An Overview of the Schwartz Theory of Basic Values]]
- [[RefiningTheTheoryOfBasicIndividualValues|Refining the theory of basic individual values]]
- [[TheConstructionOfSocialReality|The Construction of Social Reality]]
- [[TheDynamicsOfSocialPracticeEverydayLifeAndHowItChanges|The Dynamics of Social Practice: Everyday Life and How it Changes]]
- [[RuleBasedActivityRecognitionFrameworkChallengesTechniqueAndLearning|Rule-based activity recognition framework: Challenges, technique and learning]]
- [[InterpretationAndTheSciencesOfMan|Interpretation and the Sciences of Man]]
- [[IntelligenceAndItsUses|Intelligence and its uses]]
- [[AccurateActivityRecognitionInAHomeSetting|Accurate activity recognition in a home setting]]
- [[HabitsAndImplementationIntentions|Habits and implementation intentions]]
- [[ReflectionsOnPastBehaviorASelfReportIndexOfHabitStrength|Reflections on Past Behavior: A Self-Report Index of Habit Strength]]
- [[ArguingToMotivateDecisions|Arguing to motivate decisions]]
- [[SimulationAndSimilarityUsingModelsToUnderstandTheWorld|Simulation and similarity: Using models to understand the world]]
- [[NetlogoItself|Netlogo itself]]
- [[ANewLookAtHabitsAndTheHabitGoalInterface|A new look at habits and the habit-goal interface]]
- [[PremackAndWoodruffChimpanzeeTheoryOfMind|Premack and Woodruff : Chimpanzee theory of mind]]

## Audit Log
- 2026-09-30: Complete independent primary-source audit found the static model faithful, but only 6 of 55 source bibliography entries were imported. Restored all 55 entries in source order, preserving genuine imported targets where their titles match. Independent re-audit remains pending.
- Audit invalidated (2026-09-30): auditor admitted relying on spot checks and previous reports before clearing flags. A full independent audit is still required.
- 2026-09-30: Full-source design audit found invented ordered/overlapping execution; opaque associations omitted strengths and belief perspectives; missing tree and inheritance constraints; nonexistent §4.3 citation. Corrected against the source passages below; independent re-audit pending.[^design]
- Independent audit found the activity/context/meaning relationships and hierarchy semantics missing. The note now distinguishes `allOf` and `partOf`, context-triggered habits, value links, and personal versus shared beliefs; dynamic learning remains explicitly out of scope. At that stage, independent re-audit remained pending.

- WITHDRAWN audit claim (2026-09-30): incomplete source checks; this audit does not establish a pass.

## LLM Justification
[^r1]: The research questions are a concise transformation of the primary source’s abstract and stated aims. Source location: Sections 3–5 and the commuting use case. Source: [Modelling Agents Endowed with Social Practices: Static Aspects](https://arxiv.org/abs/1811.10981).


[^s1]: §§1 and 4 describe the static computational groundwork and habitual/social/interconnected aspects.

[^s2]: §§5.2–5.4, Figures 4–6 and Appendix A: HabitualTrigger and RelatedValue have strength; Belief has personalStrength and sharedStrength; Agent has habitRate; AdheredValue has strength. Agent and Activity specialize ContextCue.

[^s3]: §5.1 explicitly states that order and simultaneous execution are unspecified, and sequential activities can be modeled but overlapping activities cannot. Figure 2 assigns allOf to generalization and partOf to composition.

[^s4]: §5.5, Eqs. (1)–(7): directed-tree and activity-type constraints, sibling requirement, and mean value-strength inheritance. The following paragraphs reject mandatory habit inheritance and define same as an equivalence relation.

[^s5]: §5.2 defers time cues; §5.4 defers learning dynamics; §8 states future work is to model dynamic aspects. No transition procedure is supplied by this static paper.

[^s6]: §6 verifies implementation and requirements; §7 maps the commuting scenario; §8 distinguishes this groundwork from future dynamic modeling and validation.

[^design]: Source audit checked the full text at https://arxiv.org/html/1811.10981v1. Model footnotes identify the passages supporting the corrections.
