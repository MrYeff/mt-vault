---
title: "PsychSim: Modeling Theory of Mind with Decision-Theoretic Agents"
tags:
  - model
  - simulation
authors:
  - "[[Literature/Authors/David V. Pynadath|David V. Pynadath]]"
  - "[[Literature/Authors/Stacy C. Marsella|Stacy C. Marsella]]"
publication date: "2005"
source: https://www.ijcai.org/Proceedings/05/Papers/1559.pdf
doi:
read status: Scan
⚠️: []
---
## Abstract

Agent-based modeling of human social behavior is an increasingly important research area. A key factor in human social interaction is our beliefs about others, a theory of mind. Whether we believe a message depends not only on its content but also on our model of the communicator. How we act depends not only on the immediate effect but also on how we believe others will react. In this paper, we discuss PsychSim, an implemented multiagent-based simulation tool for modeling interactions and influence. While typical approaches to such modeling have used first-order logic, PsychSim agents have their own decision-theoretic model of the world, including beliefs about its environment and recursive models of other agents. Using these quantitative models of uncertainty and preferences, we have translated existing psychological theories into a decision-theoretic semantics that allow the agents to reason about degrees of believability in a novel way. We discuss PsychSim’s underlying architecture and describe its application to a school violence scenario for illustration.[^r1]

## Research Questions
> Research Questions extracted via LLM

- How can decision-theoretic agents with recursive models represent theory of mind and social influence?[^r2]
- How do different bully motivations, teacher interventions, and the bully’s mental models affect whether violence recurs in the school scenario?[^r3]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?

PsychSim represents interacting individuals or groups whose state includes objective world features, beliefs, preferences, and models of other agents. The illustrated school scenario has a bully, victim, onlookers/class, and teacher.[^r4]

### How does it work?

The paper defines a state transition and bounded lookahead mathematically. Unreported coefficients, update magnitudes, and execution details remain source-not-specified.[^r5]

```yml
World:
  state: StateVector
  transition: TransitionProbability
  agents: [Agent]
  time: 0..

StateVector:
  features: [FeatureValue]
  power: [AgentId -> Value]
  trust: [TrusterId -> TrusteeId -> Value]
  support: [SupporterId -> SupporteeId -> Value]

Agent:
  beliefs: BeliefModel
  preferences: [Goal -> Weight]
  policy: Policy
  mental_models: [AgentId -> AgentModel]

Action:
  type: str
  actor: AgentId
  object: AgentId?

Message:
  source: AgentId
  recipients: [AgentId]
  subject: AgentId
  content: Belief | Preference | Policy | Model | StateClaim

TransitionProbability: ...
BeliefModel: ...
Goal: ...
Policy: ...
AgentModel: ...
```

- The world is represented by state features and a stochastic transition function for action effects; each agent has a subjective belief distribution over possible states and recursively structured models of others.[^r6]
- Preferences are weighted rewards over state features or counts of actions. A goal can maximize/minimize a feature (for example, an agent’s power) or maximize/minimize occurrences of an action (for example, teasing). The reward is the preference-weight vector applied to the state vector.[^r7]
- For agent `i` at time `t`, equations (2)–(3) define action value and state value as immediate expected reward plus the transition-probability-weighted value of next beliefs. At the first lookahead step, action value uses the agent’s modeled policies of the other agents; subsequent state-value projection uses modeled policies of all agents, including itself. The finite horizon `N` bounds lookahead; no discount factor is shown in these equations. Varying `N` represents different degrees of deliberation.[^r8]

```text
V_a(b_i^t) = g_i · b_i^t
  + Σ_{b_i^{t+1}} V(b_i^{t+1})
      Pr(b_i^{t+1} | b_i^t, a, π_{-i}(b_i^{t+1}))

V(b_i^t) = g_i · b_i^t
  + Σ_{b_i^{t+1}} V(b_i^{t+1})
      Pr(b_i^{t+1} | b_i^t, π(b_i^{t+1}))
```

Here `g_i` is the agent’s goal-weight vector, `b_i^t` its belief state, `a` a candidate action, and `π_{-i}`/`π` the modeled policies described in §2.3. The source’s equations (2)–(3), p. 3, use this notation; the conditional transition term includes both state dynamics and modeled agent behavior.[^r8]
- Beliefs nest beliefs, preferences, and policies about others, potentially without bound. The bullying scenario used two levels: agents modeled others at level 1, who modeled others at level 0 without beliefs. Deeper levels trade precision for computational efficiency.[^r9]
- For computational tractability, mental models use simplified stereotypes and reactive condition→action rules. Rule conditions can respond to observed actions or beliefs and combine conditions. In the scenario, bully stereotypes include dominance-seeking, sadistic, and attention-seeking; teacher stereotypes are normal (punishes violence), severe (punishes more harshly), and weak (never punishes).[^r10]
- For messages, candidate belief states (accepting versus rejecting the message) are assessed using a weighted sum of five factors: consistency, recipient self-interest, sender self-interest, trust, and support/affinity. Consistency compares how well each candidate explains the past, using Bayesian relative likelihood based on re-simulating past observations. Self-interest compares future value; sender self-interest uses the recipient’s model of the sender’s preferences. Trust and support are histories: acceptance/rejection changes trust, while the reward of another agent’s action under the observer’s preferences changes support. Factor weights and trust/support update magnitudes are source-not-specified.[^r11]
- An observed action causes no belief change if consistent with current beliefs. If inconsistent, the observer compares alternative mental models using the same weighted-factor evaluation used for messages.[^r12]
- Agents anticipate belief changes their actions may cause in others during lookahead; this can create incentives to deceive when the resulting behavior benefits the acting agent.[^r13]
- The paper gives no complete simulation schedule or global action ordering. It describes sequentially evaluating a teacher decision after the bully attacks and classmates laugh; beyond that scenario point, update ordering is not specified.[^r14]

The paper describes component procedures for selecting behavior and updating beliefs, but does not prescribe a complete global execution schedule, simultaneous/sequential commit semantics, or a full simulator loop; no global loop is inferred here.[^r15]

### What can it answer?

The paper explores whether a bullying intervention prevents the bully from attacking the victim again, conditional on bully type, who the teacher punishes, and the bully’s mental models of students and teacher. The outcome is binary success (no next attack) or failure; the reported results are scenario-specific configurations, not population-level estimates.[^r16]

In the described setup, the bully may value increasing own power, reducing victim power, and peer approval through laughter at the victim. Aggression is modeled as changing the bully’s and victim’s power, with effect probabilities conditioned on their relative power; exact transition probabilities and goal weights are not supplied.[^r17]

Goal weights for fitted bully models are selected by an automatic fitting procedure to match specified behavior. The experiment uses dominance-seeking, sadistic, and attention-seeking weightings. The paper does not report numerical fitted weights.[^r18]

Table 1 reports whether aggression recurs for the listed configurations; `*` collapses cases with the same outcome. Its barred “severe” label denotes normal or weak teacher models, as clarified in the accompanying text.[^r19]

| Bully type | Punished party | Student model | Teacher model | No next attack? |
|---|---|---|---|---|
| Sadistic | bully | * | not severe | No |
| Sadistic | bully | * | severe | Yes |
| Sadistic | class | scared | * | No |
| Sadistic | class | encouraging | not severe | No |
| Sadistic | class | encouraging | severe | Yes |
| Sadistic | none | * | not severe | No |
| Sadistic | none | * | severe | Yes |
| Attention-seeking | bully | * | * | No |
| Attention-seeking | class | scared | weak | No |
| Attention-seeking | class | scared | normal or severe | Yes |
| Attention-seeking | class | encouraging | * | No |
| Attention-seeking | none | * | * | No |
| Dominance-seeking | any | * | weak | No |
| Dominance-seeking | any | * | normal or severe | Yes |[^r20]

The table shows that a weak teacher model prevents success for all three bully types. Class punishment deters the attention-seeking bully only when classmates are believed scared and the teacher is modeled as normal or severe. The sadistic bully is deterred only with a severe teacher model; under class punishment, the bully must also believe classmates are encouraging. These are scenario results, not population estimates.[^r21]

### Where does it apply?

The authors present PsychSim as a tool for computational social science and social training environments, and use the classroom aggression scenario to illustrate exploration of intervention strategies and assumptions about preferences and beliefs. They state that their scenario exploration is ongoing and that the framework’s broader applications require further investigation.[^r24]

## Reading Notes
- Models decisions based on Markov Decision Procress
- Specifically, a survey of the social psychology literature identified the following key factors:
	- **Consistency**: People expect, prefer, and are driven to maintain consistency, and avoid cognitive dissonance, between beliefs and behaviors.
	- **Self-interest**: The inferences we draw are biased by selfinterest (e.g., motivated inference) and how deeply we analyze information in general is biased by self-interest.
	- **Speaker’s Self-interest**: If the sender of a message benefits greatly if the recipient believes it, there is often a tendency to be more critical and for influence to fail.
	- **Trust, Likability, Affinity**: The relation to the source of the message, whether we trust, like or have some group affinity for him, all impact whether we are influenced by the message
### Important
- "Computational Model of Influence" describes how the above effects are lead to accepting or rejecting a message carrying a statement
	- **Consistency:** would the new statement one better explain my past observations than my original one?
	- **Self-interest:**  given my original believe ro the new one wich leads to a future that is more favorable to me (also applicable to sender to check if malicious intrest)
	- *Bias* whats ym relationship to the sender? based on trust support wich is based on historic interactions 
	- **> combined as weighted sum of:** consistency, self-interest, speaker self-interest, trust and support

## Metadata
### References
- [[Theories of Cognitive Consistency- A Sourcebook]] — R. P. Abelson, E. Aronson, W. J. McGuire, T. M. Newcomb, M. J. Rosenberg, and P. H. Tannenbaum (eds.), 1968.[^r25]
- [[Influence- Science and Practice]] — Robert Cialdini, 2001.[^r26]
- [[Can Computers Deliberately Deceive- A Simulation Tool and Its Application to Turing’s Imitation Game]] — F. de Rosis, C. Castelfranchi, V. Carofiglio, and G. Grassano, 2003.[^r27]
- [[A Rigorous- Operational Formalization of Recursive Modeling]] — P. J. Gmytrasiewicz and E. H. Durfee, 1995.[^r28]
- [[Computer Modeling of Social Processes]] — W. Liebrand, A. Nowak, and R. Hegselmann (eds.), 1998.[^r29]
- [[Interactive Pedagogical Drama]] — S. C. Marsella, W. L. Johnson, and C. LaBore, 2000.[^r30]
- [[PsychSim- Agent-Based Modeling of Social Interactions and Influence]] — S. C. Marsella, D. V. Pynadath, and S. J. Read, 2004.[^r31]
- [[Communication and Persuasion- Central and Peripheral Routes to Attitude Change]] — R. Petty and J. Cacioppo, 1986.[^r32]
- [[Simulating Organizations- Computational Models of Institutions and Groups]] — M. Prietula, K. Carley, and L. Gasser (eds.), 1998.[^r33]
- [[Fitting and Compilation of Multiagent Models Through Piecewise Linear Functions]] — D. V. Pynadath and S. C. Marsella, 2004.[^r34]
- [[Multiagent Teamwork- Analyzing the Optimality and Complexity of Key Theories and Models]] — D. V. Pynadath and M. Tambe, 2002.[^r35]
- [[Subtypes of Victims and Aggressors in Children-s Peer Groups]] — D. Schwartz, 2000.[^r36]
- [[The Optimal Control of Partially Observable Markov Processes Over a Finite Horizon]] — R. D. Smallwood and E. J. Sondik, 1973.[^r37]
- [[Requirements for Belief Models in Cooperative Dialogue]] — J. Taylor, J. Carletta, and C. Mellish, 1996.[^r38]
- [[Natural Theories of Mind]] — A. Whiten (ed.), 1991.[^r39]

## Audit Log

- Independent audit found an incorrect source link. Corrected it to the verified official PDF; content checks passed. Re-audit pending.

- Independent re-audit passed; import finalized.

## LLM Justification
[^r1]: [IJCAI-05 paper PDF](https://www.ijcai.org/Proceedings/05/Papers/1559.pdf), abstract, p. 1; exact transcription.
[^r2]: [IJCAI-05 paper PDF](https://www.ijcai.org/Proceedings/05/Papers/1559.pdf), Introduction, p. 1.
[^r3]: [IJCAI-05 paper PDF](https://www.ijcai.org/Proceedings/05/Papers/1559.pdf), §§3.1–3.2, pp. 4–5.
[^r4]: [IJCAI-05 paper PDF](https://www.ijcai.org/Proceedings/05/Papers/1559.pdf), Introduction, p. 1; §2, p. 2.
[^r5]: [IJCAI-05 paper PDF](https://www.ijcai.org/Proceedings/05/Papers/1559.pdf), §§2.1–2.4, pp. 2–5.
[^r6]: [IJCAI-05 paper PDF](https://www.ijcai.org/Proceedings/05/Papers/1559.pdf), §2.1 “Model of the World” and “Nested Beliefs,” pp. 2–3.
[^r7]: [IJCAI-05 paper PDF](https://www.ijcai.org/Proceedings/05/Papers/1559.pdf), §2.2 “Preferences,” p. 2.
[^r8]: [IJCAI-05 paper PDF](https://www.ijcai.org/Proceedings/05/Papers/1559.pdf), §2.3 “Policies of Behavior,” p. 3, equations (2)–(3).
[^r9]: [IJCAI-05 paper PDF](https://www.ijcai.org/Proceedings/05/Papers/1559.pdf), §2.3 “Nested Beliefs,” p. 3.
[^r10]: [IJCAI-05 paper PDF](https://www.ijcai.org/Proceedings/05/Papers/1559.pdf), §2.3 “Stereotypical Mental Models,” pp. 3–4; §3.1, p. 4.
[^r11]: [IJCAI-05 paper PDF](https://www.ijcai.org/Proceedings/05/Papers/1559.pdf), §2.4, pp. 4–5, equation (4). Numeric factor weights and trust/support increments are not reported.
[^r12]: [IJCAI-05 paper PDF](https://www.ijcai.org/Proceedings/05/Papers/1559.pdf), §2.4, p. 5.
[^r13]: [IJCAI-05 paper PDF](https://www.ijcai.org/Proceedings/05/Papers/1559.pdf), §2.4, p. 5.
[^r14]: [IJCAI-05 paper PDF](https://www.ijcai.org/Proceedings/05/Papers/1559.pdf), §3.2, p. 5.
[^r15]: [IJCAI-05 paper PDF](https://www.ijcai.org/Proceedings/05/Papers/1559.pdf), §§2.1–2.4, pp. 2–5; no full execution schedule is specified.
[^r16]: [IJCAI-05 paper PDF](https://www.ijcai.org/Proceedings/05/Papers/1559.pdf), §3.2, p. 5, and Table 1, p. 6.
[^r17]: [IJCAI-05 paper PDF](https://www.ijcai.org/Proceedings/05/Papers/1559.pdf), §3.1, p. 4.
[^r18]: [IJCAI-05 paper PDF](https://www.ijcai.org/Proceedings/05/Papers/1559.pdf), §3.1, p. 4.
[^r19]: [IJCAI-05 paper PDF](https://www.ijcai.org/Proceedings/05/Papers/1559.pdf), §3.2, pp. 5–6.
[^r20]: [IJCAI-05 paper PDF](https://www.ijcai.org/Proceedings/05/Papers/1559.pdf), §3.2, pp. 5–6.
[^r21]: [IJCAI-05 paper PDF](https://www.ijcai.org/Proceedings/05/Papers/1559.pdf), §3.2, pp. 5–6.
[^r24]: [IJCAI-05 paper PDF](https://www.ijcai.org/Proceedings/05/Papers/1559.pdf), Introduction, p. 1; §4, p. 6.
[^r25]: [IJCAI-05 paper PDF](https://www.ijcai.org/Proceedings/05/Papers/1559.pdf), References, p. 6.
[^r26]: [IJCAI-05 paper PDF](https://www.ijcai.org/Proceedings/05/Papers/1559.pdf), References, p. 6.
[^r27]: [IJCAI-05 paper PDF](https://www.ijcai.org/Proceedings/05/Papers/1559.pdf), References, p. 6.
[^r28]: [IJCAI-05 paper PDF](https://www.ijcai.org/Proceedings/05/Papers/1559.pdf), References, p. 6.
[^r29]: [IJCAI-05 paper PDF](https://www.ijcai.org/Proceedings/05/Papers/1559.pdf), References, p. 6.
[^r30]: [IJCAI-05 paper PDF](https://www.ijcai.org/Proceedings/05/Papers/1559.pdf), References, p. 6.
[^r31]: [IJCAI-05 paper PDF](https://www.ijcai.org/Proceedings/05/Papers/1559.pdf), References, p. 6.
[^r32]: [IJCAI-05 paper PDF](https://www.ijcai.org/Proceedings/05/Papers/1559.pdf), References, p. 6.
[^r33]: [IJCAI-05 paper PDF](https://www.ijcai.org/Proceedings/05/Papers/1559.pdf), References, p. 6.
[^r34]: [IJCAI-05 paper PDF](https://www.ijcai.org/Proceedings/05/Papers/1559.pdf), References, p. 6.
[^r35]: [IJCAI-05 paper PDF](https://www.ijcai.org/Proceedings/05/Papers/1559.pdf), References, p. 6.
[^r36]: [IJCAI-05 paper PDF](https://www.ijcai.org/Proceedings/05/Papers/1559.pdf), References, p. 6.
[^r37]: [IJCAI-05 paper PDF](https://www.ijcai.org/Proceedings/05/Papers/1559.pdf), References, p. 6.
[^r38]: [IJCAI-05 paper PDF](https://www.ijcai.org/Proceedings/05/Papers/1559.pdf), References, p. 6.
[^r39]: [IJCAI-05 paper PDF](https://www.ijcai.org/Proceedings/05/Papers/1559.pdf), References, p. 6.
