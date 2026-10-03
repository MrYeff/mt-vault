---
title: "Reciprocal Recommender Systems: Analysis of state-of-art literature, challenges and opportunities towards social recommendation"
tags:
  - reciprocal_recommender_system
  - literature_review
  - "model"
authors:
  - "[[Literature/Authors/Iván Palomares|Iván Palomares]]"
  - "[[Literature/Authors/Carlos Porcel|Carlos Porcel]]"
  - "[[Literature/Authors/Luiz Augusto Sangoi Pizzato|Luiz Augusto Sangoi Pizzato]]"
  - "[[Literature/Authors/Ido Guy|Ido Guy]]"
  - "[[Literature/Authors/Enrique Herrera‐Viedma|Enrique Herrera‐Viedma]]"
publication date: 2020-12-07 
source: "https://arxiv.org/pdf/2007.16120v2"
doi: 10.1016/j.inffus.2020.12.001
read status: Todo
⚠️:
  - audit failed
---

## Abstract

There exist situations of decision-making under information overload in the Internet, where people have an overwhelming number of available options to choose from, e.g. products to buy in an e-commerce site, or restaurants to visit in a large city. Recommender systems arose as a data-driven personalized decision support tool to assist users in these situations: they are able to process user-related data, filtering and recommending items based on the user’s preferences, needs and/or behaviour. Unlike most conventional recommender approaches where items are inanimate entities recommended to the users and success is solely determined upon the end user’s reaction to the recommendation(s) received, in a Reciprocal Recommender System (RRS) users become the item being recommended to other users. Hence, both the end user and the user being recommended should accept the “matching” recommendation to yield a successful RRS performance. The operation of an RRS entails not only predicting accurate preference estimates upon user interaction data as classical recommenders do, but also calculating mutual compatibility between (pairs of) users, typically by applying fusion processes on unilateral user-to-user preference information. This paper presents a snapshot-style analysis of the extant literature that summarizes the state-of-the-art RRS research to date, focusing on the algorithms, fusion processes and fundamental characteristics of RRS, both inherited from conventional user-to-item recommendation models and those inherent to this emerging family of approaches. Representative RRS models are likewise highlighted. Following this, we discuss the challenges and opportunities for future research on RRSs, with special focus on (i) fusion strategies to account for reciprocity and (ii) emerging application domains related to social recommendation.

## Research Questions
> Research Questions extracted via LLM
- How do reciprocal recommenders estimate mutual compatibility when both people must accept a match?[^r1]
- What algorithmic, preference-fusion, evaluation, and application challenges characterize reciprocal recommendation?[^r1]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?
- A conceptual people-to-people recommender: successful matching requires positive responses from both users. Unilateral preferences and reciprocal ranking are distinct.[^r4]
- This notation covers normalized preference-score aggregation. The review also covers fusion of rankings, where the fused result is not a mutual-preference degree.[^r4]

```yml
World:
  users: [User]
  preferences: [UserId -> [UserId -> Score]]

User:
  profile: ()
  interactions: [()]

Score: 0..1
```

### How does it work?
- Estimate `p_x_y` and `p_y_x`, fuse them, then rank eligible users. Single-class systems allow any other user; two-class systems restrict candidates to the opposite class.[^r4]
- `FUSION` and eligibility are method-specific configurations. The conceptual synthesis defines neither an acceptance threshold nor simulated acceptance behavior.[^r4]

```
recommend(world: World, user: UserId) -> [UserId]:
  for other in ELIGIBLE(world.users, user):
    scores[other] = FUSION(
      world.preferences[user][other],
      world.preferences[other][user]
    )
  out = sort_descending(scores).keys()
```

- A common surveyed `FUSION` is the harmonic mean below; arithmetic and geometric means are alternatives. This example does not select one method for the entire review.[^r4]

```
harmonic(p_x_y: Score, p_y_x: Score) -> Score:
  if p_x_y == 0 or p_y_x == 0: out = 0
  else: out = 2 * p_x_y * p_y_x / (p_x_y + p_y_x)
```

### What can it answer?
- Organize algorithms, fusion functions and evaluation for bilateral recommendation; ranking a pair does not establish bilateral acceptance.[^r4]

### Where does it apply?
- Dating, recruitment, learning and social matching. This is the review's conceptual interface; individual surveyed algorithms and their evaluations are omitted.[^r3][^r4]

## Study Design
> Study design extracted via LLM

This is a literature analysis, not an empirical experiment or one fixed simulation. It classifies reciprocal-recommender algorithms, preference-fusion approaches, evaluation, and applications, and contributes the conceptual reciprocal-score model summarized above.[^r4][^r3]

## Metadata
### References
- [[ExplicitAndImplicitUserPreferencesInOnlineDating]]
- [[CharacterizationOfUserOnlineDatingBehaviorAndPreferenceOnALargeOnlineDatingSite]]
- [[ProcfProbabilisticCollaborativeFilteringForReciprocalRecommendation]]
- [[UnresolvedReferenceA7D3282D87FE0353]]
- [[UsingACriticToPromoteLessPopularCandidatesInAPeopleToPeopleRecommenderSystem]]
- [[HybridRecommenderSystemsSurveyAndExperiments]]
- [[MatrixFactorizationModelInCollaborativeFilteringAlgorithmsASurvey]]
- [[ScalableAndExplainableFriendRecommendationInCampusSocialNetworkSystem]]
- [[OnTheUseOfCrossDomainUserPreferencesAndPersonalityTraitsInCollaborativeFiltering]]
- [[ProceedingsOfThe7thInternationalConferenceOnEducationalDataMining]]
- [[IhrAMobileReciprocalJobRecommenderSystem]]
- [[DigitalTracesOfInterestDerivingInterestRelationshipsFromSocialMediaInteractions]]
- [[ContextAwareRecommenderSystems]]
- [[InteractionBasedCollaborativeFilteringMethodsForRecommendationInOnlineDating]]
- [[MultiCriteriaDecisionMakingMethodsAComparativeStudy]]
- [[ReciprocalRecommendationSystemForOnlineDating]]
- [[SocioSpatialPropertiesOfOnlineLocationBasedSocialNetworks]]
- [[ImprovingMatchingProcessInSocialNetworkUsingImplicitAndExplicitUserInformation]]
- [[ManagingDiversityAndInclusionAnInternationalPerspective]]
- [[AGraphicalModelFormulationOfCollaborativeFilteringNeighbourhoodMethodsWithFastMaximumEntropyTraining]]
- [[AggregationFunctionsAGuideForPractitioners]]
- [[ReciprocalAndHeterogeneousLinkPredictionInSocialNetworks]]
- [[Recon]]
- [[PersonalizedRecommendationOfSocialSoftwareItemsBasedOnSocialRelations]]
- [[RecommendingWhoToFollowOnTwitterBasedOnTweetContentsAndSocialConnections]]
- [[UnresolvedReferenceB6876605EA922639]]
- [[IdentifyingOpportunitiesForValuableEncounters]]
- [[RecommendingTwitterUsersToFollowUsingContentAndCollaborativeFilteringApproaches]]
- [[RecommenderSystemForOnlineDatingService]]
- [[AComparativeAnalysisOfOfflineAndOnlineEvaluationsAndDiscussionOfResearchPaperRecommenderSystemEvaluation]]
- [[AJobRecommenderSystemBasedOnUserClustering]]
- [[IncreasingEngagementThroughEarlyRecommenderIntervention]]
- [[OnlineDatingRecommenderSystems]]
- [[AContentBasedApproachForRecommendingPersonnelForJobPositions]]
- [[APeopleToPeopleContentBasedReciprocalRecommenderUsingHiddenMarkovModels]]
- [[RecommendingPeopleToPeopleTheNatureOfReciprocalRecommendersWithACaseStudyInOnlineDating]]
- [[ReversedCfAFastCollaborativeFilteringAlgorithmUsingAKNearestNeighborGraph]]
- [[ImpressionFormationInCorporatePeopleTagging]]
- [[APeopleToPeopleRecommendationSystemUsingTensorSpaceModels]]
- [[IslandsInTheStream]]
- [[IntelligentTourismRecommenderSystemsASurvey]]
- [[DoYouKnow]]
- [[CommunityBasedUserRecommendationInUniDirectionalSocialNetworks]]
- [[ASocialTrustBasedFriendRecommenderForOnlineCommunities]]
- [[SocialMatching]]
- [[BeyondFriendship]]
- [[ATrustAwareSystemForPersonalizedUserRecommendationsInSocialNetworks]]
- [[ThePerceptionOfOthers]]
- [[ReciprocalRecommenderSystemForOnlineDating]]
- [[UserAdaptedTravelPlanningSystemForPersonalizedScheduleRecommendation]]
- [[AReciprocalCollaborativeMethodUsingRelevanceFeedbackAndFeatureImportance]]
- [[UnresolvedReference0ADE65C2C549DD5F]]
- [[UnresolvedReference47977DFE7C3E9454]]
- [[RegressionBasedLatentFactorModels]]
- [[TheNetworkEffectsOfRecommendingSocialConnections]]
- [[AGraphBasedFriendRecommendationSystemUsingGeneticAlgorithm]]
- [[UninormAggregationOperators]]
- [[TheEffectOfSuspiciousProfilesOnPeopleRecommenders]]
- [[ImprovingMatchingProcessInSocialNetwork]]
- [[RecommendationSystemsForMarketsWithTwoSidedPreferences]]
- [[PredictingPositiveAndNegativeLinksInOnlineSocialNetworks]]
- [[RecommendationInReciprocalAndBipartiteSocialNetworksACaseStudyOfOnlineDating]]
- [[SwimmingAgainstTheStreamz]]
- [[ReciprocalRecommendationForJobMatchingWithBidirectionalFeedback]]
- [[Meet]]
- [[Friendsensing]]
- [[RelevanceAndRankingInOnlineDatingSystems]]
- [[RestrictedBoltzmannMachinesForCollaborativeFiltering]]
- [[AResearchAnalyticsFrameworkSupportedRecommendationApproachForSupervisorSelection]]
- [[QuestionRecommendationWithConstraintsForMassiveOpenOnlineCourses]]
- [[ExpertiseRecommendationATwoWayKnowledgeCommunicationChannel]]
- [[FindingAndMatchingCommunitiesInSocialNetworksUsingDataMining]]
- [[TransitiveNodeSimilarityForLinkPredictionInSocialNetworksWithPositiveAndNegativeLinks]]
- [[RelationalLearningViaCollectiveMatrixFactorization]]
- [[MakingSocialMatchingContextAware]]
- [[MatchingPeopleAndJobsABilateralRecommendationApproach]]
- [[IntrankInteractionRankingBasedTrustworthyFriendRecommendation]]
- [[Cluestr]]
- [[MiningExpertiseAndInterestsFromSocialMedia]]
- [[UtilizingPastRelationsAndUserSimilaritiesInASocialMatchingSystem]]
- [[MakeNewFriendsButKeepTheOld]]
- [[BprBayesianPersonalizedRankingFromImplicitFeedback]]
- [[ASocialMatchingSystemForAnOnlineDatingNetworkAPreliminaryStudy]]
- [[SamePlacesSameThingsSamePeople]]
- [[StochasticMatchingAndCollaborativeFilteringToRecommendPeopleToPeople]]
- [[PeopleRecommendationBasedOnAggregatedBidirectionalIntentionsInSocialNetworkSite]]
- [[Ihr]]
- [[ARecommendationMethodForOnlineDatingNetworksBasedOnSocialRelationsAndDemographicInformation]]
- [[DoYouWantToKnow]]
- [[RecommendingPeersForLearningMatchingOnDissimilarityInInterpretationsToProvokeBreakdown]]
- [[ARandomizedApproachForStructuralAndMessageBasedPrivateFriendRecommendationInOnlineSocialNetworks]]
- [[PeopleToPeopleReciprocalRecommenders]]
- [[UnresolvedReference03AD1A42D828AC78]]
- [[WeightedContentBasedMethodsForRecommendingConnectionsInOnlineSocialNetworks]]
- [[UsingInteractionSignalsForJobRecommendations]]
- [[EncountRExploringPassiveContextAwarenessForOpportunisticSocialMatching]]
- [[IncreasingMoocCompletionRatesThroughSocialInteractionsARecommendationSystem]]
- [[SupportingOpportunitiesForContextAwareSocialMatching]]
- [[CrossDomainRecommenderSystems]]
- [[MasterfulMatchmakingInServiceTransactions]]
- [[WhatIsYourOrganizationLike]]
- [[TransferLearningBasedModelForReciprocalRecommendation]]
- [[AHierarchicalSimilarityBasedJobRecommendationServiceFrameworkForUniversityStudents]]
- [[EmployerOrientedRecruitmentRecommenderServiceForUniversityStudents]]
- [[APreferenceDrivenDatabaseApproachToReciprocalUserRecommendationsInOnlineSocialNetworks]]
- [[RatingPredictionBasedJobRecommendationServiceForCollegeStudents]]
- [[NewToOnlineDatingLearningFromExperiencedUsersForASuccessfulMatch]]
- [[RecommenderSystemsEvaluationsOfflineOnlineTimeAndAATest]]
- [[ASurveyOfCollaborativeFilteringAlgorithmsForSocialRecommenderSystems]]
- [[DoesAPeerRecommenderFosterStudentsEngagementInMoocs]]
- [[ApplyingDifferentClassificationTechniquesInReciprocalJobRecommenderSystemForConsideringJobCandidatePreferences]]
- [[RecommenderSystemsTheTextbook]]
- [[ANoteOnExplicitVersusImplicitInformationForJobRecommendation]]
- [[AHybridCollaborativeFilteringModelWithDeepStructureForRecommenderSystems]]
- [[YouWillSucceedOrNotMatchingPredictionInAMarriageConsultingService]]
- [[ComparingPeerRecommendationStrategiesInAMooc]]
- [[AReciprocalRecommenderSystemForGraduatesRecruitment]]
- [[PracticalLessonsForJobRecommendationsInTheColdStartScenario]]
- [[IfItSConvenient]]
- [[WhoWillCiteYouBackReciprocalLinkPredictionInCitationNetworks]]
- [[CharacterizingContextAwareRecommenderSystemsASystematicLiteratureReview]]
- [[FoodRecommenderSystemsImportantContributionsChallengesAndFutureResearchDirections]]
- [[UserToUserRecommendationUsingTheConceptOfMovementPatternsAStudyUsingADatingSocialNetwork]]
- [[ASurveyOnSolvingColdStartProblemInRecommenderSystems]]
- [[TheInvisibleContoursOfOnlineDatingCommunitiesASocialNetworkPerspective]]
- [[IntelligentGroupSuggestionsBasedOnStudentsConceptualUnderstanding]]
- [[ReciprocalPeerRecommendationForLearningPurposes]]
- [[EvaluatingRecommendationAndSearchInTheLaborMarket]]
- [[CommunityBasedRecommendationForColdStartProblemACaseStudyOfReciprocalOnlineDatingRecommendation]]
- [[PeopleRecommendationOnSocialMedia]]
- [[CouplenetPayingAttentionToCouplesWithCoupledAttentionForRelationshipRecommendation]]
- [[IncorporatingFacialAttractivenessInPhotosForOnlineDatingRecommendation]]
- [[CollaborativeFilteringForPeopleToPeopleRecommendationInSocialNetworks]]
- [[ProvidingExplanationsForRecommendationsInReciprocalEnvironments]]
- [[FairnessInReciprocalRecommendations]]
- [[ReciprocalRankingAHybridRankingAlgorithmForReciprocalRecommendation]]
- [[SequenceAwareRecommenderSystems]]
- [[SharingNotesAnAcademicSocialNetworkBasedOnAPersonalizedFuzzyLinguisticRecommenderSystem]]
- [[EarsEmotionAwareRecommenderSystemBasedOnHybridInformationFusion]]
- [[OptimallyBalancingReceiverAndRecommendedUsersImportanceInReciprocalRecommenderSystems]]
- [[BlinddateRecommenderAContextAwareOntologyBasedDatingRecommendationPlatform]]
- [[OfflineAndOnlineEvaluationOfRecommendations]]
- [[MentorSpottingRecommendingExpertMentorsToMenteesForLiveTroubleShootingInCodementor]]
- [[UrbansocialradarAPlaceAwareSocialMatchingModelForEstimatingSerendipitousInteractionWillingnessInKoreanCulturalContext]]
- [[ArikuiADubiousUserDetectionSystemForOnlineDatingInJapan]]
- [[GroupRecommenderSystemsAnIntroduction]]
- [[NumericalStudyOfReciprocalRecommendationWithDomainMatching]]
- [[Withshare]]
- [[InformationRetrievalModelsForContactRecommendationInSocialNetworks]]
- [[GenderSpecificPreferenceInOnlineDating]]
- [[OnlineDatingRecommendationsMatchingMarketsAndLearningPreferences]]
- [[UnresolvedReference06C62687D92242AF]]
- [[UnresolvedReference6F236F7851AEAAD8]]
- [[ItSAMatchReciprocalRecommenderSystemForGraduatingStudentsAndJobs]]
- [[WeRecAFairnessAwareReciprocalRecommendationBasedOnWalrasianEquilibrium]]
- [[MultiStakeholderRecommendationAndItsConnectionToMultiSidedFairness]]
- [[LatentFactorModelsAndAggregationOperatorsForCollaborativeFilteringInReciprocalRecommenderSystems]]
- [[Privatejobmatch]]
- [[MultiStakeholderRecommendations]]
- [[ACharacterizationMethodologyForCandidatesAndRecruitersInteractionInOnlineRecruitmentServices]]
- [[EvolutionaryApproachForHealthyBundleWellbeingRecommendations]]
- [[ADeepHybridModelForRecommendationSystems]]
- [[AggregationStrategiesInUserToUserReciprocalRecommenderSystems]]
- [[MatchingOfSocialEventsAndUsersATwoWaySelectionPerspective]]
- [[LargeScaleDecisionMakingCharacterizationTaxonomyChallengesAndFutureDirectionsFromAnArtificialIntelligenceAndApplicationsPerspective]]
- [[HybridReciprocalRecommenderSystemsIntegratingItemToUserPrinciplesInReciprocalRecommendation]]
- [[ASystematicLiteratureReviewOfMulticriteriaRecommenderSystems]]
- [[DeepLearningInCitationRecommendationModelsSurvey]]
- [[ReciprocalRecommendationMatchingUsersWithTheRightUsers]]
- [[BuildingAReciprocalRecommendationSystemAtScaleFromScratchLearningsFromOneOfJapanSProminentDatingApplications]]
- [[RecommenderSystemsLeveragingMultimediaContent]]
- [[MultistakeholderRecommendationSurveyAndResearchDirections]]
- [[UserRecommendationsInReciprocalAndBipartiteSocialNetworksAnOnlineDatingCaseStudy]]
- [[FindingSomeoneYouWillLikeAndWhoWonTRejectYou]]
- [[UnresolvedReferenceE617E28E8AE0F90D]]
- [[UnresolvedReference34A37EDBBD77BD78]]
- [[UnresolvedReference2C8CD281E6A4A17F]]
- [[UnresolvedReference94EFCFBC4D52FD0A]]
- [[UnresolvedReferenceBC3B7D10B6750577]]
- [[UnresolvedReference997C821279EA56B2]]
- [[UnresolvedReference5A770E0572C94E40]]
- [[UnresolvedReference259C8370DEAAD38C]]
- [[UnresolvedReferenceF3A5D2B208E65C95]]
- [[UnresolvedReferenceF6F04C353FD6D8FB]]
- [[UnresolvedReferenceE832909E89F8CBE2]]
- [[UnresolvedReferenceCCC296C805F399A6]]
- [[UnresolvedReferenceD6F3BEDEFCD56728]]
- [[UnresolvedReference856BE6D3A38F2353]]
- [[UnresolvedReference8C88338BE00C6B18]]
- [[UnresolvedReferenceBE98648BDFDE4826]]
- [[UnresolvedReference4494A5D5289D2DC2]]
- [[UnresolvedReference30AB0BCD026068A8]]
- [[UnresolvedReference08B2E5D71CD42F22]]
- [[UnresolvedReference13772ED32FC097B5]]
- [[UnresolvedReference1A2F915A0695C030]]
- [[UnresolvedReference798BA871C3898C7F]]
- [[UnresolvedReference69AF4E7CFC94BDC8]]
- [[UnresolvedReference645056421D70417F]]
- [[UnresolvedReference23177D60FE95D03A]]
- [[UnresolvedReferenceE4B2927E7EEEA72C]]
- [[UnresolvedReference9232900E53071141]]
- [[UnresolvedReferenceB95DC71FE2A4653B]]
- [[UnresolvedReference15BBC246C9CAB4F8]]
- [[UnresolvedReferenceE6A389EF89D3C453]]
- [[UnresolvedReference7FAC14E8AF5510B1]]
- [[UnresolvedReference71FB41BED0EEDA21]]
- [[UnresolvedReferenceD1968EF3864094BE]]
- [[UnresolvedReferenceF9CC4AAB3DCA8894]]
- [[UnresolvedReference7F432C0E42F4DDA0]]
- [[UnresolvedReference3E4E96842B09F2D9]]
- [[UnresolvedReference7DE63D532004C677]]
- [[UnresolvedReferenceD1F07F39E8D657A7]]
- [[UnresolvedReferenceCF6F5957B6D25315]]
- [[UnresolvedReference20AA93827F6EDD2A]]
- [[UnresolvedReference6015C2C4A34F2097]]
- [[UnresolvedReferenceF0FAD3A6F4FD74CF]]
- [[UnresolvedReference5ACA00E470232507]]
- [[UnresolvedReference7FE508EADD6CAFA5]]
- [[UnresolvedReferenceEA9DEB4C3D5DBE73]]
- [[UnresolvedReferenceF91647AAEFE6D4C6]]
- [[UnresolvedReferenceB36075090E8D77C4]]
- [[UnresolvedReference037CF04AFEB71F40]]
- [[UnresolvedReferenceEBB907B5B159840E]]
- [[UnresolvedReferenceBBEB4032B04D2323]]
- [[UnresolvedReference01DA3DDAA5B9BDA2]]
- [[WhatIsYourOrganizationLikeAStudyOfLikingActivityInTheEnterprise]]
- [[UnresolvedReferenceFCC57EF59C89B1AF]]
- [[UnresolvedReference411ACD34453463D9]]
- [[CrossDomainRecommenderSystemsASystematicLiteratureReview]]
- [[DeepLearningBasedRecommenderSystemASurveyAndNewPerspectives]]
- [[ASurveyOnAdversarialRecommenderSystemsFromAttackDefenseStrategiesToGenerativeAdversarialNetworks]]
- [[UnresolvedReferenceD49F3DCA2C54CF2D]]
- [[UnresolvedReferenceA9C9E1758C85B9BC]]
- [[UnresolvedReference0F6E17811547F513]]
- [[IntelligentGroupSuggestionsBasedOnStudentsConceptualUnderstandingAbstractOnly]]
- [[FairnessInReciprocalRecommendationsASpeedDatingStudy]]
- [[UnresolvedReference68BDB1475382572A]]
- [[OnlineReciprocalRecommendationWithTheoreticalPerformanceGuarantees]]
- [[APeopleToPeopleMatchingSystemUsingGraphMiningTechniques]]
- [[UnresolvedReference7167B4480B1C92A2]]
- [[UnresolvedReference08D840FDE9E83F6D]]
- [[UnresolvedReferenceCD35908E4D7C63BE]]
- [[OnlineMatchmakingUsingCollaborativeFilteringAndReciprocalRecommenderSystems]]
- [[ReciprocalRecommenderSystemForLearnersInMassiveOpenOnlineCoursesMoocs]]
- [[PerformanceEvaluationOfRecommenderSystems]]
- [[RecommenderSystemsSourcesOfKnowledgeAndEvaluationMetrics]]
- [[UnresolvedReference41D99598B09DA70B]]
- [[ReciprocalRecommendationAlgorithmForTheFieldOfRecruitment]]
- [[UnresolvedReference3DB2B867CDCF29E1]]
- [[UnresolvedReference8FC4C7FA9508DB57]]
- [[ASurveyOnRecommendationsInLocationBasedSocialNetworks]]
- [[IdentifyingOpportunitiesForValuableEncountersTowardContextAwareSocialMatchingSystems]]
- [[WithshareAMobileApplicationToSupportCommunityCoproductionActivities]]
- [[UnresolvedReferenceD84931DBA5FE5F27]]

## Audit Log
- Audit invalidated (2026-09-30): auditor admitted clearing flags before completing independent source checks. A new independent audit is required.
- Strong source review (2026-09-30): Corrected conceptual-model locator to Fig. 1/Definitions 2.3–2.5, typed directed preference fusion and eligible candidate ranking; removed simulation tag and used accessible v2 paper rather than withdrawn landing version. Independent re-audit pending.
- Initial independent audit: failed on missing model mechanisms, abstract fidelity, or source-access reporting; see `vault/.automation/audit/next-forty-54-66-initial-2026-09-30.json`. Revisions added source-located model detail; independent re-audit remains pending.

- WITHDRAWN audit claim (2026-09-30): previously reported PASS; source claims, current extraction, metadata, references and footnotes checked against the available primary source. See `vault/.automation/audit/remaining-audit-b-2026-09-30.json`.

## LLM Justification
[^r1]: The paper’s abstract, at https://arxiv.org/pdf/2007.16120v2. The questions paraphrase the stated purpose, research scope, and reported approach.
[^r3]: Palomares et al., §§1, 4–6: snapshot-style literature analysis, representative algorithms, evaluation and application domains. Accessible author paper: https://arxiv.org/pdf/2007.16120v2; published DOI 10.1016/j.inffus.2020.12.001.
[^r4]: Palomares et al., §2 Definition 2.3/Eq. (3), Fig. 1 (not Fig. 2), Definitions 2.4–2.5; §3.2/Table 3 (fusion alternatives, score versus ranking fusion). Accessible author paper: https://arxiv.org/pdf/2007.16120v2.
