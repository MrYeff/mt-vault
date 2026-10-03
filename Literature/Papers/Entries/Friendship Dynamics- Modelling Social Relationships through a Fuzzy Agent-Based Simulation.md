---

title: "Friendship Dynamics: Modelling Social Relationships through a Fuzzy Agent-Based Simulation"
tags: [model, simulation]
authors:
  - "[[Literature/Authors/Samer Hassan|Samer Hassan]]"
  - "[[Literature/Authors/Mauricio Salgado|Mauricio Salgado]]"
  - "[[Literature/Authors/Juán Pavón|Juan Pavón]]"
publication date: 2011-09-13
source: https://onlinelibrary.wiley.com/doi/10.1155/2011/765640
doi: 10.1155/2011/765640
read status: Todo
⚠️: []
---

## Abstract

Social relationships such as friendship and partner choice are ruled by the proximity principle, which states that the more similar two individuals are, the more likely they will become friends. However, proximity, similarity, and friendship are concepts with blurred edges and imprecise grades of membership. This study shows how to simulate these friendship dynamics in an agent-based model that applies fuzzy sets theory to implement agent attributes, rules, and social relationships, explaining the process in detail. Although in principle it may be thought that the use of fuzzy sets theory makes agent-based modelling more elaborated, in practice it saves the modeller from taking some arbitrary decisions on how to use crisp values for representing properties that are inherently fuzzy. The consequences of applying fuzzy sets and operations to define a fuzzy friendship relationship are compared with a simpler implementation, with crisp values. By integrating agent computational models and fuzzy set theory, this paper provides useful insights into scholars and practitioners to tackle the uncertainty inherent to social relationships in a systematic way.[^r1]

## Research Questions
> Research Questions extracted via LLM
- How does Mentat represent and compare fuzzy friendship dynamics with crisp friendship rules?[^r2]
- How does graded similarity affect the rate and eventual strength of friendship in the model?[^r2]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?
- Mentat represents social-value change in a population and extends its social processes with fuzzy similarity and a graded friendship-strength relation used in mate choice.[^r3]

### How does it work?
- Agents compare age, political ideology, religiosity, education, and economic status. The fuzzy variant normalizes attributes to [0,1], maps them through fuzzy membership functions, and aggregates pairwise fuzzy similarities using a T-indistinguishability relation and OWA; the reported default uses the Lukasiewicz t-norm and standard average weights.[^r4]
- Let F(t) be friendship strength, bounded by maximum K. Section 5.2 defines dF/dt = gF(t)(1−F(t)/K), with g = R_similarity × J and J = J0 exp(p × R_similarity). Thus ties strengthen logistically; they do not weaken or break once present. The authors explicitly call the logistic rule an intuition without empirical support and say tie decay/removal is omitted.[^r5]
- Figure 4 illustrates K=1, F0=0.01; Figure 5 uses p=5.8 and J0=0.001, which the authors say were obtained experimentally. These are example parameters, not a universal calibration. The model combines crisp/fuzzy similarity and crisp/fuzzy friendship in four variants, tested under random-friend and similarity-prioritizing configurations.[^r6]

### What can it answer?
- In the internal comparison, the paper's prose says MentatFuzzAll outperforms the other variants on couple similarity and friendship. Table 2 instead gives MentatFuzzAll and MentatFuzzSim the same mean couple similarity (0.77) in the random-friend configuration; crisp-friendship cases are not graded comparisons because all couples are friends. The reported ANOVAs find differences by fuzzification at p<.001. These are model comparisons, not empirical validation of the friendship law.[^r7]

### Where does it apply?
- The mechanism applies to Mentat-style simulations where friendship strength depends on similarity and accumulated time. Its monotone, non-decaying ties omit relationship dissolution and are a substantive limitation.[^r5]

## Metadata
### References
- [[LectureNotesInArtificialIntelligence]]
- [[TheRibbonOfLoveFuzzyRuledAgentsInArtificialSocieties]]
- [[FuzzySetTheoryApplicationsInTheSocialSciences]]
- [[ProbabilisticMetricSpaces]]
- [[TheOxfordHandbookOfAnalyticalSociology]]
- [[WhatDidYouSay]]
- [[MentatADataDrivenAgentBasedSimulationOfSocialValuesEvolution]]
- [[FlameFuzzyLogicAdaptiveModelOfEmotions]]
- [[FuzzyReferralBasedCooperationInSocialNetworksOfAgents]]
- [[TheFateOfSpatialDilemmasWithDifferentFuzzyMeasuresOfSuccess]]
- [[HowCanExtremismPrevailAStudyBasedOnTheRelativeAgreementInteractionModel]]
- [[ModellingTheDynamicsOfYouthSubcultures]]
- [[WeakLinksStabilizersOfComplexSystemsFromProteinsToSocialNetworks]]
- [[PromisingTheFutureVirginityPledgesAndFirstIntercourse]]
- [[MeasuringConsumerAttitudesTowardTheMarketplaceWithTailoredInterviews]]
- [[EvaluatingPerformanceAdvantagesOfGroupingGeneticAlgorithms]]
- [[NeighborhoodContextAndTheTransitionToSexualActivityAmongYoungBlackWomen]]
- [[ExplainingTheGreatReversalInSpanishAmerica]]
- [[HomophilyAndSocialDistanceInTheChoiceOfMultipleFriendsAnAnalysisBasedOnConditionallySymmetricLogBilinearAssociationModels]]
- [[NucleusAndShieldTheEvolutionOfSocialStructureInTheIteratedPrisonerSDilemma]]
- [[SimilarityRelationsAndFuzzyOrderings]]
- [[FuzzySetsAsABasisForATheoryOfPossibility]]
- [[SocialStructuralDeterminantsOfSimilarityAmongAssociates]]
- [[FamiliesOfOwaOperators]]
- [[HomophilySelectionAndSocializationInAdolescentFriendships]]
- [[BayesModalEstimationInItemResponseModels]]
- [[ContextualEffectsOnTheSexualBehaviorOfAdolescentWomen]]
- [[AnEvolutionaryApproachToNorms]]
- [[WhatDidYouSayEmergentCommunicationInAMultiAgentSpatialConfiguration]]
- [[OnTheStructureOfFIndistinguishabilityOperators]]
- [[ADecadeOfNetworkChangeTurnoverPersistenceAndStabilityInPersonalCommunities]]
- [[FreedomAndControlInModernSociety]]
- [[ModelingCivilViolenceAnAgentBasedComputationalApproach]]
- [[SocialContextsSocialNetworksAndUrbanNeighborhoodsEnvironmentalConstraintsOnFriendshipChoice]]
- [[ExperiencesCreatingThreeImplementationsOfTheRepastAgentModelingToolkit]]
- [[TheEvolutionOfFuzzyRulesAsStrategiesInTwoPlayerGames]]
- [[AgentBasedModellingAndSimulationForTheAnalysisOfSocialPatterns]]
- [[StudyingCumulativeCulturalEvolutionInTheLaboratory]]
- [[SocialCirclesASimpleStructureForAgentBasedSocialNetworkModels]]
- [[Birds of a Feather- Homophily in Social Networks]]
- [[DiscoveryAndDiffusionOfKnowledgeInAnEndogenousSocialNetwork]]
- [[TheStructureOfAdultFriendshipChoices]]
- [[ChainsOfAffectionTheStructureOfAdolescentRomanticAndSexualNetworks]]
- [[TheDisseminationOfCulture]]
- [[IntroducingUncertaintyIntoSocialSimulationUsingFuzzyLogicForAgentBasedModelling]]
- [[DeepeningTheDemographicMechanismsInADataDrivenSocialSimulationOfMoralValuesEvolution]]
- [[CommunicationsTravelAndSocialNetworksSince1840AStudyUsingAgentBasedModels]]
- [[FuzzyLogicalRulesInAMultiAgentSystem]]
- [[FuzzySetsFuzzyLogicAndFuzzySystems]]
- [[FuzzySetTheory]]
- [[SacredAndSecular]]
- [[TheContagiousnessOfDivorce]]
- [[GrowingArtificialSocieties]]
- [[FuzzySets]]
- [[AnnualReviewOfSociologyVol37]]
- [[GrowingArtificialSocietiesSocialScienceFromTheBottomUp]]
- [[FuzzySetsAndModelsOfInternationalRelations]]
- [[DifferentialEquations]]
- [[HomophilyAndSocialDistanceInTheChoiceOfMultipleFriendsAnAnalysisBasedOnConditionallySymmetricLogBilinearAssociationModel]]
- [[UnresolvedReference6BA987826CEA5FFF]]
- [[UnresolvedReference93F37583B2E377F2]]
- [[UnresolvedReferenceDC10E6E73F03587C]]
- [[MultiAgentBasedSimulationX]]
- [[UnresolvedReference17295E36319976EF]]
- [[MultiAgentBasedSimulationIx]]
- [[FuzzySetsFuzzyLogicAndFuzzySystemsSelectedPapersByLotfiAZadeh]]
- [[UnresolvedReferenceF8CEAE2CEA45B487]]


Reference list preserved from the prior note in original order; bibliography completeness has not been checked against the primary source.

## Audit Log
- Initial independent audit found unsupported claims that ties dissolve and missing friendship-growth rules/results. Corrected by removing dissolution from the research questions, stating monotone logistic growth and no tie decay/breaking, adding the reported parameters and internal variant comparison, and limiting interpretation to model comparison.[^r5][^r6][^r7]
- Corrected author display to publisher spelling Juan Pavón.[^r8]

## LLM Justification
[^r1]: Hassan et al., publisher abstract, https://onlinelibrary.wiley.com/doi/10.1155/2011/765640.
[^r2]: Hassan et al., Sections 1 and 6, https://pdfs.semanticscholar.org/2c3b/ef77179d5fdaf4faddee8a632af966cd3ab8.pdf.
[^r3]: Hassan et al., Sections 2–3, Mentat overview and fuzzy extension, same full text.
[^r4]: Hassan et al., Sections 4.1–4.2.2 and Equation (4.1), same full text.
[^r5]: Hassan et al., Section 5.2, pp. 12–13, Equations (5.1)–(5.3), same full text.
[^r6]: Hassan et al., Section 5.2, Figure 4 (K, F0), Figure 5 (p, J0), p. 13; Section 6 and Table 1, pp. 16–17, same full text.
[^r7]: Hassan et al., Section 6, Table 2 and discussion, pp. 16–17, same full text.
[^r8]: Wiley article metadata, https://onlinelibrary.wiley.com/doi/10.1155/2011/765640.
