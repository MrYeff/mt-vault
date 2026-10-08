---

title: "HUMAT: An Integrated Framework for Modelling Individual Motivations, Social Exchange and Network Dynamics"
tags:
  - model
  - simulation
authors:
  - "[[Literature/Authors/Wander Jager|Wander Jager]]"
  - "[[Literature/Authors/Patrycja Antosz|Patrycja Antosz]]"
  - "[[Literature/Authors/Loes Bouman|Loes Bouman]]"
  - "[[Literature/Authors/Teng Li|Teng Li]]"
  - "[[Literature/Authors/J. Gareth Polhill|J. Gareth Polhill]]"
  - "[[Literature/Authors/Timo Szczepanska|Timo Szczepanska]]"
  - "[[Literature/Authors/Shaoni Wang|Shaoni Wang]]"
publication date: 2025-01-31
source:
  - https://www.jasss.org/28/1/4.html
doi: 10.18564/jasss.5611
read status: Todo
---
## Abstract
In this paper we present HUMAT, an integrated modelling framework that supports the simulation of social dynamics. HUMAT integrates theoretical ideas about human motives, cognitive dissonance, individual and social decision strategies, and the processes of influence that take place in networked communities. As such, HUMAT provides a generic model that can be implemented in a wide variety of cases dealing with opinion and behaviour dynamics in a social context, be it the adoption of a physical innovation or the promotion of an attitude in an online platform. The multi-theoretical background of HUMAT also provides a perspective on what types of qualitative and quantitative data can be used to parameterise real cases. This paper aims to provide an overview of the different processes modelled in HUMAT. Three applications are used to illustrate how HUMAT can be used to simulate and study social dynamics. The validation of the HUMAT framework is discussed in the context of the dynamic theory of social complexity.[^r0]

## Research Questions
> Research questions distilled from the primary paper; phrasing is paraphrased.[^r0]
- How can HUMAT integrate individual motives, cognitive dissonance, decision strategies, and social influence to simulate social dynamics?[^r0]
- How is HUMAT parameterised for a particular social case?[^r0]
- How is HUMAT's validity assessed?[^r0]

## Model
> Model extracted via LLM according to [[Model Notation]]. This describes the basic two-option ODD instance; application-specific extensions are separate.[^r7]

### What does it represent?

Agents choose between A and B using experiential, social and value motives. They store information about their network neighbors.[^r1]

State follows Tables 1–3. Neighbor importance and satisfaction start at zero; their choice is observed. Initial positions, cached social satisfaction, counters and detailed persuasion bookkeeping are omitted from this type summary.[^r1][^r18]

```yml
World:
  agents: [Agent]
  max_ticks: u32

Agent:
  choice: Choice
  importance: Motives(0..1)
  aspiration: 0..1
  tolerance: 0..1
  alternatives: [Choice -> Alternative]
  neighbors: [AgentId -> View]
  current_strength: 0..1 # source's singular gate; update unspecified
  social_dilemma: bool
  non_social_dilemma: bool
  signalling: bool
  inquiring: bool # setter absent from Inquire submodel
  signalling_list: [AgentId]
  inquiry_list: [AgentId]

Choice: A | B

Motives(Value):
  experiential: Value
  social: Value
  values: Value

Alternative:
  satisfaction: Motives(-1..1)
  evaluation: Motives(-1..1)
  total: -1..1
  dissonance: 0..1
  strength: 0..1

View:
  choice: Choice
  importance: Motives(0..1) # initially zero
  satisfaction: [Choice -> NonSocial(-1..1)] # initially zero
  same_choice: bool # stored match flag
  inquired: bool
  signalled: bool
  inquiry_score: 0..
  signalling_score: 0..

NonSocial(Value):
  experiential: Value
  values: Value
```

### How does it work?

Constants follow Appendix A. Beta shapes configure the four experiential/value satisfaction distributions.[^r8]

```
IMPORTANCE_DIST = Normal(0.5, 0.14), truncated to [0, 1]
ASPIRATION_INIT = Uniform(0, 1)
BETA_SHAPES = [(12,4), (8,4), (4,4), (4,8), (4,12)]
NETWORK_RADIUS = 35 # Create networks; Stochasticity instead says distance <36
INITIAL_LINK_FRACTION = 0.20
SIMILARITY_WEIGHT = 0.4
ASPIRATION_WEIGHT = 0.4
CHOICE_TOLERANCE = 0.1
SATISFACTION_RANGE = 2
DISSONANCE_RANGE = 1
EXPERIENTIAL_RANGE = 2
```

Initialization follows this order; the source leaves some details of the later synchronization unresolved.[^r8][^r18]

1. Create agents at the origin; draw aspiration and an integer heading from 0–359°; move forward an integer distance of 0–39 patches.[^r8]
2. Connect each agent to a random 20% of agents within `NETWORK_RADIUS`. With no link, choose a nearest agent; break distance ties randomly.[^r8]
3. In random agent order, draw motive importance and tolerance from `IMPORTANCE_DIST`; draw experiential/value satisfaction from configured Beta distributions; compute importance × satisfaction evaluations.[^r8]
4. Set **basic choice**: compare the mean of the two non-social evaluations for A/B; choose the larger, randomizing exact ties.[^r8]
5. Set **initial choice**: build neighbor views, set social motives and dilemma flags, then call `choose(agent, initializing=true)`.[^r8]
6. Set alter representations and sorted interaction lists; initialize other neighbor fields to zero. Set dissonances for all agents in random order.[^r8]

Each tick exchanges information, then updates dissonances in random agent order. The gate below is deliberately partial: the paper does not specify how its singular `current_strength` stays synchronized with the per-choice strengths.[^r2][^r18]

```
sim_step(mut world: World):
  for ego_id in random_order(ids(world.agents)):
    ego = world.agents[ego_id]
    ego.signalling = false
    ego.inquiring = false
    if source_current_strength(ego) > 0:
      if ego.social_dilemma and ego.non_social_dilemma:
        exchange(world, ego_id, random(Signal, Inquire))
      else if ego.social_dilemma:
        exchange(world, ego_id, Signal)
      else if ego.non_social_dilemma:
        exchange(world, ego_id, Inquire)
  for id in random_order(ids(world.agents)):
    update_dissonances(world.agents[id])


source_current_strength(agent: Agent) -> 0..1:
  ... # Table 1: chosen alternative's strength.
      # No singular-field synchronization procedure is given.
```

`update_dissonances` uses stored neighbor choices. It also identifies the chosen alternative's dilemma; the source does not specify zero-denominator behavior.[^r9][^r18]

```
update_dissonances(mut agent: Agent):
  for choice in [A, B]:
    option = agent.alternatives[choice]
    fraction = count(v.choice == choice for v in agent.neighbors)
      / len(agent.neighbors)
    option.satisfaction.social = 2 * fraction - 1
    for motive in [experiential, social, values]:
      option.evaluation[motive] = agent.importance[motive]
        * option.satisfaction[motive]
    option.total = mean(option.evaluation)
    P = sum(positive(option.evaluation))
    N = sum(abs(negative(option.evaluation)))
    option.dissonance = 2 * min(P, N) / (P + N)
    option.strength = max(0, (option.dissonance - agent.tolerance)
      / (1 - agent.tolerance))

  e = agent.alternatives[agent.choice].evaluation
  agent.social_dilemma = e.social < 0
    and (e.experiential > 0 or e.values > 0)
  agent.non_social_dilemma = e.social >= 0
    and (e.experiential < 0 or e.values < 0)
```

Partner lists contain IDs. Sort stored views by previous-contact flag first, preferred choice match second, persuasion third. The source prioritizes uncontacted opposite-choice neighbors for signalling and uncontacted same-choice neighbors for inquiry; it gives no filter or exhaustion rule.[^r10]

Exchange direction and view refresh follow the two submodels. `refresh_traits` copies the communicated importance and experiential/value satisfaction into the indicated view; `blend` is defined below. Comments retain bookkeeping whose exact aggregation is unspecified.[^r10][^r15][^r18]

```
exchange(mut world: World, ego_id: AgentId, mode: Signal | Inquire):
  ego = world.agents[ego_id]
  alter_id = first(if mode == Signal: ego.signalling_list
    else: ego.inquiry_list)
  alter = world.agents[alter_id]

  if mode == Signal:
    view = alter.neighbors[ego_id]
    refresh_traits(view, ego)
    view.choice = ego.choice
    blend(alter, view, ego.aspiration - alter.aspiration)
    update_dissonances(alter)
    choose(alter)
    ego.neighbors[alter_id].choice = alter.choice
    ego.neighbors[alter_id].same_choice = alter.choice == ego.choice
    ego.neighbors[alter_id].signalled = true
    # Update signalling score: source sums items 25–30, including
    # itself. Its non-circular construction is unresolved.
    ego.signalling_list = order_neighbors(ego, Signal)
    ego.signalling = true
    # Increment sender's #signalling.
    update_dissonances(ego)
    choose(ego)
  else:
    view = ego.neighbors[alter_id]
    refresh_traits(view, alter) # BEFORE using received traits
    view.inquired = true # Table 3: already inquired with
    weights = blend(ego, view, ego.aspiration - alter.aspiration)
    view.inquiry_score = sum(
      weights[c][m] for c in [A, B], m in [experiential, values]
    ) # Table 3 item 29 = sum of items 21–24
    update_dissonances(ego)
    choose(ego)
    alter.neighbors[ego_id].choice = ego.choice
    alter.neighbors[ego_id].same_choice = ego.choice == alter.choice
    # Increment alter's #inquired.
    update_dissonances(alter)
    choose(alter)
    ego.inquiry_list = order_neighbors(ego, Inquire)
    # Inquire does not specify setting ego.inquiring to true.
    # The corresponding output indicator remains under-specified.


order_neighbors(agent: Agent, mode: Signal | Inquire) -> [AgentId]:
  if mode == Signal:
    out = neighbor IDs sorted by stored view.signalled ascending,
      not view.same_choice descending, signalling_score descending
  else:
    out = neighbor IDs sorted by stored view.inquired ascending,
      view.same_choice descending, inquiry_score descending


blend(
  mut listener: Agent,
  view: View,
  aspiration_difference: f64
) -> [Choice -> NonSocial(0..1)]:
  aspiration = clamp(ASPIRATION_WEIGHT * aspiration_difference, 0, 1)
  for choice in [A, B]:
    option = listener.alternatives[choice]
    for motive in [experiential, values]:
      heard = view.satisfaction[choice][motive]
      heard_eval = view.importance[motive] * heard
      similarity = 0
      if sign(option.evaluation[motive]) == sign(heard_eval):
        similarity = SIMILARITY_WEIGHT * (
          1 - abs(listener.importance[motive] - view.importance[motive])
        )
      weight = similarity * aspiration
      weights[choice][motive] = weight
      option.satisfaction[motive] =
        (1 - weight) * option.satisfaction[motive] + weight * heard
  out = weights
```

Choice compares satisfaction, then lower dissonance, then experiential satisfaction. A comparison proceeds to the next dimension only when its difference is strictly below `CHOICE_TOLERANCE × range`. If all differences are small, initialization randomizes; later calls retain the current choice.[^r11]

```
choose(mut agent: Agent, initializing: bool = false):
  a = agent.alternatives[A]
  b = agent.alternatives[B]
  if abs(a.total - b.total) >= CHOICE_TOLERANCE * SATISFACTION_RANGE:
    agent.choice = if a.total > b.total: A else: B
  else if abs(a.dissonance - b.dissonance)
      >= CHOICE_TOLERANCE * DISSONANCE_RANGE:
    agent.choice = if a.dissonance < b.dissonance: A else: B
  else if abs(a.satisfaction.experiential - b.satisfaction.experiential)
      >= CHOICE_TOLERANCE * EXPERIENTIAL_RANGE:
    agent.choice = if a.satisfaction.experiential > b.satisfaction.experiential:
      A else: B
  else if initializing:
    agent.choice = random(A, B)
```

Source conflicts and missing rules:[^r6][^r9][^r15][^r16][^r18]

- Aspiration: initialization uses [0,1]; Stochasticity says [0,3).
- Network radius: Create networks says within 35 Euclidean cells; Stochasticity says distance <36. These differ for noninteger distances.[^r19]
- Habit: narrative requires more satisfaction **and** less dissonance; the choice procedure uses successive comparisons.
- Activation: Appendix A's Interaction narrative requires a dilemma and negligible satisfaction/dissonance differences; Signal or inquire gates on positive strength.
- Social satisfaction: Interaction says same-choice fraction must meet social importance; Set social motive's sign boundary is 50% for positive importance.
- Knowledge: Table 3's introduction assumes perfect knowledge of all neighbor choices. The submodels calculate from stored views and refresh selected views; global choice synchronization is not specified. Stale views are therefore an implementation possibility, not the stated knowledge assumption.
- The singular chosen-strength gate has no specified synchronization with per-choice strength after choice changes.
- The signalling score's self-inclusive sum, partner exhaustion, zero denominators and inquiry-indicator setter are unresolved. The procedures are a partial specification, not runnable replacement code.

### What can it answer?

- Given motives and a network, how do A/B choices change?[^r3]
- Given those choices, how do satisfaction and dissonance change?[^r3]
- Given a case-specific intervention, does the outcome cross a tipping point?[^r3][^r12]
- Basic observations: A/B fractions, average satisfaction from each alternative, dissonance of agents choosing each alternative, and numbers of signalling/inquiring agents. The Inquire submodel does not specify its indicator setter.[^r13][^r19]
- Dialogue example: unanimous support despite remaining dissatisfaction. Groningen: 14,165 agents, 1,000 runs, reported vote distribution peak 49.54 (SD 0.72); campaigns or a safety event can tip the outcome.[^r12]
- Vaccination extension adds availability heuristic, confirmation bias and fear. Higher disease severity raises vaccination and vaccinated-group satisfaction; unvaccinated-group satisfaction declines slightly.[^r12]

### Where does it apply?

- Case-defined choices and direct social networks: community dialogue, a referendum and vaccination.[^r4]
- Parameters/data and extensions depend on the case. The basic ODD has no time-series input or generic procedure for adding/removing ties.[^r13][^r14]

## Metadata
### References
All 71 entries below match the primary paper bibliography one-to-one in source order. Targets use filename-safe source-title forms; each display alias retains the bibliography title. No matching reference notes existed in the vault target inventory at import time.[^r17]

- [[From intentions to actions- A theory of planned behavior|From intentions to actions: A theory of planned behavior]]
- [[SMARTEES simulation implementations, deliverable 7.2|SMARTEES simulation implementations, deliverable 7.2]]
- [[SMARTEES simulation implementations, deliverable 7.3|SMARTEES simulation implementations, deliverable 7.3]]
- [[Sensemaking of causality in agent-based models|Sensemaking of causality in agent-based models]]
- [[Dynamical affinity in opinion dynamics modeling|Dynamical affinity in opinion dynamics modeling]]
- [[Social Learning through Imitation|Social Learning through Imitation]]
- [[Reports on scenario development and experiments for selected cases|Reports on scenario development and experiments for selected cases]]
- [[From beliefs to attitudes- Polias, a model of attitude dynamics based on cognitive modeling and field data|From beliefs to attitudes: Polias, a model of attitude dynamics based on cognitive modeling and field data]]
- [[Crafting mixed-method evaluation designs|Crafting mixed-method evaluation designs]]
- [[Birth and death in a continuous opinion dynamics model|Birth and death in a continuous opinion dynamics model]]
- [[A focus theory of normative conduct- A theoretical refinement and reevaluation of the role of norms in human behavior|A focus theory of normative conduct: A theoretical refinement and reevaluation of the role of norms in human behavior]]
- [[Priority challenges for social and behavioral research and its modeling|Priority challenges for social and behavioral research and its modeling]]
- [[Finding the sweet spot between efficacy and acceptance of COVID restrictions|Finding the sweet spot between efficacy and acceptance of COVID restrictions]]
- [[Co-developing beliefs and social influence networks - Towards understanding socio-cognitive processes like Brexit|Co-developing beliefs and social influence networks - Towards understanding socio-cognitive processes like Brexit]]
- [[Generative Social Science|Generative Social Science]]
- [[Agent_Zero- Toward Neurocognitive Foundations for Generative Social Science|Agent_Zero: Toward Neurocognitive Foundations for Generative Social Science]]
- [[A theory of social comparison processes|A theory of social comparison processes]]
- [[A Theory of Cognitive Dissonance|A Theory of Cognitive Dissonance]]
- [[Simulation for the social scientist|Simulation for the social scientist]]
- [[How to relate models to reality- An epistemological framework for the validation and verification of computational models|How to relate models to reality? An epistemological framework for the validation and verification of computational models]]
- [[Introduction to action research- Social research for social change|Introduction to action research: Social research for social change]]
- [[The ODD protocol- A review and first update|The ODD protocol: A review and first update]]
- [[Testing the action-based model of cognitive dissonance- The effect of action-orientation on post-decisional attitudes|Testing the action-based model of cognitive dissonance: The effect of action-orientation on post-decisional attitudes]]
- [[Über den anschaulichen Inhalt der quantentheoretischen Kinematik und Mechanik|Über den anschaulichen Inhalt der quantentheoretischen Kinematik und Mechanik]]
- [[Self-Organization, emergence and the architecture of complexity|Self-Organization, emergence and the architecture of complexity]]
- [[Communication and Persuasion- Psychological Studies of Opinion Change|Communication and Persuasion: Psychological Studies of Opinion Change]]
- [[Case-Based reasoning, social dilemmas, and a new equilibrium concept|Case-Based reasoning, social dilemmas, and a new equilibrium concept]]
- [[Modelling consumer behaviour|Modelling consumer behaviour]]
- [[Enhancing the realism of simulation (EROS)- On implementing and developing psychological theory in social simulation|Enhancing the realism of simulation (EROS): On implementing and developing psychological theory in social simulation]]
- [[Simulating the role of norms in processes of social innovation- Three case studies|Simulating the role of norms in processes of social innovation: Three case studies]]
- [[Simulations as a dialogue tool- Strengthening community engagement and local democratic processes|Simulations as a dialogue tool: Strengthening community engagement and local democratic processes]]
- [[Simulating community dynamics for transitional urban planning processes|Simulating community dynamics for transitional urban planning processes]]
- [[Meeting targets- Tools to support integrated assessment modelling of global change|Meeting targets: Tools to support integrated assessment modelling of global change]]
- [[-Reinstatement- of the communicator in delayed measurement of opinion change|"Reinstatement" of the communicator in delayed measurement of opinion change]]
- [[Renovating the pyramid of needs- Contemporary extensions built upon ancient foundations|Renovating the pyramid of needs: Contemporary extensions built upon ancient foundations]]
- [[Measuring stability and change in personal culture using panel data|Measuring stability and change in personal culture using panel data]]
- [[Editorial for the research topic- Tipping points in societies|Editorial for the research topic: Tipping points in societies]]
- [[A Philosophical Essay on Probabilities|A Philosophical Essay on Probabilities]]
- [[How availability heuristic, confirmation bias and fear may drive societal polarisation- An opinion dynamics simulation of the case of COVID-19 vaccination|How availability heuristic, confirmation bias and fear may drive societal polarisation: An opinion dynamics simulation of the case of COVID-19 vaccination]]
- [[Deterministic nonperiodic flow|Deterministic nonperiodic flow]]
- [[Motivation and Personality|Motivation and Personality]]
- [[Development and human needs|Development and human needs]]
- [[Social isolation in america- Changes in core discussion networks over two decades|Social isolation in america: Changes in core discussion networks over two decades]]
- [[Editorial- Modelling values in social, technical, and ecological systems|Editorial: Modelling values in social, technical, and ecological systems]]
- [[Better be convincing or better be stylish- A theory based multi-Agent simulation to explain minority influence in groups via arguments or via peripheral cues|Better be convincing or better be stylish? A theory based multi-Agent simulation to explain minority influence in groups via arguments or via peripheral cues]]
- [[One theory - many formalizations- Testing different code implementations of the theory of planned behaviour in energy agent-Based models|One theory - many formalizations: Testing different code implementations of the theory of planned behaviour in energy agent-Based models]]
- [[Gemeente Groningen’s report from the referendum- Uitslag en Achtergrond van het Referendum Noorderplantsoen|Gemeente Groningen’s report from the referendum: Uitslag en Achtergrond van het Referendum Noorderplantsoen]]
- [[Dynamical Social Psychology|Dynamical Social Psychology]]
- [[Dynamical social psychology- An introduction|Dynamical social psychology: An introduction]]
- [[Social norms as solutions- Policies may influence large-Scale behavioral tipping|Social norms as solutions: Policies may influence large-Scale behavioral tipping]]
- [[Habits and intention in everyday life- The multiple processes by which past behavior predicts future behavior|Habits and intention in everyday life: The multiple processes by which past behavior predicts future behavior]]
- [[Case studies, cross-Site comparisons, and the challenge of generalization- Comparing agent-Based models of land-Use change in frontier regions|Case studies, cross-Site comparisons, and the challenge of generalization: Comparing agent-Based models of land-Use change in frontier regions]]
- [[Conditioned Reflexes|Conditioned Reflexes]]
- [[Communication and Persuasion- Central and Peripheral Routes to Attitude Change|Communication and Persuasion: Central and Peripheral Routes to Attitude Change]]
- [[Using computational modeling for building theory- A double edged sword|Using computational modeling for building theory: A double edged sword]]
- [[The persuasiveness of source credibility- A critical review of five decades’ evidence|The persuasiveness of source credibility: A critical review of five decades’ evidence]]
- [[Diffusion of Innovations|Diffusion of Innovations]]
- [[Critical Transitions in Nature and Society|Critical Transitions in Nature and Society]]
- [[Shaping the social-ecological transformation. How social barriers can be overcome and how resonance potentials can be utilised|Shaping the social-ecological transformation. How social barriers can be overcome and how resonance potentials can be utilised]]
- [[A framework for mapping and comparing behavioral theories in models of social-ecological systems|A framework for mapping and comparing behavioral theories in models of social-ecological systems]]
- [[Modeling dynamic identities and uncertainty in social interactions- Bayesian affect control theory|Modeling dynamic identities and uncertainty in social interactions: Bayesian affect control theory]]
- [[Formalising theories of human decision-making for agent-based modelling of social-ecological systems- Practical lessons learned and ways forward|Formalising theories of human decision-making for agent-based modelling of social-ecological systems: Practical lessons learned and ways forward]]
- [[The Behavior of Organisms|The Behavior of Organisms]]
- [[Bourdieu and education- How useful is Bourdieu’s theory for researchers-|Bourdieu and education: How useful is Bourdieu’s theory for researchers?]]
- [[The effect and modification of the Traffic Circulation Plan (VCP) - Traffic planning in Groningen in the 1980s|The effect and modification of the Traffic Circulation Plan (VCP) - Traffic planning in Groningen in the 1980s]]
- [[Good intentions, bad habits, and effects of forming implementation intentions on healthy eating|Good intentions, bad habits, and effects of forming implementation intentions on healthy eating]]
- [[Integronsters’, integral and integrated modeling|Integronsters’, integral and integrated modeling]]
- [[Gaming polarisation- Using agent-Based simulation as a dialogue tool|Gaming polarisation: Using agent-Based simulation as a dialogue tool]]
- [[Development of a formal system for representing behaviour-change theories|Development of a formal system for representing behaviour-change theories]]
- [[The animat path to AI|The animat path to AI]]
- [[Global greenhouse gas emissions from animal-based foods are twice those of plant-based foods|Global greenhouse gas emissions from animal-based foods are twice those of plant-based foods]]

## Audit Log
- Independent source audit passed after corrections; extraction and references are finalized.[^r5]
- A further audit found the unreported radius discrepancy, undefined inquiry-ranking score and missing indicator fields. These were corrected or explicitly marked as source omissions and passed independent re-audit.[^r19]
- Re-audit found inconsistent state paths, mutation syntax, incomplete initialization, and mislocated knowledge/activation statements. The corrected model uses explicit ID lookup, numeric view defaults, ordered setup, stored social satisfaction and a clearly partial gate; independent re-audit passed.[^r18]
- 2026-10-03: Independent audit of an earlier snapshot failed (H1–H7: source conflicts, cached partner selection, exchange update order, initialization details, and item-30 ambiguity). Corrections were incorporated and passed independent re-audit.[^r5]

## LLM Justification
[^r0]: Abstract copied verbatim from the primary publication record/full text. Research questions are concise paraphrases of the paper’s stated aims/questions. https://www.jasss.org/28/1/4.html
[^r1]: Jager et al., “HUMAT,” Appendix A, “Overview” and state variables tables (Tables 1–2); Section 2, “The HUMAT Framework.” https://www.jasss.org/28/1/4.html
[^r2]: Jager et al., “HUMAT,” Appendix A, Tables 1–4 and “Initialisation,” “Process overview and scheduling,” “Signal or inquire,” “Signal,” “Inquire,” “Set dissonances,” “Update dissonances,” and “Choose alternative.” https://www.jasss.org/28/1/4.html
[^r3]: Jager et al., “HUMAT,” Section 2.5, “Use and outputs.” https://www.jasss.org/28/1/4.html
[^r4]: Jager et al., “HUMAT,” Section 3, “Examples of HUMAT Implementations,” and abstract. https://www.jasss.org/28/1/4.html
[^r5]: Audit state for this current import; source cache and process record are in `vault/.automation/audit/noted-simulations-2026-10-03/humat-repair.json`.
[^r6]: Jager et al., “HUMAT,” Appendix A, “Stochasticity” (aspiration 0 to <3), Table 1 and “Create agents” ([0,1]), “Process overview and scheduling” (habit narrative), and “Choose alternative” (thresholded procedure). https://www.jasss.org/28/1/4.html
[^r7]: Jager et al., “HUMAT,” Appendix A, “Process overview and scheduling,” “Submodels,” “Signal,” “Inquire,” and “Update dissonances,” Tables 1–4. Pseudocode condenses per-alter records; source ambiguities and omitted details are identified in the accompanying bullets. https://www.jasss.org/28/1/4.html
[^r8]: Jager et al., “HUMAT,” Appendix A, “Initialisation,” “Create agents,” “Create networks,” “Set non-social motives,” “Set basic choice,” “Set initial choice,” and “Set alter representations”; the conflicting aspiration range is stated in “Stochasticity.” https://www.jasss.org/28/1/4.html
[^r9]: Jager et al., “HUMAT,” Appendix A, “Update motive evaluations,” “Set social motive,” and “Update dissonances.” https://www.jasss.org/28/1/4.html
[^r10]: Jager et al., “HUMAT,” Appendix A, “Signal or inquire,” “Signal,” “Inquire,” and “Set alter representations.” The two interaction directions update different agents, as stated in the corresponding submodels. https://www.jasss.org/28/1/4.html
[^r11]: Jager et al., “HUMAT,” Section 2.2, “Attitude formation,” and Appendix A, “Choose alternative.” The narrative habit rule and operational comparison differ. https://www.jasss.org/28/1/4.html
[^r12]: Jager et al., “HUMAT,” Section 3, subsections “Using HUMAT for a stylized model,” “The Groningen case,” and “The COVID-19 vaccination case,” and Figures 1–5. https://www.jasss.org/28/1/4.html
[^r13]: Jager et al., “HUMAT,” Appendix A “Observation” and “Input data,” and Section 2.5 “Use and outputs.” https://www.jasss.org/28/1/4.html
[^r14]: Jager et al., “HUMAT,” Section 2.3, “Social networks.” The section leaves tie adaptation to application design. https://www.jasss.org/28/1/4.html
[^r15]: Jager et al., “HUMAT,” Appendix A, “Signal,” especially alter-representation-list item 30 and its subsequent sort; Table 3 defines items 25–30. https://www.jasss.org/28/1/4.html
[^r16]: Jager et al., “HUMAT,” Appendix A, Design concepts > Interaction (negligible-gap activation and social-importance threshold) versus Submodels > Signal or inquire, Set social motive and Identify dilemmas (operational rules). Section 2 and Appendix A attitude-formation narrative also describe the habit rule. https://www.jasss.org/28/1/4.html
[^r17]: Jager et al., “HUMAT,” complete “References” section. Reference target policy and inventory: `vault/.automation/audit/repair-2026-10-03/reference-target-policy.json` and `existing-paper-targets.json`. https://www.jasss.org/28/1/4.html

[^r18]: Appendix A, Tables 1–3: singular strength refers to the chosen alternative; per-choice strength is stored separately; Table 3 initially stores zero importance/satisfaction and explicitly assumes perfect knowledge of neighbor choices. Initialisation > Setup Humats specifies Set non-social motives → Set basic choice → Set initial choice → Set alter representations → Set dissonances. Submodels > Signal/Inquire specify selected-view refresh and participant update order. Type summaries omit cached social satisfaction, counters and derived persuasion bookkeeping; comments identify those operations. The unspecified gate synchronization and self-inclusive signalling-score sum are left as partial procedures. Corrections and prior failed re-audit: vault/.automation/audit/noted-simulations-2026-10-03/audit-humat-reaudit.json. https://www.jasss.org/28/1/4.html

[^r19]: Appendix A, Stochasticity says links to agents at distance <36 patches; Create networks says within 35-cell Euclidean distance. Table 3 defines inquiry score item 29 as the sum of items 21–24; Set alter representations and Inquire sort by contact flag ascending, same-choice flag descending, persuasion descending. Signal sorts by signalled ascending, different-choice descending, signalling score descending. Table 1 and Observation define signalling/inquiring indicators; Signal explicitly sets its indicator, while Inquire does not give the corresponding setter. The note does not invent that missing assignment. Failed audit: vault/.automation/audit/noted-simulations-2026-10-03/audit-humat-final.json. https://www.jasss.org/28/1/4.html
