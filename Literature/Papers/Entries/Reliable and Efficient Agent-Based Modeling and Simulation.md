---
title: "Reliable and Efficient Agent-Based Modeling and Simulation"
tags:
  - agent_based_model
  - simulation_framework
authors:
  - "[[Literature/Authors/Alessia Antelmi|Alessia Antelmi]]"
  - "[[Literature/Authors/Pasquale Caramante|Pasquale Caramante]]"
  - "[[Literature/Authors/Gennaro Cordasco|Gennaro Cordasco]]"
  - "[[Literature/Authors/Giuseppe D’Ambrosio|Giuseppe D’Ambrosio]]"
  - "[[Literature/Authors/Daniele De Vinco|Daniele De Vinco]]"
  - "[[Literature/Authors/Francesco Foglia|Francesco Foglia]]"
  - "[[Literature/Authors/Luca Postiglione|Luca Postiglione]]"
  - "[[Literature/Authors/Carmine Spagnuolo|Carmine Spagnuolo]]"
publication date: 2024-03-31 
source: "https://www.jasss.org/27/2/4.html"
doi: 10.18564/jasss.5300
read status: Todo
---

## Abstract

Agent-based models represent a primary methodology to untangle and study complex systems. Over the last decade, the need for more elaborate computing-demanding models gave rise to many frameworks and tools to run ABM simulations. Current state-of-the-art ABM tools either focus on ease of use, performance, or a trade-off between these two elements. Still, efficiency-oriented solutions (required for both large and small-scale simulations) are vulnerable to memory flaws which could invalidate the experiment results. This work aims to merge efficiency, reliability, and safeness under an innovative ABM software framework based on the Rust programming language. Our framework, krABMaga, is an open-source library that offers a high-level environment by exploiting metaprogramming and expandable visualization features. We equipped our library with a dynamic simulation monitoring system and model exploration and optimization capabilities over parallel, distributed, and cloud architectures. After having presented the overall architecture and functionalities of krABMaga, we discuss a performance comparison of our framework against the mostly adopted ABM software and the scalability potential of our simulation engine on a model calibration experiment running over an AWS EC2 virtual cluster machine. All code and examples models are available on GitHub.

## Research Questions
> Research Questions extracted via LLM
- Can krABMaga combine runtime efficiency with reliability and safety for agent-based simulation?[^r1]
- How does its simulation performance and scalability compare with established ABM tools and a distributed calibration experiment?[^r1]

## Study Design
> Study design extracted via LLM

This is a software-framework and performance study, not a substantive behavioral model. The authors compare krABMaga with established ABM tools and report scalability testing in a model-calibration experiment on an AWS EC2 cluster.[^r3]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?

- `krABMaga` is a discrete-event ABM framework, not a single behavioral theory. A model defines its agents, simulation state/fields, scheduler, and optional choice of visualization and experiment/optimization tools.[^m1]

```yml
World:
  state: State
  agents: [Agent]
  scheduler: Scheduler
  fields: [Grid2D | Field2D | Network | HNetwork]

Agent:
  step: ()
  before_step: ()? 
  after_step: ()?
  is_stopped: bool?

State:
  init: ()
  before_step: ()?
  after_step: ()?
  update: ()
  end_condition: bool?

Scheduler:
  event_queue: PriorityQueue[ScheduledAgent]
  current_step: u32
  max_steps: u32
```

### How does it work?

- A step runs state-level pre-step behavior, selects due agents from the event queue by scheduled time and priority, invokes each agent's optional `before_step`, required `step`, and optional `after_step`, reschedules repeating agents, then runs state-level `after_step` and `update`. Execution stops at the maximum step count or the state end condition. `schedule_once` and `schedule_repeating` control the event queue.[^m2]

```
sim_step(mut world: World):
  world.state.before_step()
  due = world.scheduler.pop_due(world.scheduler.current_step)
  for agent in order_by_priority(due):
    agent.before_step(world.state)
    agent.step(world.state)
    agent.after_step(world.state)
    if not agent.is_stopped(world.state):
      world.scheduler.reschedule(agent)
  world.state.after_step(world.scheduler)
  world.state.update(world.scheduler.current_step)
  stop_if(world.scheduler.max_steps, world.state.end_condition)
```

- Fields can be sparse or dense grids, continuous 2D space, directed/undirected/weighted networks, or hypergraphs. Field values use separate read and write structures: agents read the previous-step state and write changes for the next update. Writes are sequential; reads can run concurrently. `lazy_update` swaps buffers when all prior values can be discarded, while `update` copies values when they must persist. Unbuffered access can inspect writes made earlier in the same step.[^m3]
- The Wolf–Sheep–Grass tutorial demonstrates how a domain model plugs in: wolves and sheep move, lose energy, reproduce if alive, and consume grass or sheep after movement. Sheep only eat fully grown grass not already eaten that step; wolves only eat sheep not already killed that step. New agents and killed sheep are queued in the state and added/removed from the scheduler after the step; grass growth and field synchronization occur in `State.update`.[^m4]
- Monitoring macros can repeat runs and test reproducibility under a fixed seed; a terminal interface tracks step, CPU/memory, and steps per second. Parameter sweeps run each configuration for fixed steps and repetitions, then return expected outputs. Optimization options include random, genetic/evolutionary, and Bayesian search, with sequential, parallel, distributed, or cloud backends.[^m5]

### What can it answer?

- The framework study benchmarks Flockers, Schelling, Wolf–Sheep–Grass, and ForestFire against Agents.jl, MASON, Mesa, NetLogo, and Repast. The same Ubuntu 21.10/8-vCPU/16-GB VM was used; each model was run 10 times at scales from 1,000 to 128,000 agents, with grid dimensions scaled so the listed agent/area pairs imply roughly 10% occupancy. The article calls this approximately 10% density but prints `width × height / number of agents` as its calculation, which is the inverse of conventional occupancy; the source definition is internally inconsistent. Runtime excludes engine initialization. The authors report krABMaga as fastest in nearly every tested case; Agents.jl matched it in one case while using up to 90% of available memory. Larger workloads were unavailable for some tools because of memory limits.[^m6]
- A second study calibrates an SIR model on a Barabási–Albert contact network. Susceptible nodes become infected with probability `β` based on infected neighbors; infectious nodes recover with probability `γ`; recovered nodes remain immune. A randomly selected node starts infected, and each step represents one day. The target is Italy's seven-day-moving-average daily infections over 45 days in Dec. 2021–Jan. 2022, normalized by 60 million; the simulation runs 10,000 agents for 51 days.[^m7]
- Evolutionary calibration uses 128 initial parameter pairs `(β, γ)`, 20 simulation repetitions per candidate, and 2,000 generations. Each generation keeps the top 20%, fills the remaining 80% by crossover of prior candidates, and mutates one randomly selected gene; the objective is mean error from the target series. About five million runs were estimated to require 172 sequential days and took 45 hours using distributed execution. The prose reports a 96× speedup, while Table 2 reports 92× for 16 c4.2xlarge nodes/128 vCPUs; both source values are retained as a discrepancy.[^m8]

### Where does it apply?

- Use it to implement and run configurable ABMs with monitoring, visualization, parameter exploration, calibration and parallel/distributed execution. This paper does not establish a universal agent decision rule or demonstrate empirical validity of the example WSG/SIR models. The article does not give explicit numeric bounds for the SIR genes or the fitted `(β, γ)` values in its text; these are left unspecified here.[^m5][^m7][^m8]

## Metadata
### References
- [[Agent based modelling and simulation tools- A review of the state-of-art software|Agent based modelling and simulation tools: A review of the state-of-art software]]
- [[PyLogo- A Python reimplementation of (much of) NetLogo|PyLogo: A Python reimplementation of (much of) NetLogo]]
- [[PolicySpace2- Modeling markets and endogenous public policies|PolicySpace2: Modeling markets and endogenous public policies]]
- [[Challenges, tasks, and opportunities in modeling agent-based complex systems|Challenges, tasks, and opportunities in modeling agent-based complex systems]]
- [[Advanced tutorial- Parallel and distributed methods for scalable discrete simulation|Advanced tutorial: Parallel and distributed methods for scalable discrete simulation]]
- [[More is different|More is different]]
- [[Experimenting with agent-Based model simulation tools|Experimenting with agent-Based model simulation tools]]
- [[Distributed simulation of hybrid systems with AnyLogic and HLA|Distributed simulation of hybrid systems with AnyLogic and HLA]]
- [[Rust language for supercomputing applications|Rust language for supercomputing applications]]
- [[No free lunch when estimating simulation parameters|No free lunch when estimating simulation parameters]]
- [[Effect of control measure on the development of new COVID-19 cases through SIR model simulation|Effect of control measure on the development of new COVID-19 cases through SIR model simulation]]
- [[Parallel agent-based simulation with repast for high performance computing|Parallel agent-based simulation with repast for high performance computing]]
- [[Experiences in developing a distributed agent-based modeling toolkit with Python|Experiences in developing a distributed agent-based modeling toolkit with Python]]
- [[Distributed MASON- A scalable distributed multi-agent simulation environment|Distributed MASON: A scalable distributed multi-agent simulation environment]]
- [[An agent-based modeling approach applied to the spread of cholera|An agent-based modeling approach applied to the spread of cholera]]
- [[Agents.jl- A performant and feature-full agent-based modeling software of minimal code complexity|Agents.jl: A performant and feature-full agent-based modeling software of minimal code complexity]]
- [[What is a complex system, after all-|What is a complex system, after all?]]
- [[SESSL- A domain-Specific language for simulation experiments|SESSL: A domain-Specific language for simulation experiments]]
- [[A stochastic agent-based model of the SARS-CoV-2 epidemic in France|A stochastic agent-based model of the SARS-CoV-2 epidemic in France]]
- [[A general framework for agent-based modelling of complex systems|A general framework for agent-based modelling of complex systems]]
- [[PyNetLogo- Linking NetLogo with Python|PyNetLogo: Linking NetLogo with Python]]
- [[The Netlogo-Based dynamic model for the teaching|The Netlogo-Based dynamic model for the teaching]]
- [[Efficient global optimization of expensive black-box functions|Efficient global optimization of expensive black-box functions]]
- [[RustBelt- Securing the foundations of the rust programming language|RustBelt: Securing the foundations of the rust programming language]]
- [[Utilizing Python for agent-Based modeling- The Mesa framework|Utilizing Python for agent-Based modeling: The Mesa framework]]
- [[Design guidelines for agent based model visualization|Design guidelines for agent based model visualization]]
- [[MASON- A multiagent simulation environment|MASON: A multiagent simulation environment]]
- [[The Rust language|The Rust language]]
- [[Complex adaptive systems modeling with Repast Simphony|Complex adaptive systems modeling with Repast Simphony]]
- [[A lightweight formalism for reference lifetimes and borrowing in rust|A lightweight formalism for reference lifetimes and borrowing in rust]]
- [[SAFE- Simulation Automation Framework for Experiments|SAFE: Simulation Automation Framework for Experiments]]
- [[Improving execution speed of models implemented in NetLogo|Improving execution speed of models implemented in NetLogo]]
- [[Fear, behaviour, and the COVID-19 pandemic- A city-Scale agent-Based model using socio-Demographic and spatial map data|Fear, behaviour, and the COVID-19 pandemic: A city-Scale agent-Based model using socio-Demographic and spatial map data]]
- [[OpenMOLE, a workflow engine specifically tailored for the distributed exploration of simulation models|OpenMOLE, a workflow engine specifically tailored for the distributed exploration of simulation models]]
- [[FLAME GPU- Complex system simulation framework|FLAME GPU: Complex system simulation framework]]
- [[A survey on parallel and distributed multi-agent systems for high performance computing simulations|A survey on parallel and distributed multi-agent systems for high performance computing simulations]]
- [[Rust Doc Lang - Meet safe and unsafe|Rust Doc Lang - Meet safe and unsafe]]
- [[The nlrx R package- A next-generation framework for reproducible NetLogo model analyses|The nlrx R package: A next-generation framework for reproducible NetLogo model analyses]]
- [[An introduction to complex systems science and its applications|An introduction to complex systems science and its applications]]
- [[Finding Forms of Flocking- Evolutionary Search in ABM Parameter-Spaces|Finding Forms of Flocking: Evolutionary Search in ABM Parameter-Spaces]]
- [[GeoMason- Geospatial support for MASON|GeoMason: Geospatial support for MASON]]
- [[The explicit representation of context in agent-Based models of complex adaptive spatial systems|The explicit representation of context in agent-Based models of complex adaptive spatial systems]]
- [[R marries NetLogo- Introduction to the RNetLogo package|R marries NetLogo: Introduction to the RNetLogo package]]
- [[Software review- The ECJ toolkit|Software review: The ECJ toolkit]]
- [[NetLogo|NetLogo]]
- [[ConnectedScience- Learning biology through constructing and testing computational theories - An embodied modeling approach|ConnectedScience: Learning biology through constructing and testing computational theories - An embodied modeling approach]]
- [[Thinking like a wolf, a sheep, or a firefly- Learning biology through constructing and testing computational theories - An embodied modeling approach|Thinking like a wolf, a sheep, or a firefly: Learning biology through constructing and testing computational theories - An embodied modeling approach]]
- [[Agent-Based model for urban administration- A case study of bridge construction and its traffic dispersion effect|Agent-Based model for urban administration: A case study of bridge construction and its traffic dispersion effect]]
- [[A study of C-C++ code weaknesses on stack overflow|A study of C/C++ code weaknesses on stack overflow]]
- [[Replication of an agent-based model using the replication standard|Replication of an agent-based model using the replication standard]]

## Audit Log
- 2026-10-03: Independent full-source re-audit passed. Framework update order, tutorial, benchmark and calibration controls/outcomes and 50 references verified; printed density and speedup discrepancies remain explicit. `audit failed` removed after the pass.
- Audit invalidated (2026-09-30): auditor admitted clearing flags before completing independent source checks. A new independent audit is required.
- Strong source review (2026-09-30): Verified full published article; copied abstract from the inspected publisher HTML (which differs slightly from PDF phrasing) and confirmed 31 March 2024 date. Independent re-audit pending.
- Initial independent audit: failed on abstract fidelity or incomplete source verification; revisions made. Independent re-audit remains pending. See `vault/.automation/audit/next-forty-54-66-initial-2026-09-30.json`.

- WITHDRAWN audit claim (2026-09-30): previously reported PASS; source claims, current extraction, metadata, references and footnotes checked against the available primary source. See `vault/.automation/audit/remaining-audit-b-2026-09-30.json`.

## LLM Justification
[^r1]: The paper’s abstract, at https://www.jasss.org/27/2/4.html. The questions paraphrase the stated purpose, research scope, and reported approach.
[^r3]: Antelmi et al., §2 (krABMaga framework), §3 (Wolf, Sheep, and Grass implementation tutorial), and §5 (performance comparison and distributed calibration on AWS EC2). Full published text: https://www.jasss.org/27/2/4.html.
[^m1]: Antelmi et al., §2 (krABMaga architecture and safe Rust goals). Full published text: https://www.jasss.org/27/2/4.html.
[^m2]: Antelmi et al., §2 scheduler workflow and scheduling APIs; scheduler queue order and state/agent lifecycle hooks. Full published text: https://www.jasss.org/27/2/4.html.
[^m3]: Antelmi et al., §2 simulation fields and field-update semantics (double buffering; `lazy_update`, `update`, and unbuffered access). Full published text: https://www.jasss.org/27/2/4.html.
[^m4]: Antelmi et al., §3 Wolf, Sheep, and Grass tutorial, §§3.1–3.12 (movement, eating, reproduction, queued agent lifecycle and state update). Full published text: https://www.jasss.org/27/2/4.html.
[^m5]: Antelmi et al., §2 monitoring and high-performance model exploration/optimization APIs. Full published text: https://www.jasss.org/27/2/4.html.
[^m6]: Antelmi et al., §5 model simulation experiment and Figs. 15–16 (models, platforms, machine, scale, repetitions, runtime outcomes and memory constraints). Full published text: https://www.jasss.org/27/2/4.html.
[^m7]: Antelmi et al., §5 model calibration experiment (SIR network, transition probabilities, data window and simulation setting). Full published text: https://www.jasss.org/27/2/4.html.
[^m8]: Antelmi et al., §5 optimization strategy/results and Table 2 (population, repetitions, generations, evolutionary operators, execution count, wall time and speedup discrepancy). Full published text: https://www.jasss.org/27/2/4.html.
