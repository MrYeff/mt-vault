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
- Explore plausible interactions and design alternatives. Evaluation compares generated/real conversations from 50 subreddits, ablates goals/rules/personas, and studies 16 designers using the tool.[^r4]

### Where does it apply?
- Early social-system prototyping. This summary omits literal prompt templates and UI; plausibility/design-usefulness evaluations do not calibrate future community behavior.[^r3][^r4]

## Metadata
### References
- [[ParadigmShiftTheNewPromiseOfInformationTechnology]]
- [[Building Successful Online Communities- Evidence-Based Social Design]]
- [[ProceedingsOfThe24thInternationalConferenceOnMachineLearning]]
- [[ExperimentalEvidenceOfMassiveScaleEmotionalContagionThroughSocialNetworks]]
- [[AnIterativeDesignMethodologyForUserFriendlyNaturalLanguageOfficeInformationApplications]]
- [[Sauron]]
- [[Silk]]
- [[AutomaticIdentificationOfPersonalInsultsOnSocialNewsSites]]
- [[TheRiseAndDeclineOfAnOpenCollaborationSystem]]
- [[TheReflectivePractitionerHowProfessionalsThinkInAction]]
- [[PiggybackPrototyping]]
- [[ReflectivePhysicalPrototypingThroughIntegratedDesignTestAndAnalysis]]
- [[TrollingInAsynchronousComputerMediatedCommunicationFromUserDiscussionsToAcademicDefinitions]]
- [[TheTroubleWithSocialComputingSystemsResearch]]
- [[DesignAsExploration]]
- [[DesignGalleries]]
- [[Voyant]]
- [[FromInfrastructureToCulture]]
- [[HeSaysSheSays]]
- [[AuthoringSensorBasedInteractionsByDemonstrationWithDirectManipulationAndPatternRecognition]]
- [[PaperPrototypingWhatIsItGoodFor]]
- [[AugmentingInteractiveTablesWithMiceKeyboards]]
- [[Designscape]]
- [[TheIntellectualChallengeOfCscwTheGapBetweenSocialRequirementsAndTechnicalFeasibility]]
- [[ExperimentalStudyOfInequalityAndUnpredictabilityInAnArtificialCulturalMarket]]
- [[CyberbullyingVictimizationAmongTurkishOnlineSocialUtilityMembers]]
- [[GraphClusterRandomization]]
- [[AnEmpiricalMethodologyForWritingUserFriendlyNaturalLanguageComputerApplications]]
- [[PrototypingForTinyFingers]]
- [[TrustworthyOnlineControlledExperiments]]
- [[UnresolvedReferenceBC85C9AA9F9CAFED]]
- [[ExperiencePrototyping]]
- [[InformedConsentAndTheFacebookEmotionalManipulationStudy]]
- [[ThisPostWillJustGetTakenDown]]
- [[TheToastboard]]
- [[AnyoneCanBecomeATroll]]
- [[TheBagOfCommunities]]
- [[LearningVisualImportanceForGraphicDesignsAndDataVisualizations]]
- [[YouCanTStayHere]]
- [[RevisitingTheRiseAndDeclineInAPopulationOfPeerProductionProjects]]
- [[RedditRulesCharacterizingAnEcosystemOfGovernance]]
- [[TheInternetSHiddenRules]]
- [[TheFightFor15TheRightWageForAWorkingAmerica]]
- [[PreventingHarassmentAndIncreasingGroupParticipationThroughSocialNormsIn2190OnlineScienceDiscussions]]
- [[UnresolvedReferenceF86C5559DE311E16]]
- [[UnexpectedExpectationsPublicReactionToTheFacebookEmotionalContagionStudy]]
- [[ContextsOfUninhibitedOnlineBehavior]]
- [[TheImpliedTruthEffectAttachingWarningsToASubsetOfFakeNewsHeadlinesIncreasesPerceivedAccuracyOfHeadlinesWithoutWarnings]]
- [[FantasticallyOrderedPromptsAndWhereToFindThemOvercomingFewShotPromptOrderSensitivity]]
- [[StudyingRedditASystematicOverviewOfDisciplinesApproachesMethodsAndEthics]]
- [[GenlineAndGenformTwoToolsForInteractingWithGenerativeLanguageModelsInACodeEditor]]
- [[TwitterManipulatesYourFeedEthicalConsiderations]]
- [[PromptmakerPromptBasedPrototypingWithLargeLanguageModels]]
- [[ProceedingsOfThe24thAnnualConferenceOnComputerGraphicsAndInteractiveTechniquesSiggraph97]]
- [[PrototypingToolsAndTechniques]]
- [[SurvivingAnEternalSeptember]]
- [[MeasuringThePrevalenceOfAntiSocialBehaviorInOnlineCommunities]]
- [[Chi11ExtendedAbstractsOnHumanFactorsInComputingSystemsVancouverBcCanadaChiEa11]]
- [[UnresolvedReference6CFE671E65DE740A]]
- [[LanguageModelsAreFewShotLearnersAdvancesInNeuralInformationProcessingSystems33]]
- [[ProceedingsOfTheInternationalAaaiConferenceOnWebAndSocialMediaVol96170]]
- [[HowHateGroups]]
- [[DesignCulturalProbesInteractions61]]
- [[UnresolvedReference47AC906B236E25A7]]
- [[UnresolvedReferenceA2B99F20B4CD350B]]
- [[UnresolvedReference8DBCC7B93D7A4105]]
- [[WhatDoPrototypesPrototypeInHandbookOfHumanComputerInteraction]]
- [[UnresolvedReference6D99E1056ADB44F8]]
- [[UnresolvedReferenceB334C6A568FDD7F9]]
- [[TrustworthyOnlineControlledExperimentsFivePuzzlingOutcomesExplainedKdd12]]
- [[UnresolvedReferenceFA1F1736A5DF429A]]
- [[UnresolvedReferenceA47D2B6ADB58ECA8]]
- [[UnresolvedReference80E63E50C1937FA7]]
- [[TowardACriticalMass]]
- [[StudyingRedditASystematicOverviewOfDisciplinesApproachesMethodsAndEthicsSocialMediaSociety72]]
- [[ProlificQuicklyFindResearchParticipantsYouCanTrustHttpsWwwProlificCo]]
- [[LanguageModelsAreUnsupervisedMultitaskLearnersOpenaiBlog18]]
- [[UnresolvedReference04E1A688A28BD79A]]
- [[ProceedingsOfThe38thInternationalConferenceOnMachineLearning]]
- [[UnresolvedReferenceC5CF670488AFE490]]
- [[DilemmasInAGeneralTheoryOfPlanningPolicySciences42]]
- [[ExperimentalStudyOfInequalityAndUnpredictabilityInAnArtificialCulturalMarketScience3115762]]
- [[UnresolvedReferenceE99C3C37FC0AA48E]]
- [[UnresolvedReferenceDC1A24B0DE03DCDE]]
- [[AGeneralInductiveApproachForAnalyzingQualitativeEvaluationDataAmericanJournalOfEvaluation27]]
- [[TheStateOfOnlineHarassment]]
- [[SuperglueAStickierBenchmarkForGeneralPurposeLanguageUnderstandingSystemsAdvancesInNeuralInformationProcessingSystems32]]
- [[UnresolvedReferenceE28988A297021D88]]
- [[UnresolvedReference18DF4963971B7A73]]
- [[UnresolvedReference1299C9340D451A1C]]
- [[Retrieved]]
- [[DefendingAgainstNeuralFakeNewsAdvancesInNeuralInformationProcessingSystems32]]
- [[InternationalConferenceOnMachineLearningPmlrPmlr1269712706]]

## Audit Log
- Audit invalidated (2026-09-30): auditor admitted clearing flags before completing independent source checks. A new independent audit is required.
- Strong source review (2026-09-30): Expanded actual persona→top-level-post→iterative-reply prompt chain, responder selection/stopping rules, WhatIf moderator context and Multiverse setting; stated normal-probability and stopping ambiguity. Independent re-audit pending.
- Initial independent audit: failed on missing model mechanisms, abstract fidelity, or source-access reporting; see `vault/.automation/audit/next-forty-54-66-initial-2026-09-30.json`. Revisions added source-located model detail; independent re-audit remains pending.

- WITHDRAWN audit claim (2026-09-30): previously reported PASS; source claims, current extraction, metadata, references and footnotes checked against the available primary source. See `vault/.automation/audit/remaining-audit-b-2026-09-30.json`.

## LLM Justification
[^r1]: The paper’s abstract, at https://arxiv.org/abs/2208.04024. The questions paraphrase the stated purpose, research scope, and reported approach.
[^r3]: Park et al., §§3.2–3.4 (Generate, WhatIf, Multiverse), §4.2.1–4.2.5 (persona expansion, top-level-post/reply prompts, Bernoulli continuation, responder selection, context truncation and temperature), §4.3 (base davinci engine). §4.2.3 leaves the normal standard deviation and [0,1] handling unspecified. Full published paper: https://hci.stanford.edu/publications/2022/Park_SocialSimulacra_UIST22.pdf.
[^r4]: Park et al., §§5.1–5.3 (50 subreddits created after GPT-3 release, real/generated comparisons and prompt ablations), §6 (16 designers), §7.1 (limitations of generation/design feedback). Full published paper: https://hci.stanford.edu/publications/2022/Park_SocialSimulacra_UIST22.pdf.
