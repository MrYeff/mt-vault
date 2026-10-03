---
title: "Exploring Trade-Offs for Online Mental Health Matching: Agent-Based Modeling Study"
tags:
  - model
  - simulation
authors:
  - "[[Literature/Authors/Yuhan Liu|Yuhan Liu]]"
  - "[[Literature/Authors/Anna Fang|Anna Fang]]"
  - "[[Literature/Authors/Glen Moriarty|Glen Moriarty]]"
  - "[[Literature/Authors/Cristopher Firman|Cristopher Firman]]"
  - "[[Literature/Authors/Robert E. Kraut|Robert E. Kraut]]"
  - "[[Literature/Authors/Haiyi Zhu|Haiyi Zhu]]"
publication date: 2024-10-01
source: https://formative.jmir.org/2024/1/e58241/PDF
doi: 10.2196/58241
read status: Todo
⚠️: []
---

## Abstract

BACKGROUND: Online mental health communities (OMHCs) are an effective and accessible channel to give and receive social support for individuals with mental and emotional issues. However, a key challenge on these platforms is finding suitable partners to interact with given that mechanisms to match users are currently underdeveloped or highly naive. OBJECTIVE: In this study, we collaborated with one of the world's largest OMHCs; our contribution is to show the application of agent-based modeling for the design of online community matching algorithms. We developed an agent-based simulation framework and showcased how it can uncover trade-offs in different matching algorithms between people seeking support and volunteer counselors. METHODS: We used a comprehensive data set spanning January 2020 to April 2022 to create a simulation framework based on agent-based modeling that replicates the current matching mechanisms of our research site. After validating the accuracy of this simulated replication, we used this simulation framework as a "sandbox" to test different matching algorithms based on the deferred acceptance algorithm. We compared trade-offs among these different matching algorithms based on various metrics of interest, such as chat ratings and matching success rates. RESULTS: Our study suggests that various tensions emerge through different algorithmic choices for these communities. For example, our simulation uncovered that increased waiting time for support seekers was an inherent consequence on these sites when intelligent matching was used to find more suitable matches. Our simulation also verified some intuitive effects, such as that the greatest number of support seeker-counselor matches occurred using a "first come, first served" protocol, whereas relatively fewer matches occurred using a "last come, first served" protocol. We also discuss practical findings regarding matching for vulnerable versus overall populations. Results by demographic group revealed disparities-underaged and gender minority groups had lower average chat ratings and higher blocking rates on the site when compared to their majority counterparts, indicating the potential benefits of algorithmically matching them. We found that some protocols, such as a "filter"-based approach that matched vulnerable support seekers only with a counselor of their same demographic, led to improvements for these groups but resulted in lower satisfaction (-12%) among the overall population. However, this trade-off between minority and majority groups was not observed when using "topic" as a matching criterion. Topic-based matching actually outperformed the filter-based protocol among underaged people and led to significant improvements over the status quo among all minority and majority groups-specifically, a 6% average chat rating improvement and a decrease in blocking incidents from 5.86% to 4.26%. CONCLUSIONS: Agent-based modeling can reveal significant design considerations in the OMHC context, including trade-offs in various outcome metrics and the potential benefits of algorithmic matching for marginalized communities.[^r1]

## Research Questions
> Research Questions extracted via LLM

- How do alternative matching algorithms trade off matching success, waiting time, and conversation outcomes in the studied online mental-health community?[^r1]
- How do matching-policy outcomes differ for vulnerable user groups and the overall population?[^r2]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?

- The agent-based simulation represents support seekers and volunteer counselors on the collaborating peer-support platform, using chat logs and user data from January 2020 through April 2022.[^r1]
- It first reproduces the site's existing queue-based matching process, validates that replication against observed platform distributions, then tests alternative policies in the validated simulation.[^r1]

### How does it work?

- Each simulation period is one minute.[^r3]
- New support-seeker and counselor agents are generated from observed minute-by-minute arrival patterns and assigned observed gender, birth-year, and topic distributions; seekers receive an empirical patience limit, and matched chats receive an empirically distributed duration.[^r3]
- Online, non-chatting agents can be matched.[^r3]
- In the status-quo replication, counselors choose randomly from the live queue, with decision time modeled by an exponential distribution (λ=1.25).[^r3]
- Unmatched seekers wait into the next period and leave when their patience limit is exceeded, while matched agents are offline for the chat duration.[^r3]

- For alternative policies, support seekers propose in preference order; counselors hold preferred applications and reject the rest until no further rejections occur.[^r4][^r5][^r6]
- Counselors follow policy recommendations 90% of the time and select randomly 10% of the time.[^r4][^r5][^r6]
- The seven policies are first-come-first-served, last-come-first-served, similarity, gender, age, topic, and filter-based matching (the latter protects teenagers and gender-minority seekers).[^r4][^r5][^r6]
- Random-forest predictors use seeker/counselor gender, birth year, and topic: rating prediction reaches 0.72 accuracy and F1, while blocking prediction reaches 0.91 accuracy and F1; rating training uses an 80/20 split and SMOTE balancing.[^r4][^r5][^r6]
- The authors compare real and simulated outcome distributions (Pearson r=.99 for ratings, .949 for blocking).[^r4][^r5][^r6]
- The simulation permits one chat per agent, while the live site allows counselors multiple chats, likely contributing to the status-quo matching-rate gap (78.35% in simulation versus 83.27% in site data).[^r4][^r5][^r6]
- They evaluate predicted rating, blocked-pair percentage, match success, and waiting time.[^r4][^r5][^r6]

### What can it answer?

- Within the site data and model assumptions, the simulation estimates trade-offs between matching outcomes for the overall population and demographic subgroups.[^r2]
- The authors report topic-based matching improved average chat ratings and reduced blocking relative to the replicated status quo, while results remain estimates from this platform-specific model.[^r2]

### Where does it apply?

- The study is about matching in the collaborating peer-support platform.[^r1]
- Its outcomes are predictions from this platform-specific simulation and classifiers; they do not by themselves establish effects on long-term friendship or other community settings.[^r1]

## Metadata
### References

> ⚠️ Bibliography needs reconciliation: the note has 56 links, including 11 unresolved identifiers, while the primary article has 51 numbered references.

- "[[NeuroticAndPsychoticLanguageBehaviour]]"
- "[[HandbookOfGameTheoryWithEconomicApplications]]"
- "[[AReviewOfTherapistCharacteristicsAndTechniquesPositivelyImpactingTheTherapeuticAlliance]]"
- "[[AcceptanceAndCommitmentTherapyForSelfStigmaAroundSexualOrientationAMultipleBaselineEvaluation]]"
- "[[TheMentalHealthOfMultiethnicLesbianAndBisexualAdolescentFemalesTheRoleOfSelfEfficacyStressAndBehavioralRisks]]"
- "[[PsychotherapyFactorsAssociatedWithTheRaceOfTheTherapist]]"
- "[[CultureAndSocialSupport]]"
- "[[ResearchOnClientExperiencesOfTherapyIntroductionToTheSpecialSection]]"
- "[[MentalHealthServicesForYoungPeopleMatchingTheServiceToTheNeed]]"
- "[[Agent-Based Modeling to Inform Online Community Design- Impact of Topical Breadth- Message Volume- and Discussion Moderation on Member Commitment and Contribution]]"
- "[[PeerSupportAndYoungPeopleSHealth]]"
- "[[ParticipantsExperiencesOfBeingInterviewedAboutAnEmotiveTopic]]"
- "[[PsychotherapeuticServicesForEthnicMinoritiesTwoDecadesOfResearchFindings]]"
- "[[SexMakesADifferenceHowGenderAffectsTheTherapeuticRelationship]]"
- "[[PearsonSCorrelationCoefficient]]"
- "[[AgentBasedModellingOfExcitationPropagationInSocialMediaGroups]]"
- "[[TheBostonPublicSchoolMatch]]"
- "[[SmoteSyntheticMinorityOverSamplingTechnique]]"
- "[[TheNewYorkCityHighSchoolMatch]]"
- "[[StigmaMentalHealthAndResilienceInAnOnlineSampleOfTheUsTransgenderPopulation]]"
- "[[MentalHealthDiscourseOnRedditSelfDisclosureSocialSupportAndAnonymity]]"
- "[[TheFutureOfMentalHealthCarePeerToPeerSupportAndSocialMedia]]"
- "[[OnlinePeerToPeerSupportInYouthMentalHealthSeizingTheOpportunity]]"
- "[[UnresolvedReference7E79237D91744B28]]"
- "[[TheGrowthOfPeerSupportAnInternationalCharter]]"
- "[[IdentityVictimizationAndSupportFacebookExperiencesAndMentalHealthAmongLgbtqYouth]]"
- "[[InvestigatingSupportSeekingFromPeersForPregnancyInOnlineHealthCommunities]]"
- "[[SocialMediaRecommenderSystemsReviewAndOpenResearchIssues]]"
- "[[TransparentToWhomNoAlgorithmicAccountabilityWithoutACriticalAudience]]"
- "[[UserAttitudesTowardsAlgorithmicOpacityAndTransparencyInOnlineReviewingPlatforms]]"
- "[[ThroughTheLookingGlass]]"
- "[[OnlineTransgenderHealthInformationSeekingFacilitatorsBarriersAndFutureDirections]]"
- "[[OnlineMentalHealthCommunitiesSelfEfficacyAndTransitionToFurtherSupport]]"
- "[[FutureDirectionsInUnderstandingAndAddressingMentalHealthAmongLgbtqYouth]]"
- "[[UnresolvedReferenceB2CF0723B430BCD0]]"
- "[[OnlinePeerToPeerSupportQualitativeAnalysisOfUkAndUsOpenMentalHealthFacebookGroups]]"
- "[[ConsiderationsInDesigningDigitalPeerSupportForMentalHealthInterviewStudyAmongUsersOfADigitalSupportSystemBuddyProject]]"
- "[[SchedulingHomogeneousImpatientCustomers]]"
- "[[TheRedesignOfTheMatchingMarketForAmericanPhysiciansSomeEngineeringAspectsOfEconomicDesign]]"
- "[[BuildingSuccessfulOnlineCommunities]]"
- "[[CounselingAndPsychotherapyWithAsianAmericansReviewOfTheLiterature]]"
- "[[CulturalMistrustAnImportantPsychologicalConstructForDiagnosisAndTreatmentOfAfricanAmericans]]"
- "[[BehaviorModificationInBlackPopulations]]"
- "[[EthnicMinoritiesRatingsOfEthnicallySimilarAndEuropeanAmericanCounselorsAMetaAnalysis]]"
- "[[MatchingForPeerSupportExploringAlgorithmicMatchingForOnlineMentalHealthCommunities]]"
- "[[MetricsForPeerCounselingTriangulatingSuccessOutcomesForOnlineTherapyPlatforms]]"
- "[[UnresolvedReferenceF5D42D6737F78829]]"
- "[[UnresolvedReference4245EEAD6A1F3B00]]"
- "[[UnresolvedReference72AEB21D48AC978D]]"
- "[[UnresolvedReference86A049E07F67A29F]]"
- "[[UnresolvedReferenceF9BFC41EBE6DAFC9]]"
- "[[UnresolvedReferenceC6D5442E7EE54572]]"
- "[[UnresolvedReferenceD8B87B9570DF3213]]"
- "[[InformationSystemsResearch]]"
- "[[UnresolvedReferenceEBBB1D6AF44326DB]]"
- "[[UnresolvedReferenceAC0CB290F7E4BE66]]"


## Audit Log
- 2026-09-29 initial independent audit failed: publication date was incorrect and the model summary omitted one-minute scheduling, agent generation/attributes, patience and chat dynamics, the deferred-acceptance update loop, policy set, and prediction/validation mechanics. Corrected the date and added these rules with publisher-PDF section/page footnotes. Status remains `not audited` pending independent re-audit.
- 2026-09-29 independent re-audit found that the baseline queue rule, recommendation randomization, outcome predictors, validation results, and one-chat-per-agent discrepancy remained underspecified. Added the source-backed mechanics, predictor/validation metrics, and page-specific footnotes; references and order were not changed. Awaiting final audit.
- Independent final check passed. A further check against the publisher PDF clarified that chat duration is assigned when a pair matches, rather than to a counselor at arrival.

- Independent final check passed after correction; bibliography mapping remains unverified as stated above.

## LLM Justification
[^r1]: Liu et al., “Methods,” “Simulation Framework,” and “Matching Policies” (publisher PDF pp. 2–10): describes the Jan 2020–Apr 2022 platform data, replication/validation, deferred-acceptance policies, and measured outcomes. https://formative.jmir.org/2024/1/e58241/PDF
[^r2]: Liu et al., “Results” and “Discussion” (publisher PDF pp. 10–14): reports subgroup comparisons and the topic-based policy results against the replication protocol. https://formative.jmir.org/2024/1/e58241/PDF
[^r3]: Liu et al., “Simulation Period,” “Generation of Agents,” “Patience Level,” “Chat Length,” and “Matching Support Seekers and Volunteer Counselors” (publisher PDF pp. 4-6): specifies one-minute steps, empirical arrival/attribute distributions, seeker patience/cancellation, counselor chat duration, and queue availability/selection. https://formative.jmir.org/2024/1/e58241/PDF
[^r4]: Liu et al., “Applicant-Proposing Deferred Acceptance Algorithm,” “Matching Algorithms,” “Building an Agent-Based Simulation: Prediction Models,” and “Validation of the Agent-Based Simulation” (publisher PDF pp. 7-10): defines the proposal/hold/reject loop, seven policies, pair-outcome predictors, validation approach, and reported metrics. https://formative.jmir.org/2024/1/e58241/PDF
[^r5]: Liu et al., “Building an Agent-Based Simulation: Prediction Models” and “Validation of the Agent-Based Simulation” (publisher PDF pp. 6-8): specifies rating/blocking random-forest predictors, training/SMOTE details, Pearson correlations, and one-chat-per-agent limitation explaining the lower simulation match rate. https://formative.jmir.org/2024/1/e58241/PDF
[^r6]: Liu et al., “Matching Algorithms—Overview” (publisher PDF p. 9): each counselor has a 90% chance of taking a policy recommendation and a 10% chance of random selection. https://formative.jmir.org/2024/1/e58241/PDF
