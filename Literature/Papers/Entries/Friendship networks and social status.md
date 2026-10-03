---

title: "Friendship networks and social status"
tags: [model, social_networks, status]
authors:
  - "[[Literature/Authors/Brian Ball|Brian Ball]]"
  - "[[Literature/Authors/Mark E. J. Newman|Mark E. J. Newman]]"
publication date: 2013-04-15
source: https://doi.org/10.1017/nws.2012.4
doi: 10.1017/nws.2012.4
read status: Todo
⚠️: []
---

## Abstract

In empirical studies of friendship networks, participants are typically asked, in interviews or questionnaires, to identify some or all of their close friends, resulting in a directed network in which friendships can, and often do, run in only one direction between a pair of individuals. Here we analyze a large collection of such networks representing friendships among students at US high and junior-high schools and show that the pattern of unreciprocated friendships is far from random. In every network, without exception, we find that there exists a ranking of participants, from low to high, such that almost all unreciprocated friendships consist of a lower-ranked individual claiming friendship with a higher-ranked one. We present a maximum-likelihood method for deducing such rankings from observed network data and conjecture that the rankings produced reflect a measure of social status. We note in particular that reciprocated and unreciprocated friendships obey different statistics, suggesting different formation processes, and that rankings are correlated with other characteristics of the participants that are traditionally associated with status, such as age and overall popularity as measured by total number of friends.[^r1]

## Research Questions
> Research Questions extracted via LLM
- Do unreciprocated friendship nominations consistently run from lower-ranked to higher-ranked students, and can a likelihood model infer this ordering?[^r2]
- Do reciprocal and one-way ties follow distinct rank-distance patterns, and how do inferred ranks relate to age and popularity?[^r2]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?
- A directed nomination network with latent individual ranks. It treats reciprocated dyads as an undirected process and unreciprocated dyads as a directed process; this is a statistical inference model, not an agent simulation.[^r3]

### How does it work?
- For ranks r_i and r_j, the expected rate of a mutual edge is α(r_i−r_j), constrained symmetric; the expected rate of a one-way edge j→i is β(r_i−r_j), which need not be symmetric. The model assumes both tie rates depend only on rank difference, allowing mutual and one-way ties to have distinct patterns. Self-ties are excluded and the prior over rankings is uniform.[^r3]
- The authors fit ranks and α/β by maximum likelihood with EM: given current α/β, estimate the posterior over rankings q(R) and expected dyad counts by rank difference; then maximize the expected log-likelihood for new α/β and repeat to convergence. Because summing over rankings is intractable, MCMC samples rankings from q(R); reported rank estimates summarize these posterior samples.[^r4]

### What can it answer?
- Across 84 AddHealth school networks covering over 90,000 students, minimum-violations rankings place 98% of one-way nominations from lower to higher rank. The inferred ranks are positively associated with age/grade and total popularity; interpreting them as social status remains the authors’ conjecture.[^r5]

### Where does it apply?
- Directed school friendship nominations. Rank differences and edge direction are statistical patterns in observed networks; they do not identify a causal social-status process.[^r6]

## Metadata
### References
- [[TheStructureOfPositiveInterpersonalRelationsInSmallGroups]]
- [[SocialNetworkAnalysis]]
- [[TheLinearOrderingProblemAlgorithmsAndApplications]]
- [[TheBowlChampionshipSeriesAMathematicalReview]]
- [[StochasticBlockmodelsForDirectedGraphs]]
- [[TheAdolescentSocietyTheSocialLifeOfTheTeenagerAndItsImpactOnEducation]]
- [[SurveyOfTheMajorWorldSportsRatingSystems]]
- [[ASurveyOfStatisticalNetworkModels]]
- [[AStochasticModelForChangeInGroupStructure]]
- [[AStudyOfALargeSociogram]]
- [[UnresolvedReference0C3E39105B9A9276]]
- [[PseudolikelihoodEstimationForSocialNetworks]]
- [[AnExponentialFamilyOfProbabilityDistributionsForDirectedGraphs]]
- [[LogitModelsAndLogisticRegressionsForSocialNetworksIAnIntroductionToMarkovGraphsAndP]]
- [[TheConceptAndDefinitionOfDominanceInAnimalBehaviour]]
- [[OnTheMinimumViolationsRankingOfATournament]]
- [[StatisticalModelsForSocialNetworks]]
- [[StochasticBlockmodelsAndCommunityStructureInNetworks]]
- [[SymmetricAcyclicDecompositionsOfNetworks]]
- [[FindingADominanceOrderMostConsistentWithALinearHierarchyANewProcedureAndReview]]
- [[BaskingInReflectedGloryAndItsLimitsWhyAdolescentsHangOutWithPopularPeers]]
- [[KnowingYourPlaceSelfPerceptionsOfStatusInFaceToFaceGroups]]
- [[TheEffectsOfIndividualAndStructuralCharacteristicsOnIntransitivityInSocialNetworks]]
- [[ConfidenceSetsForNetworkStructure]]
- [[UnresolvedReference80049AFB6A4451FB]]
- [[AnnualReviewOfSociologyVol37]]
- [[UnresolvedReference6BA987826CEA5FFF]]
- [[UnresolvedReferenceCD584BC8D20AFCF9]]
- [[UnresolvedReference1C0695551EB994F5]]
- [[UnresolvedReferenceE1A8D0EB0160E492]]
- [[TheHumanGroup]]


Reference list preserved from the prior note in original order; bibliography completeness has not been checked against the primary source.

## Audit Log
- Initial independent audit found the statistical model too generic to reproduce and its empirical scale/results omitted. Added separate reciprocal/unreciprocated dyad processes α/β, rank-difference dependence, uniform rank prior/no self-ties, EM plus MCMC estimation, and the AddHealth scale and principal findings.[^r3][^r4][^r5]

## LLM Justification
[^r1]: Ball and Newman, Cambridge Core abstract, https://www.cambridge.org/core/journals/network-science/article/abs/friendship-networks-and-social-status/18CD7D21D1A2852C27C74374BAF22432.
[^r2]: Ball and Newman, author preprint, Abstract and Introduction, https://arxiv.org/pdf/1205.6822.
[^r3]: Ball and Newman, author preprint, “Inference of rank from network structure,” pp. 2–3, Eqs. (1)–(11).
[^r4]: Ball and Newman, author preprint, EM fitting and MCMC approximation, pp. 3–4, Eqs. (2)–(11).
[^r5]: Ball and Newman, author preprint, Results, pp. 4–6.
[^r6]: Ball and Newman, author preprint, Introduction and Conclusion, pp. 1 and 6.
