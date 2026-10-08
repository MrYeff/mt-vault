---
title: "SARDINE: A Simulator for Automated Recommendation in Dynamic and Interactive Environments"
tags:
  - recommender_system
  - simulation
  - "model"
authors:
  - "[[Literature/Authors/Romain Deffayet|Romain Deffayet]]"
  - "[[Literature/Authors/Thibaut Thonet|Thibaut Thonet]]"
  - "[[Literature/Authors/Dongyoon Hwang|Dongyoon Hwang]]"
  - "[[Literature/Authors/Vassilissa Lehoux‐Lebacque|Vassilissa Lehoux]]"
  - "[[Literature/Authors/Jean-Michel Renders|Jean-Michel Renders]]"
  - "[[Literature/Authors/Maarten de Rijke|Maarten de Rijke]]"
publication date: 2024-04-08 
source: "https://arxiv.org/html/2311.16586"
doi: 10.1145/3656481
read status: Todo
---

## Abstract

Simulators can provide valuable insights for researchers and practitioners who wish to improve recommender systems, because they allow one to easily tweak the experimental setup in which recommender systems operate, and as a result lower the cost of identifying general trends and uncovering novel findings about the candidate methods. A key requirement to enable this accelerated improvement cycle is that the simulator is able to span the various sources of complexity that can be found in the real recommendation environment that it simulates. With the emergence of interactive and data-driven methods—e.g., reinforcement learning or online and counterfactual learning-to-rank—that aim to achieve user-related goals beyond the traditional accuracy-centric objectives, adequate simulators are needed. In particular, such simulators must model the various mechanisms that render the recommendation environment dynamic and interactive, e.g., the effect of recommendations on the user or the effect of biased data on subsequent iterations of the recommender system. We therefore propose SARDINE, a flexible and interpretable recommendation simulator that can help accelerate research in interactive and data-driven recommender systems. We demonstrate its usefulness by studying existing methods within nine diverse environments derived from SARDINE, and even uncover novel insights about them.

## Research Questions
> Research Questions extracted via LLM
- How can a recommender simulator represent dynamic, interactive effects such as recommendations changing users and feedback changing later data?[^r1]
- How do recommendation methods behave across the nine environments derived from SARDINE?[^r1]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?
- Cold-start sessions over fixed synthetic item/topic embeddings; the agent chooses a slate, the user clicks or skips, and enabled dynamics alter the user vector.[^r3]
- Items cover 2 or 3 topics; users cover 3, 4 or 5. Nonzero components start Uniform(0,1), then the vector is unit-normalized.[^r3]

```yml
World:
  items: [Item]
  user: Vector
  history: [Interaction]
  topic_timeouts: [TopicId -> 0..]

Item:
  embedding: Vector
  main_topic: TopicId

Vector: [0..1]
TopicId: u32

Interaction:
  step: u32
  slate: [ItemId]
  clicks: [bool]

Observation:
  Full:
    user: Vector
    histogram: Vector
    timeouts: Vector
  Partial:
    slate: [ItemId]
    clicks: [bool]
    histogram: Vector
```

### How does it work?
- First slate: random items from the simulator; later slates: the agent's policy. Return reward = click count and continue to session length. The typed rules below use environment settings in CAPS.[^r3]

```
click_probability(
  user: Vector,
  item: Item,
  rank: 1..
) -> 0..1:
  relevance = dot(item.embedding, user)
  attractiveness = ALPHA / (1 + exp(-LAMBDA * (relevance - MU)))
  out = attractiveness * EPSILON^(rank - 1)


clicked_influence(
  user: Vector,
  clicked: [Item]
) -> Vector:
  if clicked.is_empty(): ... # update unspecified in the paper
  else: out = OMEGA * user + (1 - OMEGA) * mean(clicked.embedding)
```

- Clicks are sampled Bernoulli at each rank. Influence is enabled by the chosen environment; `OMEGA` is the old-user weight (1 disables drift). When there are zero clicks, the source does not specify the clicked-item mean or resulting influence update; the note leaves that case undefined.[^r3][^r5]
- Boredom uses clicks in the last `T_B` steps, keeping at most the newest `N_B` clicks. A main-topic count **greater than** `TAU_B` triggers boredom.[^r3][^r5]
- Topic-loss zeros that component for `T_B` steps and restores its old value; churn-and-return zeros the entire vector for that duration.[^r3][^r5]
- The paper does not fully specify composition with influence or repeated timer resets.[^r3][^r5]
- Full observation: current user vector, `clip(topic_count / TAU_B, 0, 1)`, and remaining topic timeout divided by `T_B` (inactive topics use `T_B`). Partial: last slate IDs, click flags, same histogram.[^r3]
- Experiments use churn-and-return only. Table 3 varies settings: single/top-K sessions use `L=100`, `N_ITEMS=1000`, `N_TOPICS=10`; reranking uses `L=10`, `N_ITEMS=S=10`. Main click settings are `LAMBDA=100`, `MU=0.65`, `ALPHA=1`, `EPSILON=0.85`; uncertain slate variants use `LAMBDA ∈ {10,5,2}`, and reranking uses `LAMBDA=5`, `MU=0.30`. Dynamic settings use `N_B=10`, `T_B=5`, `TAU_B=5`; enabled influence uses `OMEGA=0.95`. The study compares Random, Greedy Oracle, REINFORCE (with Top-K for slates), SAC (with Top-K, GeMS, or single-item), and HAC. RL agents train for 500,000 recommendation steps; evaluation uses five seeds and 25 new-user episodes per checkpoint at 50,000-step intervals.[^r4]
- ⚠️ Churn prose claims zero clicks, but the printed sigmoid yields positive click probability at zero relevance. No extra no-click gate is imposed here.[^r5]

### What can it answer?
- Compare methods across nine configurations, measuring cumulative clicks and bored steps; vary bias, uncertainty, state observability and long-term dynamics.[^r4]
- Results expose distinct trade-offs: in static single-item recommendation, Greedy Oracle returns 100 and SAC approaches it by 200,000 steps; with boredom and influence, Greedy Oracle is about 50 return/50 bored steps while SAC reaches near 70 with low, declining boredom. On SlateTopK-Bored, SAC + Top-K beats the greedy oracle by a wide margin and has the least boredom; using matrix-factorization rather than ideal embeddings sharply reduces its return to around oracle level, while SAC + GeMS is less affected. With influence added, HAC falls below Greedy Oracle and SAC + GeMS. Under partial observability, transformer encoders improve over GRU for slate top-K but both remain below the oracle; in uncertain environments, transformer performance is maintained around 125 return at λ=10 and both SAC + Top-K variants beat the oracle at λ=5, while λ=2 makes random recommendation competitive. In reranking, PBM reaches 21.17 versus Greedy Oracle 21.45 on the static environment, while dCTR reaches 9.28; on the bored environment SAC reaches 14.82 versus PBM 13.14 and Greedy Oracle 13.69. PBM's normalized-propensity MSE worsens from 0.570 static to 0.915 with boredom.[^r6]

### Where does it apply?
- Synthetic interactive recommendation benchmarks. Agent architectures, training settings and remaining per-environment settings are omitted; no real-world behavioral validity is established.[^r4]

## Metadata
### References
- [[Thompson Sampling for Contextual Bandits with Linear Payoffs|Thompson Sampling for Contextual Bandits with Linear Payoffs]]
- [[Algorithmic Effects on the Diversity of Consumption on Spotify|Algorithmic Effects on the Diversity of Consumption on Spotify]]
- [[Bootstrapped Personalized Popularity for Cold Start Recommender Systems|Bootstrapped Personalized Popularity for Cold Start Recommender Systems]]
- [[From a “Cold” to a “Warm” Start in Recommender systems|From a “Cold” to a “Warm” Start in Recommender systems]]
- [[Top-K Off-Policy Correction for a REINFORCE Recommender System|Top-K Off-Policy Correction for a REINFORCE Recommender System]]
- [[Click Models for Web Search|Click Models for Web Search]]
- [[The Effect of People Recommenders on Echo Chambers and Polarization|The Effect of People Recommenders on Echo Chambers and Polarization]]
- [[An Experimental Comparison of Click Position-Bias Models|An Experimental Comparison of Click Position-Bias Models]]
- [[An Offline Metric for the Debiasedness of Click Models|An Offline Metric for the Debiasedness of Click Models]]
- [[Offline Evaluation for Reinforcement Learning-Based Recommendation- A Critical Issue and Some Alternatives|Offline Evaluation for Reinforcement Learning-Based Recommendation: A Critical Issue and Some Alternatives]]
- [[Generative Slate Recommendation with Reinforcement Learning|Generative Slate Recommendation with Reinforcement Learning]]
- [[Alleviating Matthew Effect of Offline Reinforcement Learning in Interactive Recommendation|Alleviating Matthew Effect of Offline Reinforcement Learning in Interactive Recommendation]]
- [[Recent Advances in the Foundations and Applications of Unbiased Learning to Rank|Recent Advances in the Foundations and Applications of Unbiased Learning to Rank]]
- [[Soft Actor-Critic- Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor|Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor]]
- [[Interactive Recommender Systems- A Survey of the State of the Art and Future Research Challenges and Opportunities|Interactive Recommender Systems: A Survey of the State of the Art and Future Research Challenges and Opportunities]]
- [[Session-based Recommendations with Recurrent Neural Networks|Session-based Recommendations with Recurrent Neural Networks]]
- [[State Encoders in Reinforcement Learning for Recommendation- A Reproducibility Study|State Encoders in Reinforcement Learning for Recommendation: A Reproducibility Study]]
- [[Keeping Dataset Biases out of the Simulation- A Debiased Simulator for Reinforcement Learning Based Recommender Systems|Keeping Dataset Biases out of the Simulation: A Debiased Simulator for Reinforcement Learning Based Recommender Systems]]
- [[Learning User Preferences in Non-Stationary Environments|Learning User Preferences in Non-Stationary Environments]]
- [[SlateQ- A Tractable Decomposition for Reinforcement Learning with Recommendation Sets|SlateQ: A Tractable Decomposition for Reinforcement Learning with Recommendation Sets]]
- [[RecSim- A Configurable Simulation Platform for Recommender Systems|RecSim: A Configurable Simulation Platform for Recommender Systems]]
- [[Recommender Systems — beyond Matrix Completion|Recommender Systems — beyond Matrix Completion]]
- [[A Common Misassumption in Online Experiments with Machine Learning Models|A Common Misassumption in Online Experiments with Machine Learning Models]]
- [[Unbiased Learning-to-Rank with Biased Feedback|Unbiased Learning-to-Rank with Biased Feedback]]
- [[SCOPE-RL- A Python Library for Offline Reinforcement Learning, Off-Policy Evaluation, and Policy Selection|SCOPE-RL: A Python Library for Offline Reinforcement Learning, Off-Policy Evaluation, and Policy Selection]]
- [[A Lightweight Method for Modeling Confidence in Recommendations with Learned Beta Distributions|A Lightweight Method for Modeling Confidence in Recommendations with Learned Beta Distributions]]
- [[Towards Validating Long-Term User Feedbacks in Interactive Recommendation Systems|Towards Validating Long-Term User Feedbacks in Interactive Recommendation Systems]]
- [[A Contextual-Bandit Approach to Personalized News Article Recommendation|A Contextual-Bandit Approach to Personalized News Article Recommendation]]
- [[Continuous control with deep reinforcement learning|Continuous control with deep reinforcement learning]]
- [[Exploration and Regularization of the Latent Action Space in Recommendation|Exploration and Regularization of the Latent Action Space in Recommendation]]
- [[Cold-start, warm-start and everything in between- An autoencoder based approach to recommendation|Cold-start, warm-start and everything in between: An autoencoder based approach to recommendation]]
- [[Deployment-Efficient Reinforcement Learning via Model-Based Offline Optimization|Deployment-Efficient Reinforcement Learning via Model-Based Offline Optimization]]
- [[Being Accurate is Not Enough- How Accuracy Metrics Have Hurt Recommender Systems|Being Accurate is Not Enough: How Accuracy Metrics Have Hurt Recommender Systems]]
- [[Algorithmic Balancing of Familiarity, Similarity, & Discovery in Music Recommendations|Algorithmic Balancing of Familiarity, Similarity, & Discovery in Music Recommendations]]
- [[Recommender Systems|Recommender Systems]]
- [[Computationally Efficient Optimization of Plackett-Luce Ranking Models for Relevance and Fairness|Computationally Efficient Optimization of Plackett-Luce Ranking Models for Relevance and Fairness]]
- [[Robust Generalization and Safe Query-Specialization in Counterfactual Learning to Rank|Robust Generalization and Safe Query-Specialization in Counterfactual Learning to Rank]]
- [[Reinforcement Learning Algorithm for Non-stationary Environments|Reinforcement Learning Algorithm for Non-stationary Environments]]
- [[RecoGym- A Reinforcement Learning Environment for the problem of Product Recommendation in Online Advertising|RecoGym: A Reinforcement Learning Environment for the problem of Product Recommendation in Online Advertising]]
- [[Active Learning in Recommender Systems|Active Learning in Recommender Systems]]
- [[Open Bandit Dataset and Pipeline- Towards Realistic and Reproducible Off-Policy Evaluation|Open Bandit Dataset and Pipeline: Towards Realistic and Reproducible Off-Policy Evaluation]]
- [[Fast Slate Policy Optimization- Going Beyond Plackett-Luce|Fast Slate Policy Optimization: Going Beyond Plackett-Luce]]
- [[MARS-Gym- A Gym Framework to Model, Train, and Evaluate Recommender Systems for Marketplaces|MARS-Gym: A Gym Framework to Model, Train, and Evaluate Recommender Systems for Marketplaces]]
- [[Online Evaluation Methods for the Causal Effect of Recommendations|Online Evaluation Methods for the Causal Effect of Recommendations]]
- [[Semantic Conceptions of Information|Semantic Conceptions of Information]]
- [[Virtual-Taobao- Virtualizing Real-World Online Retail Environment for Reinforcement Learning|Virtual-Taobao: Virtualizing Real-World Online Retail Environment for Reinforcement Learning]]
- [[Multi-Armed Bandits in Recommendation Systems- A Survey of the State-of-the-art and Future Directions|Multi-Armed Bandits in Recommendation Systems: A Survey of the State-of-the-art and Future Directions]]
- [[Take a Fresh Look at Recommender Systems from an Evaluation Standpoint|Take a Fresh Look at Recommender Systems from an Evaluation Standpoint]]
- [[Off-Policy Evaluation for Slate Recommendation|Off-Policy Evaluation for Slate Recommendation]]
- [[Gymnasium|Gymnasium]]
- [[RL4RS- A Real-World Dataset for Reinforcement Learning Based Recommender System|RL4RS: A Real-World Dataset for Reinforcement Learning Based Recommender System]]
- [[A Comprehensive Survey of Continual Learning- Theory, Method and Application|A Comprehensive Survey of Continual Learning: Theory, Method and Application]]
- [[Learning Robust Recommenders through Cross-Model Agreement|Learning Robust Recommenders through Cross-Model Agreement]]
- [[Rethinking Reinforcement Learning for Recommendation- A Prompt Perspective|Rethinking Reinforcement Learning for Recommendation: A Prompt Perspective]]
- [[Evaluating Recommender Systems- Survey and Framework|Evaluating Recommender Systems: Survey and Framework]]

## Audit Log
- 2026-10-03: Independent full-source re-audit passed. Source mechanisms, settings, outcomes and all 55 references checked; the unsupported zero-click transition was removed and source gaps remain explicit. `audit failed` removed after the pass.
- Audit invalidated (2026-09-30): auditor admitted clearing flags before completing independent source checks. A new independent audit is required.
- Strong source review (2026-09-30): Fixed influence guard/parameter consistency, explicit click formula and normalized observation definitions; distinguished both boredom variants from churn-only experiments; recorded missing empty-click/composition rules and nonzero sigmoid-at-zero conflict. Independent re-audit pending.
- Initial independent audit: failed on missing model mechanisms, abstract fidelity, or source-access reporting; see `vault/.automation/audit/next-forty-54-66-initial-2026-09-30.json`. Revisions added source-located model detail; independent re-audit remains pending.

- WITHDRAWN audit claim (2026-09-30): previously reported PASS; source claims, current extraction, metadata, references and footnotes checked against the available primary source. See `vault/.automation/audit/remaining-audit-b-2026-09-30.json`.

## LLM Justification
[^r1]: The paper’s abstract, at https://arxiv.org/abs/2311.16586. The questions paraphrase the stated purpose, research scope, and reported approach.
[^r3]: Deffayet et al., §§2–3.5: session sequence, sparse normalized embeddings, Eqs. (1)–(2), position-based Bernoulli clicks; boredom/influence and exact observation vectors. Full text: https://arxiv.org/html/2311.16586.
[^r4]: Deffayet et al., §4.1/Table 2 (nine variants, experiments use churn-and-return), §4.3/Table 3 (environment settings), §4.4 (return/boredom metrics), §1.3 (no human-mind/live-performance guarantee). Full text: https://arxiv.org/html/2311.16586.
[^r5]: Source conflict/underspecification: §3.4 influence divides by the number of clicked items without stating the zero-click case; simultaneous boredom/influence composition and repeated timeout handling are not fully stated. Churn is said to imply no clicks, but §3.3 Eq. (2) and the position-based rule give ALPHA/(1+exp(LAMBDA*MU))*EPSILON^(rank-1)>0 for finite settings. The zero-click mean and resulting update remain unspecified; no update behavior is inferred. Full text: https://arxiv.org/html/2311.16586.

[^r6]: §§5.1–5.3, Figures 2–6 and Table 4: single-item returns/boredom and partial-observability comparisons; slate top-K results under ideal versus matrix-factorization embeddings, influence, partial state and λ uncertainty; reranking protocol, returns, and normalized-propensity MSE. Five seeded runs are reported for validation results.
