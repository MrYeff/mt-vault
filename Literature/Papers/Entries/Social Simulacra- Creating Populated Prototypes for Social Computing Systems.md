---
title: "Social Simulacra: Creating Populated Prototypes for Social Computing Systems"
tags:
  - social_computing
  - llm_simulation
  - "model"
  - "simulation"
authors:
  - "[[Literature/Authors/Joon-Sung Park|Joon-Sung Park]]"
  - "[[Literature/Authors/Lindsay Popowski|Lindsay Popowski]]"
  - "[[Literature/Authors/Carrie Jun Cai|Carrie Jun Cai]]"
  - "[[Literature/Authors/Meredith Ringel Morris|Meredith Ringel Morris]]"
  - "[[Literature/Authors/Percy Liang|Percy Liang]]"
  - "[[Literature/Authors/Michael S. Bernstein|Michael S. Bernstein]]"
publication date: 2022-10-28 
source: "https://hci.stanford.edu/publications/2022/Park_SocialSimulacra_UIST22.pdf"
doi: 10.1145/3526113.3545616
read status: Todo
⚠️:
  - audit failed
---

## Abstract

Social computing prototypes probe the social behaviors that may arise in an envisioned system design. This prototyping practice is currently limited to recruiting small groups of people. Unfortunately, many challenges do not arise until a system is populated at a larger scale. Can a designer understand how a social system might behave when populated, and make adjustments to the design before the system falls prey to such challenges? We introduce social simulacra, a prototyping technique that generates a breadth of realistic social interactions that may emerge when a social computing system is populated. Social simulacra take as input the designer’s description of a community’s design—goal, rules, and member personas—and produce as output an instance of that design with simulated behavior, including posts, replies, and anti-social behaviors. We demonstrate that social simulacra shift the behaviors that they generate appropriately in response to design changes, and that they enable exploration of “what if?” scenarios where community members or moderators intervene. To power social simulacra, we contribute techniques for prompting a large language model to generate thousands of distinct community members and their social interactions with each other; these techniques are enabled by the observation that large language models’ training data already includes a wide variety of positive and negative behavior on social media platforms. In evaluations, we show that participants are often unable to distinguish social simulacra from actual community behavior and that social computing designers successfully refine their social computing designs when using social simulacra.

## Research Questions
> Research Questions extracted via LLM
- Can large language models populate a social-computing prototype with diverse people and plausible social interactions?[^r1]
- How do generated behaviors respond to design changes, and can the prototypes help designers explore interventions?[^r1]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?
- SimReddit generates a populated social-computing prototype from a community goal, rules and seed personas. Synthetic participants contribute posts and replies; designers explore alternative designs/interventions.[^r3]
- These types expose prompt inputs and outputs; personas are natural-language interests/personality descriptions.[^r3]

```yml
World:
  design: Design
  personas: [Persona]
  threads: [Thread]

Design:
  goal: str
  rules: [str]
  seeds: [Persona]

Persona:
  description: str

Thread:
  messages: [Message]

Message:
  author: PersonaId
  text: str
```

### How does it work?
- GPT-3 davinci expands example personas with a few-shot list prompt (`SEEDS=10`, `POPULATION=1000` defaults). For a top-level post, prompt with author persona, repeated community rules, goal and headline-style HTML span; generation stops at the closing span.[^r3]
- Generate replies iteratively, conditioning each on the responder, rules and previous thread. Choose a new persona with probability 0.5; otherwise choose a prior participant other than the latest speaker. If context overflows, truncate from the first post.[^r3]
- Per-thread reply probability is sampled Normal(mean 0.65, unspecified standard deviation); continue by Bernoulli trials. The text says stop after “more than 8 replies,” leaving the precise boundary and treatment of probabilities outside [0,1] unspecified.[^r3]
- WhatIf replaces the current responder persona (e.g., a troll) and can append a moderator intervention to the conversation context. Multiverse reuses the prompts with temperature raised from 0.7 to 0.8.[^r3]
- The typed procedure summarizes the documented prompt order; `LLM` is the configured davinci text-completion model.[^r3]

```
generate_post(
  design: Design,
  author: PersonaId,
  personas: [Persona]
) -> Message:
  context = (personas[author], design.goal, design.rules)
  text = LLM.complete(headline_prompt(context), stop="</span>")
  out = Message(author, text)


generate_reply(
  design: Design,
  thread: Thread,
  responder: PersonaId,
  personas: [Persona]
) -> Message:
  context = (personas[responder], design.rules, thread.messages)
  text = LLM.complete(reply_prompt(context), stop="</span>")
  out = Message(responder, text)
```

### What can it answer?
- Explore plausible interactions and design alternatives. In the technical evaluation, 200 participants judged real and synthetic threads from 50 subreddits (100 real/synthetic comparisons) across full SimReddit, crowdworker, no-community-description and no-persona conditions. The table reports mean error rates of 41%, 32%, 21% and 34%, respectively; full SimReddit outperformed every comparison (`F(3,196)=22.49`, `p<.001`). The following prose gives 33% for the no-persona condition, while the table gives 34%; the note preserves that one-point source discrepancy. In the designer study, 16 experienced practitioners used generations and WhatIf/Multiverse to revise community goals/rules and consider moderation; all reported useful unexpected insights, while the authors frame outputs as design prompts rather than predictions.[^r4]

### Where does it apply?
- Early social-system prototyping. This summary omits literal prompt templates and UI; plausibility/design-usefulness evaluations do not calibrate future community behavior.[^r3][^r4]

## Metadata
### References

- [[The Intellectual Challenge of CSCW- The Gap between Social Requirements and Technical Feasibility|The Intellectual Challenge of CSCW: The Gap between Social Requirements and Technical Feasibility]]
- [[Cyberbullying victimization among Turkish online social utility members|Cyberbullying victimization among Turkish online social utility members]]
- [[Prototyping Tools and Techniques|Prototyping Tools and Techniques]]
- [[The Trouble with Social Computing Systems Research|The Trouble with Social Computing Systems Research]]
- [[On the opportunities and risks of foundation models|On the opportunities and risks of foundation models]]
- [[Language models are few-shot learners|Language models are few-shot learners]]
- [[Experience prototyping|Experience prototyping]]
- [[Learning visual importance for graphic designs and data visualizations|Learning visual importance for graphic designs and data visualizations]]
- [[-This Post Will Just Get Taken Down-- Characterizing Removed Pro-Eating Disorder Social Media Content|"This Post Will Just Get Taken Down": Characterizing Removed Pro-Eating Disorder Social Media Content]]
- [[You can’t stay here- The efficacy of reddit’s 2015 ban examined through hate speech|You can’t stay here: The efficacy of reddit’s 2015 ban examined through hate speech]]
- [[The Internet’s Hidden Rules- An Empirical Study of Reddit Norm Violations at Micro, Meso, and Macro Scales|The Internet’s Hidden Rules: An Empirical Study of Reddit Norm Violations at Micro, Meso, and Macro Scales]]
- [[The bag of communities- Identifying abusive behavior online with preexisting internet data|The bag of communities: Identifying abusive behavior online with preexisting internet data]]
- [[Anyone Can Become a Troll- Causes of Trolling Behavior in Online Discussions|Anyone Can Become a Troll: Causes of Trolling Behavior in Online Discussions]]
- [[Antisocial behavior in online discussion communities|Antisocial behavior in online discussion communities]]
- [[How hate groups’ secret sound system works|How hate groups’ secret sound system works]]
- [[The toastboard- Ubiquitous instrumentation and automated checking of breadboarded circuits|The toastboard: Ubiquitous instrumentation and automated checking of breadboarded circuits]]
- [[Reddit rules! characterizing an ecosystem of governance|Reddit rules! characterizing an ecosystem of governance]]
- [[Twitter manipulates your feed- Ethical considerations|Twitter manipulates your feed: Ethical considerations]]
- [[Informed consent and the Facebook emotional manipulation study|Informed consent and the Facebook emotional manipulation study]]
- [[Design- cultural probes|Design: cultural probes]]
- [[RealToxicityPrompts- Evaluating Neural Toxic Degeneration in Language Models|RealToxicityPrompts: Evaluating Neural Toxic Degeneration in Language Models]]
- [[Piggyback prototyping- Using existing, large-scale social computing systems to prototype new ones|Piggyback prototyping: Using existing, large-scale social computing systems to prototype new ones]]
- [[Groupware and social dynamics- Eight challenges for developers|Groupware and social dynamics: Eight challenges for developers]]
- [[The rise and decline of an open collaboration system- How Wikipedia’s reaction to popularity is causing its decline|The rise and decline of an open collaboration system: How Wikipedia’s reaction to popularity is causing its decline]]
- [[Unexpected expectations- Public reaction to the Facebook emotional contagion study|Unexpected expectations: Public reaction to the Facebook emotional contagion study]]
- [[Trolling in asynchronous computer-mediated communication- From user discussions to academic definitions|Trolling in asynchronous computer-mediated communication: From user discussions to academic definitions]]
- [[Authoring sensor-based interactions by demonstration with direct manipulation and pattern recognition|Authoring sensor-based interactions by demonstration with direct manipulation and pattern recognition]]
- [[Reflective physical prototyping through integrated design, test, and analysis|Reflective physical prototyping through integrated design, test, and analysis]]
- [[Augmenting Interactive Tables with Mice & Keyboards|Augmenting Interactive Tables with Mice & Keyboards]]
- [[Design as Exploration- Creating Interface Alternatives through Parallel Authoring and Runtime Tuning|Design as Exploration: Creating Interface Alternatives through Parallel Authoring and Runtime Tuning]]
- [[Design as Exploration- Creating Interface Alternatives through Parallel Authoring and Runtime Tuning|Design as Exploration: Creating Interface Alternatives through Parallel Authoring and Runtime Tuning]]
- [[Measuring massive multitask language understanding|Measuring massive multitask language understanding]]
- [[What do prototypes prototype-|What do prototypes prototype?]]
- [[Language Models as Zero-Shot Planners- Extracting Actionable Knowledge for Embodied Agents|Language Models as Zero-Shot Planners: Extracting Actionable Knowledge for Embodied Agents]]
- [[GPT-3 Explained|GPT-3 Explained]]
- [[PromptMaker- Prompt-based Prototyping with Large Language Models|PromptMaker: Prompt-based Prototyping with Large Language Models]]
- [[Genline and genform- Two tools for interacting with generative language models in a code editor|Genline and genform: Two tools for interacting with generative language models in a code editor]]
- [[Contexts of uninhibited online behavior- Flaming in social newsgroups on Usenet|Contexts of uninhibited online behavior: Flaming in social newsgroups on Usenet]]
- [[An empirical methodology for writing user-friendly natural language computer applications|An empirical methodology for writing user-friendly natural language computer applications]]
- [[An iterative design methodology for user-friendly natural language office information applications|An iterative design methodology for user-friendly natural language office information applications]]
- [[Surviving an “Eternal September”- How an Online Community Managed a Surge of Newcomers|Surviving an “Eternal September”: How an Online Community Managed a Surge of Newcomers]]
- [[He Says, She Says- Conflict and Coordination in Wikipedia|He Says, She Says: Conflict and Coordination in Wikipedia]]
- [[Trustworthy Online Controlled Experiments- Five Puzzling Outcomes Explained|Trustworthy Online Controlled Experiments: Five Puzzling Outcomes Explained]]
- [[Experimental evidence of massive-scale emotional contagion through social networks|Experimental evidence of massive-scale emotional contagion through social networks]]
- [[Building Successful Online Communities- Evidence-Based Social Design|Building successful online communities: Evidence-based social design]]
- [[SILK- Sketching Interfaces like Krazy|SILK: Sketching Interfaces like Krazy]]
- [[Deal or no deal- end-to-end learning for negotiation dialogues|Deal or no deal? end-to-end learning for negotiation dialogues]]
- [[Generated knowledge prompting for commonsense reasoning|Generated knowledge prompting for commonsense reasoning]]
- [[Pre-train, prompt, and predict- A systematic survey of prompting methods in natural language processing|Pre-train, prompt, and predict: A systematic survey of prompting methods in natural language processing]]
- [[Fantastically ordered prompts and where to find them- Overcoming few-shot prompt order sensitivity|Fantastically ordered prompts and where to find them: Overcoming few-shot prompt order sensitivity]]
- [[Design Galleries- A General Approach to Setting Parameters for Computer Graphics and Animation|Design Galleries: A General Approach to Setting Parameters for Computer Graphics and Animation]]
- [[Toward a “Critical Mass” Theory of Interactive Media|Toward a “Critical Mass” Theory of Interactive Media]]
- [[Preventing harassment and increasing group participation through social norms in 2,190 online science discussions|Preventing harassment and increasing group participation through social norms in 2,190 online science discussions]]
- [[Designscape- Design with interactive layout suggestions|Designscape: Design with interactive layout suggestions]]
- [[Measuring the Prevalence of Anti-Social Behavior in Online Communities|Measuring the Prevalence of Anti-Social Behavior in Online Communities]]
- [[The implied truth effect- Attaching warnings to a subset of fake news headlines increases perceived accuracy of headlines without warnings|The implied truth effect: Attaching warnings to a subset of fake news headlines increases perceived accuracy of headlines without warnings]]
- [[Studying Reddit- A Systematic Overview of Disciplines, Approaches, Methods, and Ethics|Studying Reddit: A Systematic Overview of Disciplines, Approaches, Methods, and Ethics]]
- [[Prolific- Quickly find research participants you can trust|Prolific: Quickly find research participants you can trust]]
- [[Language models are unsupervised multitask learners|Language models are unsupervised multitask learners]]
- [[Scaling language models- Methods, analysis & insights from training gopher|Scaling language models: Methods, analysis & insights from training gopher]]
- [[Zero-Shot Text-to-Image Generation|Zero-Shot Text-to-Image Generation]]
- [[Reddit by the Numbers|Reddit by the Numbers]]
- [[Prototyping for tiny fingers|Prototyping for tiny fingers]]
- [[Dilemmas in a general theory of planning|Dilemmas in a general theory of planning]]
- [[The fight for $15- The right wage for a working America|The fight for $15: The right wage for a working America]]
- [[Experimental Study of Inequality and Unpredictability in an Artificial Cultural Market|Experimental Study of Inequality and Unpredictability in an Artificial Cultural Market]]
- [[Sauron- embedded single-camera sensing of printed physical user interfaces|Sauron: embedded single-camera sensing of printed physical user interfaces]]
- [[Few-shot text generation with pattern-exploiting training|Few-shot text generation with pattern-exploiting training]]
- [[The Reflective Practitioner- How Professionals Think In Action|The Reflective Practitioner: How Professionals Think In Action]]
- [[Paper prototyping- what is it good for- A comparison of paper-and computer-based low-fidelity prototyping|Paper prototyping- what is it good for? A comparison of paper-and computer-based low-fidelity prototyping]]
- [[Paper prototyping- The fast and easy way to design and refine user interfaces|Paper prototyping: The fast and easy way to design and refine user interfaces]]
- [[Automatic Identification of Personal Insults on Social News Sites|Automatic Identification of Personal Insults on Social News Sites]]
- [[Paradigm shift- The new promise of information technology|Paradigm shift: The new promise of information technology]]
- [[Revisiting- The rise and decline- in a population of peer production projects|Revisiting" The rise and decline" in a population of peer production projects]]
- [[A General Inductive Approach for Analyzing Qualitative Evaluation Data|A General Inductive Approach for Analyzing Qualitative Evaluation Data]]
- [[Graph cluster randomization- Network exposure to multiple universes|Graph cluster randomization: Network exposure to multiple universes]]
- [[The state of online harassment|The state of online harassment]]
- [[Superglue- A stickier benchmark for general-purpose language understanding systems|Superglue: A stickier benchmark for general-purpose language understanding systems]]
- [[Ethical and social risks of harm from Language Models|Ethical and social risks of harm from Language Models]]
- [[PromptChainer- Chaining Large Language Model Prompts through Visual Programming|PromptChainer: Chaining Large Language Model Prompts through Visual Programming]]
- [[AI Chains- Transparent and Controllable Human-AI Interaction by Chaining Large Language Model Prompts|AI Chains: Transparent and Controllable Human-AI Interaction by Chaining Large Language Model Prompts]]
- [[Voyant- generating structured feedback on visual designs using a crowd of non-experts|Voyant: generating structured feedback on visual designs using a crowd of non-experts]]
- [[From infrastructure to culture- A-B testing challenges in large scale social networks|From infrastructure to culture: A/B testing challenges in large scale social networks]]
- [[Describing Personas|Describing Personas]]
- [[Defending against neural fake news|Defending against neural fake news]]
- [[Calibrate before use- Improving few-shot performance of language models|Calibrate before use: Improving few-shot performance of language models]]

## Audit Log
- Audit invalidated (2026-09-30): auditor admitted clearing flags before completing independent source checks. A new independent audit is required.
- Strong source review (2026-09-30): Expanded actual persona→top-level-post→iterative-reply prompt chain, responder selection/stopping rules, WhatIf moderator context and Multiverse setting; stated normal-probability and stopping ambiguity. Independent re-audit pending.
- Initial independent audit: failed on missing model mechanisms, abstract fidelity, or source-access reporting; see `vault/.automation/audit/next-forty-54-66-initial-2026-09-30.json`. Revisions added source-located model detail; independent re-audit remains pending.

- WITHDRAWN audit claim (2026-09-30): previously reported PASS; source claims, current extraction, metadata, references and footnotes checked against the available primary source. See `vault/.automation/audit/remaining-audit-b-2026-09-30.json`.

## LLM Justification
[^r1]: The paper’s abstract, at https://arxiv.org/abs/2208.04024. The questions paraphrase the stated purpose, research scope, and reported approach.
[^r3]: Park et al., §§3.2–3.4 (Generate, WhatIf, Multiverse), §4.2.1–4.2.5 (persona expansion, top-level-post/reply prompts, Bernoulli continuation, responder selection, context truncation and temperature), §4.3 (base davinci engine). §4.2.3 leaves the normal standard deviation and [0,1] handling unspecified. Full published paper: https://hci.stanford.edu/publications/2022/Park_SocialSimulacra_UIST22.pdf.
[^r4]: Park et al., §§5.1–5.3 (50 subreddits created after GPT-3 release, real/generated comparisons and prompt ablations), §6 (16 designers), §7.1 (limitations of generation/design feedback). Full published paper: https://hci.stanford.edu/publications/2022/Park_SocialSimulacra_UIST22.pdf.
