---

title: "Humanoid Agents: Platform for Simulating Human-like Generative Agents"
tags:
  - model
  - simulation
  - generative_agents
authors:
  - "[[Literature/Authors/Zhilin Wang|Zhilin Wang]]"
  - "[[Literature/Authors/Yu Ying Chiu|Yu Ying Chiu]]"
  - "[[Literature/Authors/Yu Cheung Chiu|Yu Cheung Chiu]]"
publication date: 2023-12-06
source:
  - https://doi.org/10.18653/v1/2023.emnlp-demo.15
  - https://aclanthology.org/2023.emnlp-demo.15/
doi: 10.18653/v1/2023.emnlp-demo.15
read status: Todo
⚠️: []
---
## Abstract

Just as computational simulations of atoms, molecules and cells have shaped the way we study the sciences, true-to-life simulations of human-like agents can be valuable tools for studying human behavior. We propose Humanoid Agents, a system that guides Generative Agents to behave more like humans by introducing three elements of System 1 processing: Basic needs (e.g. hunger, health and energy), Emotion and Closeness in Relationships. Humanoid Agents are able to use these dynamic elements to adapt their daily activities and conversations with other agents, as supported with empirical experiments. Our system is designed to be extensible to various settings, three of which we demonstrate, as well as to other elements influencing human behavior (e.g. empathy, moral values and cultural background). Our platform also includes a Unity WebGL game interface for visualization and an interactive analytics dashboard to show agent statuses over time. Our platform is available on https://www.humanoidagents.com/ and code is on https://github.com/HumanoidAgents/HumanoidAgents.[^r0]

## Research Questions
> Research questions distilled from the primary paper; phrasing is paraphrased.[^r0]
- How can basic needs, emotional states, and relationship closeness guide generative agents toward more human-like daily activity and conversation?[^r0]
- Do these System 1 elements alter agent behavior as intended in the demonstrated scenarios?[^r0]

## Model
> Model extracted via LLM according to [[Model Notation]].

### What does it represent?
- Humanoid Agents adds needs, emotion, and relationship closeness to LLM-driven agents. The implementation uses ChatGPT 3.5.[^r1]
- Agents track five needs (fullness, fun, health, social, energy), seven emotions (angry, sad, afraid, surprise, happy, neutral, disgusted), and pairwise closeness on a 0–30 scale.[^r1]
- Defaults are 5/10 for each need except energy 10/10, neutral emotion, and closeness 5 (rather close).[^r1]

### How does it work?
- The agent first makes a day plan, decomposed into 1-hour plans and then 15-minute actions. It reconsiders future plans when emotion is non-neutral or any need is ≤3.[^r2]
- Satisfying activities can raise the corresponding need by one; otherwise needs decay. In the demonstration schedule, fullness/health fall by 1 every five hours, social/fun by 4, and energy by 5.[^r2]
- Co-located agents may converse; their LLM-generated dialogue alternates until someone declines or ten turns are reached.[^r2]
- Each agent independently judges whether it enjoyed the conversation and updates closeness by +1 or −1; emotion may also change.[^r2]
- The paper does not provide a fixed deterministic action policy: prompts and LLM judgments mediate planning and updates.[^r2]

### What can it answer?
- Demonstrations use Lin’s Family, Friends, and Big Bang Theory worlds, each run for two weekdays at 15-minute intervals from 6 a.m. to midnight.[^r3]
- For a narrow validation, three annotators labeled one Lin’s Family day: 144 activity annotations per need/emotion dimension and 30 dialogue examples, with majority-vote labels and micro-F1 evaluation (fullness .972, social .743, fun .660, health .694, energy .861, emotion .840, closeness .900).[^r3]
- Performance was weaker for fun, health, and social needs, where the system overpredicted satisfying activities.[^r3]
- A separate intervention set each need to zero and compared activity-time allocation with the normal run; the paper reports changes by need/world.[^r3]
- This tests selected judgments and interventions, not general human likeness.[^r3]

### Where does it apply?
- The paper demonstrates three simulated settings and an interactive interface, and proposes extending the platform with factors such as empathy, moral values, and culture.[^r4]
- These examples do not establish validity across other settings or human behavior. This summary omits prompt text and other implementation details.[^r4]

## Metadata
### References
Bibliography completeness not verified; the following preserves the originally captured reference links in their original order.

- [[AnArgumentForBasicEmotions]]
- [[TheCostsOfFamilyAndFriendsAn18MonthLongitudinalStudyOfRelationshipMaintenanceAndDecay]]
- [[SatisfyingCommunicationAndRelationshipLabelsIntimacyAndLengthOfRelationshipAsPerceptualFramesOfNaturalisticConversations]]
- [[MethodsOfCopingWithSocialDesirabilityBiasAReview]]
- [[TheSocialBrainHypothesisAndItsImplicationsForSocialEvolution]]
- [[OnHappinessAndHumanPotentialsAReviewOfResearchOnHedonicAndEudaimonicWellBeing]]
- [[TensionsInTheParentAndAdultChildRelationshipLinksToSolidarityAndAmbivalence]]
- [[DiscreteHierarchicalOrganizationOfSocialGroupSizes]]
- [[TogetherInGroupTherapyFathersAndTheirAdolescentSons]]
- [[TwoSidesOfEmotionExploringPositivityAndNegativityInSixBasicEmotionsAcrossCultures]]
- [[CometCommonsenseTransformersForAutomaticKnowledgeGraphConstruction]]
- [[UnresolvedReference20ADEBEA4366F80A]]
- [[PersonalizingDialogueAgentsIHaveADogDoYouHavePetsToo]]
- [[UnresolvedReference1DE44EB008A042E4]]
- [[Author2vecAFrameworkForGeneratingUserEmbedding]]
- [[UnresolvedReferenceF1B0E5B60B39F42C]]
- [[VisuallyGroundedReasoningAcrossLanguagesAndCultures]]
- [[ExtractingAndInferringPersonalAttributesFromDialogue]]
- [[IntimateRelationships]]
- [[AutomatingMoralReasoningInvitedPaper]]
- [[HowToBeHelpfulOnOnlineSupportForums]]
- [[ATheoryOfHumanMotivation]]
- [[VoyagerAnOpenEndedEmbodiedAgentWithLargeLanguageModels]]
- [[GenerativeAgentsInteractiveSimulacraOfHumanBehavior]]

## Audit Log
- Initial independent audit failed on 2026-09-30. Added initial states/defaults, plan decomposition and replanning threshold, need changes, conversation stopping rule and closeness update; specified demonstration schedule and the limited annotation/intervention evaluations. The 24 captured reference links remain in original order; bibliography alias completeness has not been source-verified. See `vault/.automation/audit/next-fifteen-31-35-initial-2026-09-30.json`.[^r5]

## LLM Justification
[^r0]: Abstract copied verbatim from the primary publication record/full text. Research questions are concise paraphrases of the paper’s stated aims/questions. Bibliography links retained in source order from vault/.automation/import/next-fifteen-original-2026-09-30.json.
[^r1]: Wang, Chiu & Chiu, “Humanoid Agents,” Abstract and Figure 1, p. 167. https://aclanthology.org/2023.emnlp-demo.15.pdf
[^r2]: Wang, Chiu & Chiu, “Humanoid Agents,” Sections 2–3, especially the need, emotion, relationship closeness, and conversation procedures, pp. 168–170. https://aclanthology.org/2023.emnlp-demo.15.pdf
[^r3]: Wang, Chiu & Chiu, “Humanoid Agents,” Section 3, experiments and Section 4.4, analytics dashboard, pp. 169–171. https://aclanthology.org/2023.emnlp-demo.15.pdf
[^r4]: Wang, Chiu & Chiu, “Humanoid Agents,” Abstract; Section 5 demonstrations and Section 6 conclusion, pp. 171–172. https://aclanthology.org/2023.emnlp-demo.15.pdf
[^r5]: Process log based on the initial audit record; this is a record of corrections, not an independent re-audit.
