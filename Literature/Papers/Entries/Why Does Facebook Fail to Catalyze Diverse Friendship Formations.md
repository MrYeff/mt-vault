---
title: "Why Does Facebook Fail to Catalyze Diverse Friendship Formations?"
tags:
  - model
  - simulation
authors:
  - "[[Literature/Authors/Firman M. Firmansyah|Firman M. Firmansyah]]"
publication date: 2021
source: https://www.informs-sim.org/wsc21papers/271.pdf
doi: 
read status: Todo
---
## Abstract

This study sought to understand why Facebook, the largest social networking site intended to “bring the world closer together”, fails to catalyze diverse friendship formations. In doing so, it employs agent-based modeling built on the Framework for Intergroup Relations and Multiple Affiliations Networks (FIRMAN). As demonstrated in 600 simulations, Facebook has primarily enhanced users' tie capacity (TC) to maintain a larger number of friendships while doing little to empower users' tie outreachability (TO) to tolerate group differences. These conditions inevitably hinder diverse friendship formations on Facebook.

## Research Questions
> Research Questions extracted via LLM

- How do tie capacity and tie outreachability jointly affect homogeneous and diverse friendship formation under offline and Facebook-like conditions?[^r1]

## Model
> Model extracted via LLM according to [[Model Notation]]

FIRMAN is a stylized agent-based friendship model in weighted social-identity space.[^r2]

```yml
World:
  agents: [Agent]
  identity_dimensions: [SI1, SI2]

Agent:
  identity: [0 | 1, 0 | 1]
  TO: 0.. # tolerated social-identity distance
  TC: u32 # maximum number of friends
  friends: [AgentId]

sim_step(mut world: World):
  for candidate pair (a, b):
    distance = weighted_identity_distance(a, b)
    if a.TO >= distance and b.TO >= distance
       and a.friends.count < a.TC and b.friends.count < b.TC:
      add reciprocal friendship
  report homogeneous and diverse dyads
```

- The source’s prose prints the capacity inequality as `TC < num_f`, inconsistent with TC being a maximum; above, remaining capacity is interpreted as `num_f < TC`.[^r3]
- The design uses SI1 minority share 50% (weight 1), SI2 share 30% (weight 2), `n ∈ {50,500}`, TC Gaussian means `μ ∈ {3,50}` and variances `σ² ∈ {1,5}`, and TO binomial `m=3`, `q ∈ {0.3,0.5,0.7}`. There are 600 simulations, 100 trials per cell.[^r4]

### What does it represent?
How tie capacity and tolerance for identity differences constrain reciprocal friendship formation.[^r2]

### How does it work?
Weighted identity distance and each endpoint’s TO/remaining TC determine tie eligibility. The note flags the source’s contradictory capacity inequality rather than treating it as unambiguous.[^r3]

### What can it answer?
It compares total dyads and homogeneous/diverse proportions across capacity and tolerance scenarios. More capacity raises tie counts; more outreachability can improve diversity, although homogeneous ties remain more common.[^r5]

### Where does it apply?
It is a two-dimensional, stylized comparison of hypothetical offline and Facebook-like conditions; it does not model Facebook recommender algorithms or observed friendship trajectories.[^r2]
## Metadata
### References

- [[WhyDoHomogeneousFriendshipsPersistInADiversePopulationMakingSenseOfHomophily]]
- [[SourcesOfSegregationInSocialNetworksANovelApproachUsingFacebook]]
- [[IdentityTheoryAndSocialIdentityTheory]]


## Audit Log
- Audit invalidated (2026-09-30): auditor admitted incomplete independent checks and premature flag removal. Previous valid audits, if any, remain separate.

## LLM Justification
[^r1]: https://www.informs-sim.org/wsc21papers/271.pdf; Introduction and FIRMAN theoretical framework, pp. 1–2.
[^r2]: Same source; §2, defines identity-space nodes, weighted dimensions, tie distance, TO, and TC.
[^r3]: Same source; §2, p. 1, describes reciprocal tie feasibility. The article’s printed capacity inequality conflicts with its maximum-capacity definition; the note makes this interpretation explicit rather than concealing the inconsistency.
[^r4]: Same source; §3 Methods, p. 2, gives population composition, weights, factor values, and 100 trials per cell.
[^r5]: Same source; §4 Results and Discussion, p. 2, reports tie counts and effects of capacity and outreachability.
