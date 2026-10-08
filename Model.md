## Relationships

- *T1* correlates_with *T2*
	- intensity 
- *A1* thinks *Statement*

- if *A1* correlates_with *E1* → high chance to attend
- I think: *A1* correlates_with *T#GOOD* → i like *A1*
- *T1* correlates_with *T2* → They have something to do with each other

### Example

- I think Gabber-Night exists 
	- ❌ labels don't have any meaning (T1821 exists doesn't express anything)
- I think Gabber-Night → Gabber → Techno
	- `Gabber-Night correlates_with(0.9) Gabber 
	- `Techno correlates_with(0.9) Gabber 
- I like Bob // I think Bob is good
	- `Bob correlates_with(0.7) Good 
- I think Bob doesn't like me
	- `Bob thinks (Me correlates_with(-0.5) Good)
- I think Communism is good
	- `Communism correlates_with(0.9) Good 
- I think Bob thinks Communism is bad
	- `Bob thinks (Communism correlates_with(-0.9) Good)
- I plan to attend Gabber-Night
	- `Me correlates_with(0.7) Gabber-Night 
- I think Bob plans to attend Gabber-Night
	- `Bob correlates_with(-0.9) Gabber-Night

## World

Notation: [[Model Notation]].

```yml
World:
	agents: [Agent]
	events: [Event]
	topics: [Topic]

Agent:
	identity: TopicId
	hard_facts: ...
	in_think: [Thought]
	focus: [ThoughtId -> 0..1]

Thought:
	Correlation: 
		a: TopicId
		b: TopicId
		correlation: -1..1
		certainty: 0..1
	IndirectThought:
		thinker: AgentId
		thought: Thought
		certainty: 0..1

Event:
	identity: TopicId
	hard_facts: ...
```

## Simulation

- When I encounter another agent a Thought is selected
- Focused Thought change randomly over related topics
- I update my indirect_thought immediately after hearing the thought of my interlocutor
- if i think about a thought of a previous interlocutor the idea will diffuse into my thoughts based on my relationship to him
	- diffusion speed is controlled by agent genes: generaly, specificaly
- tripple correlations try to even out
- change is dominantly induced in regions with focus

## Operations

> how are thoughts moving?

- *interaction* if I meet A and we talk about a `T1 ~ T2` I learn `A -> T1 ~ T2` 
- *decay* some properties of thoughts decay over time (e.g. certainty - maybe sigmoid)
- *reflection* 
	- `T1 ~ T2`, `T2 ~ T3`, `T1 ~ T3` should be balanced
	- `T1 ~ T2`, `A -> T1 ~ T2`, `A ~ Trustworthy` should be balanced

## Parameters

- *correlation* (-1..1): how strongly does `A ~ B`
- *certainty* (0..1):  how sure am i about X

## Special Topics
> special topics are used to infer information about an agent or my perspective of an agent for the simulation

- *Good*: positive correlation means thinker thinks positively of this topic 
- *Trustworthy*: positive correlation means thinker thinks source is trustworthy
- *~Me*: positive correlation means i plan to atend an event

## Thought update

- high *certainty* → linear change to *certainty* weak shift in *correlation*
- low *certainty* → linear change to *certainty* strong shift in *correlation*


- high *certainty* + high *correlation* `T1 ≈ T2`, `T2 ≈ T3`  → `T1 ≈ T3`

### high certainty example

| relationship      | *correlation* | *certainty* |
| ----------------- | ------------- | ----------- |
| `T1 ~ T2`         | 0.4           | 0.9         |
| `A -> T1 ~ T2`    | -0.9          | 0.5 -> 0.9  |
| `A ~ Trustworthy` | 0.9           | 0.9         |
- all *correlation* barely moves
- all *certainty* slightly reduced

```
MIN_RATE = 0.01
MAX_RATE = 0.20
CERTAINTY_RATE = 0.05


fn update(
	current: Thought,            # T1 ~ T2
	incoming: IndirectThought, # A -> T1 ~ T2
	source_trust: Thought,       # A ~ Trustworthy
):

	# source_trust is my belief that the speaker is Trustworthy.
	# Unknown trust gives a neutral weight of 0.5.
	
	trust = 0.5 + 0.5 × source_trust.correlation × source_trust.certainty
	evidence = incoming.certainty  × incoming.thought.certainty × trust
	
	base_lr = MIN_RATE + (MAX_RATE − MIN_RATE) × (1 − current.certainty)
	lr = base_lr × evidence
	
	difference = abs(incoming.thought.correlation − current.correlation)
	certainty_change = CERTAINTY_RATE × evidence × (1 − current.certainty × difference)
	
	current.correlation += lr × (incoming.thought.correlation − current.correlation)
	current.certainty = clamp(current.certainty + certainty_change, 0, 1)
```

`incoming.certainty` is how sure the speaker is; `understanding` is how sure I am that I understood them. A credible disagreement lowers my certainty when `current.certainty × difference > 1`. Otherwise it raises certainty.
