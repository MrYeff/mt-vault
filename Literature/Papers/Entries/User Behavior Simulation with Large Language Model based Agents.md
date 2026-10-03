---
title: "User Behavior Simulation with Large Language Model based Agents"
tags:
  - model
  - simulation
authors:
  - "[[Literature/Authors/Lei Wang|Lei Wang]]"
  - "[[Literature/Authors/Jingsen Zhang|Jingsen Zhang]]"
  - "[[Literature/Authors/Yang, Hao|Yang, Hao]]"
  - "[[Literature/Authors/Chen, Zhiyuan|Chen, Zhiyuan]]"
  - "[[Literature/Authors/Tang, Jiakai|Tang, Jiakai]]"
  - "[[Literature/Authors/Zhang, Zeyu|Zhang, Zeyu]]"
  - "[[Literature/Authors/Xu Chen|Xu Chen]]"
  - "[[Literature/Authors/Yankai Lin|Yankai Lin]]"
  - "[[Literature/Authors/Hao Sun|Hao Sun]]"
  - "[[Literature/Authors/Ruihua Song|Ruihua Song]]"
  - "[[Literature/Authors/Wayne Xin Zhao|Wayne Xin Zhao]]"
  - "[[Literature/Authors/Xu, Jun|Xu, Jun]]"
  - "[[Literature/Authors/Dou, Zhicheng|Dou, Zhicheng]]"
  - "[[Literature/Authors/Wang, Jun|Wang, Jun]]"
  - "[[Literature/Authors/Ji-Rong Wen|Ji-Rong Wen]]"
publication date: 2024-02-15
source: https://arxiv.org/html/2306.02552v3
doi: 10.48550/arxiv.2306.02552
read status: Todo
⚠️:
  - audit failed
---
## Abstract

Simulating high quality user behavior data has always been a fundamental problem in human-centered applications, where the major difficulty originates from the intricate mechanism of human decision process. Recently, substantial evidences have suggested that by learning huge amounts of web knowledge, large language models (LLMs) can achieve human-like intelligence. We believe these models can provide significant opportunities to more believable user behavior simulation. To inspire such direction, we propose an LLM-based agent framework and design a sandbox environment to simulate real user behaviors. Based on extensive experiments, we find that the simulated behaviors of our method are very close to the ones of real humans. Concerning potential applications, we simulate and study two social phenomenons including (1) information cocoons and (2) user conformity behaviors. This research provides novel simulation paradigms for human-centered applications.

## Research Questions
> Research Questions extracted via LLM

- Can a profile-memory-action LLM-agent simulator generate believable recommender and social behaviors, and support studies of information cocoons and conformity?[^r1]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?
RecAgent simulates profile-conditioned users interacting with a recommender and their social contacts, with sensory, short-term and long-term memory.[^r2]

The state/action types and memory rules below condense the Results framework and Methods; symbolic thresholds, `K`, `N`, activity parameters and forgetting proportionality are not assigned invented numerical values. Item details, recommender internals and timestamp encoding are omitted; profile fields are optional.[^r2][^r3][^r6]

```yml
World:
  agents: [Agent]
  items: [Item]
  friends: [AgentId -> [AgentId]]
  recommender: Recommender
  round: u32

Agent:
  profile: # manual | LLM-generated | real-data alignment
    name: str?
    gender: str?
    age: u32?
    traits: [str]?
    career: str?
    interests: [str]?
    behavioral_features: [Watcher | Explorer | Critic | Chatter | Poster]?
  short_term: [Memory]
  long_term: [Memory]
  activity: 0..

Memory:
  content: str
  importance: f64
  timestamp: Time
  enhancers: [Memory]

Action: Search | Browse | Click | NextPage | Chat | Broadcast

Item: ...
Recommender: ...
Time: ... # timestamp encoding unspecified
```

### How does it work?
- Each round, users decide whether to act; activity levels follow `p(x)=ALPHA * X_MIN^ALPHA / x^(ALPHA+1)`, `x≥X_MIN`. The article gives this density but no explicit density-to-activation probability conversion.[^r2]
- `Search` requests relevant items; `Browse` receives recommendations; `Click` selects items to watch/purchase; `NextPage` requests another slate; `Chat` exchanges information one-to-one; `Broadcast` shares with contacts. Social messages become recipients' observations.[^r2]
- Each action prompt combines the behavior-relevant profile (filtered using ChatGPT), memory, instruction with optional few-shot examples, and current context/timing. LLM responses execute the corresponding sandbox action; generated observations feed memory.[^r3]

- The writing/retrieval rules and printed forgetting function are summarized below. Reflection generates high-level long-term insights and merges highly similar memories/insights; its triggering and merge thresholds are not fixed in this summary.[^r3]

```
write_observation(
  mut agent: Agent,
  observation: str, importance_score: f64, timestamp: Time
):
  record = (LLM.compress(observation), importance_score, timestamp)
  for old in agent.short_term:
    if embedding_similarity(old.content, record.content) > THRESHOLD:
      old.enhancers.push(record)
      if |old.enhancers| reaches K:
        agent.long_term.push(old, LLM.insights(old, old.enhancers))
  agent.short_term.push(record) # retained even if no match

read_memory(agent: Agent, observation: str) -> [Memory]:
  out = top_N_relevant(agent.long_term, observation) + agent.short_term

forgetting_score(s: 0..1, r: 0..1) -> 0..1:
  out = 1 - ((s + r) / 2) * max(r^BETA, DELTA)
  # s,r,DELTA in (0,1); BETA > 1
  # long-term forgetting probability is proportional to out
```

- The displayed action type covers the six Results behaviors. Appendix A.3 also prompts entry into recommender/social modes, leaving, and doing nothing; those orchestration choices are omitted here. Profile fields may be left empty for a configured application. The paper does not specify the score normalization, threshold values, or scheduling of reflection/forgetting.[^r3][^r7]

- The sensory-memory triplet calls `s` importance, whereas the forgetting paragraph calls `s,r` normalized recency and importance respectively. The formula is retained exactly with that local definition; this notation inconsistency and the unspecified normalization/proportionality prevent claiming a complete executable forgetting implementation.[^r3]

### What can it answer?
- Recommendation believability: 20 MovieLens-1M users; withhold the last `a` items and mix them with `b` negatives. Agents select `a` items; compare ground-truth overlap against embedding/RecSim and human selections.[^r4]
- Social believability: three annotators rate chat/broadcast outputs from 20 agents after 5, 10 and 15 rounds on a 1–5 scale, using profiles and previous behaviors.[^r4]
- Memory evaluation: three annotators rate retrieved memories for relevance and informativeness on a 1–5 scale, using 15 sampled behaviors.[^r4]
- Information cocoon: 50 agents, 50 rounds, MF retrained each round, five items per slate; outcome is mean user category entropy `−mean_u sum_c f[u,c] log(f[u,c])`. After round 20, replace one item randomly and/or add one friend with different interests; vary replacement frequency `{1,5,10}` rounds, replacement count `{1,3,5}`, and friend count `{1,3,5}`. More diversity improves entropy; randomness reduces agent-rated satisfaction on 1–10.[^r5]
- Conformity: initially five well-connected agents watch a movie and share opinions; after each round every agent gives a 1–10 score. Compare score concentration and `AC(i)=sum_{u with i friends,r=1..10} 1(score[u,r]≠score[u,r−1]) / (10 * |U_i|)`; more friends associate with more score changes.[^r5]

### Where does it apply?
Evidence concerns movie recommendation and sandbox social exchange; real-data initialization and human judgments support these specific tasks. Recommendation algorithms, profiles, interventions and human participation are configurable.[^r4][^r6]

## Metadata
### References

- [[HumanCenteredArtificialIntelligenceAndMachineLearning]]
- [[HumanCenteredArtificialIntelligenceReliableSafeTrustworthy]]
- [[UserDataPrivacyFacebookCambridgeAnalyticaAndPrivacyProtection]]
- [[BigDataPrivacyIssuesInPublicSocialMedia]]
- [[VirtualTaobaoVirtualizingRealWorldOnlineRetailEnvironmentForReinforcementLearning]]
- [[RecSim- A Configurable Simulation Platform for Recommender Systems]]
- [[SyntheticDataBasedSimulatorsForRecommenderSystemsASurvey]]
- [[LenskitForPythonNextGenerationSoftwareForRecommenderSystemsExperiments]]
- [[RecSim NG- Toward Principled Uncertainty Modeling for Recommender Ecosystems]]
- [[NetworkStructuresAndAgreementInSocialNetworkSimulations]]
- [[KeepingDatasetBiasesOutOfTheSimulationADebiasedSimulatorForReinforcementLearningBasedRecommenderSystems]]
- [[SocialRecommendationAReview]]
- [[IntroductionToSocialRecommendation]]
- [[GraphNeuralNetworksForSocialRecommendation]]
- [[ASurveyOfLargeLanguageModels]]
- [[GenerativeAgentsInteractiveSimulacraOfHumanBehavior]]
- [[UsingLargeLanguageModelsToSimulateMultipleHumansAndReplicateHumanSubjectStudies]]
- [[AligningLargeLanguageModelsWithHumanASurvey]]
- [[Gpt4TechnicalReport2023]]
- [[SelfCollaborationCodeGenerationViaChatgpt]]
- [[ASurveyOnLargeLanguageModelBasedAutonomousAgents]]
- [[HumanMemoryAProposedSystemAndItsControlProcesses]]
- [[WhatAreTheDifferencesBetweenLongTermShortTermAndWorkingMemory]]
- [[InsightsFromTheLongTailLearningLatentRepresentationsOfOnlineUserBehaviorInThePresenceOfSkewAndSparsity]]
- [[ParetoDistribution]]
- [[ProbabilisticMatrixFactorization]]
- [[EvaluatingConversationalRecommenderSystemsViaUserSimulation]]
- [[AdversarialLearningForNeuralDialogueGeneration]]
- [[ExploringTheFilterBubbleTheEffectOfUsingRecommenderSystemsOnContentDiversity]]
- [[HumanAiAdaptiveDynamicsDrivesTheEmergenceOfInformationCocoons]]
- [[GenuinePowerCurvesInForgettingAQuantitativeAnalysisOfIndividualSubjectForgettingFunctions]]
- [[ArtifactualPowerCurvesInForgetting]]
- [[SelfAttentiveSequentialRecommendation]]
- [[SequentialRecommenderSystemsChallengesProgressAndProspects]]


## Audit Log
- Audit invalidated (2026-09-30): auditor admitted incomplete independent checks and premature flag removal. Previous valid audits, if any, remain separate.

- 2026-09-30: Complete independent primary-text audit found that the note attributed memory relevance/informativeness ratings to chat/broadcast output. Corrected the distinction, restored behavioral profile features, and disclosed omitted mode/leave controls and unspecified memory scheduling. Independent re-audit remains pending.

- 2026-09-30: Initial/cheap audit failed; stronger source review corrected six actual actions, reinforcement insertion, forgetting formula and notation conflict, Pareto activity limits, prompts and concrete intervention designs. Independent re-audit pending.

- WITHDRAWN audit claim (2026-09-30): the remaining-audit-c report overstated independent source checks; it does not establish a pass.

## LLM Justification
[^r1]: https://arxiv.org/html/2306.02552v3; Introduction: aims and two applications.
[^r2]: Same source; Results, “User behavior simulator with LLM-based agents,” Figure 1 and displayed Pareto density: profile, three memory modules, six actions and round activity.
[^r3]: Same source; Methods, “Profiling Module,” “Memory Module” (sensory triplet, similarity/K conversion, displayed g(M), writing/reading/reflection) and “Action Module”: four-part prompt. Sensory s=importance differs from the forgetting paragraph's s=recency, r=importance; probability is stated only proportional to g.
[^r4]: Same source; Results, “Believability of the simulated user behaviors,” Figures 2–3: 20 users, discrimination/generation and human judgment tasks.
[^r5]: Same source; Results, “Studying the information cocoon phenomenon” (displayed entropy and Figure 4) and “Studying the user conformity phenomenon” (displayed AC and Figure 5): conditions, interventions and outcomes.
[^r6]: Same source; Methods, “Key Components of The Simulator”: interchangeable recommender, human role playing, and system interventions.

[^r7]: Same source; Supplementary Note A.3, action-selection, recommendation-entry and social prompts: Recommender/Social/Nothing modes and leave options. Methods, “Profiling Module,” lists the five behavioral features and permits empty profile fields.
