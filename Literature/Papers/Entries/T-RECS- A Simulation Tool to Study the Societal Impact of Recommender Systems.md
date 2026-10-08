---
title: "T-RECS: A Simulation Tool to Study the Societal Impact of Recommender Systems"
tags:
  - recommender_system
  - simulation_framework
  - "model"
  - "simulation"
authors:
  - "[[Literature/Authors/Eli Lucherini|Eli Lucherini]]"
  - "[[Literature/Authors/Matthew Sun|Matthew Sun]]"
  - "[[Literature/Authors/Amy Winecoff|Amy Winecoff]]"
  - "[[Literature/Authors/Arvind Narayanan|Arvind Narayanan]]"
publication date: 2021-07-19 
source: "https://arxiv.org/html/2107.08959"
doi: 10.48550/arxiv.2107.08959
read status: Todo
---

## Abstract

Simulation has emerged as a popular method to study the long-term societal consequences of recommender systems. This approach allows researchers to specify their theoretical model explicitly and observe the evolution of system-level outcomes over time. However, performing simulation-based studies often requires researchers to build their own simulation environments from the ground up, which creates a high barrier to entry, introduces room for implementation error, and makes it difficult to disentangle whether observed outcomes are due to the model or the implementation. We introduce T-RECS, an open-sourced Python package designed for researchers to simulate recommendation systems and other types of sociotechnical systems in which an algorithm mediates the interactions between multiple stakeholders, such as users and content creators. To demonstrate the flexibility of T-RECS, we perform a replication of two prior simulation-based research on sociotechnical systems. We additionally show how T-RECS can be used to generate novel insights with minimal overhead. Our tool promotes reproducibility in this area of research, provides a unified language for simulating sociotechnical systems, and removes the friction of implementing simulations from scratch.

## Research Questions
> Research Questions extracted via LLM
- Can a common open-source simulation package reduce implementation overhead and support replication of recommender-system studies?[^r1]
- How can T-RECS express user, recommender, and content-creator interactions in sociotechnical simulations?[^r1]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?
- A configurable user–algorithm feedback framework with users, items, a model and metrics; content creators are optional. Actual preferences/scores and model-predicted preferences/scores are distinct.[^r3]
- Actual preferences and actual scores are hidden from the recommender; the model infers its own representations.[^r6]
- The types are framework interfaces; distributions, scoring and behavior are selected by the researcher.[^r3]

```yml
World:
  users: [User]
  items: [Item]
  model: Model
  creators: [Creator]
  metrics: [Metric]

User:
  actual_preferences: [f64]
  actual_scores: [ItemId -> f64]

Item:
  attributes: [f64]

Model:
  predicted_preferences: [UserId -> [f64]]
  predicted_scores: [UserId -> [ItemId -> f64]]
  state: ()

Creator:
  item_distribution: ()

Feedback:
  user: UserId
  item: ItemId
  response: ()

Metric: ()
```

### How does it work?
- Predict scores (default inner product), present items, obtain feedback from actual preferences, update model state and record metrics. Optional random interleaving and treatment of newly created items depend on the configured presentation policy.[^r3]
- The event loop skips steps with no interactions. By default each user supplies one feedback per step and users are processed in parallel; a step has no fixed time duration.[^r3]
- This procedure names the configurable interfaces and follows §4.1's order. It omits creator item production/adaptation, dynamic-user updates and the separate start-up phase.[^r3][^r6]

```
sim_step(mut world: World):
  world.model.predict(world.users, world.items)
  slates = PRESENTATION_POLICY(world.model.predicted_scores)
  feedback = USER_FEEDBACK(world.users, slates)
  world.model.update(feedback)
  METRICS.record(mut world.metrics, world, feedback)
```

- Default creators generate each binary item attribute independently as Bernoulli with the creator’s attribute-specific probability; an optional creator probability controls whether an item is produced at a step.[^r5]
- Creators sample item attributes from probabilistic distributions. Their incentives/adaptation are configurable; §5.4 specifically demonstrates distributions adapting to the attributes of consumed items, rather than prescribing this as a universal default.[^r3][^r4]
- When dynamic preferences are enabled, the default update rotates the user's preference vector toward the consumed item's vector using spherical interpolation; custom drift functions are possible.[^r6]
- Default start-up presents random items and skips score prediction. The model trains on the collected interactions at phase end; start-up strategies are configurable.[^r6]

### Case-study settings and outcomes
- **Algorithmic confounding.** The replicated environment has 100 users with 20 attributes and 1,000 items with 20 attributes; user/item vectors use source-specified Dirichlet draws, and true item utility is sampled from a Beta distribution whose mean is the user–item attribute dot product. Users receive imperfect known utilities. Runs last 100 steps, adding 10 new items per step. Random startup lasts 50 steps before one training in the single-training condition, versus 10 steps before retraining each step in the repeated condition. The authors average 400 trials per recommender/mode using matched underlying profiles and utilities across recommenders. Homogenization is average interaction-set Jaccard similarity for user pairs matched by the model’s inferred similarity, relative to ideal recommendations. Repeated training increases homogenization; random recommendations resemble ideal on this metric.[^r7]
- **Structural virality.** The SIR-like diffusion model uses scale-free networks of 1,000,000 users (rather than the source study’s 25,000,000), 25 generated graphs for each power-law exponent `α ∈ {2.1, 2.3, 2.5, 2.7, 2.9}`, and reproduction values `r ∈ {0.1, 0.3, 0.5, 0.7, 0.9}`. For each run, a random seed user is infected; infection then spreads independently across susceptible contacts, with recovery preventing later spread. About 2.1 million simulations measure cascades with at least 100 infected users and structural virality among those popular cascades. Results are qualitatively similar to Goel et al.; at `r ≈ 0.5, α ≈ 2.3`, popularity probability is about 0.1%, mean structural virality about 3.7, and size/virality correlation in this replication is about 0.086.[^r7]
- **Adaptive creators.** Creator profile vectors start as `γᵢ ~ Dirichlet(10⃗)` and item-attribute distributions as `αᵢ ~ Dirichlet(0.1γᵢ)`; profiles shift toward items that received interactions in the latest step. This is one proposed interaction-maximizing adaptation, not a universal creator law. Across six recommenders, 200 trials of 500 steps show creator entropy falling over time, especially under social-filtering and popularity recommenders. Their average pairwise distance between users’ mean consumed-item vectors also rises beyond the ideal-utility comparison for non-ideal recommenders. The paper distinguishes this within-creator narrowing from convergence between creators and cautions that “homogenization” is not necessarily normatively harmful.[^r7][^r8]

### What can it answer?
- Compare simulation assumptions and metrics. Demonstrations conceptually replicate algorithmic confounding and information diffusion, then extend the former with adaptive creators. These are conceptual/constructive replications, not exact reproductions; authors rebuilt from published descriptions and report operationalization ambiguities.[^r4][^r7]

### Where does it apply?
- Recommender-mediated systems and other user/item feedback systems. This summary omits the separate case-study equations/configurations; framework defaults do not validate real user or creator behavior.[^r3][^r4]

## Metadata
### References
- [[Multistakeholder recommendation- Survey and research directions|Multistakeholder recommendation: Survey and research directions]]
- [[Ensemble-based and hybrid recommender systems]]
- [[Discrimination through optimization- How Facebook’s Ad delivery can lead to biased outcomes|Discrimination through optimization: How Facebook’s Ad delivery can lead to biased outcomes]]
- [[Deconstructing the Filter Bubble- User Decision-Making and Recommender Systems|Deconstructing the Filter Bubble: User Decision-Making and Recommender Systems]]
- [[The complexity of cooperation- Agent-based models of competition and collaboration|The complexity of cooperation: Agent-based models of competition and collaboration]]
- [[Exposure to ideologically diverse news and opinion on Facebook]]
- [[A game-theoretic approach to recommendation systems with strategic content providers]]
- [[Learning from the behavior of others- Conformity, fads, and informational cascades|Learning from the behavior of others: Conformity, fads, and informational cascades]]
- [[Agent-based modeling- Methods and techniques for simulating human systems|Agent-based modeling: Methods and techniques for simulating human systems]]
- [[Multi-method modelling- AnyLogic|Multi-method modelling: AnyLogic]]
- [[SIREN- A simulation framework for understanding the effects of recommender systems in online news environments|SIREN: A simulation framework for understanding the effects of recommender systems in online news environments]]
- [[Multisided fairness for recommendation]]
- [[Balanced neighborhoods for multi-sided fairness in recommendation]]
- [[How Algorithmic Confounding in Recommendation Systems Increases Homogeneity and Decreases Utility]]
- [[Wide & deep learning for recommender systems]]
- [[How algorithmic popularity bias hinders or promotes quality]]
- [[Playing the visibility game- How digital influencers and algorithms negotiate influence on Instagram|Playing the visibility game: How digital influencers and algorithms negotiate influence on Instagram]]
- [[On the scientific superiority of conceptual replications for scientific progress]]
- [[Fairness is not static- deeper understanding of long term fairness via simulation studies|Fairness is not static: deeper understanding of long term fairness via simulation studies]]
- [[Agent-based models]]
- [[Recommendations and user agency- the reachability of collaboratively-filtered information|Recommendations and user agency: the reachability of collaboratively-filtered information]]
- [[LensKit for Python- Next-Generation Software for Recommender Systems Experiments|LensKit for Python: Next-Generation Software for Recommender Systems Experiments]]
- [[Growing artificial societies- social science from the bottom up|Growing artificial societies: social science from the bottom up]]
- [[How YouTube Radicalized Brazil]]
- [[Automated serendipity- The effect of using search engines on news repertoire balance and diversity|Automated serendipity: The effect of using search engines on news repertoire balance and diversity]]
- [[Rumor cascades]]
- [[Balancing information exposure in social networks]]
- [[The triple-filter bubble- Using agent-based modelling to test a meta-theoretical framework for the emergence of filter bubbles and echo chambers|The triple-filter bubble: Using agent-based modelling to test a meta-theoretical framework for the emergence of filter bubbles and echo chambers]]
- [[The structural virality of online diffusion]]
- [[Data voids- Where missing data can easily be exploited|Data voids: Where missing data can easily be exploited]]
- [[The Netflix Recommender System- Algorithms, Business Value, and Innovation|The Netflix Recommender System: Algorithms, Business Value, and Innovation]]
- [[Measuring personalization of web search]]
- [[The movielens datasets- History and context|The movielens datasets: History and context]]
- [[Array programming with NumPy]]
- [[Agent-based models and microsimulation]]
- [[Evaluating collaborative filtering recommender systems]]
- [[The Problem Isn’t Fake News, It’s Bad Algorithms — Here’s Why]]
- [[Evaluating the scale, growth, and origins of right-wing echo chambers on YouTube]]
- [[Collaborative filtering for implicit feedback datasets]]
- [[Novelty and diversity in top-n recommendation–analysis and evaluation]]
- [[RecSim- A Configurable Simulation Platform for Recommender Systems]]
- [[Powered by AI- Instagram’s Explore recommender system|Powered by AI: Instagram’s Explore recommender system]]
- [[Recommendations with a purpose]]
- [[Degenerate feedback loops in recommender systems]]
- [[Recommendation independence]]
- [[Do Offline Metrics Predict Online Performance in Recommender Systems-|Do Offline Metrics Predict Online Performance in Recommender Systems?]]
- [[Homophily and minority-group size explain perception biases in social networks]]
- [[Alternative influence- Broadcasting the reactionary right on YouTube|Alternative influence: Broadcasting the reactionary right on YouTube]]
- [[Opinion formation in the digital divide]]
- [[Modelling and simulation software to support individual-based ecological modelling]]
- [[These TikTok Creators Say They’re Still Being Suppressed for Posting Black Lives Matter Content]]
- [[RecSim NG- Toward Principled Uncertainty Modeling for Recommender Ecosystems]]
- [[How to compute the Wiener index of a graph]]
- [[Right-Wing YouTube- A Supply and Demand Perspective|Right-Wing YouTube: A Supply and Demand Perspective]]
- [[Alt-right pipeline- Individual journeys to extremism online|Alt-right pipeline: Individual journeys to extremism online]]
- [[An agent-based model of message propagation in the Facebook electronic social network]]
- [[Exploring the filter bubble- the effect of using recommender systems on content diversity|Exploring the filter bubble: the effect of using recommender systems on content diversity]]
- [[The filter bubble- How the new personalized web is changing what we read and how we think|The filter bubble: How the new personalized web is changing what we read and how we think]]
- [[Scikit-learn- Machine Learning in Python|Scikit-learn: Machine Learning in Python]]
- [[Modelling opinion dynamics in the age of algorithmic personalisation]]
- [[Getting to know you- learning new user preferences in recommender systems|Getting to know you: learning new user preferences in recommender systems]]
- [[BPR- Bayesian personalized ranking from implicit feedback|BPR: Bayesian personalized ranking from implicit feedback]]
- [[Auditing radicalization pathways on YouTube]]
- [[Introduction to recommender systems handbook]]
- [[Recogym- A reinforcement learning environment for the problem of product recommendation in online advertising|Recogym: A reinforcement learning environment for the problem of product recommendation in online advertising]]
- [[Experimental study of inequality and unpredictability in an artificial cultural market]]
- [[Dynamic models of segregation]]
- [[Human interaction with recommendation systems]]
- [[Animating rotation with quaternion curves]]
- [[YouTube’s AI is the puppet master over most of what you watch]]
- [[Debiasing the human-recommender system feedback loop in collaborative filtering]]
- [[Republic.com]]
- [[Going to extremes- How like minds unite and divide|Going to extremes: How like minds unite and divide]]
- [[Republic.com 2.0]]
- [[Network segregation in a model of misinformation and fact-checking]]
- [[Netlogo- A simple environment for modeling complexity|Netlogo: A simple environment for modeling complexity]]
- [[Echo chambers and viral misinformation- Modeling fake news as complex contagion|Echo chambers and viral misinformation: Modeling fake news as complex contagion]]
- [[Searching for alternative facts]]
- [[YouTube, the Great Radicalizer]]
- [[SciPy 1.0- Fundamental Algorithms for Scientific Computing in Python|SciPy 1.0: Fundamental Algorithms for Scientific Computing in Python]]
- [[The spread of true and false news online]]
- [[Collaborative deep learning for recommender systems]]
- [[NetLogo]]
- [[Beyond parity- fairness objectives for collaborative filtering|Beyond parity: fairness objectives for collaborative filtering]]
- [[DRN- A deep reinforcement learning framework for news recommendation|DRN: A deep reinforcement learning framework for news recommendation]]
- [[Joint deep modeling of users and items using reviews for recommendation]]
- [[Improving recommendation lists through topic diversification]]

## Audit Log
- 2026-10-03: Independent full-source re-audit passed. Full primary source, all appendices, three case studies and 87 references verified. Publication date checked against initial arXiv submission; version date stored separately. `audit failed` removed after the pass.
- Bibliography correction (2026-09-30): replaced the incomplete or mixed imported list with all 87 references from the audited primary source. Original links remain in the import snapshot; independent re-audit required.
- Independent bibliography audit (2026-09-30): the primary source contains 87 references, while the preserved import has 62 links, including six unresolved identifiers. Reference reconciliation is required; the audit warning remains.
- Independent full-source audit (2026-09-30): the core framework claims passed, but the simplified loop did not explicitly identify omitted creator production, dynamic-user updates or start-up behavior. Added those limits, the default drift/start-up rules and the hidden actual-state boundary; independent re-audit required.
- Audit invalidated (2026-09-30): auditor admitted clearing flags before completing independent source checks. A new independent audit is required.
- Strong source review (2026-09-30): Replaced hard-coded random interleaving with configured presentation, separated framework state from illustrative creator dynamics and added missing item/creator interfaces; typed update procedures follow the documented feedback loop. Independent re-audit pending.
- Initial independent audit: failed on missing model mechanisms, abstract fidelity, or source-access reporting; see `vault/.automation/audit/next-forty-54-66-initial-2026-09-30.json`. Revisions added source-located model detail; independent re-audit remains pending.

- WITHDRAWN audit claim (2026-09-30): previously reported PASS; source claims, current extraction, metadata, references and footnotes checked against the available primary source. See `vault/.automation/audit/remaining-audit-b-2026-09-30.json`.

## LLM Justification
[^r1]: The paper’s abstract, at https://arxiv.org/abs/2107.08959. The questions paraphrase the stated purpose, research scope, and reported approach.
[^r3]: Lucherini et al., Fig. 1 and §§4.1–4.5: ordered score/presentation/feedback/state/metric loop; separate preference/score structures; fixed/dynamic items, probabilistic creators; event skipping and parallel feedback. Full text: https://arxiv.org/html/2107.08959.
[^r4]: Lucherini et al., §5 introduction (conceptual rather than exact replications), §§5.1–5.2 (algorithmic confounding and information diffusion), §5.4 (creator-feedback constructive extension; creator distribution/adaptation in §5.4.2). These are case-study models, not universal framework behavior. Full text: https://arxiv.org/html/2107.08959.
[^r5]: Lucherini et al., Appendix A.2.7 “Content creators”: default creator probability matrix, independent Bernoulli attributes, optional production probability and explicit warning that the simple default is not highly realistic. Full text: https://arxiv.org/html/2107.08959.
[^r6]: Lucherini et al., Appendices A.2.1 and A.2.4 (actual preferences/scores are unknown to the recommender), A.3 (optional preference drift uses spherical linear interpolation after item choice), and A.4 (random start-up presentation, omitted prediction step and training at phase end). Full text: https://arxiv.org/html/2107.08959.
[^r7]: Lucherini et al., §§5.1–5.3 and Appendix A.1.1–A.1.2: experiment settings, conceptual replication scope, Jaccard measure, SIR parameter grid and reported outcomes. Full text: https://arxiv.org/html/2107.08959.
[^r8]: Lucherini et al., §5.4 and Appendix A.1.3: creator profiles, entropy and user-distance metrics, adaptive creator results and scope caveats. Full text: https://arxiv.org/html/2107.08959.
