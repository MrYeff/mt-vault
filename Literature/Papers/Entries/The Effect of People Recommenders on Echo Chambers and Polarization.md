---
title: "The Effect of People Recommenders on Echo Chambers and Polarization"
tags:
  - model
  - simulation
authors:
  - "[[Literature/Authors/Federico Cinus|Federico Cinus]]"
  - "[[Literature/Authors/Marco Minici|Marco Minici]]"
  - "[[Literature/Authors/Corrado Monti|Corrado Monti]]"
  - "[[Literature/Authors/Francesco Bonchi|Francesco Bonchi]]"
publication date: 2022-05-31
source: https://arxiv.org/pdf/2112.00626
doi: 10.1609/icwsm.v16i1.19275
read status: Todo
⚠️:
  - audit failed
---
## Abstract

The effects of online social media on critical issues, such as polarization and misinformation, are under scrutiny due to the disruptive consequences that these phenomena can have on our societies. Among the algorithms routinely used by social media platforms, people-recommender systems are of special interest, as they directly contribute to the evolution of the social network structure, affecting the information and the opinions users are exposed to. In this paper, we propose a novel framework to assess the effect of people recommenders on the evolution of opinions. Our proposal is based on Monte Carlo simulations combining link recommendation and opinion-dynamics models. In order to control initial conditions, we define a random network model to generate graphs with opinions, with tunable amounts of modularity and homophily. Finally, we join these elements into a methodology able to study the causal relationship between the recommender system and the echo chamber effect. Our method can also assess if such relationships are statistically significant. We also show how such a framework can be used to measure, by means of simulations, the impact of different intervention strategies. Our thorough experimentation shows that people recommenders can in fact lead to a significant increase in echo chambers. However, this happens only if there is considerable initial homophily in the network. Also, we find that if the network already contains echo chambers, the effect of the recommendation algorithm is negligible. Such findings are robust to two very different opinion dynamics models, a bounded confidence model and an epistemological model.

## Research Questions
> Research Questions extracted via LLM

- How can we assess the effect of people recommenders on echo chambers and polarization?[^r1]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?
PROD co-evolves a directed follow graph and node opinions using an interchangeable people recommender and opinion rule.[^r2]
The state and schedule below summarize §3 and Algorithm 1. Parameters are the reported §5 settings; recommendations are absent edges and each node keeps its out-degree.[^r2][^r3]

```yml
World:
  nodes: [Node]
  edges: [(NodeId, NodeId)] # u follows v
  rule: BoundedConfidence | Epistemological
  recommender: DirectedJaccard | PPR | SALSA | OpinionBiased
  accepted: u32
  turn: u32

Node:
  opinion: 0..1 # Epistemological: belief that new action is better
  successes: f64? # observed experimental outcome
```

### How does it work?
The main schedule and opinion transitions are specified below; the epistemological text supplies observations but does not specify a separate experiment-refresh schedule inside Algorithm 1.[^r3][^r4]

```
N = 400
EDGES_APPROX = 5500
S = 2
R_MAX = 0.4 * |E|
T_MAX = 5000 if BoundedConfidence else 100
BC_MU = BC_EPSILON = 0.2
EPI_EPSILON = 0.005
EXPERIMENTS = 15
BASE_SUCCESS = 0.5
RUNS = 500

sim_loop(mut world: World):
  ALPHA = R_MAX / ((T_MAX / 2) * S * N)
  while world.turn < T_MAX:
    world.turn += 1
    for u in random_permutation(world.nodes):
      s = 0
      while s < S:
        if Bernoulli(ALPHA):
          v, acceptance = recommend(u, world) # non-followed v
          if Bernoulli(acceptance):
            w = random_choice(out_neighbors(u))
            replace_edge(u, w, v)
            update_opinion(world, u, v)
            s += 1; world.accepted += 1
            if world.accepted == R_MAX: ALPHA = 0
          # rejection does not increment s
        else:
          v = random_choice(out_neighbors(u))
          update_opinion(world, u, v)
          s += 1

update_opinion(mut world: World, u: NodeId, v: NodeId):
  if world.rule == BoundedConfidence:
    if abs(O[u] - O[v]) < BC_EPSILON:
      O[u] = O[u] + BC_MU * (O[v] - O[u])
  else:
    # belief drives old vs new action; old yields EXPERIMENTS/2,
    # new yields Binomial(EXPERIMENTS, BASE_SUCCESS + EPI_EPSILON)
    k = observed_successes(v)
    O[u] = 1 / (1 + ((1 - O[u]) / O[u]) *
      ((BASE_SUCCESS - EPI_EPSILON) /
       (BASE_SUCCESS + EPI_EPSILON)) ^ (2*k - EXPERIMENTS))
```

- Initialization: directed LFR communities with paper's modularity parameter `MU`; draw a community opinion uniformly on(0,1). With probability `ETA`, a node copies its community opinion; otherwise draw its own. Grid: `ETA∈[0.2,0.8]`, `MU∈[0.05,0.95]`. `R_MAX` is chosen by stepping upward until just before disconnection; the reported value is40% of edges. `ALPHA` is intended to produce roughly half a run with recommender activity and half without.[^r3][^r5]

- PPR solves `p=D*A_STOCH*p+(1−D)*e_u`. SALSA's hubs are top-k PPR nodes; authorities are their followees. With column-normalized hub→authority matrix `M_C` and row-normalized transpose `M_R`, initialize hub mass at u and iterate `r=M_C*s`, `s=d_u+(1−D_HAT)*M_R*r` to convergence. OBA uses inverse opinion distance `|O[u]−O[v]|^(−GAMMA)`. The paper does not resolve zero-distance treatment or give all k/gamma settings in this definition.[^r7]

- Directed Jaccard's printed numerator is `|N_out(u)∩N_in(u)|`, with denominator `|N_out(u)|+|N_in(v)|−|N_out(u)∩N_in(u)|`; this u/v mismatch differs from the natural candidate-overlap formula. OBA's printed normalizer sums over existing edges although candidate recommendations must be non-edges. These source conflicts are retained; neither is silently repaired.[^r7]

- Estimate each recommender's score CDF from a large sample at run start, then transform scores through that empirical CDF into acceptance probabilities, preserving ranking and standardizing score distributions. Candidate-ranking implementation details remain omitted.[^r7]

### What can it answer?
- For each initial graph, compare a recommender run against `R_MAX=0` on that same graph, average paired final-metric differences over500 graphs and use the paper's Kolmogorov–Smirnov comparison (reported significance p<0.05).[^r6]
- NCI is Pearson correlation of node opinions with outgoing-neighbor mean opinions.[^r6]
- RWC is `P_XX*P_YY−P_XY*P_YX`, where `P_ij` is probability a walk ending in partition j started in i, partitions are below/above0.5, and restart occurs on reaching a node above the95th degree percentile.[^r6]
Recommenders increase echo chambers particularly with initial `ETA>0.5` and `MU<0.3`; effects are weaker when networks are already polarized. Intervention experiments substitute recommendations probabilistically using uniform choice, opinion distance, or degree-based strategies.[^r8]

### Where does it apply?
The framework evaluates simulated graphs under supplied opinion dynamics and recommender assumptions; these causal comparisons concern simulation conditions and do not establish actual platform-user responses.[^r2][^r6]
## Metadata
### References

- [[Wtf]]
- [[TheFilterBubbleWhatTheInternetIsHidingFromYou]]
- [[ExposureToIdeologicallyDiverseNewsAndOpinionOnFacebook]]
- [[ThePagerankCitationRankingBringingOrderToTheWeb]]
- [[AuthoritativeSourcesInAHyperlinkedEnvironment]]
- [[RoleOfTheNewMediaInTheArabSpring]]
- [[BenchmarkGraphsForTestingCommunityDetectionAlgorithms]]
- [[LearningFromNeighbours]]
- [[Salsa]]
- [[TheWhoToFollowSystemAtTwitterStrategyAlgorithmsAndRevenueImpact]]
- [[WhoToFollowAndWhy]]
- [[Mixing beliefs among interacting agents]]
- [[EshuAnExtensibleWebEditorForDiagrammaticLanguages]]
- [[EchoChambersOnlinePoliticallyMotivatedSelectiveExposureAmongInternetNewsUsers]]
- [[TweetingFromLeftToRight]]
- [[MeasuringOnlineSocialBubbles]]
- [[EchoChambersOnFacebook]]
- [[TwitterAsArenaForTheAuthenticOutsiderExploringTheSocialMediaCampaignsOfTrumpAndClintonInThe2016UsPresidentialElection]]
- [[ArePeopleIncidentallyExposedToNewsOnSocialMediaAComparativeAnalysis]]
- [[AlgorithmicBiasAmplifiesOpinionFragmentationAndPolarizationABoundedConfidenceModel]]
- [[QuantifyingControversyOnSocialMedia]]
- [[PeopleRecommendationOnSocialMedia]]
- [[TheGeographicEmbeddingOfOnlineEchoChambersEvidenceFromTheBrexitCampaign]]
- [[ModellingOpinionDynamicsInTheAgeOfAlgorithmicPersonalisation]]
- [[UnresolvedReferenceAA77C024D9730F88]]
- [[LinkPredictionTechniquesApplicationsAndPerformanceASurvey]]
- [[CanCelebritiesBurstYourBubble]]
- [[TheEffectOfHomophilyOnDisparateVisibilityOfMinoritiesInPeopleRecommenderSystems]]
- [[UnresolvedReference5926DEFF1A71AE2B]]
- [[1RhythmsOfSocialInteractionMessagingWithinAMassiveOnlineNetwork]]
- [[SocialNetworksThatMatterTwitterUnderTheMicroscope]]
- [[NoEchoInTheChambersOfPoliticalInteractionsOnReddit]]
- [[ModelingHowSocialNetworkAlgorithmsCanInfluenceOpinionPolarization]]
- [[TheEchoChamberEffectOnSocialMedia]]
- [[TheLinkPredictionProblemForSocialNetworks]]
- [[UnresolvedReferenceE6EAE79D3CAB66D0]]
- [[UnresolvedReference1323CDEB67DDE8CE]]
- [[UnresolvedReference5F4033251076E0EC]]
- [[UnresolvedReference331E2753B5CF4EDA]]
- [[UnresolvedReference92F0F2280D586373]]
- [[UnresolvedReference58DB6F5181AB9EC3]]
- [[UnresolvedReference6BBAE6016DE3C25B]]
- [[UnresolvedReference5ED183BB64D4B936]]
- [[UnresolvedReference4662B120CCC01B23]]
- [[UnresolvedReferenceF9CC4AAB3DCA8894]]
- [[UnresolvedReferenceC8AF38FBDD3FB928]]
- [[UnresolvedReference9F174A612C0FFA36]]


## Audit Log
- Audit invalidated (2026-09-30): auditor admitted incomplete independent checks and premature flag removal. Previous valid audits, if any, remain separate.

- 2026-09-30: Initial/cheap audit failed; stronger source review corrected exact Alpha/rejection/accepted-link schedule, both opinion states/transitions, initial opinions, score definitions and CDF; discovered additional literal DJI u/v mismatch and retained it. Independent re-audit pending.

- WITHDRAWN audit claim (2026-09-30): the remaining-audit-c report overstated independent source checks; it does not establish a pass.

## LLM Justification
[^r1]: https://arxiv.org/pdf/2112.00626; §1: central question. Abstract retained from publisher https://ojs.aaai.org/index.php/ICWSM/article/view/19275 (different from manuscript abstract).
[^r2]: https://arxiv.org/pdf/2112.00626; §3 pp.2–3: directed graph, nonedge recommendation input/output, modular framework.
[^r3]: Same source; Algorithm1 and §3 p.3: ALPHA formula, rejection without counter increment, replacement order, accepted-link cutoff and intended half-run regimes; §5 p.6: parameter settings/disconnection calibration.
[^r4]: Same source; §3.1 pp.3–4: bounded-confidence listener-only rule; epistemological two action outcomes, Bernoulli/binomial experiment evidence and Bayesian Eq1; no separate refresh schedule is specified in Algorithm1.
[^r5]: Same source; §4.1 pp.5–6: opinion-aware LFR, community and individual uniform draws, ETA Bernoulli; §5 parameter grid.
[^r6]: Same source; §4 pp.4–5, Eq5: same-initial-graph null comparisons and KS test; §4.2 pp.5–6: NCI and RWC/restart definitions; Figures2–3 significance levels.
[^r7]: Same source; §3.2 pp.4–5, displayed DJI, Eq2 PPR, Eqs3–4 SALSA, displayed OBA and “Normalization of recommenders”: exact scores/CDF; literal DJI numerator N_in(u) and OBA denominator existing E conflict with candidate-based interpretation.
[^r8]: Same source; §§5.1–5.4 pp.6–10: conditional findings, robustness and intervention strategies.
