---

title: "Individual Motivations and Network Effects: A Multilevel Analysis of the Structure of Online Social Relationships"
tags:
  - empirical
  - social_networks
authors:
  - "[[Literature/Authors/Brooke Foucault Welles|Brooke Foucault Welles]]"
  - "[[Literature/Authors/Noshir Contractor|Noshir Contractor]]"
publication date: 2015-04-09
source:
  - https://doi.org/10.1177/0002716214565755
doi: 10.1177/0002716214565755
read status: Todo
⚠️: []
---
## Abstract

This article explores the relative influence of individual and network-level effects on the emergence of online social relationships. Using network modeling and data drawn from logs of social behavior inside the virtual world Second Life, we combine individual- and network-level theories into an integrated model of online social relationship formation. Results reveal that time spent online and the network pressure toward balance (individuals tending to form relationships with others who have relationships in common) predict the emergence of online relationship ties, while gender, age, proximity, homophily (the tendency of individuals to form relationships among people with similar traits), and preferential attachment are not significant predictors within the observed networks. We discuss these results in light of existing research on online social relationships and describe how digital data and network analytics enable novel insights about the emergence of online social relationships.[^r0]

## Research Questions
> Research questions distilled from the primary paper; phrasing is paraphrased.[^r0]
- How do individual motivations and network-level effects jointly relate to online relationship ties in Second Life?[^r0]
- Which individual and structural predictors are significant in the observed network?[^r0]

## Model
> Model extracted via LLM according to [[Model Notation]].

> This is an empirical network modeling study rather than an agent-based simulation. It estimates tie formation from Second Life behavioral logs; it specifies no agents’ decision or temporal update schedule.[^r1]

- The study samples 20 Second Life groups and fits a separate exponential random graph model (p*/ERGM) to each group network, then combines coefficients with weighted least squares.[^r1]
- It estimates association between tie presence and individual-level predictors (time online, gender, age, physical proximity, homophily) alongside structural terms: balance via geometrically weighted edgewise shared partners (GWESP), and preferential attachment.[^r1]
- Time online and balance are significant; the others are not.[^r1]
- This is cross-sectional statistical network modeling: the paper specifies no agent choices, temporal update sequence, or tie-formation process to run forward.[^r1]

## Metadata
### References
Bibliography completeness not verified; the following preserves the originally captured reference links in their original order.

- [[ExaminingTheoriesOfAdolescentFriendships]]
- [[TheOriginsOfStatusHierarchiesAFormalTheoryAndEmpiricalTest]]
- [[TheoriesOfCommunicationNetworks]]
- [[StatisticalAnalysisOfFriendshipPatternsAndBullyingBehaviorsAmongYouth]]
- [[NetworksAndOrganizationsStructureFormAndAction]]
- [[ThePsychologyOfInterpersonalRelations]]
- [[ExponentialRandomGraphPModelsAsAMethodForSocialNetworkAnalysisInCommunicationResearch]]
- [[MakingFriendsInCyberspace]]
- [[AdolescentsAndEmergingAdultsSocialNetworkingOnlineHomophilyOrDiversity]]
- [[EmpiricalAnalysisOfAnEvolvingSocialNetwork]]
- [[ModelingSocialNetworksFromSampledData]]
- [[ProximityAndPeershipBasesOfBalanceInInterpersonalAttraction]]
- [[DevelopingAModelOfAdolescentFriendshipFormationOnTheInternet]]
- [[8SocialHierarchyTheSelfReinforcingNatureOfPowerAndStatus]]
- [[SocialImplicationsOfTheInternet]]
- [[VirtuallyThereExploringProximityAndHomophilyInAVirtualWorld]]
- [[TheMappingPrincipleAndAResearchFrameworkForVirtualWorlds]]
- [[AStatnetTutorial]]
- [[CommunicationNetworksInTaskPerformingGroups]]
- [[Birds of a Feather- Homophily in Social Networks]]
- [[NewSpecificationsForExponentialRandomGraphModels]]
- [[DynamicsOfDyadsInSocialNetworksAssortativeRelationalAndProximityMechanisms]]
- [[TheSocialBehaviorsOfExpertsInMassiveMultiplayerOnlineRolePlayingGames]]
- [[CurvedExponentialFamilyModelsForSocialNetworks]]
- [[ErgmAPackageToFitSimulateAndDiagnoseExponentialFamilyModelsForNetworks]]
- [[SimilarityAndTheQualityOfOnlineAndOfflineSocialRelationshipsAmongAdolescentsInIsrael]]
- [[AMultilevelNetworkStudyOfTheEffectsOfDelinquentBehaviorOnFriendshipEvolution]]
- [[8DynamicNetworksAndBehaviorSeparatingSelectionFromInfluence]]
- [[BowlingAloneAmericaSDecliningSocialCapital]]
- [[AnIntroductionToExponentialRandomGraphPModelsForSocialNetworks]]
- [[TheDynamicsOfOrganizationalProximity]]
- [[TestingMultitheoreticalMultilevelHypothesesAboutOrganizationalNetworksAnAnalyticFrameworkAndEmpiricalExample]]
- [[TheStrengthOfStrongTiesTheImportanceOfPhilosInOrganizations]]
- [[Astatnettutorial]]
- [[SecondLifeTheSecondLifeOfVirtualReality]]
- [[ModelingSocialNetworksWithSampledData]]

## Audit Log
- Initial audit found an incomplete model account. The corrected note describes separate ERGMs for 20 groups, weighted coefficient aggregation, and GWESP; the final independent re-audit passed. The 36 legacy reference links retain their original order; bibliography completeness remains unverified. See `vault/.automation/audit/next-fifteen-31-35-correction-reaudit-2026-09-30.json`.[^r3]

## LLM Justification
[^r0]: Abstract copied verbatim from the primary publication record/full text. Research questions are concise paraphrases of the paper’s stated aims/questions. Bibliography links retained in source order from vault/.automation/import/next-fifteen-original-2026-09-30.json.
[^r1]: Foucault Welles & Contractor, “Individual Motivations and Network Effects,” data, p*/ERGM specification, and results on printed pp. 181–187; publisher abstract also states the predictor results. https://doi.org/10.1177/0002716214565755
[^r3]: Process log based on the initial audit record; this is a record of corrections, not an independent re-audit.
