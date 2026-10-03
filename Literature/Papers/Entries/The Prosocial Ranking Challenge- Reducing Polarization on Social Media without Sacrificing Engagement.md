---
title: "The Prosocial Ranking Challenge: Reducing Polarization on Social Media without Sacrificing Engagement"
tags:
  - empirical_study
  - field_experiment
authors:
  - "[[Literature/Authors/Jonathan Stray|Jonathan Stray]]"
  - "[[Literature/Authors/Ian Baker|Ian Baker]]"
  - "[[Literature/Authors/George Beknazar-Yuzbashev|George Beknazar-Yuzbashev]]"
  - "[[Literature/Authors/Ceren Budak|Ceren Budak]]"
  - "[[Literature/Authors/Julia Kamin|Julia Kamin]]"
  - "[[Literature/Authors/Kylan Rutherford|Kylan Rutherford]]"
  - "[[Literature/Authors/Mateusz Stalinski|Mateusz Stalinski]]"
  - "[[Literature/Authors/Tin Acosta|Tin Acosta]]"
  - "[[Literature/Authors/Chris Bail|Chris Bail]]"
  - "[[Literature/Authors/Michael Bernstein|Michael Bernstein]]"
  - "[[Literature/Authors/Mark Brandt|Mark Brandt]]"
  - "[[Literature/Authors/Amy Bruckman|Amy Bruckman]]"
  - "[[Literature/Authors/Anshuman Chhabra|Anshuman Chhabra]]"
  - "[[Literature/Authors/Soham De|Soham De]]"
  - "[[Literature/Authors/Kayla Duskin|Kayla Duskin]]"
  - "[[Literature/Authors/Sara Fish|Sara Fish]]"
  - "[[Literature/Authors/Beth Goldberg|Beth Goldberg]]"
  - "[[Literature/Authors/Andy Guess|Andy Guess]]"
  - "[[Literature/Authors/Dylan Hadfield-Menell|Dylan Hadfield-Menell]]"
  - "[[Literature/Authors/Muhammed Haroon|Muhammed Haroon]]"
  - "[[Literature/Authors/Safwan Hossain|Safwan Hossain]]"
  - "[[Literature/Authors/Michael Inzlicht|Michael Inzlicht]]"
  - "[[Literature/Authors/Gauri Jain|Gauri Jain]]"
  - "[[Literature/Authors/Zaria Jalan|Zaria Jalan]]"
  - "[[Literature/Authors/Yanchen Jiang|Yanchen Jiang]]"
  - "[[Literature/Authors/Alexander Landry|Alexander P. Landry]]"
  - "[[Literature/Authors/Yph Lelkes|Yph Lelkes]]"
  - "[[Literature/Authors/Hongfan Lu|Hongfan Lu]]"
  - "[[Literature/Authors/Peter Mason|Peter Mason]]"
  - "[[Literature/Authors/Jennifer McCoy|Jennifer McCoy]]"
  - "[[Literature/Authors/Smitha Milli|Smitha Milli]]"
  - "[[Literature/Authors/Paul Resnick|Paul Resnick]]"
  - "[[Literature/Authors/Emily Saltz|Emily Saltz]]"
  - "[[Literature/Authors/Martin Saveski|Martin Saveski]]"
  - "[[Literature/Authors/Lisa Schirch|Lisa Schirch]]"
  - "[[Literature/Authors/Max Spohn|Max Spohn]]"
  - "[[Literature/Authors/Siddarth Srinivasan|Siddarth Srinivasan]]"
  - "[[Literature/Authors/Alexis Tatore|Alexis Tatore]]"
  - "[[Literature/Authors/Luke Thorburn|Luke Thorburn]]"
  - "[[Literature/Authors/Joshua A. Tucker|Joshua A. Tucker]]"
  - "[[Literature/Authors/Robb Willer|Robb Willer]]"
  - "[[Literature/Authors/Magdalena Wojcieszak|Magdalena Wojcieszak]]"
  - "[[Literature/Authors/Manuel Wüthrich|Manuel Wüthrich]]"
  - "[[Literature/Authors/Sylvan Zheng|Sylvan Zheng]]"
publication date: 2026-03-20
source: https://arxiv.org/pdf/2603.19626
doi: 10.48550/arXiv.2603.19626
read status: Todo
⚠️:
  - not audited
---
## Abstract

We report the first direct comparisons of multiple alternative social media algorithms on multiple platforms on outcomes of societal interest. We used a browser extension to modify which posts were shown to desktop social media users, randomly assigning 9,386 users to a control group or one of five alternative ranking algorithms which simultaneously altered content across three platforms for six months during the US 2024 presidential election. This reduced our preregistered index of affective polarization by an average of 0.03 standard deviations (p < 0.05), including a 1.5 degree decrease in differences between the 100 point inparty and outparty feeling thermometers. We saw reductions in active use time for Facebook (-0.37 min/day) and Reddit (-0.2 min/day), but an increase of 0.32 min/day (p < 0.01) for X/Twitter. We saw an increase in reports of negative social media experiences but found no effects on well-being, news knowledge, outgroup empathy, perceptions of and support for partisan violence. This implies that bridging content can improve some societal outcomes without necessarily conflicting with the engagement-driven business model of social media.

## Research Questions
> Research Questions extracted via LLM

- What effects do alternative social-media ranking algorithms have on polarization, engagement, and other societal outcomes?[^r1]

## Study Design
> Study design extracted via LLM

- **Assignment and exposure:** A browser extension intercepted feeds for 9,386 consenting desktop users on Facebook, Reddit, and X/Twitter; random assignment selected default-feed control or one of five treatment rankers from September 2024 to February 2025. Users who kept the extension installed for at least one week entered the analyzed sample.[^r2]
- **Treatments:** `UPRANK_BRIDGING` reorders bridging items; `UPRANK_BRIDGING_DOWNRANK_TOXIC` also demotes toxic/outrage items; `CHALLENGING_STEREOTYPES` replaces political items with stereotype-challenging content; `DIVERSE_APPROVAL` replaces them with content predicted engaging to both parties; `ADD_NEWS` adds personally relevant news from factual, ideologically diverse sources. LLM-based classifiers identify content where specified; no agent-based model is used.[^r3]
- **Measures and results:** The team preregistered pooled treatment-arm estimates over ten outcomes and collected 196 million feed items, 1.2 million user posts/comments, and 84 million engagement events. Pooled treatments reduced affective polarization by 0.027 SD (about 1.5 points on the 100-point in-party/out-party thermometer gap); active use fell on Facebook and Reddit and rose on X/Twitter. The paper also reports increased negative-experience reports and null effects on well-being, news knowledge, outgroup empathy, and partisan-violence outcomes.[^r4]

## Metadata
### References

- [[RankingByEngagementAndNonEngagementSignalsLearningsFromIndustry]]
- [[TheAlgorithmicManagementOfPolarizationAndViolenceOnSocialMediaKinghtFirstAmendmentInstituteAtColumbiaUniversityNewYorkNy]]
- [[SocietalSortingAsASystemicRiskOfRecommenders]]
- [[SimulatingSocialMediaUsingLargeLanguageModelsToEvaluateAlternativeNewsFeedAlgorithms]]
- [[AnalyzingNewsEngagementOnFacebookTrackingIdeologicalSegregationAndNewsQualityInTheFacebookUrlDataset]]
- [[SocialMediaAlgorithmsCanBeRedesignedToBridgeDividesHereSHow]]
- [[EmbeddingDemocraticValuesIntoSocialMediaAisViaSocietalObjectiveFunctions]]
- [[UnresolvedReference6A8E13BC78E4DDC3]]
- [[AiAndTheFutureOfDigitalPublicSquares]]
- [[DesigningRecommenderSystemsToDepolarize]]
- [[Bridging Systems- Open Problems for Countering Destructive Divisiveness across Ranking- Recommenders- and Governance]]
- [[WhyDoesBalancedNewsProduceUnbalancedViews18975NberWorkingPapersNationalBureauOfEconomicResearch]]
- [[AltruismAndProsocialBehavior]]
- [[ResharesOnSocialMediaAmplifyPoliticalNewsButDoNotDetectablyAffectBeliefsOrOpinions]]
- [[Like-minded sources on Facebook are prevalent but not polarizing]]
- [[TheEffectsOfPoliticalAdvertisingOnFacebookAndInstagramBeforeThe2020UsElection]]
- [[HowDoSocialMediaFeedAlgorithmsAffectAttitudesAndBehaviorInAnElectionCampaignScience3816656398404]]
- [[Reranking partisan animosity in algorithmic social media feeds alters affective polarization]]
- [[TheProsocialRankingChallengeFaq]]
- [[MegastudyTesting25TreatmentsToReduceAntidemocraticAttitudesAndPartisanAnimosity]]
- [[RerankingSocialMediaFeedsAPracticalGuideForFieldExperiments]]
- [[Kdd22AssociationForComputingMachineryNewYorkNyUsa]]
- [[AnnotatorInTheLoopACaseStudyOfInDepthRaterEngagementToCreateAProsocialBenchmarkDataset]]
- [[AnnouncingExperimentalBridgingAttributesInPerspectiveApi]]
- [[BiasedAssimilationHomophilyAndTheDynamicsOfPolarization]]
- [[PartisanNewsVersusPartyCuesTheEffectOfCrossCuttingPartyAndPartisanNetworkCuesOnPolarizationAndPersuasion]]
- [[SocialMediaNewsConsumptionAndPolarizationEvidenceFromAFieldExperiment]]
- [[AdvantageAmplificationInSlowlyEvolvingLatentStateEnvironments2019Augus31653172]]
- [[WhyDepolarizationIsHardEvaluatingAttemptsToDecreasePartisanAnimosityInAmerica]]
- [[UncivilAgreementHowPoliticsBecameOurIdentityUniversityOfChicagoPress]]
- [[PoliticalSectarianismInAmerica]]
- [[TheOriginsAndConsequencesOfAffectivePolarizationInTheUnitedStatesPp]]
- [[TowardATheoryOfPerniciousPolarizationAndHowItHarmsDemocraciesComparativeEvidenceAndPossibleRemedies]]
- [[AffectivePolarizationAndMisinformationBelief]]
- [[TheRelationshipBetweenAffectivePolarizationAndDemocraticBackslidingComparativeEvidence]]
- [[DemocraticHypocrisyAndOutGroupThreatExplainingCitizenSupportForDemocraticErosion]]
- [[HowAffectivePolarizationUnderminesSupportForDemocraticNorms]]
- [[TomWoodhouseHughMiallContemporaryConflictResolution4thEditionWiley]]
- [[DoesAffectivePolarizationUndermineDemocraticNormsOrAccountabilityMaybeNot]]
- [[PartisanHostilityAndAmericanDemocracyExplainingPoliticalDivisionsAndWhenTheyMatterUniversityOfChicagoPress]]
- [[CrossCountryTrendsInAffectivePolarization]]
- [[EngagementUserSatisfactionAndTheAmplificationOfDivisiveContentOnSocialMedia]]
- [[EstimatingTheEffectSizeOfMoralContagionInOnlineNetworksAPreRegisteredReplicationAndMetaAnalysis]]
- [[ToxicPoliticsAndTiktokEngagementInThe2024US]]
- [[OutGroupAnimosityDrivesEngagementOnSocialMedia]]
- [[PartisanshipOnSocialMediaInPartyLoveAmongAmericanPoliticiansGreaterEngagementWithOutPartyHateAmongOrdinaryUsers]]
- [[ToxicContentAndUserEngagementOnSocialMediaEvidenceFromAFieldExperiment]]
- [[ShortTermExposureToFilterBubbleRecommendationSystemsHasLimitedPolarizationEffectsNaturalisticExperimentsOnYoutube]]
- [[HowAlgorithmicallyCuratedOnlineEnvironmentsInfluenceUsersPoliticalPolarizationResultsFromTwoExperimentsWithPanelData]]
- [[TwitterXUsePredictsSubstantialChangesInWellBeingPolarizationSenseOfBelongingAndOutrage]]
- [[ThePoliticalEffectsOfXSFeedAlgorithm]]
- [[QuantifyingTheInfodemicPeopleTurnedToTrustworthyNewsOutletsDuringThe2020CoronavirusPandemic]]
- [[MisunderstandingTheHarmsOfOnlineMisinformation]]
- [[FakeNewsOnTwitterDuringThe2016USPresidentialElection]]
- [[LessThanYouThinkPrevalenceAndPredictorsOfFakeNewsDisseminationOnFacebook]]
- [[MostUsersDoNotFollowPoliticalElitesOnTwitterThoseWhoDoShowOverwhelmingPreferencesForIdeologicalCongruity]]
- [[PerceivingAffectivePolarizationInTheUnitedStatesHowSocialMediaShapeMetaPerceptionsAndAffectivePolarization]]
- [[NudgingTheRecommendationAlgorithmIncreasesNewsConsumptionAndDiversityOnYoutube]]
- [[IncentivizingNewsConsumptionOnSocialMediaPlatformsUsingLargeLanguageModelsAndRealisticBotAccounts]]
- [[UnveilingTheNeelyEthicsTechnologyIndices]]
- [[AssociationsBetweenValencedNewsAndAffectInDailyLifeExperimentalAndEcologicalMomentaryAssessmentApproaches]]
- [[IsTheNewsMakingUsUnhappyTheInfluenceOfDailyNewsExposureOnEmotionalStates]]
- [[TheLittleBookOfConflictTransformationGoodBooks]]
- [[ConflictTransformationAMultiDimensionalTask20046789]]
- [[AlgorithmicNewsDiversityAndDemocraticTheoryAddingAgonismToTheMix]]
- [[CanAnAlgorithmBeAgonisticTenScenesFromLifeInCalculatedPublics]]
- [[ImplicationsOfProAndCounterattitudinalInformationExposureForAffectivePolarization]]
- [[IdeologicalCitizensProAttitudinalMediaExposureAndIdeologicalPolarizationTheMediatingRoleOfPresumedMediaInfluenceAndPresumedMediaAffect]]
- [[UnresolvedReference1C228B23C4903BCC]]
- [[TakingComplexSystemsSeriouslyVisualizingAndModelingTheDynamicsOfSustainablePeace]]
- [[EstimatingPeerEffectsInNetworksWithPeerEncouragementDesigns]]
- [[HowSocialLearningAmplifiesMoralOutrageExpressionInOnlineSocialNetworks]]
- [[IncentivizingHighQualityContentInOnlineRecommenderSystems]]
- [[AlgorithmicSelectionAndSupplyOfPoliticalNewsOnFacebook]]
- [[ApplyingConflictResolutionInsightsToTheHyperPolarizedSocietyWideConflictsThreateningLiberalDemocracies]]
- [[NotIdeologyASocialIdentityPerspectiveOnPolarization]]
- [[TheWho5WellBeingIndexASystematicReviewOfTheLiterature]]
- [[LethalMassPartisanshipPrevalenceCorrelatesElectoralContingencies]]
- [[CorrectingInaccurateMetaperceptionsReducesAmericansSupportForPartisanViolence]]
- [[GroupEmpathyTheoryTheEffectOfGroupEmpathyOnUsIntergroupAttitudesAndBehaviorInTheContextOfImmigrationThreats]]
- [[UnresolvedReference42AD66581D877C49]]
- [[EngagingPoliticallyDiverseAudiencesOnSocialMedia]]
- [[UnresolvedReference0B2C05454011A171]]
- [[UnresolvedReferenceF8808C1CF87D6825]]
- [[ActualVersusAssumedDifferencesInConstrualNaiveRealismInIntergroupPerceptionAndConflict]]
- [[AmericanPartisansVastlyUnderEstimateTheDiversityOfOtherPartisansPolicyAttitudes]]
- [[PoliticalCoherenceAndCertaintyAsDriversOfInterpersonalLikingOverAndAboveSimilarity]]
- [[InaccurateGroupMetaPerceptionsDriveNegativeOutGroupAttributionsInCompetitiveContexts]]
- [[ReducingExplicitBlatantDehumanizationByCorrectingExaggeratedMetaPerceptions]]
- [[WhyVotersWhoValueDemocracyParticipateInDemocraticBacksliding]]
- [[SeekAndYeShallBeFineAttitudesTowardPoliticalPerspectiveSeekers]]
- [[ConversationalReceptivenessImprovingEngagementWithOpposingViews]]
- [[RumorsAndHealthCareReformExperimentsInPoliticalMisinformation]]
- [[TheEffectOfMinimumWagesOnLowWageJobs]]
- [[ConsistentCovarianceMatrixEstimationWithSpatiallyDependentPanelData]]
- [[TheWelfareEffectsOfSocialMedia]]

## Audit Log
- Audit invalidated (2026-09-30): auditor admitted incomplete independent checks and premature flag removal. Previous valid audits, if any, remain separate.

- WITHDRAWN audit claim (2026-09-30): the remaining-audit-c report overstated independent source checks; it does not establish a pass.

## LLM Justification
[^r1]: https://arxiv.org/abs/2603.19626, abstract and Introduction, pp. 1–2; source of the research question.
[^r2]: https://arxiv.org/pdf/2603.19626, “Experimental Setup,” pp. 4–5, and Fig. 1 caption, p. 3; reports the browser-extension interception, sample, assignment, dates, and one-week installation inclusion rule.
[^r3]: https://arxiv.org/pdf/2603.19626, pp. 4–5, numbered treatment descriptions 1–5; treatment mechanisms and classifier use. The paper is a human field experiment, not an agent-based simulation.
[^r4]: https://arxiv.org/pdf/2603.19626, pp. 5–6, pooled results and data-collection paragraph; supports outcomes and reported effects.
