---
title: "Value-based large language model agent simulation for mutual evaluation of trust and interpersonal closeness"
tags:
  - model
  - simulation
authors:
  - "[[Literature/Authors/Yuki Sakamoto|Yuki Sakamoto]]"
  - "[[Literature/Authors/Takahisa Uchida|Takahisa Uchida]]"
  - "[[Literature/Authors/Hiroshi Ishiguro|Hiroshi Ishiguro]]"
publication date: 2025-11-24
source: https://pmc.ncbi.nlm.nih.gov/articles/PMC12644628/
doi: 10.1038/s41598-025-25531-1
read status: Todo
---
## Abstract

Large language models (LLMs) have emerged as powerful tools for simulating complex social phenomena using human-like agents with specific traits. In human societies, value similarity is important for building trust and close relationships; however, it remains unexplored whether this principle holds true in artificial societies comprising LLM agents. Therefore, this study investigates the influence of value similarity on relationship-building among LLM agents through two experiments. First, in a preliminary experiment, we evaluated the controllability of values in LLMs to identify the most effective model and prompt design for controlling the values. Subsequently, in the main experiment, we generated pairs of LLM agents imbued with specific values and analyzed their mutual evaluations of trust and interpersonal closeness following a dialogue. The experiments were conducted in English and Japanese to investigate language dependence. The results confirmed that pairs of agents with higher value similarity exhibited greater mutual trust and interpersonal closeness. Our findings demonstrate that the LLM agent simulation serves as a valid testbed for social science theories, contributes to elucidating the mechanisms by which values influence relationship building, and provides a foundation for inspiring new theories and insights into the social sciences.

## Research Questions
> Research Questions extracted via LLM

- Can two LLM agents prompted with different Schwartz values reproduce a positive relationship between value similarity and mutual trust/closeness after dialogue?[^r1]

## Model
> Model extracted via LLM according to [[Model Notation]]

- This is a controlled paired-agent experiment, not an evolving population model.[^r2]

```yml
Experiment:
  languages: [English, Japanese]
  dialogue_topics: [Hobbies, Housing]
  value_pairs: [ValuePair]
  repetitions: 10

Agent:
  assigned_value: SchwartzValue
  llm: selected_model
  prompt_design: selected_prompt

Evaluation:
  trust: [1..5, 1..5, 1..5]
  closeness: IOS_1..7
```

```
run_pair_experiment(pair, language, topic):
  instantiate two separately prompted value agents
  exchange five utterances each; pass explicit history each turn
  each agent rates the other’s trust and IOS closeness
  repeat 10 times; summarize by value-similarity level
```

- Before the main experiment, test GPT-4o, Gemini 1.5 Flash, and Claude 3.5 Sonnet on the PVQ across system/user prompt, second/third person, value definition, and language; use 50 independent runs to select the most controllable setting.[^r3]
- Main design covers 55 basic-value pairs and 10 higher-order pairs.[^r3]

### What does it represent?
A test of whether value similarity in LLM agent pairs is associated with reciprocal trust and interpersonal-closeness ratings.[^r1]

### How does it work?
The two-stage prompt selection and paired-dialogue procedure is specified above; outcomes are LLM ratings, not human-subject responses.[^r3]

### What can it answer?
It compares ratings across value similarity, language, and dialogue topic. The authors report higher trust/closeness with more similar assigned values.[^r4]

### Where does it apply?
Evidence is limited to tested model/prompt settings, Schwartz values, English/Japanese, two dialogue tasks, and the stated scales. The authors note LLM motivational and visual-judgment limits.[^r5]
## Metadata
### References

- [[UnresolvedReference6590378B37550528]]
- [[UnresolvedReference20F2BF5BE220EF1E]]
- [[GenerativeAgentsInteractiveSimulacraOfHumanBehavior]]
- [[UnresolvedReferenceC0126F35016CAE2F]]
- [[AgentSociety- Large-Scale Simulation of LLM-Driven Generative Agents Advances Understanding of Human Behaviors and Society]]
- [[UnresolvedReference68A6BB66C5707F85]]
- [[UnresolvedReference80600E23B097E362]]
- [[UnresolvedReference57702B42D7D06B33]]
- [[UnresolvedReference6E492695DEFD91F1]]
- [[UnresolvedReferenceEA3453B68BDD65C0]]
- [[UnresolvedReference6B26B0BB86A20B38]]
- [[UnresolvedReference2AC807925D9FBCE0]]
- [[UnresolvedReference4E7AD66CBFBAD4FD]]
- [[UnresolvedReference57847B6A16D2A075]]
- [[UnresolvedReference161BCFD8FAD3F0E1]]
- [[InclusionOfOtherInTheSelfScaleAndTheStructureOfInterpersonalCloseness]]
- [[UnresolvedReferenceF24DF22418743FAD]]
- [[UnresolvedReferenceE6613F24008DFBC4]]
- [[UnresolvedReferenceA40F298805CAD34F]]
- [[UnresolvedReferenceA54FF0DD94EC20A4]]
- [[SocialPenetrationTheDevelopmentOfInterpersonalRelationships]]
- [[UnresolvedReference98FE83225AFC8078]]
- [[RefiningTheTheoryOfBasicIndividualValues]]
- [[UnresolvedReference6EA04C3BCAD5130F]]
- [[UnresolvedReferenceA4FBEA4DC8AF6854]]
- [[ADomainIndependentFrameworkForModelingEmotion]]
- [[UnresolvedReferenceCE0D56BB4F903188]]
- [[UnresolvedReferenceDE5C3ECC24D4422E]]
- [[UnresolvedReferenceA87869A79121F878]]
- [[UnresolvedReference18A81A26A975048A]]
- [[UnresolvedReferenceA01B4717E3F48B77]]
- [[UnresolvedReference4E66B2819F5E1227]]
- [[UnresolvedReferenceDA3D1CA8B532F7B6]]
- [[UnresolvedReferenceACC539F0D79D6415]]
- [[UnresolvedReference640BEFC879BCC7C4]]
- [[UnresolvedReference9A1C947A040DB087]]
- [[UnresolvedReferenceA64A149A2A96B553]]
- [[UnresolvedReferenceA9CEF72D4D580ACF]]
- [[UnresolvedReferenceA1E2AA7F39414A92]]
- [[UnresolvedReferenceDC73A0D148DABCB7]]
- [[UnresolvedReference1D27950241C0D763]]
- [[UnresolvedReferenceCDDA087BCFC15535]]


## Audit Log
- Audit invalidated (2026-09-30): auditor admitted incomplete independent checks and premature flag removal. Previous valid audits, if any, remain separate.

## LLM Justification
[^r1]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12644628/; Introduction and Methods, states the value-similarity question and paired-agent design.
[^r2]: Same source; §§Methods and Preliminary Experiment, defines the two-stage controlled experiment.
[^r3]: Same source; §§Methods, “Preliminary experiment” and “Main experiment,” including Tables 1–2 and dialogue procedure, specifies models, prompt factors, value pairings, language, turn count, repetitions, and outcome measures.
[^r4]: Same source; Results, “Main experiment,” Tables 3–6, reports relation of similarity to trust and IOS evaluations.
[^r5]: Same source; Discussion and limitations, notes language scope, lack of intrinsic trust motivation, and IOS diagram limitation.
