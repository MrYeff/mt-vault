---
title: "RecSim NG: Toward Principled Uncertainty Modeling for Recommender Ecosystems"
authors:
  - "[[Literature/Authors/Martin Mladenov|Martin Mladenov]]"
  - "[[Literature/Authors/Chih‐Wei Hsu|Chih‐Wei Hsu]]"
  - "[[Literature/Authors/Vihan Jain|Vihan Jain]]"
  - "[[Literature/Authors/Eugene Ie|Eugene Ie]]"
  - "[[Literature/Authors/Christopher Colby|Christopher Colby]]"
  - "[[Literature/Authors/Nicolas Mayoraz|Nicolas Mayoraz]]"
  - "[[Literature/Authors/Hubert Pham|Hubert Pham]]"
  - "[[Literature/Authors/Dustin Tran|Dustin Tran]]"
  - "[[Literature/Authors/Ivan Vendrov|Ivan Vendrov]]"
  - "[[Literature/Authors/Craig E. Boutilier|Craig E. Boutilier]]"
source: "https://arxiv.org/html/2103.08057"
doi: "10.48550/arXiv.2103.08057"
publication date: "2021-03-14"
tags:
  - "model"
  - "simulation"
  - "recommender_systems"
read status: Todo
---

## Abstract

The development of recommender systems that optimize multi-turn interaction with users, and model the interactions of different agents (e.g., users, content providers, vendors) in the recommender ecosystem have drawn increasing attention in recent years. Developing and training models and algorithms for such recommenders can be especially difficult using static datasets, which often fail to offer the types of counterfactual predictions needed to evaluate policies over extended horizons. To address this, we develop RecSim NG, a probabilistic platform for the simulation of multi-agent recommender systems. RecSim NG is a scalable, modular, differentiable simulator implemented in Edward2 and TensorFlow. It offers: a powerful, general probabilistic programming language for agent-behavior specification; tools for probabilistic inference and latent-variable model learning, backed by automatic differentiation and tracing; and a TensorFlow-based runtime for running simulations on accelerated hardware. We describe RecSim NG and illustrate how it can be used to create transparent, configurable, end-to-end models of a recommender ecosystem, complemented by a small set of simple use cases that demonstrate how RecSim NG can help both researchers and practitioners easily develop and train novel algorithms for recommender systems.

## Research Questions
> Research Questions extracted via LLM

- How can uncertainty and multi-agent interactions be represented in recommender ecosystem simulations?[^r1]
- How can probabilistic program specifications support inference, learning, and policy evaluation across interaction horizons?[^r1]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?
- RecSim NG is a probabilistic framework for configurable recommender ecosystems, with users, recommenders and optional providers; each application supplies behavior.[^n1]

### How does it work?
The framework factors its Markov state into variables with initial distributions, transition kernels, and dependencies.[^n1]

```yml
World:
  variables: [Variable]
  entities: [Entity]

Variable:
  state: ... # application-defined value
  initial: Distribution
  transition: Distribution
  current_parents: [VariableId]
  previous_parents: [VariableId]

Entity:
  parameters: ... # shared batched population parameters
  behaviors: ... # application-supplied conditional distributions

Distribution: ...
```

- Sample current-step variables in dependency order, conditioning on their specified current-step and previous-step parents. The runtime sees all state; an individual agent only receives variables exposed to its behavior, allowing latent/partially observed state.[^n1]
- An **entity** encapsulates a population's parameters and behavior methods. A **story** creates variables/entities, binds behavior to initial/transition distributions and declares information flow. Choice models map affinities to greedy, multinomial-logit, cascade or Plackett–Luce selection; state models may be static, dynamic or belief estimators.[^n2]

The following is the specific §3.3 user example, rather than a universal RecSim NG behavioral law.[^n3]

```yml
User:
  interest: [f64]
  sensitivity: f64

Item:
  features: [f64]
  quality: -1..1
```

```
sim_step(
  mut user: User,
  slate: [Item]
):
  weights = exp(-euclidean(item.features, user.interest))
    for item in slate
  item = sample(slate, normalize(weights))
  noise = sample(gaussian_noise)
  user.interest += user.sensitivity * item.quality * (
    item.features-user.interest
  ) + noise
```

- The example initializes interest with a unit-normal vector. Quality is observed only after consumption and affects interest movement, while choice depends on feature distance. Gaussian noise is added to the interest update; its covariance and the sensitivity/slate values are not specified in this source.[^n3]
- The §4.3 ecosystem example instead holds user interests static and samples provider/user communities. MNL choice gives consumed-item utility as affinity plus Gaussian noise; provider discounted engagement determines how much content it generates. Compare myopic affinity ranking with a capped provider boost intended to favor low-engagement providers.[^n4]
- Reporting tension: the boost paragraph says it increases with provider engagement minus mean engagement, yet describes increased exposure for low-engagement providers. The exact direction cannot be inferred from that prose alone.[^n5]
- In §4.1, the partially observed policy embeds a finite history of the last 15 consumed items and engagement, learns a belief representation of latent user interests, and uses REINFORCE. The illustrative run uses slate size 2, item dimension 20, batches of 1,000 users and horizon 100; Figure 1 averages over 20 runs.[^n7]
- In §4.2, the learning example holds each user's interest vector static but evolves satisfaction according to whether the best-affinity item on the current slate improves or worsens relative to the previous slate; a user-specific latent sensitivity controls the normal update mean. A fixed randomized recommender generates trajectories; the learning model uses Monte Carlo EM with Hamiltonian Monte Carlo, initializing sensitivity from Uniform(0,1).[^n8]
- This extraction omits complete inference/learning APIs, other use-case implementations, and fitted behavior parameters. Generic transitions and recommendations are supplied by the story; the code above instantiates only the stated user example.[^n1][^n2][^n3]

### What can it answer?
- It supports trajectory simulation, probabilistic inference, latent-model learning, and policy comparison. The paper illustrates latent-state estimation, learning from trajectories, and long-horizon ecosystem utility.[^n6]

### Where does it apply?
- It applies when ecosystem behavior and uncertainty can be specified as a probabilistic program; results depend on the chosen entities, dependencies and story.[^n1][^n2]

## Metadata
### References
- [[WES- Agent-based User Interaction Simulation on Real Infrastructure|WES: Agent-based User Interaction Simulation on Real Infrastructure]]
- [[The Arcade Learning Environment- An Evaluation Platform for General Agents|The Arcade Learning Environment: An Evaluation Platform for General Agents]]
- [[From Recommendation Systems to Facility Location Games|From Recommendation Systems to Facility Location Games]]
- [[A Game-Theoretic Approach to Recommendation Systems with Strategic Content Providers|A Game-Theoretic Approach to Recommendation Systems with Strategic Content Providers]]
- [[Equity of Attention- Amortizing Individual Fairness in Rankings|Equity of Attention: Amortizing Individual Fairness in Rankings]]
- [[Pyro- Deep universal probabilistic programming|Pyro: Deep universal probabilistic programming]]
- [[Pattern Recognition and Machine Learning |Pattern Recognition and Machine Learning ]]
- [[Farm- Architecture for Distributed Agent-based Social Simulations|Farm: Architecture for Distributed Agent-based Social Simulations]]
- [[Latent Variable Session-Based Recommendation|Latent Variable Session-Based Recommendation]]
- [[Differentiable Meta-Learning of Bandit Policies|Differentiable Meta-Learning of Bandit Policies]]
- [[Empirical Analysis of Predictive Algorithms for Collaborative Filtering|Empirical Analysis of Predictive Algorithms for Collaborative Filtering]]
- [[OpenAI Gym|OpenAI Gym]]
- [[Dopamine- A Research Framework for Deep Reinforcement Learning|Dopamine: A Research Framework for Deep Reinforcement Learning]]
- [[Top-K Off-Policy Correction for a REINFORCE Recommender System|Top-K Off-Policy Correction for a REINFORCE Recommender System]]
- [[Reinforcement Learning-based Recommender System using Biclustering Technique|Reinforcement Learning-based Recommender System using Biclustering Technique]]
- [[Learning to Interact with Users- A Collaborative-Bandit Approach|Learning to Interact with Users: A Collaborative-Bandit Approach]]
- [[Towards Conversational Recommender Systems|Towards Conversational Recommender Systems]]
- [[Deep Neural Networks for YouTube Recommendations|Deep Neural Networks for YouTube Recommendations]]
- [[A Model for Reasoning about Persistence and Causation|A Model for Reasoning about Persistence and Causation]]
- [[Challenges of Real-World Reinforcement Learning|Challenges of Real-World Reinforcement Learning]]
- [[Modeling Agents with Probabilistic Programs|Modeling Agents with Probabilistic Programs]]
- [[Horizon- Facebook’s Open Source Applied Reinforcement Learning Platform|Horizon: Facebook’s Open Source Applied Reinforcement Learning Platform]]
- [[Online Clustering of Bandits|Online Clustering of Bandits]]
- [[The Design and Implementation of Probabilistic Programming Languages|The Design and Implementation of Probabilistic Programming Languages]]
- [[The MovieLens Datasets- History and Context|The MovieLens Datasets: History and Context]]
- [[Neural Collaborative Filtering|Neural Collaborative Filtering]]
- [[SlateQ- A Tractable Decomposition for Reinforcement Learning with Recommendation Sets|SlateQ: A Tractable Decomposition for Reinforcement Learning with Recommendation Sets]]
- [[Reinforcement Learning for Slate-based Recommender Systems- A Tractable Decomposition and Practical Methodology|Reinforcement Learning for Slate-based Recommender Systems: A Tractable Decomposition and Practical Methodology]]
- [[RecSim- A Configurable Simulation Platform for Recommender Systems|RecSim: A Configurable Simulation Platform for Recommender Systems]]
- [[GroupLens- Applying Collaborative Filtering to Usenet News|GroupLens: Applying Collaborative Filtering to Usenet News]]
- [[Monitoring a Complex Physical System using a Hybrid Dynamic Bayes Net|Monitoring a Complex Physical System using a Hybrid Dynamic Bayes Net]]
- [[Collaborative Filtering Bandits|Collaborative Filtering Bandits]]
- [[Building Personalized Simulator for Interactive Search|Building Personalized Simulator for Interactive Search]]
- [[Latent Bandits|Latent Bandits]]
- [[Optimizing Long-term Social Welfare in Recommender Systems- A Constrained Matching Approach|Optimizing Long-term Social Welfare in Recommender Systems: A Constrained Matching Approach]]
- [[Advantage Amplification in Slowly Evolving Latent-State Environments|Advantage Amplification in Slowly Evolving Latent-State Environments]]
- [[MCMC using Hamiltonian dynamics|MCMC using Hamiltonian dynamics]]
- [[Deep Dyna-Q- Integrating Planning for Task-Completion Dialogue Policy Learning|Deep Dyna-Q: Integrating Planning for Task-Completion Dialogue Policy Learning]]
- [[Object-oriented Bayesian Networks|Object-oriented Bayesian Networks]]
- [[RecoGym- A Reinforcement Learning Environment for the problem of Product Recommendation in Online Advertising|RecoGym: A Reinforcement Learning Environment for the problem of Product Recommendation in Online Advertising]]
- [[A Hidden Markov Model for Collaborative Filtering|A Hidden Markov Model for Collaborative Filtering]]
- [[Probabilistic Matrix Factorization|Probabilistic Matrix Factorization]]
- [[An MDP-based Recommender System|An MDP-based Recommender System]]
- [[Virtual-Taobao- Virtualizing Real-world Online Retail Environment for Reinforcement Learning|Virtual-Taobao: Virtualizing Real-world Online Retail Environment for Reinforcement Learning]]
- [[Fairness of Exposure in Rankings|Fairness of Exposure in Rankings]]
- [[Conversational Recommender System|Conversational Recommender System]]
- [[Usage-based Web Recommendations- A Reinforcement Learning Approach|Usage-based Web Recommendations: A Reinforcement Learning Approach]]
- [[Improved Recurrent Neural Networks for Session-based Recommendations|Improved Recurrent Neural Networks for Session-based Recommendations]]
- [[ELF- An Extensive, Lightweight and Flexible Research Platform for Real-time Strategy Games|ELF: An Extensive, Lightweight and Flexible Research Platform for Real-time Strategy Games]]
- [[Bayesian layers- A module for neural network uncertainty|Bayesian layers: A module for neural network uncertainty]]
- [[Simple, Distributed, and Accelerated Probabilistic Programming|Simple, Distributed, and Accelerated Probabilistic Programming]]
- [[Deep probabilistic programming|Deep probabilistic programming]]
- [[Optimization of Large-Scale Agent-Based Simulations Through Automated Abstraction and Simplification|Optimization of Large-Scale Agent-Based Simulations Through Automated Abstraction and Simplification]]
- [[Deep Content-based Music Recommendation|Deep Content-based Music Recommendation]]
- [[AirDialogue- An Environment for Goal-oriented Dialogue Research|AirDialogue: An Environment for Goal-oriented Dialogue Research]]
- [[Simple statistical gradient-following algorithms for connectionist reinforcement learning|Simple statistical gradient-following algorithms for connectionist reinforcement learning]]
- [[Recurrent Recommender Networks|Recurrent Recommender Networks]]
- [[Mixed Negative Sampling for Learning Two-tower Neural Networks in Recommendations|Mixed Negative Sampling for Learning Two-tower Neural Networks in Recommendations]]
- [[Measuring Fairness in Ranked Outputs|Measuring Fairness in Ranked Outputs]]
- [[Measuring Recommender System Effects with Simulated Users|Measuring Recommender System Effects with Simulated Users]]
- [[FA-IR- A Fair Top-k Ranking Algorithm|FA*IR: A Fair Top-k Ranking Algorithm]]
- [[Toward Simulating Environments in Reinforcement Learning Based Recommendations|Toward Simulating Environments in Reinforcement Learning Based Recommendations]]
- [[Deep Reinforcement Learning for Page-wise Recommendations|Deep Reinforcement Learning for Page-wise Recommendations]]
- [[The AI Economist- Improving Equality and Productivity with AI-Driven Tax Policies|The AI Economist: Improving Equality and Productivity with AI-Driven Tax Policies]]

## Audit Log
- 2026-10-03: Independent full-source re-audit passed. Full primary source, three use cases and 64 references checked; unsupported covariance wording corrected and independently rechecked. `audit failed` removed after the pass.
- Audit invalidated (2026-09-30): auditor admitted relying on spot checks and previous reports before clearing flags. A full independent audit is still required.
- 2026-09-30: Full-source design audit found schema concealed current/past dependency and story mechanics; no concrete example despite full source availability; specific-example mechanism not distinguishable from universal behavior; provider boost direction prose tension unreported. Corrected against the source passages below; independent re-audit pending.[^design]
- Independent source audit found framework interface/runtime semantics and example-specific state/update structure missing. The note now distinguishes factored DBN state, runtime trajectories, inference/learning, and the example-specific satisfaction/provider model. At that stage, independent re-audit remained pending.

- WITHDRAWN audit claim (2026-09-30): incomplete source checks; this audit does not establish a pass.

## LLM Justification
[^r1]: The research questions are a concise transformation of the primary source’s abstract and stated aims. Source location: Sections 2–4 and use cases. Source: [RecSim NG: Toward Principled Uncertainty Modeling for Recommender Ecosystems](https://arxiv.org/abs/2103.08057).


[^n1]: §3.1 defines factored Markov state, initial densities, conditional transition factors and intra/inter-slice parents; runtime observability is distinct from an agent observation subset.

[^n2]: §3.2 defines Entities, Behaviors, and Stories with the user/recommender dependency example; §3.3 describes affinity/choice models and static/dynamic/belief-state building blocks.

[^n3]: §3.3 Illustration: unit-normal interest, item feature vector and quality [-1,1], choice proportional to exp(-Euclidean distance), and S_next=S+λ*q*(F-S)+Gaussian noise; quality is observed upon consumption.

[^n4]: §4.3 Ecosystem Modeling: static user interests, MNL choice, noisy-affinity utility, provider/community mixture, discounted engagement-dependent generation, myopic and capped provider-aware policies.

[^n5]: §4.3 second-policy paragraph says the boost increases/decreases proportionally to current engagement minus mean engagement, but then says it raises low-engagement recommendation odds. Both source statements are retained; this note does not choose an implementation.

[^n6]: §3.4 and §§4.1–4.3 describe inference, model learning and ecosystem-policy use cases.

[^n7]: §4.1 Partially Observable RL and Figure 1/caption: 15-item history, policy-gradient REINFORCE, slate size 2, dimension 20, 1,000 users per batch, horizon 100, and average across 20 runs.

[^n8]: §4.2 Learning Latent Variable Models: static latent interests, dynamic satisfaction driven by adjacent-slate affinity trend, per-user sensitivity, randomized data-generation policy, Uniform(0,1) learned-model sensitivity initialization, and HMC posterior sampling in Monte Carlo EM. The full tutorial model specification is external and not reproduced in the paper.

[^design]: Source audit checked the full text at https://arxiv.org/html/2103.08057. Model footnotes identify the passages supporting the corrections.
