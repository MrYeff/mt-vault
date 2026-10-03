---
title: A Framework for Sequential Planning in Multi-Agent Settings
publication date: 2005-07-01
authors:
- '[[Literature/Authors/Piotr J. Gmytrasiewicz|Piotr J. Gmytrasiewicz]]'
- '[[Literature/Authors/Prashant Doshi|Prashant Doshi]]'
source: https://www.cs.cmu.edu/afs/cs/project/jair/pub/volume24/gmytrasiewicz05a.pdf
tags:
- model
read status: Todo
doi: 10.1613/jair.1579
---
## Abstract

This paper extends the framework of partially observable Markov decision processes (POMDPs) to multi-agent settings by incorporating the notion of agent models into the state space. Agents maintain beliefs over physical states of the environment and over models of other agents, and they use Bayesian updates to maintain their beliefs over time. The solutions map belief states to actions. Models of other agents may include their belief states and are related to agent types considered in games of incomplete information. We express the agents' autonomy by postulating that their models are not directly manipulable or observable by other agents. We show that important properties of POMDPs, such as convergence of value iteration, the rate of convergence, and piece-wise linearity and convexity of the value functions carry over to our framework. Our approach complements a more traditional approach to interactive settings which uses Nash equilibria as a solution paradigm. We seek to avoid some of the drawbacks of equilibria which may be non-unique and do not capture off-equilibrium behaviors. We do so at the cost of having to represent, process and continuously revise models of other agents. Since the agent's beliefs may be arbitrarily nested, the optimal solutions to decision making problems are only asymptotically computable. However, approximate belief updates and approximately optimal plans are computable. We illustrate our framework using a simple application domain, and we show examples of belief updates and value functions.

## Research Questions
> Research Questions extracted via LLM from the published full text.[^r1]

- How can a POMDP represent an agent's beliefs about the physical world and models of other agents?[^r1]
- How are those interactive beliefs updated from the agent's action and observation?[^r2]
- How are sequential actions selected to maximize expected discounted reward?[^r3]
- Which POMDP value-iteration properties hold for finitely nested interactive POMDPs?[^r4]

## Model
> Model extracted via LLM according to [[Model Notation]] from §5, Definitions 1–3 and Proposition 2, §5.2 Eqs. 7–8, and §6 of the published paper.[^r5]

### What does it represent?

- An interactive POMDP (I-POMDP) extends a partially observable decision process by including models of other agents in the state an agent reasons about.[^r5]
- Other-agent models may be subintentional (for example, a frame with an action distribution) or intentional (a belief state and frame).[^r5]

```yml
State: ...
Action: ...
Observation: ...

IPOMDP:
  physical_states: [State]
  self_actions: [Action]
  observations: [Observation]
  transition: ...
  observation_model: ...
  reward: ...
  discount: 0..1

InteractiveState:
  physical: State
  other_model: OtherModel

OtherModel:
  Subintentional: ...
  Intentional:
    belief: [InteractiveState -> 0..1]
    frame: ...

Agent:
  belief: [InteractiveState -> 0..1]
```

### How does it work?

- The agent observes its own observation, and maintains a belief distribution over interactive states. It cannot directly observe another agent's model, and its own actions do not directly alter that model; observed environmental consequences can affect the other agent indirectly.[^r6]
- To update its belief after its action and observation, the agent predicts the other agent's action from its modeled type, then sums over possible previous interactive states and the other agent's actions, applying transition and observation probabilities and normalizing (Proposition 2).[^r2]
- It evaluates actions by expected immediate reward plus discounted continuation value, averaging over interactive states and future observations; it selects an action maximizing this value (Eqs. 7–8).[^r3]
- Finite nesting bounds recursive model evaluation. For finitely nested models, §6 establishes belief-update behavior, value-iteration convergence and its rate, and piecewise-linear/convex value functions; unbounded nesting is not represented by this terminating procedure.[^r4][^r7]

The notation leaves transition, observation, reward, and type-specific action models abstract because the paper treats them as problem inputs; it omits the full sums in the belief and value equations.[^r2][^r3]

### What can it answer?

- Given an interactive belief and a specified problem frame, which action maximizes expected discounted value?[^r3]
- How do beliefs about other agents' beliefs and behavior affect that decision?[^r2][^r3]

### Where does it apply?

Sequential decisions under partial observability where agents reason about other agents' hidden models. The paper illustrates the framework with a multi-agent Tiger domain.[^r8]

## Metadata
### References
- [[IdentifyingTheScopeOfModelingForTimeCriticalMultiagentDecisionMaking]]
- [[TamingDecentralizedPomdpsTowardsEfficientPolicyComputationForMultiagentSettings]]
- [[SequentialOptimalityAndCoordinationInMultiagentSystems]]
- [[MultiagentReinforcementLearningTheoreticalFrameworkAndAnAlgorithm]]
- [[MarkovGamesAsAFrameworkForMultiAgentReinforcementLearning]]
- [[RationalCoordinationInMultiAgentEnvironments]]
- [[PlanningAndControlInStochasticDomainsWithImperfectInformation]]
- [[TheTheoryOfLearningInGames]]
- [[OnTheUndecidabilityOfProbabilisticPlanningAndRelatedStochasticOptimizationProblems]]
- [[EvolutionarySelectionDynamicsInGamesConvergenceAndLimitProperties]]
- [[FormulationOfBayesianAnalysisForGamesWithIncompleteInformation]]
- [[NonComputableStrategiesAndDiscountedRepeatedGames]]
- [[MultiAgentInfluenceDiagramsForRepresentingAndSolvingGames]]
- [[TheComplexityOfMarkovDecisionProcesses]]
- [[TheOptimalControlOfPartiallyObservableMarkovProcessesOverAFiniteHorizon]]
- [[DecisionTheoreticPlanningStructuralAssumptionsAndComputationalLeverage]]
- [[ASurveyOfAlgorithmicMethodsForPartiallyObservedMarkovDecisionProcesses]]
- [[RecursiveMethodsInEconomicDynamics]]
- [[InteractiveEpistemologyIKnowledge]]
- [[TheComplexityOfDecentralizedControlOfMarkovDecisionProcesses]]
- [[TheHierarchicalApproachToModelingKnowledgeAndCommonKnowledge]]
- [[GameTheoryAnalysisOfConflict]]
- [[ArtificialIntelligenceAModernApproach]]
- [[SubjectiveProbabilityAndTheTheoryOfGames]]
- [[GamesWithIncompleteInformationPlayedByBayesianPlayersIIiiPartITheBasicModel]]
- [[ReasoningAboutKnowledge]]
- [[ThePowerOfParadoxSomeRecentDevelopmentsInInteractiveEpistemology]]
- [[HierarchiesOfConditionalBeliefsAndInteractiveEpistemologyInDynamicGames]]
- [[PlanningAndActingInPartiallyObservableStochasticDomains]]
- [[ValueFunctionApproximationsForPartiallyObservableMarkovDecisionProcesses]]
- [[HierarchiesOfBeliefsAndCommonKnowledge]]
- [[AnIntroductionToKolmogorovComplexityAndItsApplications]]
- [[GameTheorySecondEdition]]
- [[UnresolvedReferenceBA08BD6D564044DE]]
- [[UnresolvedReference9286FDFD47C1A226]]


## Audit Log

- 2026-09-29: Independent audit passed the model's main claims but found the list of proved properties incomplete. Added belief-update behavior and convergence rate from §6.
- 2026-09-29: Independent re-audit passed. Verified the revised claim and [^r4] against §6, Propositions 3–5 (interactive beliefs as sufficient statistics; value-iteration convergence and rate; piecewise-linear/convex value functions), and the finite-nesting discussion in §6; PDF pp. 11–14. Source: https://www.cs.cmu.edu/afs/cs/project/jair/pub/volume24/gmytrasiewicz05a.pdf.

## LLM Justification
[^r1]: §5 introduces interactive POMDPs and the addition of other-agent models to the physical state space (Definitions 1–3).
[^r2]: §5.1, Proposition 2 specifies Bayesian belief update from the agent's prior belief, previous action, and current observation, summing over the other agent's possible actions and hidden interactive states.
[^r3]: §5.2, Eqs. 7–8 define expected value and the maximizing action for a belief state, including discounted future value.
[^r4]: §6, Proposition 3 treats interactive beliefs as sufficient statistics; Propositions 4–5 establish value-iteration convergence, its rate, and piecewise-linear/convex value functions for finitely nested I-POMDPs.
[^r5]: §5, Definitions 1–3 define frames, subintentional/intentional models, agent types, and interactive states.
[^r6]: §5 states the Model Non-manipulability and Model Non-observability assumptions and their implications for private models.
[^r7]: §6 explains finite nesting as the recursion bound; §5 notes arbitrary nesting makes optimal solutions only asymptotically computable.
[^r8]: §7 describes the multi-agent Tiger application.
