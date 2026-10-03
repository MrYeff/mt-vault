---

title: "HUMAT: An Integrated Framework for Modelling Individual Motivations, Social Exchange and Network Dynamics"
tags:
  - model
  - simulation
authors:
  - "[[Literature/Authors/Wander Jager|Wander Jager]]"
  - "[[Literature/Authors/Patrycja Antosz|Patrycja Antosz]]"
  - "[[Literature/Authors/Loes Bouman|Loes Bouman]]"
  - "[[Literature/Authors/Teng Li|Teng Li]]"
  - "[[Literature/Authors/J. Gareth Polhill|J. Gareth Polhill]]"
  - "[[Literature/Authors/Timo Szczepanska|Timo Szczepanska]]"
  - "[[Literature/Authors/Shaoni Wang|Shaoni Wang]]"
publication date: 2025-01-31
source:
  - https://doi.org/10.18564/jasss.5611
  - https://www.jasss.org/28/1/4.html
doi: 10.18564/jasss.5611
read status: Todo
⚠️: []
---
## Abstract
In this paper we present HUMAT, an integrated modelling framework that supports the simulation of social dynamics. HUMAT integrates theoretical ideas about human motives, cognitive dissonance, individual and social decision strategies, and the processes of influence that take place in networked communities. As such, HUMAT provides a generic model that can be implemented in a wide variety of cases dealing with opinion and behaviour dynamics in a social context, be it the adoption of a physical innovation or the promotion of an attitude in an online platform. The multi-theoretical background of HUMAT also provides a perspective on what types of qualitative and quantitative data can be used to parameterise real cases. This paper aims to provide an overview of the different processes modelled in HUMAT. Three applications are used to illustrate how HUMAT can be used to simulate and study social dynamics. The validation of the HUMAT framework is discussed in the context of the dynamic theory of social complexity.[^r0]

## Research Questions
> Research questions distilled from the primary paper; phrasing is paraphrased.[^r0]
- How can HUMAT integrate individual motives, cognitive dissonance, decision strategies, and social influence to simulate social dynamics?[^r0]
- How can the framework be parameterised and applied to distinct social cases, and how can its validity be assessed?[^r0]

## Model
> Model extracted via LLM according to [[Model Notation]].

### What does it represent?
- HUMAT represents attitude formation and choice between alternatives A and B, with three motive groups (experiential, social, and values).[^r1]
- Each agent has motive importance, evaluations/satisfaction for each alternative, aspiration, dissonance tolerance, choice history, and information about direct alters; dissonance is computed across motives.[^r1]
- Agents initially know their alters’ choices and acquire further information through exchanges.[^r1]

### How does it work?
- **Initialize:** Each agent evaluates A and B for experiential, social, and value needs.[^r2]
- Need importances and dissonance tolerance are drawn from Normal(mean=.5, SD=.14), truncated to [0,1]; motive satisfaction uses configured beta shapes (12/4, 8/4, 4/4, 4/8, or 4/12).[^r2]
- The initialization procedure draws aspiration uniformly from [0,1]. Agents connect to a random 20% of others within 35 spatial cells, with a nearest-agent fallback.[^r2]
- Agents initially know each alter's choice; other alter attributes begin at default values and are learned through exchanges.[^r2]
- **Detect a dilemma:** Need evaluations equal importance × satisfaction. For each option, social satisfaction is `2 × fraction of alters choosing it − 1`; social evaluation multiplies this by social importance.[^r2]
- Let P sum positive need evaluations and N sum the absolute negative evaluations. Dissonance is `2 × min(P,N) / (P+N)`; dissonance strength is `max(0,(dissonance−tolerance)/(1−tolerance))`.[^r2]
- A social dilemma has negative social evaluation and a positive experiential or value evaluation. A non-social dilemma has non-negative social evaluation and a negative experiential or value evaluation.[^r2]
- **Exchange information:** At each tick, information exchange precedes the final Set dissonances step.[^r2]
- Positive dissonance strength triggers signalling for a social dilemma or inquiring for a non-social dilemma; if both apply, the action is chosen 50/50.[^r2]
- Signalling targets an uncontacted opposite-choice alter ranked by persuadability; inquiring targets an uncontacted same-choice alter ranked by persuasiveness.[^r2]
- In signalling, the recipient updates its experiential and value satisfaction from the sender; in inquiring, the initiator updates its own satisfaction from the alter.[^r2]
- Each update blends old and received satisfaction using a persuasion weight: `0.4 × (1 − |difference in motive importance|)` when the two motive evaluations have the same sign, otherwise 0, multiplied by `clamp(0.4 × (initiator aspiration − other aspiration), 0, 1)`. If dissonance persists, the agent tries the next eligible alter at a later tick.[^r2]
- **Choose:** Exchanges can update choices; then agents update dissonance in random order.[^r2]
- Compare A and B first by satisfaction, then—if scores differ by less than 10% of that dimension's range—by lower dissonance, then by higher experiential satisfaction.[^r2]
- If all three comparisons remain close, choose randomly during initialization or retain the previous choice later.[^r2]

- The source is inconsistent on aspiration: its stochasticity section says values from 0 to less than 3, while Table 1 and initialization say [0,1].[^r6]
- Its narrative also says a new preference replaces a habit only when it is more satisfying **and** less dissonant, while the procedural choice rule compares satisfaction first and uses dissonance for close cases; these are not equivalent rules.[^r6]

### What can it answer?
- Core outputs are the fractions choosing A and B, mean satisfaction and dissonance for each choice, and signal/inquire counts.[^r3]
- Section 2.5 and the case studies demonstrate broader analyses such as sensitivity, tipping points, and application-specific outcomes; those are not all baseline outputs.[^r3]

### Where does it apply?
- The paper illustrates a stylized community-dialogue model, a city referendum, and COVID-19 vaccination; it also discusses other applications.[^r4]
- HUMAT is a flexible framework, so application-specific mechanisms and measurements vary, and this concise account omits full equations and case-specific extensions.[^r4]

## Metadata
### References
Bibliography completeness not verified; the following preserves the originally captured reference links in their original order.

- [[FromIntentionsToActionsATheoryOfPlannedBehaviorInJKuhlJBeckmannEds]]
- [[SmarteesSimulationImplementationsDeliverable72]]
- [[SmarteesSimulationImplementationsDeliverable73]]
- [[SensemakingOfCausalityInAgentBasedModels]]
- [[DynamicalAffinityInOpinionDynamicsModeling]]
- [[SocialLearningThroughImitation]]
- [[ReportsOnScenarioDevelopmentAndExperimentsForSelectedCases]]
- [[FromBeliefsToAttitudesPoliasAModelOfAttitudeDynamicsBasedOnCognitiveModelingAndFieldData]]
- [[CraftingMixedMethodEvaluationDesigns]]
- [[BirthAndDeathInAContinuousOpinionDynamicsModel]]
- [[AFocusTheoryOfNormativeConductATheoreticalRefinementAndReevaluationOfTheRoleOfNormsInHumanBehavior]]
- [[PriorityChallengesForSocialAndBehavioralResearchAndItsModeling]]
- [[FindingTheSweetSpotBetweenEfficacyAndAcceptanceOfCovidRestrictionsInFSquazzoniEd]]
- [[CoDevelopingBeliefsAndSocialInfluenceNetworksTowardsUnderstandingSocioCognitiveProcessesLikeBrexit]]
- [[GenerativeSocialScience]]
- [[AgentZeroTowardNeurocognitiveFoundationsForGenerativeSocialScience]]
- [[ATheoryOfSocialComparisonProcesses]]
- [[ATheoryOfCognitiveDissonance]]
- [[SimulationForTheSocialScientist]]
- [[HowToRelateModelsToRealityAnEpistemologicalFrameworkForTheValidationAndVerificationOfComputationalModels]]
- [[IntroductionToActionResearchSocialResearchForSocialChange]]
- [[TheOddProtocolAReviewAndFirstUpdate]]
- [[TestingTheActionBasedModelOfCognitiveDissonanceTheEffectOfActionOrientationOnPostDecisionalAttitudes]]
- [[ÜberDenAnschaulichenInhaltDerQuantentheoretischenKinematikUndMechanik]]
- [[SelfOrganizationEmergenceAndTheArchitectureOfComplexityInFHeylighenCJoslynVTurchinEds]]
- [[CommunicationAndPersuasionPsychologicalStudiesOfOpinionChange]]
- [[CaseBasedReasoningSocialDilemmasAndANewEquilibriumConcept]]
- [[ModellingConsumerBehaviour]]
- [[EnhancingTheRealismOfSimulationErosOnImplementingAndDevelopingPsychologicalTheoryInSocialSimulation]]
- [[SimulatingTheRoleOfNormsInProcessesOfSocialInnovationThreeCaseStudies]]
- [[SimulationsAsADialogueToolStrengtheningCommunityEngagementAndLocalDemocraticProcesses]]
- [[SimulatingCommunityDynamicsForTransitionalUrbanPlanningProcessesInGDeRooCYamuCZuidemaEds]]
- [[MeetingTargetsToolsToSupportIntegratedAssessmentModellingOfGlobalChange]]
- [[ReinstatementOfTheCommunicatorInDelayedMeasurementOfOpinionChange]]
- [[RenovatingThePyramidOfNeedsContemporaryExtensionsBuiltUponAncientFoundations]]
- [[MeasuringStabilityAndChangeInPersonalCultureUsingPanelData]]
- [[EditorialForTheResearchTopicTippingPointsInSocieties]]
- [[APhilosophicalEssayOnProbabilities]]
- [[HowAvailabilityHeuristicConfirmationBiasAndFearMayDriveSocietalPolarisationAnOpinionDynamicsSimulationOfTheCaseOfCovid19Vaccination]]
- [[DeterministicNonperiodicFlow]]
- [[MotivationAndPersonality]]
- [[DevelopmentAndHumanNeedsInPEkinsMMaxNeefEds]]
- [[SocialIsolationInAmericaChangesInCoreDiscussionNetworksOverTwoDecades]]
- [[EditorialModellingValuesInSocialTechnicalAndEcologicalSystems]]
- [[BetterBeConvincingOrBetterBeStylishATheoryBasedMultiAgentSimulationToExplainMinorityInfluenceInGroupsViaArgumentsOrViaPeripheralCues]]
- [[OneTheoryManyFormalizationsTestingDifferentCodeImplementationsOfTheTheoryOfPlannedBehaviourInEnergyAgentBasedModels]]
- [[GemeenteGroningenSReportFromTheReferendumUitslagEnAchtergrondVanHetReferendumNoorderplantsoen]]
- [[DynamicalSocialPsychology]]
- [[DynamicalSocialPsychologyAnIntroductionInANowakKWinkowskaNowakDBréeEds]]
- [[SocialNormsAsSolutionsPoliciesMayInfluenceLargeScaleBehavioralTipping]]
- [[HabitsAndIntentionInEverydayLifeTheMultipleProcessesByWhichPastBehaviorPredictsFutureBehavior]]
- [[CaseStudiesCrossSiteComparisonsAndTheChallengeOfGeneralizationComparingAgentBasedModelsOfLandUseChangeInFrontierRegions]]
- [[ConditionedReflexes]]
- [[CommunicationAndPersuasionCentralAndPeripheralRoutesToAttitudeChange]]
- [[UsingComputationalModelingForBuildingTheoryADoubleEdgedSword]]
- [[ThePersuasivenessOfSourceCredibilityACriticalReviewOfFiveDecadesEvidence]]
- [[DiffusionOfInnovations]]
- [[CriticalTransitionsInNatureAndSociety]]
- [[ShapingTheSocialEcologicalTransformationHowSocialBarriersCanBeOvercomeAndHowResonancePotentialsCanBeUtilised]]
- [[AFrameworkForMappingAndComparingBehavioralTheoriesInModelsOfSocialEcologicalSystems]]
- [[ModelingDynamicIdentitiesAndUncertaintyInSocialInteractionsBayesianAffectControlTheory]]
- [[FormalisingTheoriesOfHumanDecisionMakingForAgentBasedModellingOfSocialEcologicalSystemsPracticalLessonsLearnedAndWaysForward]]
- [[TheBehaviorOfOrganisms]]
- [[BourdieuAndEducationHowUsefulIsBourdieuSTheoryForResearchers]]
- [[TheEffectAndModificationOfTheTrafficCirculationPlanVcpTrafficPlanningInGroningenInThe1980s]]
- [[GoodIntentionsBadHabitsAndEffectsOfFormingImplementationIntentionsOnHealthyEating]]
- [[IntegronstersIntegralAndIntegratedModeling]]
- [[GamingPolarisationUsingAgentBasedSimulationAsADialogueTool]]
- [[DevelopmentOfAFormalSystemForRepresentingBehaviourChangeTheories]]
- [[TheAnimatPathToAi]]
- [[GlobalGreenhouseGasEmissionsFromAnimalBasedFoodsAreTwiceThoseOfPlantBasedFoods]]

## Audit Log
- Initial audits found errors in the abstract and model rules. Corrections now state the source conflicts, dilemma/partner/initialization rules, and asymmetric communication updates. The final independent re-audit passed. See `vault/.automation/audit/next-fifteen-31-35-correction-reaudit-2026-09-30.json`.[^r5]

## LLM Justification
[^r0]: Abstract copied verbatim from the primary publication record/full text. Research questions are concise paraphrases of the paper’s stated aims/questions. Bibliography links retained in source order from vault/.automation/import/next-fifteen-original-2026-09-30.json.
[^r1]: Jager et al., “HUMAT,” Appendix A, “Overview” and state variables tables (Tables 1–2); Section 2, “The HUMAT Framework.” https://www.jasss.org/28/1/4.html
[^r2]: Jager et al., “HUMAT,” Appendix A, Tables 1–4 and “Initialisation,” “Process overview and scheduling,” “Signal or inquire,” “Signal,” “Inquire,” “Set dissonances,” “Update dissonances,” and “Choose alternative.” https://www.jasss.org/28/1/4.html
[^r3]: Jager et al., “HUMAT,” Section 2.5, “Use and outputs.” https://www.jasss.org/28/1/4.html
[^r4]: Jager et al., “HUMAT,” Section 3, “Examples of HUMAT Implementations,” and abstract. https://www.jasss.org/28/1/4.html
[^r5]: Process log based on the initial audit record; this is a record of corrections, not an independent re-audit.
[^r6]: Jager et al., “HUMAT,” Appendix A, “Stochasticity” (aspiration 0 to <3), Table 1 and “Create agents” ([0,1]), “Process overview and scheduling” (habit narrative), and “Choose alternative” (thresholded procedure). https://www.jasss.org/28/1/4.html
