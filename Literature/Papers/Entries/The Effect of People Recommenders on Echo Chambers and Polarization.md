---
title: The Effect of People Recommenders on Echo Chambers and Polarization
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
read status: Scan
---
## Abstract

The effects of online social media on critical issues, such as polarization and misinformation, are under scrutiny due to the disruptive consequences that these phenomena can have on our societies. Among the algorithms routinely used by social media platforms, people-recommender systems are of special interest, as they directly contribute to the evolution of the social network structure, affecting the information and the opinions users are exposed to. In this paper, we propose a novel framework to assess the effect of people recommenders on the evolution of opinions. Our proposal is based on Monte Carlo simulations combining link recommendation and opinion-dynamics models. In order to control initial conditions, we define a random network model to generate graphs with opinions, with tunable amounts of modularity and homophily. Finally, we join these elements into a methodology able to study the causal relationship between the recommender system and the echo chamber effect. Our method can also assess if such relationships are statistically significant. We also show how such a framework can be used to measure, by means of simulations, the impact of different intervention strategies. Our thorough experimentation shows that people recommenders can in fact lead to a significant increase in echo chambers. However, this happens only if there is considerable initial homophily in the network. Also, we find that if the network already contains echo chambers, the effect of the recommendation algorithm is negligible. Such findings are robust to two very different opinion dynamics models, a bounded confidence model and an epistemological model.[^r1]

## Research Questions
> Research Questions extracted via LLM

- Given an initial network, do people recommendations increase echo chambers?[^r1]
- Given an initial network, do people recommendations increase polarization?[^r1]
- Which initial conditions change these effects?[^r8]
- Which recommendation interventions reduce these effects?[^r8]

## Model
> Model extracted via LLM according to [[Model Notation]].[^r2]

### What does it represent?
PROD co-evolves a directed follow graph and node opinions using an interchangeable people recommender and opinion rule.[^r2]
A follow tie points from listener to source. Recommendations add absent ties; each agent keeps its out-degree.[^r2][^r3]

```yml
World:
  nodes: [Node]
  edges: [(NodeId, NodeId)] # u follows v
  observations:
	  accepted: u32
	  turn: u32

Node:
  opinion: 0..1 # Epistemological: belief that new action is better
  successes: f64? # epistemological variant only
  
RECOMENDER: fn (NodeId, NodeId) -> 0..1
DYNAMICS_MODEL: BoundedConfidence | Epistemological
```

### How does it work?
#### Settings
Reported experiment settings; these are configured values, not necessary properties of PROD.[^r3]

```
NODE_COUNT = 400
EDGE_COUNT_APPROX = 5500
INTERACTIONS_PER_STEP = 2
LINK_BUDGET = 0.4 * initial_edge_count
STEPS = 5000 if BoundedConfidence else 100
CONFIDENCE_RADIUS = 0.2
OPINION_SHIFT = 0.2
SUCCESS_GAIN = 0.005
EXPERIMENT_COUNT = 15
BASE_SUCCESS = 0.5
RUN_COUNT = 500
```

#### Interaction schedule
Each agent completes two interactions per step. A rejected recommendation consumes no interaction. An accepted recommendation replaces a random existing follow tie; the follower then receives influence from the new followee. After the accepted-link budget is reached, only existing ties are used.[^r3]

```
sim_loop(mut world: World):

  recommendation_rate = LINK_BUDGET / (
    (STEPS / 2) * INTERACTIONS_PER_STEP * NODE_COUNT
  )
  for step in 1..STEPS:
    world.turn = step
    for u in random_permutation(world.nodes):
      completed = 0
      while completed < INTERACTIONS_PER_STEP:
        if Bernoulli(recommendation_rate):
          v, acceptance = recommend(u, world)
          if not Bernoulli(acceptance): continue
          w = random_choice(out_neighbors(world, u))
          world.edges.remove((u, w))
          world.edges.push((u, v))
          world.accepted += 1
          if world.accepted == LINK_BUDGET:
            recommendation_rate = 0
        else:
          v = random_choice(out_neighbors(world, u))

        update_opinion(world, u, v)
        completed += 1
```

#### Variant: bounded confidence
The follower observes the followee's opinion. Only the follower changes; an opinion outside the confidence radius has no effect.[^r4]

```
update_opinion(mut world: World, u: NodeId, v: NodeId):

  current = world.nodes[u].opinion
  heard = world.nodes[v].opinion
  if abs(current - heard) < CONFIDENCE_RADIUS:
    world.nodes[u].opinion = current + OPINION_SHIFT * (
      heard - current
    )
```

#### Variant: epistemological learning
Opinion is belief that a new action is better than an old action. Agents observe another agent's experimental results, rather than simply copying its opinion.[^r4]

- Old action: known success probability `BASE_SUCCESS`; the model assigns `EXPERIMENT_COUNT / 2` successes.[^r4]
- New action: true success probability `BASE_SUCCESS + SUCCESS_GAIN`; successes are drawn from a binomial distribution.[^r4]
- The agent's belief determines which action it performs. Algorithm 1 does not specify when experiments are refreshed. The text also does not fully formalize belief-to-action selection. The procedure below covers only the stated Bayesian update; it is not a complete epistemological simulation.[^r4]

```
update_opinion(mut world: World, u: NodeId, v: NodeId):

  belief = world.nodes[u].opinion
  successes = world.nodes[v].successes
  likelihood_ratio = (
    (BASE_SUCCESS - SUCCESS_GAIN) /
    (BASE_SUCCESS + SUCCESS_GAIN)
  ) ^ (2 * successes - EXPERIMENT_COUNT)

  world.nodes[u].opinion = 1 / (
    1 + ((1 - belief) / belief) * likelihood_ratio
  )
```

#### Initialization and recommendation
- Generate a directed LFR network with communities and power-law degrees.[^r5]
- Draw each community's opinion uniformly from `0..1`.[^r5]
- With probability `ETA`, an agent copies its community opinion; otherwise draw an independent opinion.[^r5]
- Vary homophily `ETA` over `0.2..0.8` and the paper's modularity parameter `MU` over `0.05..0.95`.[^r5]
- Calibrate the link budget by increasing it until just before rewiring disconnects the graph; reported budget: 40% of initial edges.[^r3]
- The recommendation rate targets roughly half the run with recommendations and half without; the cutoff depends on accepted links, not elapsed time.[^r3]

- PPR solves `p=D*A_STOCH*p+(1−D)*e_u`. SALSA's hubs are top-k PPR nodes; authorities are their followees. With column-normalized hub→authority matrix `M_C` and row-normalized transpose `M_R`, initialize hub mass at u and iterate `r=M_C*s`, `s=d_u+(1−D_HAT)*M_R*r` to convergence. OBA uses inverse opinion distance `|O[u]−O[v]|^(−GAMMA)`. The paper does not resolve zero-distance treatment or give all k/gamma settings in this definition.[^r7]

- Directed Jaccard's printed numerator is `|N_out(u)∩N_in(u)|`, with denominator `|N_out(u)|+|N_in(v)|−|N_out(u)∩N_in(u)|`; this u/v mismatch differs from the natural candidate-overlap formula. OBA's printed normalizer sums over existing edges although candidate recommendations must be non-edges. These source conflicts are retained; neither is silently repaired.[^r7]

- Estimate each recommender's score CDF from a large sample at run start, then transform scores through that empirical CDF into acceptance probabilities, preserving ranking and standardizing score distributions. The paper gives ranked candidates, but does not fully specify how `recommend` chooses a candidate or handles no available candidate. The main procedure therefore describes the framework, not a complete executable implementation.[^r7]

### What can it answer?
- For each initial graph, compare a recommender run against `LINK_BUDGET=0` on that same graph, average paired final-metric differences over 500 graphs and use the paper's Kolmogorov–Smirnov comparison (reported significance p<0.05).[^r6]
- NCI is Pearson correlation of node opinions with outgoing-neighbor mean opinions.[^r6]
- RWC is `P_XX*P_YY−P_XY*P_YX`, where `P_ij` is probability a walk ending in partition j started in i, partitions are below/above 0.5, and restart occurs on reaching a node above the 95th degree percentile. The stated partitions exclude opinions exactly equal to 0.5; their treatment is unspecified.[^r6]
Recommenders increase echo chambers particularly with initial `ETA>0.5` and `MU<0.3`; effects are weaker when networks are already polarized. Intervention experiments substitute recommendations probabilistically using uniform choice, opinion distance, or degree-based strategies.[^r8]

### Where does it apply?
- People recommendations that change a directed follow network; not a ranked content feed.[^r2]
- One opinion per agent; no modeled friendship quality, belonging, or shared activities.[^r2][^r9]
- Fixed agents and fixed out-degree in the standard procedure; following someone replaces a tie rather than increasing the contact budget.[^r3][^r9]
- No direct quantitative validation against real-world data. Comparing algorithms establishes effects inside these simulation assumptions.[^r9]
- Useful for this project: testing whether recommendations separate opinion groups. Additional rules and validation are needed to test social integration.[^r10]
## Reading Notes

- people recommenders mainly use:
	- network structure (e.g., recommending friends of friends)
	- content (e.g., recommending users with similar interests)
- opinion dynamics model
	- Bounded Confidence Model: if opinions are close enough people they get closer
	- epistemological mode: observe world and inform others
- tested recomenders 
	- link predictors (only based on netwerk topology)
	- opinion based recomender
- initialisation: random network + opinions model based on Lancichinetti, Fortunato,
and Radicchi
- metrics: measuring if eco chambers increase or decrease
- key findings:
	- People recommenders can strengthen echo chambers, if  count(homophilic links) > count(heterophilic links)
	- This effect becomes negligible (or even reversed) if the network is already segregated in polarized communities.
	- findings consistent between 
		- different opinion dynamics models 
		- recommender algorithms. 
	- some recomenders contribute mor to polarisation
	- recommending users to users with different opinions might reduce echo chambers
## Metadata
### References

- [[Exposure to ideologically diverse news and opinion on Facebook|Exposure to ideologically diverse news and opinion on Facebook]]
- [[Learning from neighbours|Learning from neighbours]]
- [[Tweeting From Left to Right- Is Online Political Communication More Than an Echo Chamber-|Tweeting From Left to Right: Is Online Political Communication More Than an Echo Chamber?]]
- [[Who to follow and why- link prediction with explanations|Who to follow and why: link prediction with explanations]]
- [[The geographic embedding of online echo chambers- Evidence from the Brexit campaign|The geographic embedding of online echo chambers: Evidence from the Brexit campaign]]
- [[The echo chamber effect on social media|The echo chamber effect on social media]]
- [[Modeling how social network algorithms can influence opinion polarization|Modeling how social network algorithms can influence opinion polarization]]
- [[Mixing beliefs among interacting agents|Mixing Beliefs Among Interacting Agents]]
- [[Can celebrities burst your bubble-|Can celebrities burst your bubble?]]
- [[Twitter as arena for the authentic outsider- Exploring the social media campaigns of Trump and Clinton in the 2016 US presidential election|Twitter as arena for the authentic outsider: Exploring the social media campaigns of Trump and Clinton in the 2016 US presidential election]]
- [[The effect of homophily on disparate visibility of minorities in people recommender systems|The effect of homophily on disparate visibility of minorities in people recommender systems]]
- [[Are people incidentally exposed to news on social media- A comparative analysis|Are people incidentally exposed to news on social media? A comparative analysis]]
- [[Quantifying controversy on social media|Quantifying controversy on social media]]
- [[Echo chambers online-- Politically motivated selective exposure among Internet news users|Echo chambers online?: Politically motivated selective exposure among Internet news users]]
- [[PageRank beyond the web|PageRank beyond the web]]
- [[The who-to-follow system at Twitter- Strategy, algorithms, and revenue impact|The who-to-follow system at Twitter: Strategy, algorithms, and revenue impact]]
- [[Rhythms of social interaction- Messaging within a massive online network|Rhythms of social interaction: Messaging within a massive online network]]
- [[WTF- the who to follow service at Twitter|WTF: the who to follow service at Twitter]]
- [[People recommendation on social media|People recommendation on social media]]
- [[Social networks that matter- Twitter under the microscope|Social networks that matter: Twitter under the microscope]]
- [[Role of the new media in the Arab Spring|Role of the new media in the Arab Spring]]
- [[Authoritative sources in a hyperlinked environment|Authoritative sources in a hyperlinked environment]]
- [[Spring embedders and force directed graph drawing algorithms|Spring embedders and force directed graph drawing algorithms]]
- [[Link prediction techniques, applications, and performance- A survey|Link prediction techniques, applications, and performance: A survey]]
- [[Benchmark graphs for testing community detection algorithms|Benchmark graphs for testing community detection algorithms]]
- [[SALSA- the stochastic approach for link-structure analysis|SALSA: the stochastic approach for link-structure analysis]]
- [[The link-prediction problem for social networks|The link-prediction problem for social networks]]
- [[No echo in the chambers of political interactions on Reddit|No echo in the chambers of political interactions on Reddit]]
- [[Measuring online social bubbles|Measuring online social bubbles]]
- [[The PageRank citation ranking- Bringing order to the web|The PageRank citation ranking: Bringing order to the web]]
- [[The Filter Bubble- What the Internet Is Hiding from You|The Filter Bubble: What the Internet Is Hiding from You]]
- [[Modelling opinion dynamics in the age of algorithmic personalisation|Modelling opinion dynamics in the age of algorithmic personalisation]]
- [[Echo Chambers on Facebook|Echo Chambers on Facebook]]
- [[Social influence and unfollowing accelerate the emergence of echo chambers|Social influence and unfollowing accelerate the emergence of echo chambers]]
- [[Algorithmic bias amplifies opinion fragmentation and polarization- A bounded confidence model|Algorithmic bias amplifies opinion fragmentation and polarization: A bounded confidence model]]


## Audit Log
- Independent source audit passed after corrections; extraction and references are finalized.[^r11]
- Independent audit found a missing exact reference-title alias and missing source markers on the copied abstract and formal-extraction preamble. These were corrected and passed independent re-audit.[^r11]
- 2026-10-03: Earlier content review recorded unspecified candidate selection, epistemological action/evidence scheduling, and the RWC boundary at opinion 0.5; these gaps are disclosed above. Earlier review claimed a passing re-audit, but this repair is awaiting a fresh independent audit. The prior reference-skip authorization was revoked; the source bibliography was reconciled below.
- Audit invalidated (2026-09-30): auditor admitted incomplete independent checks and premature flag removal. Previous valid audits, if any, remain separate.

- 2026-09-30: Initial/cheap audit failed; stronger source review corrected exact Alpha/rejection/accepted-link schedule, both opinion states/transitions, initial opinions, score definitions and CDF; discovered additional literal DJI u/v mismatch and retained it. Independent re-audit completed on 2026-10-03 (see above).

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

[^r9]: Same source; §6 Discussion: fixed population/edge count, lack of direct quantitative real-data comparison, multidimensional opinions proposed as extension; §3 state contains follow ties and scalar opinions.
[^r10]: Project comparison, not a paper finding: [[What are my goal - LLM]] targets social integration. PROD’s §4.2 outcomes measure opinion-neighbor correlation and random-walk separation, not relationship quality or participation.
[^r11]: Independent full-source audit and corrections recorded in vault/.automation/audit/noted-simulations-2026-10-03/prod-independent-audit.json. Bibliography entry: “Mixing Beliefs Among Interacting Agents”; abstract source is the publisher record cited in r1.
