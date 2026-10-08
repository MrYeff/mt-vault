# Simulation reading list

> Reading priorities proposed via LLM for [[What are my goal - LLM]] and [[Model]].

The original five were examples, not an exhaustive list or a ranking. This list ranks candidates already in the vault by usefulness for testing information algorithms that improve social integration. It is a reading order, not a ranking of scientific quality or a complete survey.[^scope]

## Read first

1. **PsychSim** — [[PsychSim- Modeling Theory of Mind with Decision-Theoretic Agents]]
   - Closest comparison for nested beliefs: agents act using models of others’ beliefs, goals and reactions. Read §§2.1–2.4 first. The school-bullying example is not a social-media integration test.[^psychsim]

2. **Reputation Game** — [[A Reputation Game Simulation- Emergent Social Phenomena from Information Theory]]
   - Closest comparison for uncertain beliefs and credibility: communication changes perceived honesty, beliefs about others’ beliefs and directed friend/enemy judgments. Read §§3–4, then Appendix A for belief updating. These judgments are not validated measures of human friendship.[^reputation]

3. **PROD** — [[The Effect of People Recommenders on Echo Chambers and Polarization]]
   - People recommendations → directed follow changes → opinions. Start here for a small algorithm-testing baseline. Follow ties are not friendship quality.[^m1]

4. **Ren & Kraut** — [[Agent-Based Modeling to Inform Online Community Design- Impact of Topical Breadth- Message Volume- and Discussion Moderation on Member Commitment and Contribution]]
   - Personalized message exposure → informational and relational benefits → participation. Closest of this selection to your interest in belonging and community commitment. Login commitment is not measured belonging.[^m2]

5. **Bartley et al.** — [[Bias Reduction in Social Networks Through Agent-Based Simulations]]
   - Feed algorithms → biased perceptions of the network. Read for imperfect information without a complex cognitive model. Traits and the underlying network stay fixed.[^m3]

6. **Liu et al.** — [[Exploring Trade-Offs for Online Mental Health Matching- Agent-Based Modeling Study]]
   - Matching algorithms → support conversations, waiting time and subgroup outcomes. Read for a data-based evaluation process. Chat ratings and blocking do not measure lasting friendships.[^m4]

7. **Sutcliffe et al.** — [[Social Relationships and the Emergence of Social Networks]]
   - Interaction → trust → relationship formation and decay. Read for relationship mechanisms to combine with an exposure model. No ranked feed; some exact rules remain unspecified.[^m5]

## Read next

8. **Construct** — [[Construct User Guide]]
   - Existing framework for knowledge exchange and dynamic interactions. Read to decide whether to configure an existing engine. Start with the Standard Interaction Model, not the whole manual.[^m6]

9. **T-RECS** — [[T-RECS- A Simulation Tool to Study the Societal Impact of Recommender Systems]]
   - Read for separating recommender algorithms, user behavior and measurements. Content feedback is supported; friendship dynamics need an added mechanism.[^m7]

10. **HUMAT** — [[HUMAT- An Integrated Framework for Modelling Individual Motivations- Social Exchange and Network Dynamics]]
   - Read for motives and social influence on choices. Its core A/B choice model is narrower than your topic beliefs; do not assume it already supplies imperfect knowledge of others’ choices.[^m8]

11. **FIRMAN** — [[How Does Facebook Retain Segregated Friendship- An Agent-Based Model Approach]]
   - Read for capacity limits and identity-based friendship formation. Lower priority for information algorithms: reciprocal ties and no ranked feed.[^m9]

## Read if needed

12. **BayesACT** — [[Affect control processes- Intelligent affective interaction using a partially observable Markov decision process]]
   - Read if uncertainty about identities and affect must determine interaction choices. Richer belief state and decision rules than your current scalar associations; not a ready-made feed simulator.[^m10]

13. **OASIS** — [[OASIS- Open Agent Social Interaction Simulations with One Million Agents]]
   - Read if you want an LLM-based social-media environment with recommendations and follow/comment actions. Treat reproduced phenomena as evidence for those experiments, not validation of social integration.[^m11]

14. **Concordia** — [[Generative agent-based modeling with actions grounded in physical- social- or digital space using Concordia]]
   - Read if conversations and shared activities require language-based agents. A configurable framework, not one fixed model of friendship.[^m12]

## Read alongside the simulations

> These inform representation and validation; they are not complete simulation alternatives.

- [[Cognitive social structures]] — Represent what each person thinks the network looks like, separately from other people’s reports.[^c1]
- [[Are You Your Friends- Friend- Poor Perception of Friendship Ties Limits the Ability to Promote Behavioral Change]] — Check why perceived reciprocity and directed friendship must be separate.[^c2]
- [[Parasocial Interaction and Parasocial Relationship- Conceptual Clarification and a Critical Assessment of Measures]] — Define what a parasocial relationship means before treating every one-sided edge as one.[^c3]
- [[The Focused Organization of Social Ties]] — Read when adding shared activities and meeting contexts.[^c4]
- [[A causal test of the strength of weak ties]] — Study evaluation of a real people-recommendation intervention. Its outcome is job mobility, not belonging.[^c5]

## Other relevant branches

- RecSim / RecSim NG / SARDINE: read when recommender feedback, uncertainty or sequential policy evaluation becomes the main implementation problem. [[RecSim- A Configurable Simulation Platform for Recommender Systems]]; [[RecSim NG- Toward Principled Uncertainty Modeling for Recommender Ecosystems]]; [[SARDINE- Simulator for Automated Recommendation in Dynamic and Interactive Environments]].[^b1]
- SimSoM: read when information diffusion and manipulation matter more than relationship formation. The vault extraction still has an audit-failed flag. [[Quantifying the vulnerabilities of the online public square to adversarial manipulation tactics]].[^b2]
- Construct-SC: especially relevant to beliefs about others’ knowledge and memory limits. Read the primary paper; its vault extraction still has an audit-failed flag. [[The Power of Social Cognition]].[^b3]
- Other LLM environments: compare if choosing that approach; do not read all before implementing a small baseline. [[Y Social- an LLM-powered Social Media Digital Twin]]; [[AgentSociety- Large-Scale Simulation of LLM-Driven Generative Agents Advances Understanding of Human Behaviors and Society]]; [[Humanoid Agents- Platform for Simulating Human-like Generative Agents]].[^b4]

## LLM Justification

[^scope]: Ranking is a project-specific judgment: prioritize algorithm interventions, relationship outcomes, imperfect information and simple mechanisms. Coverage is the inspected vault candidates, not all published simulations. Paper-entry warnings and existing audits are unchanged; inclusion does not certify an extraction.
[^m1]: [[The Effect of People Recommenders on Echo Chambers and Polarization]] — Model and limitations; fixed out-degree and scalar opinions. Relevance and reading priority are recommendations, not findings of the paper.
[^m2]: [[Agent-Based Modeling to Inform Online Community Design- Impact of Topical Breadth- Message Volume- and Discussion Moderation on Member Commitment and Contribution]] — §§4–5 and validation: participation benefits, interpersonal bonds, moderation conditions; baseline validation does not validate moderation effects. Relevance and reading priority are recommendations, not findings of the paper.
[^m3]: [[Bias Reduction in Social Networks Through Agent-Based Simulations]] — §§3.1–3.4: fixed traits, observed network exposure, feed policies and local bias. Relevance and reading priority are recommendations, not findings of the paper.
[^m4]: [[Exploring Trade-Offs for Online Mental Health Matching- Agent-Based Modeling Study]] — Methods / Simulation Framework / Matching Policies / Validation: platform replication and predicted conversation outcomes. Relevance and reading priority are recommendations, not findings of the paper.
[^m5]: [[Social Relationships and the Emergence of Social Networks]] — Model and limitations in the audited entry: interaction histories, directed trust and relationship dynamics. Also see the earlier Computational Modelling paper. Relevance and reading priority are recommendations, not findings of the paper.
[^m6]: [[Construct User Guide]] — Knowledge Network / Interaction Sphere / Models and Construct Program Flow / Standard Interaction Model, PDF pp. 20–25, 50–52. Relevance and reading priority are recommendations, not findings of the paper.
[^m7]: [[T-RECS- A Simulation Tool to Study the Societal Impact of Recommender Systems]] — Framework and case studies in the audited entry: configurable user–item feedback and conceptual replications. Relevance and reading priority are recommendations, not findings of the paper.
[^m8]: [[HUMAT- An Integrated Framework for Modelling Individual Motivations- Social Exchange and Network Dynamics]] — Core model and Table 3: experiential, social and value motives; perfect knowledge assumption for choices. See conflicts recorded in the audited entry. Relevance and reading priority are recommendations, not findings of the paper.
[^m9]: [[How Does Facebook Retain Segregated Friendship- An Agent-Based Model Approach]] — Accessible author manuscript model; published full text remains unavailable as marked in the entry. Relevance and reading priority are recommendations, not findings of the paper.
[^m10]: [[Affect control processes- Intelligent affective interaction using a partially observable Markov decision process]] — Abstract and §3.1: probabilistic affective sentiments, application-specific POMDP and utility-directed actions. Relevance and reading priority are recommendations, not findings of the paper.
[^m11]: [[OASIS- Open Agent Social Interaction Simulations with One Million Agents]] — Abstract and framework description: dynamic social environment, action space, recommendations and reported phenomena. Relevance and reading priority are recommendations, not findings of the paper.
[^m12]: [[Generative agent-based modeling with actions grounded in physical- social- or digital space using Concordia]] — Abstract and framework: memory/components, observations, actions and Game Master environment updates. Relevance and reading priority are recommendations, not findings of the paper.
[^c1]: [[Cognitive social structures]] — §§2–3: perceiver × sender × receiver reports and aggregation; measurement, not an update rule.
[^c2]: [[Are You Your Friends- Friend- Poor Perception of Friendship Ties Limits the Ability to Promote Behavioral Change]] — Abstract / Methods / Results: friendship nominations, imperfect perception of directionality and the activity intervention.
[^c3]: [[Parasocial Interaction and Parasocial Relationship- Conceptual Clarification and a Critical Assessment of Measures]] — Abstract and conceptual distinctions: within-viewing parasocial interaction versus relationship; scale comparison.
[^c4]: [[The Focused Organization of Social Ties]] — Conceptual account of social foci organizing opportunities for ties.
[^c5]: [[A causal test of the strength of weak ties]] — Randomized LinkedIn recommendation experiments and job-mobility outcomes.
[^b1]: [[RecSim- A Configurable Simulation Platform for Recommender Systems]]; [[RecSim NG- Toward Principled Uncertainty Modeling for Recommender Ecosystems]]; [[SARDINE- Simulator for Automated Recommendation in Dynamic and Interactive Environments]]. Branch placement is a reading recommendation based on the entries’ stated scope; warnings are retained in those entries.
[^b2]: [[Quantifying the vulnerabilities of the online public square to adversarial manipulation tactics]]. Branch placement is a reading recommendation based on the entries’ stated scope; warnings are retained in those entries.
[^b3]: [[The Power of Social Cognition]]. Branch placement is a reading recommendation based on the entries’ stated scope; warnings are retained in those entries.
[^b4]: [[Y Social- an LLM-powered Social Media Digital Twin]]; [[AgentSociety- Large-Scale Simulation of LLM-Driven Generative Agents Advances Understanding of Human Behaviors and Society]]; [[Humanoid Agents- Platform for Simulating Human-like Generative Agents]]. Branch placement is a reading recommendation based on the entries’ stated scope; warnings are retained in those entries.

[^psychsim]: [[PsychSim- Modeling Theory of Mind with Decision-Theoretic Agents]] — §§2.1–2.4 define world states, preferences, nested agent models, bounded lookahead and influence; §3 illustrates school violence. Priority is a project judgment based on [[Model]], not a paper result.
[^reputation]: [[A Reputation Game Simulation- Emergent Social Phenomena from Information Theory]] — §§3–4 and Appendix A define uncertain honesty beliefs, theory of mind, communication and belief compression; Appendix B.4.1 defines directional friend/enemy judgments. §§1 and 5 state proof-of-concept and ad-hoc strategy limits. Priority is a project judgment.
