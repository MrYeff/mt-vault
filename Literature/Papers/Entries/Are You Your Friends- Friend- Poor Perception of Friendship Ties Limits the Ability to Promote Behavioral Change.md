---
title: "Are You Your Friends’ Friend? Poor Perception of Friendship Ties Limits the Ability to Promote Behavioral Change"
tags:
authors:
  - "[[Literature/Authors/Abdullah Almaatouq|Abdullah Almaatouq]]"
  - "[[Literature/Authors/Laura Radaelli|Laura Radaelli]]"
  - "[[Literature/Authors/Alex ‘Sandy’ Pentland|Alex Pentland]]"
  - "[[Literature/Authors/Erez Shmueli|Erez Shmueli]]"
publication date: 2016-03-22
source: "https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0151588&type=printable"
doi: "10.1371/journal.pone.0151588"
read status: Todo
⚠️: []
---
## Abstract

Persuasion is at the core of norm creation, emergence of collective action, and solutions to 'tragedy of the commons' problems. In this paper, we show that the directionality of friendship ties affect the extent to which individuals can influence the behavior of each other. Moreover, we find that people are typically poor at perceiving the directionality of their friendship ties and that this can significantly limit their ability to engage in cooperative arrangements. This could lead to failures in establishing compatible norms, acting together, finding compromise solutions, and persuading others to act. We then suggest strategies to overcome this limitation by using two topological characteristics of the perceived friendship network. The findings of this paper have significant consequences for designing interventions that seek to harness social influence for collective action.

## Research Questions
> Research Questions extracted via LLM
- How do friendship reciprocity and directionality relate to peer influence and change in physical activity?[^r1]
- Can social embeddedness and social centrality help predict friendship reciprocity and directionality?[^r2]

## Model
> Model extracted via LLM according to [[Model Notation]]

- The paper combines friendship nomination surveys, a physical-activity intervention, and regression/classification analyses. (Methods, “The FunFit Experiment”; Results, Table 1 and “Predicting Directionality.”)[^r2][^r4]
- For the intervention analysis, the outcome is each ego’s average daily activity in P2 divided by average daily activity in P1; predictors include reciprocal, incoming, and outgoing friendship indicators and tie strength, with demographic and baseline-activity controls in expanded regressions.[^r2][^r4]
- The two peer-pressure arms are pooled and the control arm is omitted in this directionality analysis.[^r2][^r4]
- The paper separately predicts tie type using social embeddedness (common friends) and social centrality (degree-centrality difference), and also reports several alternative feature measures in the supplement.[^r2][^r4]
- This summary omits study-specific sampling and coefficient details.[^r2][^r4]

### What does it represent?
How friendship tie direction and reciprocity relate to observed intervention response and to predictions of tie type. [^r2]

### How does it work?

```yml
Person: ...

Dyad:
  ego: PersonId
  alter: PersonId
  ego_nominates_alter: bool
  alter_nominates_ego: bool
  tie_strength: f32
  social_embeddedness: f32
  social_centrality_difference: f32

InterventionRecord:
  ego: PersonId
  activity_ratio_p2_over_p1: f32
  treatment: Control | PeerSee | PeerReward
```

```
fit_activity_regression(
  records: [InterventionRecord],
  dyads: [Dyad]
): ...

predict_tie_type(
  dyads: [Dyad]
): ...
```

- The paper’s intervention regression reports positive coefficients for reciprocal friendship and for the incoming tie that the authors call “ego perceived friend” (alter nominates ego). (Results, Table 1.)[^r3]
- The outgoing tie, called “alter perceived friend” (ego nominates alter), is not statistically significant. (Results, Table 1.)[^r3]
- These are regression associations, not causal transition rules. (Results, Table 1.)[^r3]

### What can it answer?
- Whether reported tie direction and reciprocity covary with the P2/P1 activity ratio in this intervention.[^r5]
- How well social embeddedness/centrality measures predict tie reciprocity and direction. The paper reports logistic-regression and Random Forest classifiers and evaluates classification with ROC AUC. (Results, “Predicting Directionality,” Figs. 3–4.)[^r5]

### Where does it apply?
To the paper’s friendship nomination datasets and Friends and Family physical-activity intervention; the directionality regression pools Peer See and Peer Reward and reports 76 observations. (Results, Table 1.)[^r3][^r4]

## Metadata
### References
> ⚠️ The 68 links below have not been reconciled with the paper's 52 numbered references; completeness and mapping remain unverified.

- [[CloseFriendshipsInAdolescence]]
- [[DifferentialStabilityOfReciprocalFriendshipsAndUnilateralRelationshipsAmongPreschoolChildren]]
- [[ClusteringAndPreferentialAttachmentInGrowingNetworks]]
- [[SocialInfluenceAndCollectiveActionAnExperimentInvestigatingTheEffectsOfVisibilityAndSocialInformationModeratedByPersonality]]
- [[SocialComputingBehavioralCulturalModelingAndPrediction]]
- [[SocialCapitalAsSocialMechanismsAndCollectiveAssetsTheExampleOfStatusAuctionsAmongColleagues]]
- [[CreatingSocialContagionThroughViralProductDesignARandomizedTrialOfPeerInfluenceInNetworks]]
- [[ASystematicReviewOfPeerSupportProgramsForSmokingCessationInDisadvantagedGroups]]
- [[AdolescentPeerNetworksAsAContextForSocialAndEmotionalSupport]]
- [[SocialStructureAndCompetitionInInterfirmNetworksTheParadoxOfEmbeddedness]]
- [[EconomicActionAndSocialStructureTheProblemOfEmbeddedness]]
- [[UnresolvedReference6BFD0D671FAA96BF]]
- [[IntimacyOfFriendshipInterpersonalCompetenceAndAdjustmentDuringPreadolescenceAndAdolescence]]
- [[InducingPeerPressureToPromoteCooperation]]
- [[AnExperimentalStudyOfHomophilyInTheAdoptionOfHealthBehavior]]
- [[ReciprocalFriendshipReciprocalRejectionAndSocioEmotionalAdjustmentTheSocialExperiencesOfChildrenWithLearningDisordersOverAOneYearPeriod]]
- [[IdentificationOfEffectiveOpinionLeadersInTheDiffusionOfTechnologicalInnovationASocialNetworkApproach]]
- [[Friendship networks and social status]]
- [[ThePeerRelationsOfDropoutsAComparativeStudyOfAtRiskAndNotAtRiskYouths]]
- [[CulturalCapitalAndHighSchoolBullies]]
- [[HealthyBuddiesANovelPeerLedHealthPromotionProgramForThePreventionOfObesityAndEatingDisordersInChildrenInElementarySchool]]
- [[ComparativeStudyOfSegmentationOfPeriodicMotionDataForMobileGaitAnalysis]]
- [[SexDifferencesInChildrenSFriendships]]
- [[SensingTheHealthStateOfACommunity]]
- [[MaximizingTheSpreadOfInfluenceThroughASocialNetwork]]
- [[SocialSensing]]
- [[SensingUnderstandingAndShapingSocialBehavior]]
- [[AdolescentsAndTheirFriends]]
- [[DecliningVoterTurnoutInAdvancedIndustrialDemocracies1950To1997]]
- [[ChildrenSFriendshipRelationsAMetaAnalyticReview]]
- [[TieStrengthEmbeddednessAndSocialInfluenceALargeScaleNetworkedExperiment]]
- [[SocialInfluenceComplianceAndConformity]]
- [[SocialFmriInvestigatingAndShapingSocialMechanismsInTheRealWorld]]
- [[SocialCapitalIntellectualCapitalAndTheOrganizationalAdvantage]]
- [[TheStrengthOfWeakTies]]
- [[DynamicSpreadOfHappinessInALargeSocialNetworkLongitudinalAnalysisOver20YearsInTheFraminghamHeartStudy]]
- [[TheStrengthOfTheStrongestTiesInCollaborativeProblemSolving]]
- [[TheSpreadOfObesityInALargeSocialNetworkOver32Years]]
- [[StreetCornerSocietyTheSocialStructureOfAnItalianSlum]]
- [[PredictingTieStrengthWithSocialMedia]]
- [[ComplexContagionsAndTheWeaknessOfLongTies]]
- [[DoSocialSupportInterventionsBuddySystemsAidSmokingCessationAReview]]
- [[StructureAndTieStrengthsInMobileCommunicationNetworks]]
- [[RealityMiningSensingComplexSocialSystems]]
- [[DiabetesBuddies]]
- [[TheSpreadOfBehaviorInAnOnlineSocialNetworkExperiment]]
- [[ImportanceOfSocialSupportInTheAdjustmentOfChildrenWithLearningProblems]]
- [[CorrelatesOfPeerAcceptanceInAChineseSampleOfSixYearOlds]]
- [[SocialNetworkTargetingToMaximisePopulationBehaviourChangeAClusterRandomisedControlledTrial]]
- [[DoYouLikeMeAsMuchAsILikeYouFriendshipReciprocityAndItsEffectsOnSchoolOutcomesAmongAdolescents]]
- [[TheCriticalMassInCollectiveAction]]
- [[SomePrinciplesOfStratification]]
- [[UnresolvedReferenceA4189C99B0FEBDD9]]
- [[UnresolvedReference6088526CBA506A91]]
- [[ModelingInfectionWithMultiAgentDynamics]]
- [[UnresolvedReference880A6720EABE4E4D]]
- [[IdentifyingInfluentialAndSusceptibleMembersOfSocialNetworks]]
- [[UnresolvedReference6BA987826CEA5FFF]]
- [[UnresolvedReference780BB9ED027DFD16]]
- [[UnresolvedReference8438144EA834A4AF]]
- [[DecliningVoterTurnoutInAdvancedIndustrialDemocracies1950To1997TheEffectsOfDecliningGroupMobilization]]
- [[DiabetesBuddiesPeerSupportThroughAMobilePhoneBuddySystem]]
- [[UnresolvedReferenceFBCF8AD7315076D5]]
- [[CulturalCapitalAndHighSchoolBulliesHowSocialInequalityImpactsSchoolViolence]]
- [[IntimacyOfFriendshipInterpersonalCompetenceAndAdjustmentDuringPreescenceAndAdolescence]]
- [[ComplexContagionsAndTheWeaknessOfLongTies1]]
- [[DynamicSpreadOfHappinessInALargeSocialNetworkLongitudinalAnalysisOfTheFraminghamHeartStudySocialNetwork]]
- [[WirelessHealth2010]]

## Audit Log
- Initial audit failed because the outcome was described as a generic change, tie-direction labels were ambiguous, and the treatment arms and classification procedures were underspecified. Corrected to the paper’s P2/P1 outcome ratio, named and defined all three arms and the incoming/outgoing labels, and identified the reported classifiers and ROC AUC evaluation. Awaiting independent re-audit.

- Independent re-audit passed after the source and bibliography corrections.

## LLM Justification
[^r1]: Primary full text, Abstract; “Directionality and Induced Peer-Pressure,” pp. 2–3; analysis and Table 1, pp. 5–7; prediction sections, pp. 7–9.
[^r2]: Primary full text, Methods, “The FunFit Experiment”; Results, intervention analysis and “Predicting Directionality,” especially Table 1 and pp. 7–9.
[^r3]: Primary full text, Results, Table 1 and intervention analysis, pp. 5–7; Table 1 reports 76 observations and the labeled tie-type coefficients.
[^r4]: Primary full text, Results, intervention analysis, p. 5: two peer-pressure treatments are pooled and control omitted; Table 1, p. 6, identifies Peer See and Peer Reward conditions.
[^r5]: Primary full text, Results, “Predicting Directionality,” pp. 7–9: logistic regression and Random Forest classification results, with ROC AUC reported.
