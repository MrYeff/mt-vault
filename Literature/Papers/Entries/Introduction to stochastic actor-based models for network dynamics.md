---

title: "Introduction to stochastic actor-based models for network dynamics"
tags:
  - model
authors:
  - "[[Literature/Authors/Tom A. B. Snijders|Tom A. B. Snijders]]"
  - "[[Literature/Authors/Gerhard G. van de Bunt|Gerhard G. van de Bunt]]"
  - "[[Literature/Authors/Christian Steglich|Christian Steglich]]"
publication date: "2010"
source:
  - https://doi.org/10.1016/j.socnet.2009.02.004
  - https://www.stats.ox.ac.uk/~snijders/SnijdersSteglichVdBunt2009.pdf
doi: "10.1016/j.socnet.2009.02.004"
read status: Todo
⚠️: []
---
## Abstract

Stochastic actor-based models are models for network dynamics that can represent a wide variety of influences on network change, and allow to estimate parameters expressing such influences, and test corresponding hypotheses. The nodes in the network represent social actors, and the collection of ties represents a social relation. The assumptions posit that the network evolves as a stochastic process ‘driven by the actors’, i.e., the model lends itself especially for representing theories about how actors change their outgoing ties. The probabilities of tie changes are in part endogenously determined, i.e., as a function of the current network structure itself, and in part exogenously, as a function of characteristics of the nodes (‘actor covariates’) and of characteristics of pairs of nodes (‘dyadic covariates’). In an extended form, stochastic actor-based models can be used to analyze longitudinal data on social networks jointly with changing attributes of the actors: dynamics of networks and behavior. This paper gives an introduction to stochastic actor-based models for dynamics of directed networks, using only a minimum of mathematics. The focus is on understanding the basic principles of the model, understanding the results, and on sensible rules for model selection.[^r1]

## Research Questions
> Research Questions extracted via LLM

- How can directed social network change between observed waves be represented and statistically estimated using an actor-based stochastic process?[^r2]
- Which structural, actor and dyadic tendencies help account for observed tie changes, and do co-evolving actor attributes help distinguish selection from influence?[^r2]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?
A statistical actor-driven model of directed tie and optionally ordinal behavior change between observed network waves, intended to test hypotheses and estimate parameters from longitudinal data; it is not this paper’s single empirical simulation study.[^r3]

### How does it work?
- **State:** binary directed ties; the joint extension includes actor behavior on a discrete ordinal scale. The process is continuous-time and Markovian, with observations at discrete waves; estimates condition on the first wave.[^r3]
- **Opportunity rates:** Actor change opportunities follow stochastic rate processes whose actor-specific rates may depend on network position (such as centrality) and actor covariates (such as age or sex).[^r3]
- **Tie choice:** At a tie opportunity, a focal sender is selected, then may toggle one outgoing tie or keep the status quo.[^r3]
- Actor choice probabilities depend on an objective function, expressed as a weighted sum of network/covariate effects.[^r3]
- The paper’s basic account assumes the actor has full information but the specified objective can require only a personal network.[^r3]
- **Joint behavior extension:** at a behavior opportunity, one actor changes behavior one scale step up/down or stays; network and behavior changes have distinct opportunity and choice processes, with no simultaneous coordinated change.[^r3]
- Effects, rate functions and parameter values are chosen for the research question and estimated from the data; the article provides examples rather than one universal parameterization. Simplification here omits the estimation algorithm, effect-specific equations and diagnostic/model selection rules.[^r3]

### What can it answer?
It can test modeled tendencies such as reciprocity, transitivity and homophily, and in the joint extension examine whether network selection or behavior influence accounts for similarity among connected actors, conditional on specified effects and model fit.[^r3]

### Where does it apply?
- It is suited to longitudinal relations treated as durable states (for example friendship, trust or cooperation).[^r3]
- Event data such as calls are not automatically durable ties; the discussion allows event intensity to be aggregated over an interval and used as a state indicator when that operationalization is appropriate.[^r3]

## Metadata
### References
- [[TowardAStructuralTheoryOfAction]]
- [[EssaysOnBayesianInferenceForSocialNetworks]]
- [[DissectingTheSocialOnThePrinciplesOfAnalyticalSociology]]
- [[ModelsForLongitudinalNetworkData]]
- [[FriendshipSelectionAndFriendsInfluenceDynamicsOfNetworksAndActorAttributesInEarlyAdolescence]]
- [[ConditionalLogitAnalysisOfQualitativeChoiceBehavior]]
- [[ModelsAndMethodsInSocialNetworkAnalysis]]
- [[MarkovChainMonteCarloEstimationOfExponentialRandomGraphModels]]
- [[LongitudinalModelsInTheBehavioralAndRelatedSciences]]
- [[LAnalyseLongitudinaleDeReseauxSociauxTotauxAvecSienaMethodeDiscussionEtApplication]]
- [[StochasticActorOrientedModelsForNetworkChange]]
- [[TheConceptOfConfigurationOfInterpersonalRelationsInAGroupAsATimeDependentStochasticProcess]]
- [[BayesianInferenceForDynamicSocialNetworkData]]
- [[StatisticalAnalysisOfLongitudinalNetworkDataWithChangingComposition]]
- [[TheRiseAndFallOfANetworkedSocietyAFormalModel]]
- [[ADynamicModelOfSocialNetworkFormation]]
- [[AStructuralTheoryOfSocialInfluence]]
- [[ModelsForNetworkDynamicsAMarkovianFramework]]
- [[MeetingStrangersAndFriendsOfFriendsHowRandomAreSocialNetworks]]
- [[CategoricalDataAnalysis]]
- [[EmergenceOfScalingInRandomNetworks]]
- [[RegressionModelsForCategoricalAndLimitedDependentVariables]]
- [[ADynamicModelForSocialNetworks]]
- [[TheMatthewEffectInScienceTheRewardAndCommunicationSystemsOfScienceAreConsidered]]
- [[ConcurrentPartnershipsAndTransmissionDynamicsInNetworks]]
- [[AssortativeMixingInNetworks]]
- [[FrontiersInEconometrics]]
- [[EmpiricalAnalysisOfAnEvolvingSocialNetwork]]
- [[UtilityAndDynamicSocialNetworks]]
- [[SocialNetworkAnalysisMethodsAndApplications]]
- [[DelinquentPeersRevisitedDoesNetworkStructureMatter]]
- [[TreatmentOfNonResponseInLongitudinalNetworkStudies]]
- [[SequentialSocialNetworkData]]
- [[AnExponentialFamilyOfProbabilityDistributionsForDirectedGraphs]]
- [[LogitModelsAndLogisticRegressionsForSocialNetworksIAnIntroductionToMarkovGraphsAndP]]
- [[AGeneralTheoryOfBibliometricAndOtherCumulativeAdvantageProcesses]]
- [[TheAmericanCollegeAPsychologicalAndSocialInterpretationOfTheHigherLearning]]
- [[TheContributionOfInfluenceAndSelectionToAdolescentPeerGroupHomogeneityTheCaseOfAdolescentCigaretteSmoking]]
- [[LimitedDependentAndQualitativeVariablesInEconometrics]]
- [[StructureOfGrowingSocialNetworks]]
- [[AnActorOrientedDynamicNetworkApproach]]
- [[TheStatisticalEvaluationOfSocialNetworkDynamics]]
- [[ComparingResemblanceMeasures]]
- [[TakingStockOfNetworksAndOrganizationsAMultilevelPerspective]]
- [[SmokeRingsSocialNetworkAnalysisOfFriendshipGroupsSmokingAndDrugTaking]]
- [[Birds of a Feather- Homophily in Social Networks]]
- [[RecentDevelopmentsInExponentialRandomGraphPModelsForSocialNetworks]]
- [[RationalChoiceTheoryAdvocacyAndCritique]]
- [[TransitivityInStructuralModelsOfSmallGroups]]
- [[StructureAndTimeEvolutionOfAnInternetDatingCommunity]]
- [[EvolutionOfSocialNetworks]]
- [[ANoncooperativeModelOfNetworkFormation]]
- [[8DynamicNetworksAndBehaviorSeparatingSelectionFromInfluence]]
- [[TheNetworkParadigmInOrganizationalResearchAReviewAndTypology]]
- [[PartnersInPowerJobMobilityAndDynamicDealMaking]]
- [[MaximumLikelihoodEstimationForSocialNetworkDynamics]]
- [[TheChangingFaceOfMethodologicalIndividualism]]
- [[FriendshipNetworksThroughTimeAnActorOrientedDynamicStatisticalNetworkModel]]
- [[FromFactorsToActorsComputationalSociologyAndAgentBasedModeling]]
- [[BeyondDyadicInterdependenceActorOrientedModelsForCoEvolvingSocialNetworksAndIndividualBehaviors]]
- [[AStochasticModelForDirectedGraphsWithTransitionRatesDeterminedByReciprocity]]
- [[SociologicalMethodology1980]]
- [[ClusteringAndHierarchyInInterpersonalRelationsTestingTwoGraphTheoreticalModelsOn742Sociomatrices]]
- [[SociologicalMethodology1978]]
- [[StudentPeerGroupInfluence]]
- [[ManualForSienaVersion21]]
- [[ProceedingsOfTheXliiiScientificMeetingItalianStatisticalSociety]]
- [[ModelingTheCoevolutionOfNetworksAndBehavior]]
- [[StatisticalMethodsForNetworkDynamics]]
- [[GeneralizedExchange]]
- [[SociologicalMethodology1981]]
- [[UnresolvedReference6BA987826CEA5FFF]]
- [[TheMatthewEffectInScience]]
- [[UnresolvedReference56D807EE2BBE7C95]]
- [[UnresolvedReferenceE815E8B3A36EF15C]]
- [[UnresolvedReference7900CB41463C24A2]]
- [[UnresolvedReferenceC635129A2E1AB0B7]]
- [[UnresolvedReference9EFF6C34ED2723A9]]
- [[UnresolvedReferenceDE3AC01AE6C601CA]]
- [[UnresolvedReferenceBCB02E1410628742]]
- [[UnresolvedReference3A093F7D1230CD56]]
- [[UnresolvedReference4F087C88B3E0C6B0]]
- [[UnresolvedReference77D4F25245CDEA21]]
- [[UnresolvedReferenceFA44CFCF5413224D]]
- [[LAnalyseLongitudinaleDeRéseauxSociauxTotauxAvecSienaMéthodeDiscussionEtApplicationBms]]
- [[UnresolvedReferenceF463FC4F6B5F0EBD]]
- [[UnresolvedReference1106FB008600889C]]
- [[UnresolvedReference08C7247F4D0F450C]]
- [[TreatmentOfNonResponseInLongitudinalNetworkData]]
- [[ContributionsAuProblèmeDeLImmigrationPostGlaciaireDeLaFloreAlpine]]
- [[TheConfigurationOfInterpersonalRelationsInAGroupAsATimeDependentStochasticProcess]]
- [[BayesianInferenceForDynamicNetworkData]]
- [[TheMethodOfDecreasingAbstraction]]
- [[UnresolvedReference9796EE6CEFEB1225]]
- [[FromFactorsToActorsComputationalSociologyAndAgentBasedModelling]]
- [[UnresolvedReferenceB19681FB699F45FA]]
- [[AGeneralTheoryOfBibliometricAndOtherAdvantageProcesses]]
- [[UnresolvedReference74FEF378B178DB3B]]
- [[StochasticActorOrientedDynamicNetworkAnalysis]]
- [[UnresolvedReferenceEE7965E22FE52B34]]
- [[UnresolvedReference58D2E7FE4591AA3B]]
- [[AnActorOrientedDynamicNetworkApproachTheCaseOfInterorganizationalNetworkEvolution]]
- [[FriendshipNetworksThroughTimeAnActorOrientedStatisticalNetworkModel]]
- [[UnresolvedReference7956CE9ECDFEA61D]]
- [[LogitModelsAndLogisticRegressionForSocialNetworksIAnIntroductionToMarkovGraphsAndP]]

Bibliography completeness is not verified; the links above preserve the originally collected reference list in its original order, including unresolved entries. This list has not been checked against the primary paper bibliography.[^r4]

## Audit Log
Initial independent audit failed on abstract exactness and two model details. Removed the manuscript copyright footer from the abstract, added actor-specific opportunity-rate dependence on network position/covariates, and qualified event-tie aggregation as an available operationalization rather than a categorical requirement. Bibliography links and order are unchanged. Pending independent re-audit.

## LLM Justification
[^r1]: Exact abstract copied from the article abstract (p. 1); the 2009 author-manuscript footer is excluded. [Author full text](https://www.stats.ox.ac.uk/~snijders/SnijdersSteglichVdBunt2009.pdf).
[^r2]: Paraphrased from introduction (pp. 1–3) and abstract; tutorial objectives, [author full text](https://www.stats.ox.ac.uk/~snijders/SnijdersSteglichVdBunt2009.pdf).
[^r3]: Section 2.1, assumptions 5–6 (PDF pp. 6–7); Section 2.2/objective function (pp. 7–9); Section 4.1, rate functions (pp. 16–18); network-behavior extension (pp. 26–29); discussion of event data and interval aggregation (Section 2.1, pp. 4–7); [author full text](https://www.stats.ox.ac.uk/~snijders/SnijdersSteglichVdBunt2009.pdf).
[^r4]: Reference links copied in order from pre-import note metadata; article reports pp. 44–60 in Social Networks 32 (2010), DOI 10.1016/j.socnet.2009.02.004. Bibliography completeness not checked against article.
