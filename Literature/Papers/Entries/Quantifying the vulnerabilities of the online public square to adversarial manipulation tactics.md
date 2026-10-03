---
title: "Quantifying the vulnerabilities of the online public square to adversarial manipulation tactics"
authors:
  - "[[Literature/Authors/Bao Tran Truong|Bao Tran Truong]]"
  - "[[Literature/Authors/Xiaodan Lou|Xiaodan Lou]]"
  - "[[Literature/Authors/Alessandro Flammini|Alessandro Flammini]]"
  - "[[Literature/Authors/Filippo Menczer|Filippo Menczer]]"
source: "https://academic.oup.com/pnasnexus/article/3/7/pgae258/7701371"
doi: "10.1093/pnasnexus/pgae258"
publication date: "2024-06-28"
tags:
  - "model"
  - "simulation"
  - "social_media"
read status: Todo
⚠️:
  - audit failed
---

## Abstract

Social media, seen by some as the modern public square, is vulnerable to manipulation. By controlling inauthentic accounts impersonating humans, malicious actors can amplify disinformation within target communities. The consequences of such operations are difficult to evaluate due to the challenges posed by collecting data and carrying out ethical experiments that would influence online communities. Here we use a social media model that simulates information diffusion in an empirical network to quantify the impacts of adversarial manipulation tactics on the quality of content. We find that the presence of hub accounts, a hallmark of social media, exacerbates the vulnerabilities of online communities to manipulation. Among the explored tactics that bad actors can employ, infiltrating a community is the most likely to make low-quality content go viral. Such harm can be further compounded by inauthentic agents flooding the network with low-quality, yet appealing content, but is mitigated when bad actors focus on specific targets, such as influential or vulnerable individuals. These insights suggest countermeasures that platforms could employ to increase the resilience of social media users to manipulation.

## Research Questions
> Research Questions extracted via LLM

- Which adversarial tactics most effectively amplify low-quality content in a modeled online public square?[^r1]
- How do network hubs, infiltration, flooding, and targeting affect content diffusion and quality?[^r1]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?
- SimSoM models competing messages circulating through a static directed follower network with authentic accounts and an infiltrating inauthentic subnetwork.[^m1]

### How does it work?
The compact state distinguishes global message attributes from feed-specific engagement and age.[^m1]

```yml
World:
  accounts: [Account]
  messages: [Message]
  infiltration: 0..1
  deception: 0..1
  flooding: 1..64
  target: Random | Hubs | Misinformation | Partisanship | Liberal | Conservative

Account:
  kind: Authentic | Inauthentic
  follows: [AccountId]
  feed: [Entry]

Message:
  quality: 0..1
  appeal: 0..1

Entry:
  message: MessageId
  friend_shares: 0..
  first_seen: f64
```

The main diffusion/quality/convergence settings are fixed in the reported experiments.[^m1][^m2][^m3]

```
POST_PROBABILITY = 0.5
FEED_CAPACITY = 15
QUALITY_EXPONENT = 10
APPEAL_EXPONENT = 4
RECENCY_RATE = 0.4
RECENCY_POWER = 0.4
BAD_ACTOR_SHARE = 0.05
DEFAULT_INFILTRATION = 0.01
DEFAULT_DECEPTION = 0
DEFAULT_FLOODING = 1
QUALITY_SMOOTHING = 0.8
CONVERGENCE_THRESHOLD = 0.0001
REPLICATIONS = 10
```

- An activated account creates a new message with `POST_PROBABILITY`; otherwise it reshares one from its feed. Deliver to followers' feeds, retaining the most recent `FEED_CAPACITY` distinct messages. Follower links point follower→friend; messages move in the reverse direction.[^m1]
- Reshare weights are `appeal * friend_shares * exp(-RECENCY_RATE*age^RECENCY_POWER)`, normalized across the feed. Age is time since first arrival in that feed; engagement counts the posting/resharing by that account's friends. Flooding makes bad actors share θ times, boosting engagement.[^m1]
- Authentic new quality has density `τ*exp(τ*q)/(exp(τ)-1)` on `[0,1]`, τ=`QUALITY_EXPONENT`; appeal independently has density `(1+α)*(1-a)^α`, α=`APPEAL_EXPONENT`. Bad actors create quality zero; with probability ϕ set appeal one, otherwise draw authentic-style appeal.[^m2]
- Add βN bad actors, β=`BAD_ACTOR_SHARE`. Their directed random-walk growth starts with four fully connected nodes; each new node follows three others, using a random friend-of-friend with probability 0.5 for two of them. Bad actors neither follow nor reshare authentic content in this study.[^m4]
- Each authentic account follows each bad actor with probability γ; targeted variants weight this probability by followers, misinformation score, partisanship, or leaning, keeping expected authentic followers per bad actor γN fixed.[^m4]
- The authentic network is a sampled Twitter graph: 10,006 nodes in a 94-core, then edge sampling gives 1,809,798 edges. Compare the original network with degree-preserving, community-preserving, and random shuffles to separate hubs/clusters.[^m5]
- Measure mean quality across authentic feeds. Stop when successive smoothed quality changes fall below `CONVERGENCE_THRESHOLD`; report quality relative to a no-bad-actor baseline over `REPLICATIONS` runs. Reshare/exposure cascades count extinct messages; exposure means a message is in an account's feed while activated.[^m3]
- This extraction omits graph-generation implementation and convergence diagnostics. No search, personalization, detailed cognitive behavior, or complex contagion is represented in this model.[^m6]

### What can it answer?
- It compares how infiltration, deception, flooding, targeting, and network structure affect feed quality and cascade reach.[^m3][^m4][^m5]

### Where does it apply?
- It studies modeled information-quality suppression on the sampled network; it does not directly estimate live-platform interventions or opinion consensus.[^m6]

## Metadata
### References
- [[MeasuringEmotionalContagionInSocialMedia]]
- [[CommittedActivistsAndTheReshapingOfStatusQuoSocialConsensus]]
- [[TheProductionOfInformationInTheAttentionEconomy]]
- [[TheRiseOfSocialBots]]
- [[AnInternetResearchProjectDrawsConservativeIre]]
- [[TheRoleOfInflexibleMinoritiesInTheBreakingOfDemocraticOpinionDynamics]]
- [[HowSocialInfluenceCanUndermineTheWisdomOfCrowdEffect]]
- [[PartisanAsymmetriesInOnlinePoliticalActivity]]
- [[GrowingNetworkWithLocalRulesPreferentialAttachmentClusteringHierarchyAndDegreeCorrelations]]
- [[FameEmergesAsAResultOfSmallMemory]]
- [[SocialConsensusThroughTheInfluenceOfCommittedMinorities]]
- [[SocialMediaAndTheElections]]
- [[CharacterizingAndModelingTheDynamicsOfOnlinePopularity]]
- [[RobustDynamicClassesRevealedByMeasuringTheResponseFunctionOfASocialSystem]]
- [[EpidemicsAndRumours]]
- [[EffectOfZealotryInHighDimensionalOpinionDynamicsModels]]
- [[NoveltyAndCollectiveAttention]]
- [[CompetitionInducedCriticalityInAModelOfMemePopularity]]
- [[CompetitionAmongMemesInAWorldWithLimitedAttention]]
- [[SocialComputingAndTheAttentionEconomy]]
- [[ConfirmationBiasAUbiquitousPhenomenonInManyGuises]]
- [[TheSimpleRulesOfSocialContagion]]
- [[ExperimentalStudyOfInequalityAndUnpredictabilityInAnArtificialCulturalMarket]]
- [[OptimalNetworkModularityForInformationDiffusion]]
- [[ViralityPredictionAndCommunityStructureInSocialNetworks]]
- [[TheSpreadingOfMisinformationOnline]]
- [[SocialBotsDistortThe2016USPresidentialElectionOnlineDiscussion]]
- [[SocialMediaAndFakeNewsInThe2016Election]]
- [[EvidenceOfComplexContagionOfInformationInSocialMediaAnExperimentUsingTwitterBots]]
- [[NetworkDynamicsOfSocialInfluenceInTheWisdomOfCrowds]]
- [[HowAlgorithmicPopularityBiasHindersOrPromotesQuality]]
- [[AnatomyOfAnOnlineMisinformationNetwork]]
- [[InfluenceOfAugmentedHumansInOnlineInteractionsDuringVotingEvents]]
- [[TheSpreadOfTrueAndFalseNewsOnline]]
- [[TheScienceOfFakeNews]]
- [[AnalyticalStudyOfQualityBiasedCompetitionDynamicsForMemesInSocialMedia]]
- [[TheSpreadOfLowCredibilityContentBySocialBots]]
- [[ExperimentalEvidenceForTippingPointsInSocialConvention]]
- [[QuantifyingBiasesInOnlineInformationExposure]]
- [[TheDarkSideOfInformationProliferation]]
- [[ActingThePart]]
- [[BotsIncreaseExposureToNegativeAndInflammatoryContentInOnlineSocialSystems]]
- [[ArmingThePublicWithArtificialIntelligenceToCounterSocialBots]]
- [[LessThanYouThinkPrevalenceAndPredictorsOfFakeNewsDisseminationOnFacebook]]
- [[FakeNewsOnTwitterDuringThe2016USPresidentialElection]]
- [[SocialMediaSContributionToPoliticalMisperceptionsInUSPresidentialElections]]
- [[FriendshipParadoxBiasesPerceptionsInDirectedNetworks]]
- [[TheRoleOfBotSquadsInThePoliticalPropagandaOnTwitter]]
- [[InternetResearchAgencyTwitterActivityPredicted2016USElectionPolls]]
- [[TheExistentialThreatFromCyberEnabledInformationWarfare]]
- [[AResponseToFakeNewsAsAResponseToCitizensUnited]]
- [[InformationGerrymanderingAndUndemocraticDecisions]]
- [[AssessingTheRussianInternetResearchAgencySImpactOnThePoliticalAttitudesAndBehaviorsOfAmericanTwitterUsersInLate2017]]
- [[PausingToConsiderWhyAHeadlineIsTrueOrFalseCanHelpReduceTheSharingOfFalseNews]]
- [[TheGrowingAmplificationOfSocialMediaMeasuringTemporalAndSocialContagionDynamicsForOver150LanguagesOnTwitterFor20092020]]
- [[FightingCovid19MisinformationOnSocialMediaExperimentalEvidenceForAScalableAccuracyNudgeIntervention]]
- [[UnresolvedReferenceEB2124D23CC4C97F]]
- [[NeutralBotsProbePoliticalBiasOnSocialMedia]]
- [[OnTheOrganizationOfTheUSGovernmentForRespondingToAdversarialInformationWarfareAndInfluenceOperations]]
- [[UnresolvedReferenceA5BFAFF7F62BB612]]
- [[UnresolvedReference780FD646FD99E77F]]
- [[UnresolvedReferenceF5B15AA81CCCA89B]]
- [[UnresolvedReference67827D8599A16492]]
- [[UnresolvedReference7E7201D5E4A86C4A]]
- [[UnresolvedReference0BD19DA599D8D100]]
- [[UnresolvedReference7684A175FE5BA867]]
- [[TacklingMisinformationWhatResearchersCouldDoWithSocialMediaData]]
- [[LazyNotBiasedSusceptibilityToPartisanFakeNewsIsBetterExplainedByLackOfReasoningThanByMotivatedReasoning]]
- [[DisinformationAndSocialBotOperationsInTheRunUpToThe2017FrenchPresidentialElection]]
- [[ShiftingAttentionToAccuracyCanReduceMisinformationOnline]]
- [[RightAndLeftPartisanshipPredictsAsymmetricVulnerabilityToMisinformation]]
- [[UnresolvedReferenceD58B3FE5747A6146]]
- [[EffectsOfNetworkStructureCompetitionAndMemoryTimeOnSocialSpreadingPhenomena]]
- [[UnresolvedReference513E72B6930123A4]]
- [[TheEchoChamberEffectOnSocialMedia]]
- [[UnresolvedReference1166166B69E2AFB8]]
- [[ComparingInformationDiffusionMechanismsByMatchingOnCascadeSize]]
- [[TheDifference]]
- [[CombiningInterventionsToReduceTheSpreadOfViralMisinformation]]
- [[LearningThroughTheGrapevineAndTheImpactOfTheBreadthAndDepthOfSocialNetworks]]
- [[StudyingFakeNewsSpreadingPolarisationDynamicsAndManipulationByBotsATaleOfNetworksAndLanguage]]
- [[ExposureToTheRussianInternetResearchAgencyForeignInfluenceCampaignOnTwitterInThe2016UsElectionAndItsRelationshipToAttitudesAndVotingBehavior]]
- [[MathematicalModelingOfDisinformationAndEffectivenessOfMitigationPolicies]]
- [[TheAttentionEconomy]]
- [[SupersharersOfFakeNewsOnTwitter]]
- [[MisunderstandingTheHarmsOfOnlineMisinformation]]
- [[UnresolvedReference982181BD67A8C65E]]
- [[UnresolvedReference9C09CAFB7C54D9AB]]
- [[UnresolvedReference63B1BFC801423120]]
- [[UnresolvedReferenceCDC912B0BE813AD7]]
- [[UnresolvedReferenceB7F1AD292AE7CCC6]]
- [[UnresolvedReference19FBBF0006889363]]
- [[UnresolvedReferenceBF25BAA10F047E9C]]
- [[UnresolvedReference01572F814B5B9900]]
- [[UnresolvedReference353220D4A4C8837F]]
- [[UnresolvedReference29E6EFA86B1E535D]]
- [[UnresolvedReference52D1E43BC42AE311]]
- [[UnresolvedReference42FFF9AD90802CB0]]
- [[UnresolvedReferenceCDF11E9492D03966]]
- [[ActingThePartExaminingInformationOperationsWithinBlacklivesmatterDiscourse]]
- [[UnresolvedReferenceD7DBFE1D43D23FD5]]
- [[UnresolvedReference6A883A5D6081394F]]
- [[UnresolvedReferenceCBF3C45AF77802A9]]
- [[UnresolvedReferenceD684663C2D4D1858]]
- [[CyberwarHowRussianHackersAndTrollsHelpedElectAPresident]]
- [[UnresolvedReferenceE8AC98969EC50EE7]]
- [[UnresolvedReference61439C8106DFA750]]
- [[UnresolvedReference992AAB24FE9A2614]]
- [[UnresolvedReference5BBF42F0C52DEFF8]]
- [[UnresolvedReference62CD483B0BDAA44E]]
- [[UnresolvedReference21BC5EAD5B184F49]]
- [[UnresolvedReference53BB1BDB5D0EA1EA]]
- [[UnresolvedReferenceDFEC36E5C90C72FD]]
- [[UnresolvedReference2F9690027311419E]]
- [[TheWisdomOfCrowds]]
- [[TheDifferenceHowThePowerOfDiversityCreatesBetterGroupsFirmsSchoolsAndSocieties]]
- [[UnresolvedReferenceF63316524C89254B]]
- [[UnresolvedReferenceE8E18E3F623EA722]]
- [[StardomAndTalent]]
- [[UnresolvedReference77B4A0CCD7A0D851]]
- [[UnresolvedReferenceFF443115BDF7CA0B]]
- [[UnresolvedReferenceFF0B27F98B458154]]
- [[UnresolvedReference62A4721ABA677317]]
- [[ExposureToSocialEngagementMetricsIncreasesVulnerabilityToMisinformation]]

## Audit Log
- Audit invalidated (2026-09-30): auditor admitted relying on spot checks and previous reports before clearing flags. A full independent audit is still required.
- 2026-09-30: Full-source design audit found opaque source distributions concealed independent quality/appeal rules; feed-specific engagement/age state omitted; posting/feed/recency/convergence constants omitted; bad-actor growth and non-resharing of authentic messages omitted; targeting fixed-follower control omitted. Corrected against the source passages below; independent re-audit pending.[^design]
- Independent audit found the network/data construction and tactic mechanisms omitted. The note now specifies feed selection, message attributes, sampled follower network and reduction, γ/ϕ/θ tactics, targeting features, and exposure-quality outcomes. At that stage, independent re-audit remained pending.

- WITHDRAWN audit claim (2026-09-30): incomplete source checks; this audit does not establish a pass.

## LLM Justification
[^r1]: The research questions are a concise transformation of the primary source’s abstract and stated aims. Source location: Model and Results sections. Source: [Quantifying the vulnerabilities of the online public square to adversarial manipulation tactics](https://academic.oup.com/pnasnexus/article/3/7/pgae258/7701371).


[^m1]: Methods → Social media diffusion model: static edge direction, μ=.5, σ=15, normalized appeal×engagement×recency weights, stretched-exponential recency and θ flooding. Results/Figure 1 describes distinct recent messages.

[^m2]: Methods → Quality and appeal supplies exact independent distributions, τ=10, α=4, q=0 bad-actor content and ϕ mixture setting a=1.

[^m3]: Methods → Overall quality, Cascade construction, Simulation framework and parameters: moving average ρ=.8, relative-change ε=.0001, ten runs, extinct cascades and activation-defined exposure. Results defines relative quality against a no-bad-actor baseline.

[^m4]: Methods → Bad-actor subnetwork and Bad-actor targeting tactics: β=.05, four-node seed, outdegree3, friend-of-friend probability .5, γ links, no authentic following/resharing by bad actors, targeted feature weighting and conserved γN expectation.

[^m5]: Methods → Follower network and Simulation framework: news-sharing sample, 94-core 10006 nodes/1809798 sampled edges, degree/community/random rewiring controls.

[^m6]: Discussion → limitations: omitted search/personalization/cognition/complex contagion; focus is quality suppression rather than opinion consensus.

[^design]: Source audit checked the full text at https://academic.oup.com/pnasnexus/article/3/7/pgae258/7701371. Model footnotes identify the passages supporting the corrections.
