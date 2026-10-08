---
title: "On Generative Agents in Recommendation"
authors:
  - "[[Literature/Authors/An Zhang|An Zhang]]"
  - "[[Literature/Authors/Yuxin Chen|Yuxin Chen]]"
  - "[[Literature/Authors/Leheng Sheng|Leheng Sheng]]"
  - "[[Literature/Authors/Xiang Wang|Xiang Wang]]"
  - "[[Literature/Authors/Tat‐Seng Chua|Tat‐Seng Chua]]"
source: "https://arxiv.org/html/2310.10108"
doi: "10.1145/3626772.3657844"
publication date: "2024-07-10"
tags:
  - "model"
  - "simulation"
  - "recommender_systems"
  - "llm_agents"
read status: Todo
---

## Abstract

Recommender systems are the cornerstone of today’s information dissemination, yet a disconnect between offline metrics and online performance greatly hinders their development. Addressing this challenge, we envision a recommendation simulator, capitalizing on recent breakthroughs in human-level intelligence exhibited by Large Language Models (LLMs). We propose Agent4Rec, a user simulator in recommendation, leveraging LLM-empowered generative agents equipped with user profile, memory, and actions modules specifically tailored for the recommender system. In particular, these agents’ profile modules are initialized using real-world datasets (e.g., MovieLens, Steam, Amazon-Book), capturing users’ unique tastes and social traits; memory modules log both factual and emotional memories and are integrated with an emotion-driven reflection mechanism; action modules support a wide variety of behaviors, spanning both taste-driven and emotion-driven actions. Each agent interacts with personalized recommender models in a page-by-page manner, relying on a pre-implemented collaborative filtering-based recommendation algorithm. We delve into both the capabilities and limitations of Agent4Rec, aiming to explore an essential research question: “To what extent can LLM-empowered generative agents faithfully simulate the behavior of real, autonomous humans in recommender systems?” Extensive and multi-faceted evaluations of Agent4Rec highlight both the alignment and deviation between agents and user-personalized preferences. Beyond mere performance comparison, we explore insightful experiments, such as emulating the filter bubble effect and discovering the underlying causal relationships in recommendation tasks. Our codes are available at https://github.com/LehengTHU/Agent4Rec.[^r1]

## Research Questions
> Research Questions extracted via LLM

- To what extent do LLM-powered agents simulate behavior and preferences in recommender systems?[^r1]
- How do agent memory, emotions, and recommender exposure affect simulated preference behavior and filter bubbles?[^r1]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?
- Agent4Rec simulates dataset-initialized users viewing personalized recommendations, with profile, factual/emotional memory, and LLM-driven actions.[^u1]

### How does it work?
The architecture separates user traits, memory, item descriptions, and recommendation policy.[^u1][^u2]

```yml
World:
  agents: [Agent]
  items: [Item]
  agent_framework: ModifiedLangChain
  llm: GPT3.5Turbo
  recommender: Random | Popularity | MF | LightGCN | MultVAE

Agent:
  tastes: str
  activity: 0..
  conformity: 0..
  diversity: u32
  memory: [Memory]
  reflection_after: u32 # configurable action count

Memory:
  description: str
  embedding: [f64]
  kind: Factual | Emotional
  emotional_state: {satisfaction: str, fatigue: str}

Item:
  quality: f64
  popularity: 0..
  genres: [str]
  summary: str
```

- Profile traits are computed from historical interactions: activity is the number of interacted items; conformity is the mean squared rating deviation from item-average ratings; diversity is the number of distinct genres in the user’s history. For interacted items \(I_u\):

  \[ T_{act}^{u}=\sum_{i\in I_u}y_{ui},\qquad T_{conf}^{u}=\frac{\sum_{i\in I_u}y_{ui}(r_{ui}-R_i)^2}{\sum_{i\in I_u}y_{ui}},\qquad T_{div}^{u}=\left|\bigcup_{i:y_{ui}=1}G_i\right| \]

  The paper divides each trait into three uneven tiers. It randomly samples 25 historical items per user, labels ratings ≥3 as like, and uses ChatGPT to summarize tastes and rating patterns.[^u1]
- Store recommended items, view/rating/exit feedback, satisfaction and fatigue as text and embedding memories. Retrieve relevant memories for decisions and append new experience. Reflect on satisfaction/fatigue after a configured action-count threshold; the paper does not give one universal threshold value.[^u3]
- A page shows item descriptions; the LLM chooses watch/skip, gives watched-item ratings and feelings, evaluates satisfaction/fatigue, then chooses continue/exit using emotional memory and activity trait. After exit, interview the agent for system ratings and explanations.[^u4]
- Item quality comes from historical ratings, popularity from review counts; few-shot LLM prompts generate genres and summaries from titles. Remove items with incorrect generated genres. The recommender is a replaceable module; separate experiments retrain with agent feedback between pages.[^u2]

The movie example and strategy evaluation use these fixed settings.[^u1][^u5]

```
AGENTS = 1000
PROFILE_HISTORY_ITEMS = 25
PROFILE_LIKE_MIN_RATING = 3
ITEM_GENRES = 18
ITEMS_PER_PAGE = 4
MAX_PAGES = 5
EVALUATION_LIKE_THRESHOLD = 3 # strict: rating > threshold
```

The paper’s implementation modifies LangChain and uses ChatGPT `gpt-3.5-turbo` for every agent; recommendation algorithms are replaceable modules.[^u1][^u2]

- The profile labels rating ≥`PROFILE_LIKE_MIN_RATING` as like, while strategy evaluation counts likes only above `EVALUATION_LIKE_THRESHOLD`; preserve this source distinction. Exit is enforced at `MAX_PAGES` in that experiment.[^u1][^u5]
- Alignment results are mixed: on the preference discrimination task, the paper reports accuracy near 65% and recall near 75%, while precision and F1 fall sharply as unobserved distractors increase. Simulated ratings broadly reproduce the MovieLens distribution but agents give very few 1–2 ratings; diversity tiers show weaker separation in the overlapping MovieLens genres.[^u5]
- In strategy evaluation, algorithmic recommenders outperform random/popularity baselines on the reported satisfaction measures. Table 2 is metric-specific: LightGCN has the highest viewing ratio, like ratio, and satisfaction, while MF has the highest mean like count and exit-page value. Adding viewed-item feedback improves offline Recall@20/NDCG@20 and simulated satisfaction across MF, MultVAE, and LightGCN; adding unviewed items generally worsens them.[^u5]
- In the four-round filter-bubble study, recommended genre diversity falls and top-genre concentration rises. DirectLiNGAM over simulated movie data identifies quality and popularity as causes of ratings and a popularity→exposure→views feedback pathway; these are results of the fitted simulator data, not independently established human causal effects.[^u5]
- This extraction omits complete prompt wording, memory-retrieval implementation, and fitted recommendation algorithms. Actions are generated by LLM prompts, not a specified numerical transition law.[^u3][^u4]

### What can it answer?
- It compares ratings and social traits with real-user data, evaluates viewing/likes/exit/satisfaction, and explores feedback training, filter bubbles and causal discovery.[^u5]

### Where does it apply?
- It applies to the paper's recommendation datasets and configured user tasks; reported alignment includes deviations and does not establish universal human fidelity.[^u6]

## Metadata
### References

- [[Reinforcement Learning based Recommender Systems- A Survey]]
- [[A new approach to evaluating novel recommendations]]
- [[Bias and Debias in Recommender System- A Survey and Future Directions]]
- [[Generative Adversarial User Model for Reinforcement Learning Based Recommendation System]]
- [[Recommendation system based on deep learning methods- a systematic review and new directions]]
- [[Challenges of Real-World Reinforcement Learning]]
- [[All The Cool Kids, How Do They Fit In-- Popularity and Demographic Biases in Recommender Evaluation and Effectiveness]]
- [[Is it an Agent, or Just a Program-- A Taxonomy for Autonomous Agents]]
- [[S³- Social-network Simulation System with Large Language Model-Empowered Agents]]
- [[CIRS- Bursting Filter Bubbles by Counterfactual Interactive Recommender System]]
- [[Causal inference in recommender systems- A survey and future directions]]
- [[Mitigating the Filter Bubble while Maintaining Relevance- Targeted Diversification with VAE-based Recommender Systems]]
- [[The Netflix Recommender System- Algorithms, Business Value, and Innovation]]
- [[Language Models Represent Space and Time]]
- [[The MovieLens Datasets- History and Context]]
- [[LightGCN- Simplifying and Powering Graph Convolution Network for Recommendation]]
- [[CausPref- Causal Preference Learning for Out-of-Distribution Recommendation]]
- [[Keeping Dataset Biases out of the Simulation- A Debiased Simulator for Reinforcement Learning based Recommender Systems]]
- [[Recommender AI Agent- Integrating Large Language Models for Interactive Recommendations]]
- [[RecSim- A Configurable Simulation Platform for Recommender Systems|RecSim: A Configurable Simulation Platform for Recommender Systems]]
- [[A Roadmap of Agent Research and Development]]
- [[Self-Attentive Sequential Recommendation]]
- [[Trustworthy online controlled experiments- five puzzling outcomes explained]]
- [[Matrix Factorization Techniques for Recommender Systems]]
- [[Private traits and attributes are predictable from digital records of human behavior]]
- [[Cognitive neuroscience of emotional memory]]
- [[Breaking Filter Bubble- A Reinforcement Learning Framework of Controllable Recommender System]]
- [[Variational Autoencoders for Collaborative Filtering]]
- [[Large Language-Recommendation Assistant]]
- [[AgentSims- An Open-Source Sandbox for Large Language Model Evaluation]]
- [[Training Socially Aligned Language Models in Simulated Human Society]]
- [[MINDSim- User Simulator for News Recommenders]]
- [[Learning to recommend with social trust ensemble]]
- [[RoCo- Dialectic Multi-Robot Collaboration with Large Language Models]]
- [[Feedback loop and bias amplification in recommender systems]]
- [[A large language model-assisted education tool to provide feedback on open-ended responses]]
- [[Image-Based Recommendations on Styles and Substitutes]]
- [[A user profile modeling using social annotations- a survey]]
- [[Exploring the filter bubble- the effect of using recommender systems on content diversity]]
- [[Training language models to follow instructions with human feedback]]
- [[Cooperative Multi-Agent Learning- The State of the Art]]
- [[Generative Agents- Interactive Simulacra of Human Behavior]]
- [[Causal inference in statistics- A primer]]
- [[Communicative Agents for Software Development]]
- [[Tool Learning with Foundation Models]]
- [[RecoGym- A Reinforcement Learning Environment for the problem of Product Recommendation in Online Advertising]]
- [[Testing the General Deductive Reasoning Capacity of Large Language Models Using OOD Examples]]
- [[Toolformer- Language Models Can Teach Themselves to Use Tools]]
- [[Algorithm of Thoughts- Enhancing Exploration of Ideas in Large Language Models]]
- [[Virtual-Taobao- Virtualizing Real-World Online Retail Environment for Reinforcement Learning]]
- [[DirectLiNGAM- A direct method for learning a linear non-Gaussian structural equation model]]
- [[Voyager- An Open-Ended Embodied Agent with Large Language Models]]
- [[A Survey on Large Language Model based Autonomous Agents]]
- [[When Large Language Model based Agent Meets User Behavior Analysis- A Novel User Simulation Paradigm]]
- [[RecMind- Large Language Model Powered Agent For Recommendation]]
- [[Chain-of-Thought Prompting Elicits Reasoning in Large Language Models]]
- [[AutoGen- Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework]]
- [[The Rise and Potential of Large Language Model Based Agents- A Survey]]
- [[Towards autonomous system- flexible modular production system enhanced with large language model agents]]
- [[Exploring Large Language Models for Communication Games- An Empirical Study on Werewolf]]
- [[Top-N Recommendation with Counterfactual User Preference Simulation]]
- [[Boosting Differentiable Causal Discovery via Adaptive Sample Reweighting]]
- [[Incorporating Bias-aware Margins into Contrastive Loss for Collaborative Filtering]]
- [[Empowering Collaborative Filtering with Principled Adversarial Contrastive Loss]]
- [[Invariant Collaborative Filtering to Popularity Distribution Shift]]
- [[Causal Distillation for Alleviating Performance Heterogeneity in Recommender Systems]]
- [[Deep Learning Based Recommender System- A Survey and New Perspectives]]
- [[Incorporating Social Role Theory into Topic Models for Social Media Content Analysis]]
- [[Let Me Do It For You- Towards LLM Empowered Recommendation via Tool Learning]]
- [[Disentangling User Interest and Conformity for Recommendation with Causal Embedding]]

## Audit Log
- 2026-10-03: Independent full-source re-audit passed. Full Agent4Rec v3 profile, memory, actions, experiment controls/results, limitations and all 70 source references independently checked. `audit failed` removed after the pass.
- Audit invalidated (2026-09-30): auditor admitted relying on spot checks and previous reports before clearing flags. A full independent audit is still required.
- 2026-09-30: Full-source design audit found previous note falsely claimed source unreadable; profile equations and emotional-memory mechanism omitted; watch/rate/continue/exit procedure omitted; profile/evaluation rating-boundary distinction omitted; strategy-evaluation page cap and outcomes omitted. Corrected against the source passages below; independent re-audit pending.[^design]

- WITHDRAWN audit claim (2026-09-30): incomplete source checks; this audit does not establish a pass.

## LLM Justification
[^r1]: The research questions are a concise transformation of the primary source’s abstract and stated aims. Source location: Section 2 “Agent4Rec” and evaluation sections. Source: [On Generative Agents in Recommendation](https://arxiv.org/html/2310.10108).


[^u1]: §2.1.1: profile traits and equations, three uneven tiers, 25 sampled items, and like ≥3. Figure 1 and §1 specify 1000 agents and movie/MovieLens-1M example; the architecture also uses Steam and Amazon-Book.

[^u2]: §2.2: quality/popularity from ratings/reviews, eighteen generated genre categories, title-derived summaries and pruning; configurable recommendation algorithms. §3.4 studies retraining between recommendation pages.

[^u3]: §2.1.2: factual/emotional memory, text and vector storage, retrieval/writing/reflection; reflection is triggered after a predefined action count without a universal value stated there.

[^u4]: §2.1.3: taste-driven viewing/rating/feelings, emotional reasoning from page/memory, activity-aware exit, and post-exit interview.

[^u5]: §§3.1–3.5 compare alignment and strategies. §3.3 sets four movies/page, maximum five pages, likes rating >3, and viewing/likes/exit/satisfaction metrics; §4 examines filter bubbles and causal discovery.

[^u6]: §§3 and 6 discuss observed alignment and deviations, simulator limitations and future work.

[^design]: Source audit checked the full text at https://arxiv.org/html/2310.10108. Model footnotes identify the passages supporting the corrections.
