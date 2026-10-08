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

- [[Exploring trust, group satisfaction, and performance in geographically dispersed and co-located university technology commercialization teams]]
- [[AccessibilityAndFitAsDeterminantsOfTheSalienceOfSocialCategorizations|Accessibility and fit as determinants of the salience of social categorizations]]
- [[TheSocialSelfOnBeingTheSameAndDifferentAtTheSameTime|The social self: On being the same and different at the same time]]
- [[On perceptual readiness]]
- [[GroupBasedEmotionsEvidenceForEmotionPerformanceRelationshipsInTeamSports|Group-based emotions: Evidence for emotion-performance relationships in team sports]]
- [[TowardsAProcessModelOfHumanPersonalityTraits|Towards a process model of human personality traits]]
- [[RhetoricMattersASocialNormsExplanationForTheAnomalyOfFraming|Rhetoric matters: A social norms explanation for the anomaly of framing]]
- [[TransculturalBelievabilityInEmbodiedAgentsAMatterOfConsistentAdaptation|Transcultural believability in embodied agents: A matter of consistent adaptation]]
- [[PersonalityStructureEmergenceOfTheFiveFactorModel|Personality structure: Emergence of the five-factor model]]
- [[OneForAllAllForOneAgentsWithSocialIdentities|One for all, all for one: Agents with social identities]]
- [[Dynamic identity model for agents]]
- [[Creating individual agents through personality traits]]
- [[What is identity (as we now use the word)]]
- [[ATheoryOfSocialComparisonProcesses|A theory of social comparison processes]]
- [[Comparing human and synthetic group behaviors- A model based on social psychology|Comparing human and synthetic group behaviors: A model based on social psychology]]
- [[SciprAComputationalModelToSimulateCulturalIdentitiesForPredictingReactionsToEvents|SCIPR: A computational model to simulate cultural identities for predicting reactions to events]]
- [[UnderstandingTheRelationshipBetweenIndividualismCollectivismAndTeamPerformanceThroughAnIntegrationOfSocialIdentityTheoryAndTheSocialRelationsModel|Understanding the relationship between individualism–collectivism and team performance through an integration of social identity theory and the social relations model]]
- [[Intergroup behavior in organizations- A field test of social identity theory|Intergroup behavior in organizations: A field test of social identity theory]]
- [[Culture consequences- Comparing values, behaviors, intitutions, and organizations across nations|Culture consequences: Comparing values, behaviors, intitutions, and organizations across nations]]
- [[ATaleOfTwoTheoriesACriticalComparisonOfIdentityTheoryWithSocialIdentityTheory|A tale of two theories: A critical comparison of identity theory with social identity theory]]
- [[FairnessAndTheAssumptionsOfEconomics|Fairness and the assumptions of economics]]
- [[Social identity modeling- past work and relevant issues for socio-cultural modeling|Social identity modeling: past work and relevant issues for socio-cultural modeling]]
- [[Optimal distinctiveness theory- A framework for social identity, social cognition, and intergroup relations|Optimal distinctiveness theory: A framework for social identity, social cognition, and intergroup relations]]
- [[OnTheInterpretationOfGivingInDictatorGames|On the interpretation of giving in dictator games]]
- [[FairGameTheIntuitiveEconomicsOfResourceExchangeInFourYearOlds|Fair game: The intuitive economics of resource exchange in four-year olds]]
- [[IntergroupRelationsInsightsFromATheoreticallyIntegrativeApproach|Intergroup relations: Insights from a theoretically integrative approach]]
- [[SimulationOfTheDynamicsOfNonplayerCharactersEmotionsAndSocialRelationsInGames|Simulation of the dynamics of nonplayer characters’ emotions and social relations in games]]
- [[StabilityAndMalleabilityOfTheSelfConcept|Stability and malleability of the self-concept]]
- [[UsingRitualsToExpressCulturalDifferencesInSyntheticCharacters|Using rituals to express cultural differences in synthetic characters]]
- [[SocialImportanceDynamicsAModelForCulturallyAdaptiveAgents|Social importance dynamics: A model for culturally-Adaptive agents]]
- [[CategorizationInSocialPsychology|Categorization in social psychology]]
- [[The salience of social categories]]
- [[EvidenceForImplicitEvaluativeInGroupBiasAffectBiasedSpontaneousTraitInferenceInAMinimalGroupParadigm|Evidence for implicit evaluative in-group bias: Affect-biased spontaneous trait inference in a minimal group paradigm]]
- [[TheDynamicNatureOfIdentityFromTheBrainToBehavior|The dynamic nature of identity: From the brain to behavior]]
- [[Introducing personality into team dynamics]]
- [[Too close for comfort- Adapting to the user’s cultural background|Too close for comfort? Adapting to the user’s cultural background]]
- [[CultureSpecificFirstMeetingEncountersBetweenVirtualAgents|Culture-specific first meeting encounters between virtual agents]]
- [[PersonalityDrivenSocialBehaviorsInBelievableAgents|Personality-driven social behaviors in believable agents]]
- [[AContinuousOpinionDynamicsModelBasedOnThePrincipleOfMetaContrast|A continuous opinion dynamics model based on the principle of meta-contrast]]
- [[An Agent-Based Model of Social Identity Dynamics|An agent-based model of social identity dynamics]]
- [[Social psychology]]
- [[IdentityTheoryAndSocialIdentityTheory|Identity theory and social identity theory]]
- [[Self and identity]]
- [[Experiments in intergroup discrimination]]
- [[SocialCategorizationAndIntergroupBehaviour|Social categorization and intergroup behaviour]]
- [[AnIntegrativeTheoryOfIntergroupConflict|An integrative theory of intergroup conflict]]
- [[ModellingTheEmergenceOfResourceSharingConventionsAnAgentBasedApproach|Modelling the emergence of resource-sharing conventions: An agent-based approach]]
- [[SocialIdentityTheory|Social identity theory]]
- [[SocialIdentityTheoryAndSelfCategorizationTheory|Social identity theory and self-categorization theory]]
- [[RediscoveringTheSocialGroupASelfCategorizationTheory|Rediscovering the social group: A self-Categorization Theory]]
- [[SelfAndCollectiveCognitionAndSocialContext|Self and collective: Cognition and social context]]
- [[SocialIdentificationAndPsychologicalGroupFormation|Social identification and psychological group formation]]

## Audit Log
- 2026-10-03: Independent full-source re-audit passed. Prior full-source content pass retained; all52references and six filename-safe target changes independently rechecked, preserving source titles/order. `audit failed` removed after the pass.
- 2026-10-03: Reopened reference-target check: six targets contained filename-unsafe colons. Source-title aliases retained; independent re-audit pending. Earlier content/source pass remains recorded.
- 2026-10-03: Independent full-source re-audit passed. Full DIMA equations, both configured use cases, source omissions, abstract/metadata and all 52 source references independently checked. `audit failed` removed after the pass.
- 2026-10-03: Rebuilt all references against the complete current publisher HTML bibliography in source order; 52 source entries resolved to title-bearing links. The earlier audit record’s 55-entry count conflicts with the cached published HTML, which contains 52 reference paragraphs; no three unsupported entries were retained. Model text and warning unchanged. Independent re-audit pending.

- Audit invalidated (2026-09-30): auditor admitted incomplete independent checks and premature flag removal. Previous valid audits, if any, remain separate.

- 2026-09-30: Initial/cheap audit failed; stronger source review corrected normative matching versus comparative fit, actual fit/distance/dispersion rules, group memory and normalized accessibility; rejected cheap-audit claim that Eq10 fixes a universal formula; concrete dictator/trash rules. Independent re-audit pending.

- WITHDRAWN audit claim (2026-09-30): the remaining-audit-c report overstated independent source checks; it does not establish a pass.

## LLM Justification
[^r1]: https://www.jasss.org/26/3/9.html; Abstract and Introduction: aim.
[^r2]: Same source; “Model integration in social agent architecture,” Figure 1 and “Social context”/“Agents”/“Normative social groups”: inputs, types and module boundaries.
[^r3]: Same source; “Clustering” and “Salience and active identity,” Eqs.1–10 and Table5: iterative K-means example, thresholds, normative matching Eq5, comparative fit Eq7, distance Eq8, dispersion Eq9, salience Eq3, new groups Eq6, identity Eq4. Eq10 explicitly uses an unspecified function; “The DIMA Model” and “Salience: Accessibility” explicitly permit scenario-specific functions and require normalization.
[^r4]: Same source; “Use Case: Dictator Game,” Eq11 and setup/results: settings, growth factor0.01, five context variations, adaptive comparison and wealth/offer measures.
[^r5]: Same source; “Use Case: Trash Collection,” Eq12 and setup/results: grid, tasks, 500steps/50runs, field of view, color-based linear interpolation, growth0.01 and outcomes.
