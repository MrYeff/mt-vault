---
title: "The latent cognitive structures of social networks"
tags:
  - model
authors:
  - "[[Literature/Authors/Izabel Aguiar|Izabel Aguiar]]"
  - "[[Literature/Authors/Johan Ugander|Johan Ugander]]"
publication date: 2024-04-25
source: https://www.cambridge.org/core/journals/network-science/article/latent-cognitive-structures-of-social-networks/5C675C255AB9B9FE5A6A9F2E39E4909C
doi: 10.1017/nws.2024.7
read status: Todo
⚠️:
  - audit failed
---
## Abstract

When people are asked to recall their social networks, theoretical and empirical work tells us that they rely on shortcuts, or heuristics. Cognitive social structures (CSSs) are multilayer social networks where each layer corresponds to an individual’s perception of the network. With multiple perceptions of the same network, CSSs contain rich information about how these heuristics manifest, motivating the question, Can we identify people who share the same heuristics? In this work, we propose a method for identifying cognitive structure across multiple network perceptions, analogous to how community detection aims to identify social structure in a network. To simultaneously model the joint latent social and cognitive structure, we study CSSs as three-dimensional tensors, employing low-rank nonnegative Tucker decompositions (NNTuck) to approximate the CSS—a procedure closely related to estimating a multilayer stochastic block model (SBM) from such data. We propose the resulting latent cognitive space as an operationalization of the sociological theory of social cognition by identifying individuals who share relational schema. In addition to modeling cognitively independent, dependent, and redundant networks, we propose a specific model instance and related statistical test for testing when there is social-cognitive agreement in a network: when the social and cognitive structures are equivalent. We use our approach to analyze four different CSSs and give insights into the latent cognitive structures of those networks.

## Research Questions
> Research Questions extracted via LLM

- Can multiple perceived networks reveal shared relational schemas, latent social/cognitive structure, and social-cognitive agreement?[^r1]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?
A Poisson factor model of multiple perceptions of the same directed network: outgoing/incoming social memberships and shared cognitive schemas.[^r2]

The types and rate below summarize Eq. (1) and Definitions 1–4; memberships are nonnegative weights, not normalized probabilities.[^r2][^r3]

```yml
CSS:
  ties: [[[u32]]] # N × N × L; layer = respondent

NNTuck:
  U: [[0..]] # N × K outgoing memberships
  V: [[0..]] # N × K incoming memberships
  Y: [[0..]] # L × C cognitive memberships
  G: [[[0..]]] # K × K × C affinities
  variant: Independent | Dependent | Redundant | Agreement
```

### How does it work?
The model rate and agreement-fitting order are specified below. Algorithm 1's tensor multiplicative formulas are omitted; the block states the objective and the additional constraints/order defining Algorithm 2.[^r2][^r3][^r5]

```
RESTARTS_STANDARD = 20
RESTARTS_AGREEMENT = 50
CV_MASKS = 5

rate(m: NNTuck, i: u32, j: u32, l: u32) -> 0..:
  out = sum(a,b,c: m.U[i,a] * m.V[j,b] * m.Y[l,c] * m.G[a,b,c])
  # CSS.ties[i,j,l] ~ Poisson(out)

fit_agreement(css: CSS) -> NNTuck:
  initialize nonnegative Y, V, G; U = Y; K = C < L
  repeat Algorithm 2 termination criterion:
    multiplicatively update V, then U, then Y (Algorithm 1)
    U = Y = (U + Y) / 2
    multiplicatively update G (Algorithm 1)
    retain iterate with lowest KL(css, rate)
  out = best retained iterate across RESTARTS_AGREEMENT starts
```

- `Independent`: `C=L`, `Y=I`; `Dependent`: `C<L`, free `Y`; `Redundant`: `C=1`, `Y=ones`; `Agreement`: `K=C<L`, `U=Y`. Standard fitting maximizes Poisson likelihood (equivalently minimizes KL divergence), keeping fixed factors fixed.[^r2][^r3]
- Algorithm 1 converges monotonically to a local optimum; Algorithm 2's averaging is heuristic, nonmonotone and has no convergence guarantee. Multiple starts provide no certificate of a global maximum.[^r5]
- Ordinary Wilks LRT validity fails because NNTuck is nonidentifiable and global maximum-likelihood fits are not assured.[^r6]
- The paper uses randomly split data with split-LRT, which does not require identifiability or nestedness.[^r6]
- It is lower-powered, its split may be suboptimal, and it still requires a maximized null likelihood; agreement-test conclusions therefore require particular caution.[^r6]
- The paper does not specify a complete tensor-splitting implementation here.[^r6]
- Five train/test masks and best-of-20 fitting select dimensions by average test AUC; split-LRT compares redundancy against `C=2`, dependence against independence and agreement against a sufficiently large dependent alternative; final factors are visualized and interpreted.[^r4][^r6]

### What can it answer?
It identifies respondents whose perceived networks share a generative schema and evaluates social–cognitive agreement in four CSS datasets. Schemas are interpreted after fitting; the factorization does not directly name their cognitive content.[^r4]

### Where does it apply?
It applies to multilayer perceptions over common nodes, with CSS normally having one respondent per layer (`L=N`); its block-model structure may miss schemas such as triadic closure.[^r2][^r4]

## Metadata
### References

- [[StructuralLeverageInMarketing]]
- [[SocialNetworkAnalysis]]
- [[ClusteringNetworkLayersWithTheStrataMultilayerStochasticBlockModel]]
- [[MathematicalFormulationOfMultilayerNetworks]]
- [[TheChildInAmericaBehaviorProblemsAndPrograms]]
- [[BestRankRRRSuperSymmetricTensorApproximationAContinuousTimeApproach]]
- [[Cognitive social structures]]
- [[SystematicBiasesInSocialPerception]]
- [[EfficientAndPrincipledMethodForDetectingCommunitiesInNetworks]]
- [[RelationalSchemasAndTheProcessingOfSocialInformation]]
- [[FillingInTheBlanksATheoryOfCognitiveCategoriesAndTheStructureOfSocialAffiliation]]
- [[TensorDecompositionsAndApplications]]
- [[HumansUseCompressionHeuristicsToImproveTheRecallOfSocialNetworks]]
- [[AMacrosociologicalTheoryOfSocialStructure]]
- [[SubjectiveProbabilitiesOfInterpersonalRelationships]]
- [[CognitiveStructureAndInformantAccuracy]]
- [[MaximizingTheSpreadOfInfluenceThroughASocialNetwork]]
- [[JustLikeAWomanEffectsOfGenderBiasedPerceptionsOfFriendshipNetworkBrokerageOnAttributionsAndPerformance]]
- [[LatentSpaceApproachesToSocialNetworkAnalysis]]
- [[NameGeneratorsInSurveysOfPersonalNetworks]]
- [[RelationalSchemasToInvestigateTheProcessOfLeadershipEmergence]]
- [[AlternatingProximalGradientMethodForSparseNonnegativeTuckerDecomposition]]
- [[TheMicrostructuresOfNetworkRecallHowSocialNetworksAreEncodedAndRepresentedInHumanMemory]]
- [[StructuralMeasuresForMultiplexNetworks]]
- [[AnApproachForRelatingSocialStructureToCognitiveStructure]]
- [[AssessingThePoliticalLandscapeStructureCognitionAndPowerInOrganizations]]
- [[InformantAccuracyInSocialNetworkDataIvAComparisonOfCliqueLevelStructureInBehavioralAndCognitiveNetworkData]]
- [[InformantAccuracyInSocialNetworkData]]
- [[CultureAndCognition]]
- [[CoarseThinkingAndPersuasion]]
- [[OrganizationalNetworkPerceptionsVersusRealityASmallWorldAfterAll]]
- [[ComputingANonnegativeMatrixFactorizationProvably]]
- [[StructuralReducibilityOfMultilayerNetworks]]
- [[ComparingClusteringsByTheVariationOfInformation]]
- [[WhenDoesNonNegativeMatrixFactorizationGiveACorrectDecompositionIntoParts]]
- [[IdentitiesInFluxCognitiveNetworkActivationInTimesOfChange]]
- [[SocialNetworkSchemasAndTheLearningOfIncompleteNetworks]]
- [[Cognitive social structuresInSocialNetworkResearchAReview]]
- [[AnEcologyOfAffiliation]]
- [[ASocialCognitiveConceptionOfSocialStructure]]
- [[BayesianPoissonTuckerDecompositionForLearningTheStructureOfInternationalRelations]]
- [[SpectralEntropiesAsInformationTheoreticToolsForComplexNetworkComparison]]
- [[TheAnnalsOfMathematicalStatistics]]
- [[CommunityDetectionLinkPredictionAndLayerInterdependenceInMultilayerNetworks]]
- [[LayerCommunitiesInMultiplexNetworks]]
- [[EmergentLeadershipStructuresInInformalGroupsADynamicCognitivelyInformedNetworkModel]]
- [[TensorialAndBipartiteBlockModelsForLinkPredictionInLayeredNetworksAndTemporalNetworks]]
- [[LatentSpaceModelsForNetworkPerceptionData]]
- [[UnresolvedReference0DC12ECDE329E503]]
- [[ActiveMatrixFactorizationForSurveys]]
- [[UnresolvedReference36246BA5B93A4B0E]]
- [[UnresolvedReferenceFCC251D7F5E3EBD8]]
- [[UnresolvedReference60BD20988E42A2AC]]
- [[ALatentSpaceModelForCognitive social structuresData]]
- [[UnresolvedReference8D91F97DDE49AA89]]
- [[DisentanglingHomophilyCommunityStructureAndTriadicClosureInNetworks]]
- [[UnresolvedReferenceD7FF457D1E1B9444]]
- [[UnresolvedReferenceF4655494990BF59B]]
- [[EvolutionOnADancingLandscapeOrganizationsAndNetworksInDynamicBlauSpace]]
- [[UnresolvedReference8BBE8A685BB38E08]]
- [[ANoteOnUniversalInference]]
- [[ThePsychologyOfInterpersonalRelations]]
- [[UnresolvedReference25F69C4B2D743CED]]
- [[LatentNetworkModelsToAccountForNoisyMultiplyReportedSocialNetworkData]]
- [[ADiscussionOfANoteOnUniversalInferenceByTseAndDavison]]
- [[VolumeRegularizedNonnegativeTuckerDecompositionWithIdentifiabilityGuarantees]]
- [[UnresolvedReference0FD2B8A8906A4AE3]]
- [[UnresolvedReference6F56B4B76431505C]]
- [[UnresolvedReference0C014DAB6F3B3FC2]]
- [[UnresolvedReference47C0409E191E116B]]
- [[IeeeCvpr]]
- [[UnresolvedReference3933F145C9975230]]
- [[UnresolvedReference8CF5C2A278DF0EFF]]
- [[UnresolvedReference997C86CD10E457AA]]
- [[UnresolvedReference7A17D0C7336D2148]]
- [[HierarchicalBlockStructuresAndHighResolutionModelSelectionInLargeNetworks]]
- [[UnresolvedReference134C514D53779461]]
- [[UnresolvedReference620248FE5981763A]]
- [[TheAcquaintanceProcess]]
- [[UnresolvedReference4E33E4C4659FC68E]]
- [[Neurips]]
- [[UnresolvedReference0ED4F79F816AF1B9]]
- [[TheSmallWorldProblem]]


## Audit Log
- Audit invalidated (2026-09-30): auditor admitted incomplete independent checks and premature flag removal. Previous valid audits, if any, remain separate.

- 2026-09-30: Strong source review corrected redundant/agreement constraints, restart counts, Algorithm 2 order/averaging, and invalid ordinary-LRT implication. Independent re-audit pending.

- WITHDRAWN audit claim (2026-09-30): the remaining-audit-c report overstated independent source checks; it does not establish a pass.

## LLM Justification
[^r1]: https://www.cambridge.org/core/journals/network-science/article/latent-cognitive-structures-of-social-networks/5C675C255AB9B9FE5A6A9F2E39E4909C; §1 states the motivating question and contributions.
[^r2]: Same source; §§1 and 3.1, pp. 202–211, defines CSS layers and the NNTuck factorization.
[^r3]: Same source; §§3.2–3.4, Definitions 1–4: exact variant constraints and fixed-factor fitting.
[^r4]: Same source; §§3.5–4, pp. 218–229, defines inference tests and analyzes four empirical CSS datasets.
[^r5]: Same source; §3.4 and Appendix B, Algorithms 1–2: initialization Y,V,G then U=Y; updates V→U→Y, average U/Y, then core; retain best iterate; 20 standard starts; Appendix C/Figure C1 specifies 50 agreement starts and lack of guarantees.
[^r6]: Same source; §3.5, Definitions 5–8 and Appendix C: nonidentifiability, Wilks failure, split-LRT, random splitting, power and null-MLE caveats; §4 pipeline gives cross-validation and comparisons.
