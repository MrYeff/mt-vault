---
title: "Affect control processes: Intelligent affective interaction using a partially observable Markov decision process"
tags:
authors:
  - "[[Literature/Authors/Jesse Hoey|Jesse Hoey]]"
  - "[[Literature/Authors/Tobias Schröder|Tobias Schröder]]"
  - "[[Literature/Authors/Areej Alhothali|Areej Alhothali]]"
publication date: 2016-02-01
source: https://cs.uwaterloo.ca/~jhoey/teaching/cs886-affect/papers/bayesact.pdf
doi: 10.1016/j.artint.2015.09.004
read status: Todo
---
## Abstract

This paper describes a novel method for building affectively intelligent human-interactive agents. The method is based on a key sociological insight that has been developed and extensively verified over the last twenty years, but has yet to make an impact in artificial intelligence. The insight is that resource bounded humans will, by default, act to maintain affective consistency. Humans have culturally shared fundamental affective sentiments about identities, behaviours, and objects, and they act so that the transient affective sentiments created during interactions confirm the fundamental sentiments. Humans seek and create situations that confirm or are consistent with, and avoid and supress situations that disconfirm or are inconsistent with, their culturally shared affective sentiments. This "affect control principle" has been shown to be a powerful predictor of human behaviour. In this paper, we present a probabilistic and decision-theoretic generalisation of this principle, and we demonstrate how it can be leveraged to build affectively intelligent artificial agents. The new model, called BayesAct, can maintain multiple hypotheses about sentiments simultaneously as a probability distribution, and can make use of an explicit utility function to make value-directed action choices. This allows the model to generate affectively intelligent interactions with people by learning about their identity, predicting their behaviours using the affect control principle, and taking actions that are simultaneously goal-directed and affect-sensitive. We demonstrate this generalisation with a set of simulations. We then show how our model can be used as an emotional "plug-in" for artificially intelligent systems that interact with humans in two different settings: an exam practice assistant (tutor) and an assistive device for persons with a cognitive disability.


## Research Questions
> Research Questions extracted via LLM

- How can Affect Control Theory be extended into a probabilistic, decision-theoretic agent that reasons over uncertain affective identities and sentiments?[^r1]
- Can such an agent balance task goals with affect-sensitive interaction in simulations and human-interactive applications?[^r2]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?
BayesAct extends an application-specific POMDP with uncertain affective sentiments so an agent can choose both an action’s propositional content (“what”) and affective delivery (“how”).[^r3]

### How does it work?
The schema summarizes the POMDP variables and action/observation split defined in §3.1.[^r8]
```
EPA:
  evaluation: f32
  potency: f32
  activity: f32

EPAEvent:
  agent: EPA
  behavior: EPA
  client: EPA

ApplicationState:
  interaction_turn: ...
  other_state: ...

ApplicationAction: ...
ApplicationObservation: ...
AffectObservation: ...

BayesActState:
  application: ApplicationState
  fundamentals: EPAEvent
  transients: EPAEvent

Observation:
  application: ApplicationObservation
  affect: AffectObservation

Action:
  propositional: ApplicationAction
  affective_delivery: EPA

BayesAct:
  belief: [BayesActState -> 0..1]
  transition: ...
  observation_model: ...
  reward: ...
```
- F and T are continuous nine-dimensional vectors, each containing EPA sentiments for the agent, behaviour, and client. These are not categorical identity or behaviour distributions.[^r8]
- BayesAct recasts ACT’s actor/object roles as the fixed agent/client referents; the current turn is encoded in X and determines which actor/client rows are used in the empirical impression map.[^r8]
- The stochastic observation Ωf is evidence about the client’s behavior sentiment, inferred from data rather than directly measured; Ωx provides evidence about application state.[^r8]
- After an action and new observations, Bayesian filtering updates the belief over S={F,T,X}.[^r8]

- Transient sentiments follow the turn-conditioned empirical ACT impression map M(X)G; fundamental-sentiment transitions balance low deflection against inertia.[^r4][^r16]
- Reward combines an application-dependent task term Rₓ with an affective term Rₛ that penalizes deflection between F and T.[^r4][^r16]
- The paper leaves the exact task reward and its relative weight against affective reward to the application.[^r4][^r16]

- The agent chooses a pair: propositional task action A and continuous EPA affective delivery Ba.[^r5][^r9]
- The paper describes POMCP but uses a greedy one-step approximation for Ba: it approximates the belief by a point at the expected (or most likely) state, samples candidate affective actions from the ACT-normal distribution, and selects the sampled Ba with greatest expected next reward.[^r5][^r9]
- Propositional actions A are handled by iterating over them as in POMCP; the full multi-step rollout is not used.[^r5][^r9]
- Application-specific transition, observation, and reward functions still need to be supplied.[^r5][^r9]

- General implementation defaults are α=1.0 for deflection covariance, βa=βc=0.01 for identity inertia, β′a=β′c=0.01 for initial identity variance, γ=1.0 for environment noise, γd=0.9 when discounting is needed, and N=300 particles; roughening noise is σr=N⁻¹ᐟ³.[^r10]
- Individual applications can override these values and define their own X dynamics, reward, and input/output mappings.[^r10]

### What can it answer?
- In simulations, BayesAct learns hidden identities and adapts to changing identities under varying observation noise.[^r6]
- In the authors’ reported runs, roughly 50 samples were sufficient for robustness up to environment noise σe=2, and identity samples typically converged near the true identities within about 15 iterations.[^r6]
- In preliminary handwashing simulations, adaptive BayesAct actions were more robust across client identities than a fixed affective policy; the paper describes the applications as demonstrations requiring further empirical testing.[^r6]

### Where does it apply?
It applies when affective inputs and outputs can be represented in EPA space; the paper assumes signal recognition and generation are supplied by other components.[^r7]

## Metadata
### References
- [[ExpressionOfAffectsInEmbodiedConversationalAgents]]
- [[ABlueprintForAffectiveComputingASourcebookAndManual]]
- [[SynthesisOfEmotionalSpeech]]
- [[AnIntegrativeTheoryOfIntergroupConflict]]
- [[AffectControlTheory]]
- [[EmbodiedConversationalAgents]]
- [[NormativeMultiAgentSystems]]
- [[AnAffectControlTheoryOfTechnology]]
- [[TheSocialPsychologyOfIntergroupRelations]]
- [[SocialCommitmentsInADepersonalizedWorld]]
- [[SelfIdentityAndSocialInstitutions]]
- [[ExpressiveOrderConfirmingSentimentsInSocialActions]]
- [[IntroductionToComputationalSocialSciencePrinciplesAndApplications]]
- [[PlanningForHumanRobotInteractionInSociallySituatedTasks]]
- [[StrategiesForAffectControlledActionSelectionInSoarRl]]
- [[ABlueprintForAffectiveComputingASourcebook]]
- [[FlameFuzzyLogicAdaptiveModelOfEmotions]]
- [[ProceedingsOfTheSixteenthConferenceOnUncertaintyInArtificialIntelligence2000]]
- [[DescarteSErrorEmotionReasonAndTheHumanBrain]]
- [[ProbabilisticAlgorithmsInRobotics]]
- [[SurveyingCulturesDiscoveringSharedConceptionsAndSentiments]]
- [[HotThoughtMechanismsAndApplicationsOfEmotionalCognition]]
- [[CoherenceInThoughtAndAction]]
- [[TheEmotionalBrainTheMysteriousUnderpinningsOfEmotionalLife]]
- [[PsychsimModelingTheoryOfMindWithDecisionTheoreticAgents]]
- [[ModelingLearnerAffectWithTheoreticallyGroundedDynamicBayesianNetworks]]
- [[ProceedingsOfThe2015ConferenceOfTheNorthAmericanChapterOfTheAssociationForComputationalLinguisticsHumanLanguageTechnologies]]
- [[AppraisalProcessesInEmotion]]
- [[UnderstandingComputersAndCognitionANewFoundationForDesign]]
- [[CultureConstrainedAffectiveConsistencyOfInterpersonalBehavior]]
- [[TowardsRoboticAssistantsInNursingHomesChallengesAndResults]]
- [[BayesianAffectControlTheory]]
- [[BridgingTheGapBetweenSocialAnimalAndUnsocialMachineASurveyOfSocialSignalProcessing]]
- [[TheCognitiveStructureOfEmotions]]
- [[TheCoachPromptingSystemToAssistOlderAdultsWithDementiaThroughHandwashingAnEfficacyStudy]]
- [[EmotionAndAdaptation]]
- [[BeingAndTime]]
- [[ImpressionsFromEvents]]
- [[ModifiedSocialIdentitiesAmalgamationsAttributionsAndEmotions]]
- [[DescartesErrorEmotionReasonAndTheHumanBrain]]
- [[StudiesOnTheGeneralityOfAffectiveMeaningSystems]]
- [[EvidenceForAThreeFactorTheoryOfEmotions]]
- [[TheDynamicsOfJapaneseAndAmericanInterpersonalEventsBehavioralSettingsVersusPersonalityTraits]]
- [[TemporalityAndIdentityLossDueToAlzheimerSDisease]]
- [[CultureAsSharedCognitiveRepresentations]]
- [[OptimalControlOfMarkovProcessesWithIncompleteStateInformation]]
- [[HedAComputationalModelOfAffectiveAdaptationAndEmotionDynamics]]
- [[ConsensusAndStratificationInTheAffectiveMeaningOfHumanSociality]]
- [[AffectiveComputingWithPrimaryAndSecondaryEmotionsInAVirtualHuman]]
- [[CrossCulturalUniversalsOfAffectiveMeaning]]
- [[MemoryOfMyselfAutobiographicalMemoryAndIdentityInAlzheimerSDisease]]
- [[CanARationalAgentAffordToBeAffectlessAFormalApproach]]
- [[AttitudesAndCognitiveOrganization]]
- [[TheImpactOfEmotionsOnLearningAndAchievementTowardsATheoryOfCognitiveMotivationalMediators]]
- [[ASurveyOfPointBasedPomdpSolvers]]
- [[EmpiricallyBuildingAndEvaluatingAProbabilisticModelOfUserAffect]]
- [[DecisionTheoreticPlanningStructuralAssumptionsAndComputationalLeverage]]
- [[TheAffectiveControlOfEventsWithinSettings]]
- [[ASurveyOfAlgorithmicMethodsForPartiallyObservedMarkovDecisionProcesses]]
- [[TractablePomdpRepresentationsForIntelligentTutoringSystems]]
- [[TheMeasurementOfMeaning]]
- [[PeopleSensorsDecisions]]
- [[EmotionAndAction]]
- [[AffectiveDynamicsOfLeadershipAnExperimentalTestOfAffectControlTheory]]
- [[RewardIsAssessedInThreeDimensionsThatCorrespondToTheSemanticDifferential]]
- [[TheTheoryOfMoralSentiments]]
- [[OpinionMiningAndSentimentAnalysis]]
- [[NovelApproachToNonlinearNonGaussianBayesianStateEstimation]]
- [[SarsopEfficientPointBasedPomdpPlanningByApproximatingOptimallyReachableBeliefSpaces]]
- [[ADomainIndependentFrameworkForModelingEmotion]]
- [[TheStrengthOfWeakIdentitiesSocialStructuralSourcesOfSelfSituationAndEmotionalExperience]]
- [[AffectivelyAlignedCognitiveAssistanceUsingBayesianAffectControlTheory]]
- [[SolvingTheEmotionParadoxCategorizationAndTheExperienceOfEmotion]]
- [[SymbolicInteractionismAsAffectControl]]
- [[AffectDetectionAnInterdisciplinaryReviewOfModelsMethodsAndTheirApplications]]
- [[MarkovDecisionProcessesDiscreteStochasticDynamicProgramming]]
- [[EconomicsAndIdentity]]
- [[ModelingInteractionsInSmallGroups]]
- [[IntrinsicallyMotivatedReinforcementLearning]]
- [[FlowThePsychologyOfOptimalExperience]]
- [[PointBasedValueIterationForContinuousPomdps]]
- [[Mach]]
- [[RaoBlackwellisedParticleFilteringForDynamicBayesianNetworks]]
- [[DissectingTheSocialityOfEmotionAMultilevelApproach]]
- [[WhatDeterminesAFeelingSPositionInAffectiveSpaceACaseForAppraisal]]
- [[ASurveyOfAffectRecognitionMethodsAudioVisualAndSpontaneousExpressions]]
- [[TheWorldOfEmotionsIsNotTwoDimensional]]
- [[EmotionCognitionAndBehavior]]
- [[ProbabilisticReasoningInIntelligentSystemsNetworksOfPlausibleInference]]
- [[SocialComputingFromSocialInformaticsToSocialIntelligence]]
- [[MonteCarloSamplingMethodsForApproximatingInteractivePomdps]]
- [[PlanningAndActingInPartiallyObservableStochasticDomains]]
- [[MonteCarloPlanningInLargePomdps]]
- [[NormsInMasDefinitionsAndRelatedConcepts]]
- [[BayesianAffectControlTheoryOfSelf]]
- [[GoodNewsOrBadNewsUsingAffectControlTheoryToAnalyzeReadersReactionTowardsNewsArticles]]
- [[UnderstandingComputersAndCognitionANewFoundationOfDesign]]
- [[TheSocioEmotionalBasisOfHumanInteractionAndCommunicationHowWeConstructOurSocialWorld]]
- [[ProbabilisticRobotics]]
- [[AffectiveComputing]]
- [[PartiallyObservableSequentialDecisionMakingForProblemSelectionInAnIntelligentTutoringSystem]]
- [[PartiallyObservableMarkovDecisionProcessesForSpokenDialogSystems]]
- [[ModelingDynamicIdentitiesAndUncertaintyInSocialInteractions]]
- [[DecisionTheoryModelsForApplicationsInArtificialIntelligenceConceptsAndSolutions]]
- [[DescartesErrorEmotionReasonAndTheHumanBrainNewYorkGrossetPutnam1994]]
- [[AnIntroductionToFullyAndPartiallyObservableMarkovDecisionProcesses]]
- [[HandbookOfCognitionAndEmotion]]
- [[FlowThePsychologyOfOptimalExperienceNewYorkHarperperennial1990]]
- [[MonteCarloPlanningForSociallyAlignedAgentsUsingBayesianAffectControlTheory]]
- [[ThinkingFastAndSlow]]
- [[EmotionDrivenReinforcementLearning]]
- [[ProceedingsOfThe2013AcmInternationalJointConferenceOnPervasiveAndUbiquitousComputing]]
- [[ComputationalModelsOfEmotion]]
- [[2013HumaineAssociationConferenceOnAffectiveComputingAndIntelligentInteraction]]
- [[UnresolvedReference6BA987826CEA5FFF]]
- [[ContemporarySocialPsychologicalTheories]]
- [[UnresolvedReference43EDD9AE509F7296]]
- [[UnresolvedReference910C7E8FC1FF927F]]
- [[UnresolvedReference1F8A262FCB0DB7B0]]
- [[UnresolvedReferenceDABA1D3AC66A423C]]
- [[UnresolvedReference98F6020366D065C2]]
- [[UnresolvedReference40264F4E4E78276D]]
- [[UnresolvedReference12E9C0CC256F77BA]]
- [[UnresolvedReference3FD88A9E0BE4471F]]
- [[UnresolvedReferenceC188AE402CD0DE26]]
- [[UnresolvedReference5B318C2DB5253B99]]
- [[UnresolvedReference5147C8B96B4E8184]]
- [[UnresolvedReference949C610EA6B14B90]]
- [[UnresolvedReference662EE65658B0D403]]
- [[UnresolvedReference70BF66A3A6A0A3A5]]
- [[UnresolvedReference4D72A4DBDE525A0D]]
- [[UnresolvedReferenceFE7DE71A7E11BBCC]]
- [[UnresolvedReferenceB84A5A78A161E2E0]]
- [[UnresolvedReference30B15F5DA0761C39]]
- [[UnresolvedReferenceA49A9E82C7FCA42E]]
- [[UnresolvedReferenceA8D7CB79E145FB77]]
- [[UnresolvedReference00A0546E5E9BD1DB]]
- [[UnresolvedReferenceD675810715377D6D]]
- [[UnresolvedReference32445035085CA461]]
- [[UnresolvedReference4DBCFFB907644A78]]
- [[UnresolvedReference7EBD29D800B42511]]
- [[SymbolicInteraction]]
- [[UnresolvedReferenceDE2FCE6C4316D0F2]]
- [[UnresolvedReference6C5E284E41974840]]
- [[UnresolvedReferenceF3A297B8F973D6C0]]
- [[UnresolvedReferenceE6A6276B4A13257F]]
- [[StudiesOfTheGeneralityOfAffectiveMeaningSystems]]
- [[UnresolvedReferenceABF8C32C93142044]]
- [[AnAffectControlTheoryAsAFoundationForTheDesignOfSociallyIntelligentSystems]]
- [[UnresolvedReferenceC845F1080AD1E52C]]
- [[UnresolvedReference28054B6823EBA748]]
- [[CultureConstrainedAffectiveConsistencyOfInterpersonalBehaviorATestOfAffectControlTheoryWithNonverbalExpressions]]
- [[OptimalControlOfMarkovDecisionProcessesWithIncompleteStateEstimation]]
- [[UnresolvedReferenceE88BC7D6113B1651]]
- [[UnresolvedReferenceCD346D2B51FBDEE1]]
- [[UnresolvedReference6010F3AADCE19947]]
- [[UnresolvedReferenceC6090264EF1DEB6B]]
- [[UnresolvedReference268B38C4083C5529]]
- [[UnresolvedReference37F8F9A7F02CF15F]]
- [[UnresolvedReference048C3ED384FD98C3]]
- [[MachMyAutomatedConversationCoach]]
- [[UnresolvedReference4A00D9F9FFE5AD27]]
- [[UnresolvedReference9373D6761D5EA028]]
- [[UnresolvedReference22764BA647C1E087]]
- [[UnresolvedReference30740F218127553E]]
- [[UnresolvedReferenceB8AAB4DE9F11A795]]
- [[UnresolvedReferenceA0D95C8D7B12BBCA]]
- [[AppraisalTheory]]
- [[UnresolvedReferenceCA4A3DAAB3DBEC87]]
- [[SocialNorms]]
- [[TractablePomdpPlanningAlgorithmsForOptimalTeachingInSpais]]
- [[PeopleSensorsDecisionsCustomizableAndAdaptiveTechnologiesForAssistanceInHealthcare]]
- [[UnresolvedReference899FE201670052EE]]
- [[ModelingDynamicIdentitiesAndUncertaintyInSocialInteractionsBayesianAffectControlTheory]]
- [[UnresolvedReference1EF26BDEE46944CC]]
- [[UnresolvedReference1705D7EEEDA5A547]]
- [[UnresolvedReferenceDA9351417A1034C9]]
- [[UnresolvedReferenceFF9F86863A58A178]]

## Audit Log
- Initial audit found the EPA state/action representation incomplete and the planning rule underspecified. Cross-audit then identified the missing fixed agent/client referents and turn-in-X rule, the inferential nature of Ωf, action-selection approximation details, general default parameters, and reported outcomes; these have now been added with source locations.[^r15]
- A further independent check found turn represented twice in the schema and transition/reward rules hidden under placeholders. The schema and rule summary now follow §3.1.[^r8][^r16]
- Independent final re-audit passed: the state schema, turn-conditioned affect transition, task/deflection reward split, planning approximation, defaults, and reported simulation findings are supported by the cited source sections.[^r8][^r9][^r10][^r16]

## LLM Justification
[^r1]: Hoey, Schröder, and Alhothali, “Affect Control Processes,” abstract and §1 Introduction, PDF pp. 1–2; https://cs.uwaterloo.ca/~jhoey/teaching/cs886-affect/papers/bayesact.pdf.
[^r2]: Same paper, abstract and §4 Experiments and Results, PDF pp. 1, 17–22; same URL.
[^r3]: Same paper, §2.2 POMDPs and §3.1 Basic Formulation, PDF pp. 3–8; same URL.
[^r4]: Same paper, §§3.2, 3.4, and 3.5, PDF pp. 8–14; same URL.
[^r5]: Same paper, §3.4–3.5, PDF pp. 11–14; describes the greedy one-step policy approximation and application-dependent transitions; same URL.
[^r6]: Same paper, §4 Experiments and Results, PDF pp. 17–22; same URL.
[^r7]: Same paper, §2.2, PDF p. 4; assumes detection and generation of emotional signals in EPA space; same URL.
[^r8]: Hoey, Schröder & Alhothali, “Affect control processes,” §3.1.1, PDF pp. 7–10 (F/T referents, agent/client encoding, turn in X, role-conditioned M); §3.1.4, p. 11 (Ωf and Ωx observation functions); §3.2, pp. 11–12 (belief update); source URL above.
[^r9]: Ibid., §§3.4–3.5, PDF pp. 13–16, especially Eqs. 32 and 35 and p. 16 (point-state approximation, candidate affective actions, one-step expected-reward selection, and handling of propositional actions); source URL above.
[^r10]: Ibid., §3.6, PDF pp. 18–19, parameter-default table (general settings and their meanings); source URL above.
[^r15]: Audit log basis: source §§3.1–3.6, PDF pp. 7–19; §4, pp. 20–29; source URL above.
[^r16]: Ibid., §§3.1.1–3.1.4, PDF pp. 7–11, especially the turn-conditioned impression formation, deflection/inertia transition potential, and the task versus affective reward discussion; source URL above.
