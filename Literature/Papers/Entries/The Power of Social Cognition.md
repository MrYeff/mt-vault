---
title: "The Power of Social Cognition"
tags:
  - model
  - simulation
authors:
  - "[[Literature/Authors/Geoffrey P. Morgan|Geoffrey P. Morgan]]"
  - "[[Literature/Authors/Kenneth Joseph|Kenneth Joseph]]"
  - "[[Literature/Authors/Kathleen M. Carley|Kathleen M. Carley]]"
publication date: 2017-01-01
source: https://www.cmu.edu/joss/content/articles/volume18/MorganJosephCarley2017.pdf
doi: 10.21307/joss-2018-002
read status: Todo
⚠️:
  - audit failed
---
## Abstract

As human beings, we understand and make sense of the social world using social cognition. Social cognitions are cognitive processes through which we understand, process, and recall our interactions with others. Most agent-based models do not account for social cognition; rather, they either provide detailed models of task-related cognition or model many actors and focus on social processes. In general, the more cognitively realistic the models, the less they explain human social behavior and the more computationally expensive it is to model a single agent. In contrast, in this research an agent-based model containing an explicit model of social cognition is developed. Results from this model demonstrate that adding social cognition both improves the model veridicality and decreases computation costs.

## Research Questions
> Research Questions extracted via LLM

- Does a multi-level social-cognition mechanism improve a knowledge-diffusion ABM’s representation of social behavior and its computational efficiency?[^r1]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?
Construct-SC extends Construct’s knowledge-diffusion ABM with personal, group, and generalized-other transactive memory. Actual agent knowledge is distinct from the schema vectors, which encode an ego’s perceived knowledge of another agent or group.[^r2]

```yml
World:
  agents: [Agent]
  groups: [Group]
  simulation_turn: 0..

Agent:
  knowledge: [bool] # K bits of actual knowledge
  group_ids: [GroupId] # supplied at initialization
  personal_memory: [AgentId -> Schema]
  group_memory: [GroupId -> Schema]
  generalized_other: Schema

Schema:
  perceived_facts: [bool] # K bits
  activation: f64

Group: ...
```

### How does it work?

Perception lookup uses the personal → group → global hierarchy.[^r3]

```
lookup(
  world: World,
  ego: Agent,
  alter: AgentId,
  threshold: f64
) -> Schema:

  personal = ego.personal_memory.get(alter)
  if personal exists and personal.activation > threshold:
    out = personal
  else:
    groups = world.agents[alter].group_ids
    relevant = groups.filter(id => ego.group_memory.contains(id))
    if relevant is not empty:
      out = construct_perception(ego.group_memory, relevant)
    else:
      out = ego.generalized_other
```

- The paper describes constructing an alter perception from relevant group schemas without specifying an aggregation formula in this account.[^r3]
- Interaction preferences use homophily, expertise, and propinquity. Interactions and received information activate the relevant schemas; activation decays with disuse, and below-threshold schemas are forgotten. The paper identifies the activation method as a variant of ACT-R/Petrov but does not specify it as a universal update rule here.[^r3]
- Group memberships are fixed and visible to all agents. Initial knowledge distributions are experiment conditions; knowledge changes during simulation.[^r3]
- For a schema activated by **one interaction** `T` turns ago, the memory analysis retains it when `log(1 / sqrt(K + T)) > THRESH`, equivalently `T < exp(-2 * THRESH) - K` (Eqs. 1–2). Here `K` is the small initial activation offset, distinct from knowledge-bit count; this bound is not a complete repeated-interaction update. With `K=0.1`, `N_INT_PER_TURN=2`, `THRESH=-1`, the paper bounds personal alter memory at 15 entries and assumes groups are few relative to agents.[^r3]
- Multiple memberships start with one group and add another with probability `0.25^current_memberships`; Group 0 is twice as likely to be assigned as other groups. Knowledge initialization probabilities are group-based `(0.01, 0.3)`, random `(0.1, 0)`, or fuzzy `(0.03, 0.25)` for random/group-based knowledge.[^r4]
- The two **virtual experiments** compare full alter-level memory with multi-level Construct-SC memory.[^r4]

- **Experiment 1:** 144 combinations × 10 runs; varies group structure (4 settings), knowledge distribution (group-based, random, fuzzy), single/multiple membership, homophily/expertise drives (100/0, 60/40, 0/100), and memory design. Constants: `AGENTS=200`, `KNOWLEDGE_BITS=400`, `SUBTASKS=10`, `TURNS=800`. Outcomes: in-/out-group interaction probability, knowledge diffusion, and task competence. For competence, knowledge masks binary strings in ten contiguous knowledge blocks; each turn draws task bits within each block, and score is the fraction of correctly classified majority-1/majority-0 tasks.[^r4]
- **Experiment 2:** 8 combinations × 10 runs; varies `AGENTS ∈ {1000, 5000, 10000, 15000}` and memory design. Controls: fuzzy group knowledge (`0.03, 0.25`), multiple memberships, drives 60/40, `KNOWLEDGE_BITS=1000`, `SUBTASKS=10`, `TURNS=365`. Outcome: average turn runtime per agent.[^r4]

### What can it answer?
- Test whether multi-level memory reproduces selected social-behavior stylized facts.[^r5]
- Measure diffusion, in-group bias, task competence, memory cost, and runtime.[^r5]
- Reported results: closer fit to selected stylized facts and lower memory requirements. The timing advantage is limited to the tested conditions.[^r5]

### Where does it apply?
It applies to simulated knowledge diffusion in group-structured social networks. Group memberships and visibility are fixed inputs in the reported experiments; no claim is made that groups emerge or that all agents share the same subjective group perceptions.[^r4]

## Metadata
### References

- [[StructuralChangeAndLearningWithinOrganizations]]
- [[UnderstandingEventsAffectAndTheConstructionOfSocialAction]]
- [[CapitalAccumulationAndEconomicGrowth]]
- [[TheSoarCognitiveArchitecture]]
- [[ContextualCognitionInSocialSimulation]]
- [[TheSocialCognitiveActorAMultiActorSimulationOfOrganisations]]
- [[MetamimeticGamesModelingMetadynamicsInSocialCognition]]
- [[UnresolvedReference8FB4057736D8695E]]
- [[ImplicitSocialCognitionAttitudesSelfEsteemAndStereotypes]]
- [[DynamicModelsOfSegregation]]
- [[TheStrengthOfWeakTiesANetworkTheoryRevisited]]
- [[OrganizationalLearningAndPersonnelTurnover]]
- [[TheGenesisOfTheSelfAndSocialControl]]
- [[ValidatingAgentInteractionsInConstructAgainstEmpiricalCommunicationNetworksUsingTheCalibratedGroundingTechnique]]
- [[HierarchiesAndCliquesInTheSocialNetworksOfHealthCareProfessionalsImplicationsForTheDesignOfDisseminationStrategies]]
- [[AStructuralTheoryOfSocialInfluence]]
- [[MappingSharedUnderstandingsUsingRelationalClassAnalysisTheCaseOfTheCulturalOmnivoreReexamined]]
- [[CulturalVariationsInSocialSchemata]]
- [[ImplicitAndExplicitProcessesInSocialCognition]]
- [[BridgingTheBoundaryExternalActivityAndPerformanceInOrganizationalTeams]]
- [[MassMediaGeneratedInterpersonalCommunicationAsSourcesOfInformationAboutFamilyPlanning]]
- [[SymbolicInteractionismASocialStructuralVersion]]
- [[TheEtiologyOfSocialChange]]
- [[CoevolutionOfCommunicationAndKnowledgeNetworksInTransactiveMemorySystemsUsingComputationalModelsForTheoreticalDevelopment]]
- [[ATheoryOfGroupStability]]
- [[HumansUseCompressionHeuristicsToImproveTheRecallOfSocialNetworks]]
- [[TransactiveMemoryAContemporaryAnalysisOfTheGroupMind]]
- [[AComputerNetworkModelOfHumanTransactiveMemory]]
- [[InequalityAndHeterogeneityAPrimitiveTheoryOfSocialStructure]]
- [[ActASimpleTheoryOfComplexCognition]]
- [[SkillsToolkitsContextsAndInstitutionsClarifyingTheRelationshipBetweenDifferentApproachesToCognitionInCulturalSociology]]
- [[AligningSimulationModelsACaseStudyAndResults]]
- [[ArtificialSocialIntelligence]]
- [[ASystemOfIacNeuralNetworksAsTheBasisForSelfOrganizationInASociologicalDynamicalSystemSimulation]]
- [[TheSocialSelfOnBeingTheSameAndDifferentAtTheSameTime]]
- [[SchemataTheBuildingBlocksOfCognition]]
- [[An Agent-Based Model of Social Identity Dynamics]]
- [[OnTheCoevolutionOfStereotypeCultureAndSocialRelationships]]
- [[Birds of a Feather- Homophily in Social Networks]]
- [[AnIntegratedTheoryOfTheMind]]
- [[ManagingTheFlowOfTechnologyTechnologyTransferAndTheDisseminationOfTechnologicalInformationWithinTheRDOrganization]]
- [[TheImpactOfSocialStructureOnEconomicOutcomes]]
- [[SocialCategorizationAndIntergroupBehaviour]]
- [[TheAffectiveMeaningsOfAutomaticSocialBehaviorsThreeMechanismsThatExplainPriming]]
- [[OmnivorousnessAsTheBridgingOfCulturalHolesAMeasurementStrategy]]
- [[HowMuchDoesItHelpToKnowWhatSheKnowsYouKnowAnAgentBasedSimulationStudy]]
- [[ABehavioristicAccountOfTheSignificantSymbol]]
- [[ModelingGroupDecisionMakingInTheActRCognitiveArchitecture]]
- [[SocialSchemas]]
- [[DefiningFactorsOfInterestForLargeScaleSocioCognitiveSimulations]]
- [[UnresolvedReference43EDD9AE509F7296]]
- [[UnresolvedReference8C3821E23201158F]]
- [[UnresolvedReference26515088C2EA83BC]]
- [[UnresolvedReferenceFCD62B8F824A27C4]]
- [[UnresolvedReference43DD71A05C3B3FB3]]
- [[UnresolvedReferenceA677CF435ADB3CFC]]
- [[UnresolvedReferenceB19463972B5EE6D0]]
- [[UnresolvedReferenceC49BF7A9DFEF0FAC]]
- [[UnresolvedReferenceD1A70A683618D10A]]
- [[UnresolvedReferenceDCC57B47D3AC8EDD]]
- [[UnresolvedReference10D7365A2466698A]]
- [[TheSocialPsychologyOfIntergroupRelations]]


## Audit Log
- Audit invalidated (2026-09-30): auditor admitted incomplete independent checks and premature flag removal. Previous valid audits, if any, remain separate.

- 2026-09-30: Root review found the initial note incorrectly said the abstract did not specify mechanisms despite accessible full text. Replaced with Construct-SC schemas, activation/forgetting and personal→group→Generalized Other inference, plus both virtual experiment designs, sourced to the full paper. Pending independent re-audit.

- WITHDRAWN audit claim (2026-09-30): the remaining-audit-c report overstated independent source checks; it does not establish a pass.

- 2026-09-30: Full 23-page primary PDF audited, including visual examination of Eqs. 1–2. Added the explicitly limited activation bound and membership/knowledge initialization. Bibliography contains unresolved targets; audit failed remains pending bibliography repair and independent re-audit.

## LLM Justification
[^r1]: https://www.cmu.edu/joss/content/articles/volume18/MorganJosephCarley2017.pdf; pp. 1, 7–10, gives the model objective and two experiment questions.
[^r2]: https://www.cmu.edu/joss/content/articles/volume18/MorganJosephCarley2017.pdf; §“Modelable Social Phenomena,” p. 6, defines Construct-SC and K-bit transactive-memory schemas.
[^r3]: https://www.cmu.edu/joss/content/articles/volume18/MorganJosephCarley2017.pdf; pp. 4–7 and 15–16, describes group assumptions, schema activation/forgetting, hierarchy/fallback, interaction drives, and threshold; no universal activation equation is claimed.
[^r4]: https://www.cmu.edu/joss/content/articles/volume18/MorganJosephCarley2017.pdf; §“Virtual Experiment Design,” pp. 8–10, Tables 2–3, specifies factors, constants, outcomes, and that these are virtual experiments.
[^r5]: https://www.cmu.edu/joss/content/articles/volume18/MorganJosephCarley2017.pdf; §§Results and Discussion, pp. 11–18, reports behavior and computational outcomes.
