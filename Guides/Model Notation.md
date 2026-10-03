
## Type definition
this is a *pseudolang* meaning its goal is not to be executable nor acurate so rules are there for consistency but can be extended if needed. try sticking to this as close as posible.
```yml
MyStruct:
	field_1: u32
	field_2: str
	field_3: bool
	field_4: 0..1 # if range is specified prefer over using type  
	field_6: str? # optional str
	field_7: () # unit type, baseclass of all types
	field_8: 0.. # ranges can be unbounded  
	field_9: Bob | Alice | Kevin # onof can be represented like this 

MyStruct2: MyStruct # structs can inherit other structs
	field_5: ... # information can be ommited

MyEnum:
	Option1:
		field_1: ...
	Option2: MyStruct
	OptionThatIsAnEnum:
		Option1: ...
		Option2: ...
		Option3
		Option4
		
MyStruct3:
	field_1: InnerType # structs and enums can be defined inline
		field_1: ...
	field_2:  # structs can be defined anon inline
		field_1: ...
	field_3:  # enums can be defined anon inline
		Variant1: ...
		Variant2: ...
		
MyStruct4:
	arr_field: [f32]
	automap_field: [MyStruct2] # defines MyStruct2Id. use deeper in hirarchy
	map_field: [MyStruct2Id -> MyStruct2]
	

GenericType(X): # parameters can be types
	inner: X
	
MyStruct5:
	field_1: GenericType(f32)
	
MyRange(lo, hi): # parameters can be values too
	val: lo..hi
```
```
CONSTANT_A = 32.0
CONSTANT_B = MyStruct5 : field_1: inner: 2.0 

add(a: f32, b:f32) -> f32: # if no return ommit "-> type" 
	c = a + b
	out = c # out is the return parameter

ommited_impl(
	a: MyStruct5, 
	b: GenericType(u32)
): ...

mut_param(
	mut world: World
): ...

```
## Further Notes
- types can be used before definition
- go from big constructs to inner `World` > `Agent` > `AgentThought` > ...
- prefer using `World` as the first type if reasonable
- types should preferably be in a ```yml``` block (for better highlighting)
- procedures should preferably be in an empty ``` ```  block 
- try keeping type names short
- prefer using `sim_step` or `sim_loop` as the rentry point if reasonable
- go from big constructs to inner also applied to functions `sim_loop` > `sim_step` > ...
- wordwrap is pain so keep lines short
- use line breaks and empty lines to make it more readable
- for longer functions put 1 empty line after the function head
- 2 empty lines between multiple function definitions
- break parameters up over multiple lines unless if they are only single letter parameters
- prefer using `CONSTANTS` instead of inline number
- feel free to halucinate helper functions that all programmers know (array functions, filter ...)
## Examples

Each example stands on its own.

### 1. Opinion exchange

Agents have opinions and trust. An interaction changes the listener's
opinion. The influence rule is illustrative.

```yml
World:
	agents: [Agent]

Agent:
	opinion: -1..1
	trust: [AgentId -> 0..1]

Interaction:
	speaker: AgentId
	listener: AgentId
```

```
MAX_INFLUENCE = 0.2

sim_step(
	mut world: World,
	interaction: Interaction
):
	speaker = world.agents[interaction.speaker]
	listener = world.agents[interaction.listener]
	weight = influence(listener, interaction.speaker)

	new_opinion = shift(
		listener.opinion,
		speaker.opinion,
		weight,
	)
	world.agents[interaction.listener].opinion = new_opinion


influence(
	listener: Agent,
	speaker: AgentId
) -> 0..1:
	out = MAX_INFLUENCE * listener.trust[speaker]


shift(
	current: -1..1,
	heard: -1..1,
	weight: 0..1
) -> -1..1:
	out = current + weight * (heard - current)
```

### 2. Relational events

The core model stores an ordered action history. Its generic parameter
selects which effects determine the next action. This is the event-order
form of [[4. A Relational Event Framework for Social Action]].

```yml
World(Effects):
	actors: [Actor]
	history: [Action]
	effects: Effects

Actor:
	label: str

Action:
	sender: ActorId
	receiver: ActorId
```

Each configuration supplies `log_rate`. `possible_actions` excludes
self-contact. `recent_reply` returns the inverse recency rank of the
receiver among actors who contacted the sender (zero if absent).

```
sim_step(
	mut world: World(Effects)
):
	probabilities = next_action(world)
	chosen = sample(probabilities)
	world.history.push(chosen)

next_action(
	world: World(Effects)
) -> [Action -> 0..1]:

	for action in possible_actions(world.actors):
		rates[action] = rate(world, action)
		
	out = normalize(rates)

rate(
	world: World(Effects),
	action: Action
) -> 0..:

	score = log_rate(world.effects, action, world.history)
	out = exp(score)
```

#### Variant: recent replies

```yml
Recency:
	reply_weight: f64

RecencyWorld: World(Recency)
```

```
log_rate(
	effects: Recency,
	action: Action,
	history: [Action],
) -> f64:

	out = effects.reply_weight * recent_reply(action, history)
```

#### Variant: recent replies and actor participation

```yml
RecencyParticipation:
	reply_weight: f64
	participation: [ActorId -> f64]

ParticipationWorld: World(RecencyParticipation)
```

```
log_rate(
	effects: RecencyParticipation,
	action: Action,
	history: [Action],
) -> f64:

	reply = effects.reply_weight * recent_reply(action, history)
	sender = effects.participation[action.sender]
	receiver = effects.participation[action.receiver]
	out = reply + sender + receiver
```

### 3. Predator and prey

A continuous population model. `sim_step` advances it by `dt` using
a simple Euler approximation.

```yml
World:
	prey: 0..
	predators: 0..
	rates: Rates

Rates:
	prey_birth: 0..
	predation: 0..
	predator_growth: 0..
	predator_death: 0..
```

```
MIN_POPULATION = 0

sim_step(
	mut world: World,
	dt: 0..
) -> ():

	prey_eaten = eaten(world)
	prey_births = world.rates.prey_birth * world.prey
	predator_births = world.rates.predator_growth * prey_eaten
	predator_deaths = world.rates.predator_death * world.predators

	next_prey = world.prey + dt * (prey_births - prey_eaten)
	next_predators = world.predators + dt * (
		predator_births - predator_deaths
	)

	world.prey = max(MIN_POPULATION, next_prey)
	world.predators = max(MIN_POPULATION, next_predators)

eaten(
	world: World
) -> 0..:

	out = world.rates.predation * world.prey * world.predators
```
