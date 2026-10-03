---
title: 'Agent-Based Modeling to Inform Online Community Design: Impact of Topical Breadth, Message Volume, and Discussion Moderation on Member Commitment and Contribution'
authors:
- '[[Literature/Authors/Yuqing Ren|Yuqing Ren]]'
- '[[Literature/Authors/Robert E. Kraut|Robert E. Kraut]]'
publication date: 2013-10-16
tags:
- model
- simulation
source: https://carlsonschool.umn.edu/sites/carlsonschool.umn.edu/files/2018-10/RenKraut-HCI2014-AgentBasedModel.pdf
doi: 10.1080/07370024.2013.828565
read status: Todo
---
## Abstract

The design of complex social systems, such as online communities, requires the consideration of many parameters, a practice at odds with social science research that focuses on the effects of a small set of variables. In this article, we show how synthesizing insights from multiple, narrowly focused social science theories in an agent-based model helps us understand factors that lead to the success of online communities. The agent-based model combines insights from theories related to collective effort, information overload, social identity, and interpersonal attraction to predict motivations for online community participation. We conducted virtual experiments to develop hypotheses around three design decisions about how to orchestrate an online community—topical breadth, message volume, and discussion moderation—and the trade-offs involved in making these decisions. The simulation experiments suggest that broad topics and high message volume can lead to higher member commitment. Personalized moderation outperforms other types of moderation in increasing members' commitment and contribution, especially in topically broad communities and those with high message volume. In comparison, community-level moderation increases commitment but not contribution, and only in topically narrow communities. These simulation results suggest a critical trade-off between informational and relational benefits. This research illustrates that there are many interactions among the design decisions that are important to consider; the particulars of the community's goals often determine the effectiveness of some decisions. It also demonstrates the value of agent-based modeling in synthesizing simple social science theories to describe and prescribe behaviors in a complex system, generating novel insights that inform the design of online communities.


## Research Questions
> Research Questions extracted via LLM

- How do topical breadth, message volume, and moderation style affect community viability and member commitment?[^r1]
- How do moderation effects depend on breadth and message volume, and how do design choices trade off members’ informational, relational, and other participation benefits?[^r1]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?
A daily agent-based model of a text-based interest community. Members’ accumulated benefits and participation costs drive logins, reading, posting, newcomer entry, and inactivity; messages, membership, and interpersonal ties change as agents interact.[^r2]

### How does it work?
The schema shows the main agents, benefits, and experimental conditions described in §§4–5.[^r10][^r12]
```yml
Community:
  members: [Member]
  messages: [Message]
  settings: CommunitySettings

CommunitySettings:
  topic_breadth: TOPICS_NARROW | TOPICS_MEDIUM | TOPICS_BROAD
  mean_messages_per_day: MESSAGES_PER_DAY_LOW | MESSAGES_PER_DAY_MEDIUM | MESSAGES_PER_DAY_HIGH
  moderation: NoModeration | CommunityLevel | Personalized

Member:
  interests: [Topic]
  accumulated_benefits: BenefitVector
  costs: ParticipationCosts
  activity: Active | Inactive

BenefitVector:
  information_from_reading: BenefitValue
  information_from_sharing: BenefitValue
  identity: BenefitValue
  interpersonal_bonds: BenefitValue
  enjoyment: BenefitValue
  reputation: BenefitValue

BenefitValue: ...

ParticipationCosts:
  access: ...
  reading: ...
  posting: ...
  opportunity: ...

Topic: ...
Message: ...
```

```
TOPICS_NARROW = 1
TOPICS_MEDIUM = 5
TOPICS_BROAD = 9

MESSAGES_PER_DAY_LOW = 10
MESSAGES_PER_DAY_MEDIUM = 15
MESSAGES_PER_DAY_HIGH = 20
```
- The model separately tracks informational benefits from reading and sharing, identity, interpersonal bonds, enjoyment, and reputation, then subtracts access, reading/posting, and opportunity costs.[^r10]
- In the baseline interest community, motivation weights are 0.5 for information, 0.1 identity, 0.3 bonds, and 0.1 for enjoyment and reputation; individual weights vary normally around community means. Agents log in and post when expected benefit exceeds expected cost.[^r10]
- Reading is newest-first and continues according to past net reading benefit, capped by time, interest, and message availability.[^r10]
- Repeated interaction strengthens interpersonal ties; similar interests and off-topic messages strengthen them more, while bond benefit has diminishing returns.[^r10][^r13]
- In the baseline, reply selection equally weights message popularity, reciprocity, and interest match (the paper also varies these weights). New-thread versus reply is equally likely; a reply topic depends on the replied-to message, the member’s interests, and recently viewed messages.[^r10][^r13]
- First-time posters start on-topic; newcomer entry is proportional to community size and follows a truncated gamma distribution. Inactivity becomes more likely after 30 days without posting and a long absence from visits (about a year).[^r10][^r13]
- Moderation conditions are no filtering, community-level removal of off-topic messages, or personalized display of interest-matched messages. The authors state that a concrete personalized-moderation implementation is beyond scope; for the virtual experiment they abstract it as a filter with 80% matching accuracy (tested from 60–100%).[^r11][^r12]
- Each condition had two 365-day simulations, one with five and one with 20 constructed groups; each group started with 30 agents and 30 messages. The reported results use the five-group run, with similar replication results.[^r11][^r12]
- The model used staged daily updates: active agents read and post before the next period, then their read messages update expected benefits.[^r11][^r12]
- The full-factorial experiment compared 1, 5, or 9 topics; mean daily volume of 10, 15, or 20 messages; and the three moderation conditions. It reports posts as community activity, logins as member commitment, and informational and relational benefits.[^r12]
- “Viability” is an overarching research question, not a separate operationalized outcome. Calibration used 12 Usenet groups and validation used 25; those groups had no moderation. Thus the fit checks baseline community patterns, while moderation contrasts are virtual experiments rather than externally validated treatment effects.[^r12]

### What can it answer?
- It compares conditional effects of topical breadth, message volume, and moderation on posting, login commitment, and benefit trade-offs under its assumptions.[^r3][^r12]
- Reported results: personalized moderation produces the greatest posting/activity, with its advantage especially large in broad-topic and high-volume settings.[^r3][^r12]
- Community-level moderation produces the highest login commitment in single-topic communities, while personalized moderation leads in broader communities.[^r3][^r12]
- Broad topics increase login frequency, and higher message volume also raises logins, but these patterns vary with moderation.[^r3][^r12]

### Where does it apply?
The authors frame it for text-based interest communities such as newsgroups and web forums; broader community types require adapting the model.[^r4]

## Metadata
### References
- [[InvisibleCrowdsInCyberspaceMappingTheSocialStructureOfTheUsenet]]
- [[DesigningComplexOrganizations]]
- [[YouCanTPlay20QuestionsWithNatureAndWinProjectiveCommentsOnThePapersOfThisSymposium]]
- [[HostingWebCommunitiesBuildingRelationshipsIncreasingCustomerLoyaltyAndMaintainingACompetitiveEdge]]
- [[CommunityEffortInOnlineGroupsWhoDoesTheWorkAndWhy]]
- [[ManagingBusinessComplexityDiscoveringStrategicSolutionsWithAgentBasedModelingAndSimulation]]
- [[OnlineCommunitiesDesigningUsabilitySupportingSociability]]
- [[SmallGroupProcessesAndInterpersonalRelations]]
- [[HandbookOfRelationshipInitiation]]
- [[SideIssuesCentreStageRecentDevelopmentsInStudiesOfDeindividuationInGroupsPp202AmsterdamKnaw]]
- [[InformationSystemsResearch]]
- [[NewTelecommunicationsServices]]
- [[SideIssuesCentreStageRecentDevelopmentsInStudiesOfDeIndividuationInGroups]]
- [[HandbookOfSociologicalTheory]]
- [[PreferentialAttachmentAndMutualityInElectronicKnowledgeNetworks]]
- [[WhyShouldIShareExaminingSocialCapitalAndKnowledgeContributionInElectronicNetworksOfPractice]]
- [[ECommerceRecommendationApplications]]
- [[ChemieInCyberspace]]
- [[NetSurfersDonTRideAloneVirtualCommunitiesAsCommunities]]
- [[RefiningTheCognitiveRedefinitionOfTheGroupDeindividuationEffectsInCommonBondVsCommonIdentityGroups]]
- [[GroupDynamicsResearchAndTheory]]
- [[MultilevelTheoryResearchAndMethodsInOrganizationsFoundationsExtensionsAndNewDirections]]
- [[TheValidityOfComputationalModelsInOrganizationScienceFromModelRealismToPurposeOfTheModel]]
- [[InternetMinimalGroupParadigm]]
- [[TheImpactOfMembershipOverlapOnGrowthAnEcologicalCompetitionViewOfOnlineGroups]]
- [[PersonalizedContentRecommendationAndUserSatisfactionTheoreticalSynthesisAndEmpiricalFindings]]
- [[InterpersonalAttractionAndAttitudeSimilarity]]
- [[AMultilevelAnalysisOfSociabilityUsabilityAndCommunityDynamicsInAnOnlineHealthCommunity]]
- [[InformalSocialCommunication]]
- [[NetworkExchangePatternsInOnlineCommunities]]
- [[SocialLoafingAMetaAnalyticReviewAndTheoreticalIntegration]]
- [[TheAsaFrameworkAnUpdate]]
- [[PicturingUsenetMappingComputerMediatedCollectiveAction]]
- [[AnticipatedOngoingInteractionVersusChannelEffectsOnRelationalCommunicationInComputerMediatedInteraction]]
- [[TowardAnIntegrationOfAgentAndActivityCentricApproachesInOrganizationalProcessModelingIncorporatingIncentiveMechanisms]]
- [[UsingSocialPsychologyToMotivateContributionsToOnlineCommunities]]
- [[GroupCohesivenessAsInterpersonalAttractionAReviewOfRelationshipsWithAntecedentAndConsequentVariables]]
- [[SelfDisclosureAndLikingAMetaAnalyticReview]]
- [[FollowTheReader]]
- [[PleasureOrUtilityTimePlanningStyleAndWebUsageBehaviors]]
- [[ComputationalAndMathematicalOrganizationTheoryPerspectiveAndDirections]]
- [[FollowTheSlashDot]]
- [[SimulatingProjectWorkProcessesAndOrganizationsTowardAMicroContingencyTheoryOfOrganizationalDesign]]
- [[ActASimpleTheoryOfComplexCognition]]
- [[EmpiricalEvidenceOfInformationOverloadConstrainingChatChannelCommunityInteractions]]
- [[VirtualCommunityAttractionWhyPeopleHangOutOnline]]
- [[TalkToMe]]
- [[TellingHumansAndComputersApartAutomatically]]
- [[ModelingTeamProcessesIssuesAndASpecificExample]]
- [[ReducingIntergroupConflictFromSuperordinateGoalsToDecategorizationRecategorizationAndMutualDifferentiation]]
- [[TrustAmongStrangersInInternetTransactionsEmpiricalAnalysisOfEbaySReputationSystem]]
- [[TheQualityOfOnlineSocialRelationships]]
- [[CommonBondAndCommonIdentityGroupsOnTheInternetAttachmentAndNormativeBehaviorInOnTopicAndOffTopicChats]]
- [[AnOverviewAndUnderviewOfResearchAndTheoryWithinTheAttractionParadigm]]
- [[UnderstandingTheMotivationsParticipationAndPerformanceOfOpenSourceSoftwareDevelopersALongitudinalStudyOfTheApacheProjects]]
- [[MembershipSizeCommunicationActivityAndSustainabilityAResourceBasedModelOfOnlineSocialStructures]]
- [[YouAreWhoYouTalkToDetectingRolesInUsenetNewsgroups]]
- [[StatisticalPowerAnalysisForTheBehavioralSciences]]
- [[ComputationalApproachesToSociologicalTheorizing]]
- [[TheTopFiveReasonsForLurkingImprovingCommunityExperiencesForEveryone]]
- [[AnEmpiricalExplorationOfMassInteractionSystemDynamicsIndividualInformationOverloadAndUsenetDiscourse]]
- [[InformationOverloadAndTheMessageDynamicsOfOnlineInteractionSpacesATheoreticalModelAndEmpiricalExploration]]
- [[WebPersonalizationAsAPersuasionStrategyAnElaborationLikelihoodModelPerspective]]
- [[HowOpenSourceSoftwareWorksFreeUserToUserAssistance]]
- [[Eddi]]
- [[SocialIdentityAndSelfCategorizationProcessesInOrganizationalContexts]]
- [[ShortAndTweet]]
- [[CompetitionAmongVirtualCommunitiesAndUserValuationTheCaseOfInvestingRelatedCommunities]]
- [[DataMiningAndKnowledgeDiscoveryMakingSenseOutOfData]]
- [[TwitterAndTheDevelopmentOfAnAudience]]
- [[AllModelsAreWrongReflectionsOnBecomingASystemsScientist]]
- [[AsymmetriesInAttachmentsToGroupsAndToTheirMembersDistinguishingBetweenCommonIdentityAndCommonBondGroups]]
- [[OrganizationalConsultantCreatingAUseableTheoryForOrganizationalDesign]]
- [[TalkAmongstYourselves]]
- [[DevelopingTheoryThroughSimulationMethods]]
- [[Grouplens]]
- [[TowardACriticalMassTheoryOfInteractiveMedia]]
- [[AnEmpiricalStudyOfCriticalMassAndOnlineCommunitySurvival]]
- [[ApplyingCommonIdentityAndBondTheoryToDesignOfOnlineCommunities]]
- [[CommunitiesInCyberspace]]
- [[IntrinsicAndExtrinsicMotivationsClassicDefinitionsAndNewDirections]]
- [[ElectronicCommunitiesGlobalVillagesOrCyberbalkanizationBestThemePaper]]
- [[LeadershipAtADistanceResearchInTechnologicallySupportedWork]]
- [[StrategicOrganizationalDiagnosisAndDesign]]
- [[ManagingBusinessComplexity]]
- [[SocialIdentitySelfCategorizationAndTheSmallGroup]]
- [[EffectsOfTaskAndGroupSizeUponGroupProductivityAndMemberSatisfaction]]
- [[OrganizationalBehavior1]]
- [[TalkingAboutTactileExperiences]]
- [[UnresolvedReferenceFDB54C9320EF3FEF]]
- [[UnresolvedReference94EC589F92806CD3]]
- [[PricingElectronicMailToSolveTheProblemOfSpam]]
- [[WhyShouldIShareExaminingSocialCapitalAndKnowledgeContributionInElectronicNetworksOfPractice1]]
- [[OnlineCommunitiesDesigningUsabilityAndSupportingSociability]]
- [[OrganizationalBehavior1EssentialTheoriesOfMotivationAndLeadership]]
- [[UnresolvedReference6BA987826CEA5FFF]]
- [[TalkToMeFoundationsForSuccessfulIndividualGroupInteractionsInOnlineCommunities]]
- [[EddiInteractiveTopicBasedBrowsingOfSocialStatusStreams]]
- [[TheDynamicsOfCyberspaceExaminingAndModelingOnlineSocialStructure]]
- [[ValidatingComputationalModels]]
- [[ShortAndTweetExperimentsOnRecommendingContentFromInformationStreams]]
- [[TalkAmongstYourselvesInvitingUsersToParticipateInOnlineConversations]]
- [[UnresolvedReference44E3E85FD0F49C1A]]
- [[EvidenceBasedSocialDesignMiningTheSocialSciencesToBuildOnlineCommunities]]
- [[UnresolvedReference406E1526BEB9B736]]
- [[BuildingCommitmentAndContributionInOnlineGroupsThroughInteraction]]
- [[NormMaintenanceInOnlineCommunitiesAnalysisOfHeterarchicalModerationRegimes]]
- [[FollowTheSlashDotEffectsOfFeedbackOnNewMembersInAnOnlineCommunity]]
- [[FollowTheReaderFilteringCommentsOnSlashdot]]
- [[OnlineCommunitiesNetworksThatNurtureLongDistanceRelationshipsAndLocalTies]]
- [[SideEffectsCentreStageRecentDevelopmentsInStudiesOfDeIndividuationInGroups]]
- [[GrouplensAnOpenArchitectureForCollaborativeFilteringOfNetnews]]
- [[CommunicationBehavior]]
- [[ElectronicCommunitiesGlobalVillageOrCyberbalkans]]
- [[TwitterAndTheDevelopmentOfAnAudienceThoseWhoStayOnTopicThrive]]
- [[Netlogo]]
- [[WhyMostOnlineCommunitiesFail]]
- [[UnresolvedReferenceEBD8A8E9A0F34562]]

## Audit Log
- Initial audit found benefit mechanisms compressed, moderation scope unclear, and experimental levels/outcomes underspecified; the summary now records distinct benefit dimensions, thresholds/update sequence, moderation abstraction, design values, and measures. Independent cross-audit additionally found that conditional findings and the unmoderated scope of calibration/validation were missing; these are now stated, with moderation contrasts identified as virtual experiments.[^r15]
- A further independent check found the tie-strengthening rule, baseline reply weights, and reply-topic choice compressed. These mechanisms are now stated;[^r13]
- Re-audit found the run replication and reporting basis missing; the experiment paragraph now states both simulations per condition and which run supplies the reported results.[^r12]
- Independent final re-audit passed: the model mechanisms, experiment conditions, 365-day replication basis, reported outcome source, and calibration/validation scope are supported by the cited sections.[^r10][^r11][^r12][^r13]

## LLM Justification
[^r1]: Ren & Kraut, “Agent-Based Modeling to Inform Online Community Design,” §3.2, PDF pp. 11–12 (research questions): https://carlsonschool.umn.edu/sites/carlsonschool.umn.edu/files/2018-10/RenKraut-HCI2014-AgentBasedModel.pdf
[^r2]: Ibid., §4.1–4.2, PDF pp. 12–19 (benefits, costs, motivation, reading/posting decisions, topics, replies, entry/exit).
[^r3]: Ibid., §5.1–5.2, PDF pp. 21–28 (virtual experimental design and outcomes); §4.3, PDF pp. 19–20 (implementation/calibration).
[^r4]: Ibid., §1, PDF pp. 4–5, and §6.4, PDF pp. 33–34 (scope and limitations).
[^r10]: Ren & Kraut, “Agent-Based Modeling to Inform Online Community Design,” §§4.1–4.2, PDF pp. 12–20 (benefit and cost categories, weights, motivation/decisions, reading, reply selection, entry/inactivity); source URL above.
[^r11]: Ibid., §3.1, PDF p. 10 and §§4.3, 5.1, PDF pp. 20–23 (moderation scope, staged update, initial conditions, horizon, recommendation accuracy); source URL above.
[^r12]: Ibid., §§4.3, 5.1–5.5, PDF pp. 20–28 (calibration/validation, factor levels and measured outcomes); source URL above.
[^r13]: Ibid., §4.1, PDF pp. 16–17 and Table 3 (interpersonal tie change and diminishing bond benefit); §4.2, PDF pp. 19–20 (reply selection weights, sensitivity variation, and reply topic); source URL above.
[^r15]: Audit log basis: source §§3.1, 4.1–4.3, 5.1–5.5, PDF pp. 10–28; source URL above.
