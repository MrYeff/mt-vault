---
title: "When \"I\" Becomes \"We\": Modelling Dynamic Identity on Autonomous Agents"
tags:
  - model
  - simulation
authors:
  - "[[Literature/Authors/Inês Lobo|Inês Lobo]]"
  - "[[Literature/Authors/Joana Dimas|Joana Dimas]]"
  - "[[Literature/Authors/Samuel F. Mascarenhas|Samuel F. Mascarenhas]]"
  - "[[Literature/Authors/Diogo Rato|Diogo Rato]]"
  - "[[Literature/Authors/Rui Prada|Rui Prada]]"
publication date: 2023-06-30
source: https://www.jasss.org/26/3/9.html
doi: 10.18564/jasss.5146
read status: Todo
⚠️:
  - audit failed
---
## Abstract

Individuals change who they are in response to their social environment. In other words, one's identity is dynamic, varying according to context (e.g., individuals present, place, task). Identity has a significant impact on an individual's behaviour. Researchers have been interested in understanding how contextual aspects shape identity and, in turn, how identity influences behaviour. Agent-based simulation models are great tools to identify and predict behaviour associated with these identity processes. In addition, agents can employ identity-related mechanisms based on social theories to become more socially believable and similar to humans. The Social Identity Approach (SIA) is one of the most influential theories covering social aspects of one's identity, with many of its concepts being applied in social simulation research. This paper formalizes the Dynamic Identity Model for Agents (DIMA), an existing agent-based model based on SIA, providing a detailed theoretical foundation of the model, as well as an overview of its integration as a component into a social agent architecture. In DIMA, agents perceive themselves either as distinct individuals (personal identity) or as members of a social group (social identity), acting according to their context-dependent active identity. Two simulation scenarios are presented here to illustrate the use of this model, one based on the Dictator Game and the other on a trash collection task. This work aims to guide other researchers who want to enhance their agents with the DIMA's identity salience mechanism. As a result, they would not only be able to assess how this mechanism influences behaviour based on the context, but they would also be able to explore the dynamics between personal and social identities.

## Research Questions
> Research Questions extracted via LLM

- How does context-dependent salience of personal versus social identity affect agent decisions and behavior in social simulations?[^r1]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?
DIMA selects a personal or social identity from perceived context and previously known group prototypes, then supplies identity/salience to a separate decision module.[^r2]

These types and rules condense the model formalization (Eqs. 1–10); perception/decision modules are supplied by the scenario.[^r2][^r3]

```yml
World:
  agents: [Agent]
  context: Context

Agent:
  personal: [Characteristic -> 0..1]
  groups: [Group]

Group:
  prototype: [Characteristic -> 0..1]
  accessibility: 0..1

Context:
  agents_present: [AgentId]
  theme: [Characteristic -> 0..1] # weights sum to1

Identity: Personal | Social(GroupId)
```

### How does it work?
Normative fit matches a cluster to a remembered prototype; comparative fit supplies the numerical fit. They are not multiplied together. The block states the identity cycle and fit equations.[^r3]

```
T_CLUSTERING = T_NORMATIVE = T_SALIENCE = 0.2 # demonstration settings
ACCESS_GROWTH = 0.01 # both use cases

sim_step(mut agent: Agent, context: Context):
  project present agents' characteristics onto context.theme
  # example: K-means starts at K=1; increment K and rerun
  # until every member's centroid distance <= T_CLUSTERING
  clusters = context_clusters
  if |clusters| == 1:
    active = Personal; salience = 0
  else:
    for cluster in clusters:
      known = nearest context-projected agent.groups prototype
      if distance(cluster.centroid, known.prototype) < T_NORMATIVE:
        identity = known # use remembered prototype/accessibility
      else:
        identity = Group(cluster.centroid,
                         1 - distance(agent.personal, cluster.centroid))
        agent.groups.push(identity)
      # merge multiple out-groups using mean of their centroids/prototypes
      fit = distance(ingroup, outgroup) / 2 +
            (1 - dispersion(ingroup) + dispersion(outgroup)) / 4
      salience[identity] = fit * identity.accessibility
    best = argmax(salience)
    active = Social(best) if salience[best] > T_SALIENCE else Personal
  action = scenario_decision(active, salience, agent.personal)
  outcome = environment_apply(action)
  if active is Social:
    update its accessibility from previous value, salience, optional outcome
    normalize all agent.groups accessibilities # others consequently decay

# Eq8 distance: normalized absolute centroid/prototype difference
# Eq9 dispersion: mean normalized absolute member-to-centroid difference
```

- Equation 10 specifies only `ACC_NEXT = f(ACC, SALIENCE, optional outcome)` and the text explicitly leaves the function scenario-dependent; it does not give a universal additive update.[^r3]
- Both demonstrations use growth factor `0.01`; normalization is required, but an exact implemented function cannot be inferred from the printed equation.[^r3][^r4]

### What can it answer?
- Dictator game: 50 agents, 100 steps, 50 runs; each receives €100 and a random anonymous recipient. Personal offer is 20%; social offer is `20% * (1 + BIAS * SALIENCE)`, with `BIAS=1` for in-group, `−1` otherwise (Eq. 11). Compare empty/equal-group contexts, dispersion, group size and alternating themes with half adaptive/half always-personal agents; measure offers and accumulated wealth. More salient/adaptive groups gain wealth in these scenarios.[^r4]
- Trash task: 50 agents on a 20×20 grid, 0–10 initial trash per cell, 500 steps and 50 runs; move one cell or collect. In collisions an agent collects unless another has greater competitiveness (Eq. 12). Without trash, sociability steers toward nearby agents or empty cells. Observe eight adjacent cells; context is empty or two-valued shirt color. Active social identity linearly shifts sociability toward1/competitiveness toward0 with in-group, and toward0/1 with out-group, weighted by salience. Compare trash collected and encounters; color-conditioned grouping raises encounters and slightly reduces mean collection.[^r5]

### Where does it apply?
DIMA is a reusable identity module for agents with numeric contextual characteristics; the two demonstrations illustrate consequences of constructed behavioral rules, rather than establish human behavioral validity.[^r2][^r4][^r5]

## Metadata
### References

- [[PersonalityDrivenSocialBehaviorsInBelievableAgents]]
- [[AnIntegrativeTheoryOfIntergroupConflict]]
- [[SocialIdentificationAndPsychologicalGroupFormation]]
- [[TransculturalBelievabilityInEmbodiedAgentsAMatterOfConsistentAdaptation]]
- [[SocialImportanceDynamicsAModelForCulturallyAdaptiveAgents]]
- [[SciprAComputationalModelToSimulateCulturalIdentitiesForPredictingReactionsToEvents]]
- [[CategorizationInSocialPsychology]]
- [[ModellingTheEmergenceOfResourceSharingConventionsAnAgentBasedApproach]]
- [[ATaleOfTwoTheoriesACriticalComparisonOfIdentityTheoryWithSocialIdentityTheory]]
- [[CultureSpecificFirstMeetingEncountersBetweenVirtualAgents]]
- [[IdentityTheoryAndSocialIdentityTheory]]
- [[EvidenceForImplicitEvaluativeInGroupBiasAffectBiasedSpontaneousTraitInferenceInAMinimalGroupParadigm]]
- [[FairnessAndTheAssumptionsOfEconomics]]
- [[AccessibilityAndFitAsDeterminantsOfTheSalienceOfSocialCategorizations]]
- [[SelfAndCollectiveCognitionAndSocialContext]]
- [[FairGameTheIntuitiveEconomicsOfResourceExchangeInFourYearOlds]]
- [[IntergroupRelationsInsightsFromATheoreticallyIntegrativeApproach]]
- [[RediscoveringTheSocialGroupASelfCategorizationTheory]]
- [[TowardsAProcessModelOfHumanPersonalityTraits]]
- [[OnTheInterpretationOfGivingInDictatorGames]]
- [[PersonalityStructureEmergenceOfTheFiveFactorModel]]
- [[TheSocialSelfOnBeingTheSameAndDifferentAtTheSameTime]]
- [[UnderstandingTheRelationshipBetweenIndividualismCollectivismAndTeamPerformanceThroughAnIntegrationOfSocialIdentityTheoryAndTheSocialRelationsModel]]
- [[SimulationOfTheDynamicsOfNonplayerCharactersEmotionsAndSocialRelationsInGames]]
- [[An Agent-Based Model of Social Identity Dynamics]]
- [[SocialCategorizationAndIntergroupBehaviour]]
- [[UsingRitualsToExpressCulturalDifferencesInSyntheticCharacters]]
- [[ATheoryOfSocialComparisonProcesses]]
- [[AContinuousOpinionDynamicsModelBasedOnThePrincipleOfMetaContrast]]
- [[UnresolvedReference839FBFCF23C902C6]]
- [[OneForAllAllForOneAgentsWithSocialIdentities]]
- [[TheDynamicNatureOfIdentityFromTheBrainToBehavior]]
- [[SocialIdentityTheoryAndSelfCategorizationTheory]]
- [[RhetoricMattersASocialNormsExplanationForTheAnomalyOfFraming]]
- [[GroupBasedEmotionsEvidenceForEmotionPerformanceRelationshipsInTeamSports]]
- [[StabilityAndMalleabilityOfTheSelfConcept]]
- [[SocialIdentityTheory]]
- [[When -I- Becomes -We- Modelling Dynamic Identity on Autonomous Agents]]
- [[UnresolvedReference96A3761CD817D3C1]]
- [[UnresolvedReference43EDD9AE509F7296]]
- [[UnresolvedReference5A25462E60957DC3]]
- [[UnresolvedReference37FD56182060F5F3]]
- [[UnresolvedReference523B121BDBE29A98]]
- [[UnresolvedReferenceD98ED8A3F906C210]]
- [[UnresolvedReferenceC4CD316995708603]]
- [[UnresolvedReferenceBD6B1D881BC26C88]]
- [[UnresolvedReference2B62D17788B38D36]]
- [[UnresolvedReferenceBE0C7294DFA72360]]
- [[UnresolvedReferenceEF69167098D68D37]]
- [[UnresolvedReference7B6F2B1B5250C051]]
- [[UnresolvedReference369AD2DE677B76AD]]
- [[UnresolvedReferenceE93164DD908973E3]]
- [[UnresolvedReference74D841ADA058A814]]
- [[UnresolvedReferenceEB8BCE5863C61EA4]]
- [[UnresolvedReferenceB047BEC5AE625515]]


## Audit Log
- Audit invalidated (2026-09-30): auditor admitted incomplete independent checks and premature flag removal. Previous valid audits, if any, remain separate.

- 2026-09-30: Initial/cheap audit failed; stronger source review corrected normative matching versus comparative fit, actual fit/distance/dispersion rules, group memory and normalized accessibility; rejected cheap-audit claim that Eq10 fixes a universal formula; concrete dictator/trash rules. Independent re-audit pending.

- WITHDRAWN audit claim (2026-09-30): the remaining-audit-c report overstated independent source checks; it does not establish a pass.

## LLM Justification
[^r1]: https://www.jasss.org/26/3/9.html; Abstract and Introduction: aim.
[^r2]: Same source; “Model integration in social agent architecture,” Figure 1 and “Social context”/“Agents”/“Normative social groups”: inputs, types and module boundaries.
[^r3]: Same source; “Clustering” and “Salience and active identity,” Eqs.1–10 and Table5: iterative K-means example, thresholds, normative matching Eq5, comparative fit Eq7, distance Eq8, dispersion Eq9, salience Eq3, new groups Eq6, identity Eq4. Eq10 explicitly uses an unspecified function; “The DIMA Model” and “Salience: Accessibility” explicitly permit scenario-specific functions and require normalization.
[^r4]: Same source; “Use Case: Dictator Game,” Eq11 and setup/results: settings, growth factor0.01, five context variations, adaptive comparison and wealth/offer measures.
[^r5]: Same source; “Use Case: Trash Collection,” Eq12 and setup/results: grid, tasks, 500steps/50runs, field of view, color-based linear interpolation, growth0.01 and outcomes.
