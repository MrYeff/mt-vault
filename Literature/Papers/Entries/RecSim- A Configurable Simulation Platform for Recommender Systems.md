---
title: "RecSim: A Configurable Simulation Platform for Recommender Systems"
tags:
  - recommender_system
  - simulation
  - "model"
authors:
  - "[[Literature/Authors/Eugene Ie|Eugene Ie]]"
  - "[[Literature/Authors/Chih‐Wei Hsu|Chih‐Wei Hsu]]"
  - "[[Literature/Authors/Martin Mladenov|Martin Mladenov]]"
  - "[[Literature/Authors/Vihan Jain|Vihan Jain]]"
  - "[[Literature/Authors/Sanmit Narvekar|Sanmit Narvekar]]"
  - "[[Literature/Authors/Jing Wang|Jing Wang]]"
  - "[[Literature/Authors/Rui Wu|Rui Wu]]"
  - "[[Literature/Authors/Craig E. Boutilier|Craig E. Boutilier]]"
publication date: 2019-09-11 
source: "https://arxiv.org/html/1909.04847"
doi: 10.48550/arxiv.1909.04847
read status: Todo
---

## Abstract

We propose RecSim, a configurable platform for authoring simulation environments for recommender systems (RSs) that naturally supports sequential interaction with users. RecSim allows the creation of new environments that reflect particular aspects of user behavior and item structure at a level of abstraction well-suited to pushing the limits of current reinforcement learning (RL) and RS techniques in sequential interactive recommendation problems. Environments can be easily configured that vary assumptions about: user preferences and item familiarity; user latent state and its dynamics; and choice models and other user response behavior. We outline how RecSim offers value to RL and RS researchers and practitioners, and how it can serve as a vehicle for academic-industrial collaboration.

## Research Questions
> Research Questions extracted via LLM
- How can recommender-system environments represent sequential user interactions and item structure?[^r1]
- Which configurable assumptions about preferences, familiarity, latent state, and response behavior can researchers vary?[^r1]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?
- A configurable recommender–user environment. The simulator knows full user state; the recommender sees selected user/document features and response history.[^r3]
- The types describe component interfaces. `()` marks environment-defined payloads, not a fixed behavioral model.[^r3]

```yml
World:
  user: User
  candidates: [Document]
  history: [Response]
  recommender: Policy

User:
  state: () # observable and latent features

Document:
  features: () # observable and latent features

Response:
  choice: DocumentId?
  behavior: () # e.g. watch time or rating

Observation:
  user_features: ()
  document_features: [DocumentId -> ()]
  responses: [Response]

Policy: ()
```

### How does it work?
- Sample a user at episode start. Document candidates can be fixed, sampled or otherwise supplied. Choice, transition, observation and reward functions belong to the environment configuration.[^r3]
- The following loop follows Fig. 2. The paper simulates user episodes sequentially; an episode ends at a length limit or terminal user state.[^r3]

```
sim_step(mut world: World) -> Response:
  world.candidates = DOCUMENT_MODEL.candidates()
  observed = OBSERVATION_MODEL.project(world)
  slate = world.recommender.recommend(observed)
  response = CHOICE_MODEL.respond(world.user, slate)
  TRANSITION_MODEL.update(mut world.user, slate, response)
  world.recommender.update(response, REWARD_MODEL(world.history, response))
  world.history.push(response)
  out = response
```

- The SlateQ example makes the configurable boundary concrete: documents can carry a topic vector, length, and latent quality drawn from a topic-conditioned normal distribution; users have topic-interest vectors in `-1..1`, with document interest given by their dot product. Satisfaction is a configurable function of interest and quality. After consumption, an environment may change topic interest and reduce a time budget by document length minus an appeal-dependent bonus. The user can see a document's topic before choosing, but its quality is revealed only after consumption; multinomial-logit and exponential-cascade choice models are available.[^r5]
- In the latent-state bandit case study, the user has static but hidden topic interests and chooses documents with probability proportional to a function of topic affinity plus document quality. With high topic affinity, UCB1 and Q-learning outperform the omniscient myopic greedy agent in the reported click-rate table; when affinity is low, the gap is much smaller. These are results of the paper's particular configured environment, not a default RecSim transition law.[^r6]
- Two additional case studies use RecSim to evaluate SlateQ's decomposed slate-value learning and temporal aggregation in slowly evolving, low-signal satisfaction environments. The reported SlateQ results retain much of the full slate-search gain with a cheaper greedy serving step and tolerate some choice-model shift; temporal aggregation improves learned policies toward the fully observed-satisfaction case. The paper summarizes these studies and refers to their companion publications for further environment details.[^r7]

### What can it answer?
- Compare policies by cumulative reward, episode length and diversity; test exploration under latent preferences, slate-value decomposition, slowly changing satisfaction, and robustness to changes in user, transition or choice models.[^r4][^r6][^r7]

### Where does it apply?
- Sequential recommendation experiments. This interface omits the separate SlateQ and other case-study equations; it supplies no universal human-choice law or validated live-deployment prediction.[^r3][^r4]

## Metadata
### References
- [[TensorFlow- A system for large-scale machine learning|TensorFlow: A system for large-scale machine learning]]
- [[Further optimal regret bounds for Thompson sampling]]
- [[Learning a deep listwise context model for ranking refinement]]
- [[Finite-time analysis of the multiarmed bandit problem]]
- [[The Arcade Learning Environment- An evaluation platform for general agents|The Arcade Learning Environment: An evaluation platform for general agents]]
- [[Seq2Slate- Re-ranking and slate optimization with RNNs|Seq2Slate: Re-ranking and slate optimization with RNNs]]
- [[Planning and learning with stochastic action sets]]
- [[Empirical analysis of predictive algorithms for collaborative filtering]]
- [[OpenAI gym]]
- [[Dopamine- A research framework for deep reinforcement learning|Dopamine: A research framework for deep reinforcement learning]]
- [[Reinforcement learning when all actions are not always available]]
- [[Modeling delayed feedback in display advertising]]
- [[An empirical evaluation of Thompson sampling]]
- [[Critiquing-based recommenders- survey and emerging trends|Critiquing-based recommenders: survey and emerging trends]]
- [[Top-k off-policy correction for a REINFORCE recommender system]]
- [[Keras]]
- [[Learning to interact with users- A collaborative-bandit approach|Learning to interact with users: A collaborative-bandit approach]]
- [[Towards conversational recommender systems]]
- [[Challenges of real-world reinforcement learning]]
- [[The KL-UCB algorithm for bounded stochastic bandits and beyond]]
- [[Horizon- Facebook’s open source applied reinforcement learning platform|Horizon: Facebook’s open source applied reinforcement learning platform]]
- [[A knowledge-grounded neural conversation model]]
- [[TF-Agents- A library for reinforcement learning in tensorflow|TF-Agents: A library for reinforcement learning in tensorflow]]
- [[Soft actor-critic algorithms and applications]]
- [[Contextual markov decision processes]]
- [[The MovieLens datasets- History and context|The MovieLens datasets: History and context]]
- [[Fusing similarity models with Markov chains for sparse sequential recommendation]]
- [[Session-based recommendations with recurrent neural networks]]
- [[Focusing on the long-term- It’s good for users and business|Focusing on the long-term: It’s good for users and business]]
- [[SlateQ- A tractable decomposition for reinforcement learning with recommendation sets|SlateQ: A tractable decomposition for reinforcement learning with recommendation sets]]
- [[Beyond greedy ranking- Slate optimization via List-CVAE|Beyond greedy ranking: Slate optimization via List-CVAE]]
- [[Optimizing search engines using clickthrough data]]
- [[GroupLens- Applying collaborative filtering to Usenet news|GroupLens: Applying collaborative filtering to Usenet news]]
- [[Data center cooling using model-predictive control]]
- [[A contextual-bandit approach to personalized news article recommendation]]
- [[Collaborative filtering bandits]]
- [[Memory approaches to reinforcement learning in non-Markovian domains]]
- [[Building personalized simulator for interactive search]]
- [[Stated Choice Methods- Analysis and Application|Stated Choice Methods: Analysis and Application]]
- [[Discrete sequential prediction of continuous actions for deep RL]]
- [[Advantage amplification in slowly evolving latent-state environments]]
- [[Human-level control through deep reinforcement learning]]
- [[Deep Dyna-Q- Integrating planning for task-completion dialogue policy learning|Deep Dyna-Q: Integrating planning for task-completion dialogue policy learning]]
- [[Neural fitted Q-iteration—first experiences with a data efficient neural reinforcement learning method]]
- [[Multiple objective optimization in recommender systems]]
- [[RecoGym- A reinforcement learning environment for the problem of product recommendation in online advertising|RecoGym: A reinforcement learning environment for the problem of product recommendation in online advertising]]
- [[Probabilistic matrix factorization]]
- [[Agenda-based user simulation for bootstrapping a POMDP dialogue system]]
- [[An MDP-based recommender system]]
- [[Virtual-taobao- Virtualizing real-world online retail environment for reinforcement learning|Virtual-taobao: Virtualizing real-world online retail environment for reinforcement learning]]
- [[Mastering the game of Go with deep neural networks and tree search]]
- [[Conversational recommender system]]
- [[Deep reinforcement learning with attention for slate Markov decision processes with high-dimensional states and actions]]
- [[ELF- an extensive, lightweight and flexible research platform for real-time strategy games|ELF: an extensive, lightweight and flexible research platform for real-time strategy games]]
- [[A neural conversational model]]
- [[Q-learning]]
- [[AirDialogue- An environment for goal-oriented dialogue research|AirDialogue: An environment for goal-oriented dialogue research]]
- [[Practical diversified recommendations on YouTube with determinantal point processes]]
- [[Recurrent recommender networks]]
- [[Natural environment benchmarks for reinforcement learning]]
- [[Deep reinforcement learning for page-wise recommendations]]
- [[Toward simulating environments in reinforcement learning based recommendations]]
- [[DRN- A deep reinforcement learning framework for news recommendation|DRN: A deep reinforcement learning framework for news recommendation]]

## Audit Log
- 2026-10-03: Independent full-source re-audit passed. Full primary source and 63 references checked; history update indentation and reference-target fixes independently re-audited. `audit failed` removed after the pass.
- Bibliography correction (2026-09-30): replaced the incomplete or mixed imported list with all 63 references from the audited primary source. Original links remain in the import snapshot; independent re-audit required.
- Independent full-source audit (2026-09-30): the abstract and core framework extraction passed. The bibliography failed: the primary source contains 63 references, while the preserved import has 58 links, including seven unresolved identifiers and a title that does not match the cited contextual-MDP paper. Reference reconciliation is required; the audit warning remains.
- Audit invalidated (2026-09-30): auditor admitted clearing flags before completing independent source checks. A new independent audit is required.
- Strong source review (2026-09-30): Added typed configurable state, observable-state boundary, user-response/policy updates and episode termination; source HTML spells RecSim as in the existing abstract. Independent re-audit pending.

- WITHDRAWN audit claim (2026-09-30): previously reported PASS; source claims, current extraction, metadata, references and footnotes checked against the available primary source. See `vault/.automation/audit/remaining-audit-b-2026-09-30.json`.

## LLM Justification
[^r1]: The paper’s abstract, at https://arxiv.org/abs/1909.04847. The questions paraphrase the stated purpose, research scope, and reported approach.
[^r3]: Ie et al., §3.1 (components and observation/choice/transition factorization), §4.1 Fig. 2 steps 1–6 and episode termination, §4.2 (environment-specific reward). Full text: https://arxiv.org/html/1909.04847.
[^r4]: Ie et al., §1.4 (non-objectives: no perfect real-user simulation or direct live deployment), §4.1 (aggregate and diversity metrics, separate evaluation), §5 (distinct case studies). Full text: https://arxiv.org/html/1909.04847.
[^r5]: Ie et al., §3.2 (SlateQ simulation environment: document and user features, interest and satisfaction, time budget, choice visibility, and configurable choice models). Full text: https://arxiv.org/html/1909.04847.
[^r6]: Ie et al., §5.1 and its results table (latent-state bandits, static hidden topic interests, choice probability and click-through results). Full text: https://arxiv.org/html/1909.04847.
[^r7]: Ie et al., §§5.2–5.3 (SlateQ decomposition and advantage amplification/temporal aggregation results); the paper summarizes companion studies rather than fully specifying their implementations. Full text: https://arxiv.org/html/1909.04847.
