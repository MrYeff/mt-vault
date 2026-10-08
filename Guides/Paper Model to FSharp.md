Extract the model into f#. The main goal is not running  the model but being able to read the code aside the paper to better understand how it all fits together.

Example: [[The Effect of People Recommenders on Echo Chambers and Polarization|PROD]]; code: `models/src/prod/`.

## Process

- Read the full paper, equations, algorithms and relevant appendices. Extracted notes are navigation, not evidence.
- Identify state, parameters, initialization, update rules, choices and stopping rules.
- Implement the core loop first; connect the paper's rules and variants.
- Check equations with small examples; check one complete run.
- Audit against the source. Fix discrepancies and re-audit fixes.

## Structure

Prod was imported succesfully. Folow the overall import aproach. dont blindly copy its structure

- `0_Framework.fs`: types and simulation entry point; update order and stopping rules.
	1. Type definitions
	2. Broadly Helper functions depending on these types. marked `internal`
	3. `prod` function: describes the core loop of the simulation. its arguments define the configuration axis also described in the paper. They define the other `X_file.fs` files
- `X.file.fs`
	- helper functions are `private`
	- each file provides variants for each argument
	- `1_Initialisation.fs`: different initialisation strategies for `world
	- `2_UpdateRules.fs`: different update rules for `update`
	- `3_Recomenders.fs`: different people recomender algorithms for `recommend`
- `Helpers.fs`: shared operations not supplied by libraries.
- `Checks.fsx`: write ur validation logic in here
- `Prod.fsx`: an entry point to the project showing a small example on how to compase the `prod` function from `0_Framework` with its parameters. gereneicaly this is there to show how to use the framework.

## Policies

- **Readability is Key**: code should be readable so avoid pointless indirection and optimisations that reduce clarity.
- **Source fidelity:** preserve equation structure, algorithm order, distributions and parameter meanings. Use readable names that map to the paper's symbols.
- **Contradictions:** record the conflicting equation, prose or reference code and which interpretation is implemented. if there are any.
- **Parameters:** expose actual model parameters. Keep implementation plumbing internal. Use constants for fixed values.
- **State:** prefer `Map<SomeId, X>` over `Array<X>` for entities. IDs are keys, not array positions. Use `Set<Id * Id>` for unweighted links. Arrays/matrices are appropriate for numerical calculations.
- **Comments:** use `///` for hover documentation of functions and types. Cite section, equation or algorithm numbers beside the implementation. Explain direction, units, ranges and non-obvious choices; avoid narrating obvious code.
- **Libraries:** prefer existing FSharp.Stats/FSharpPlus operations when their semantics match the paper. Keep model-specific logic explicit.
- **Visibility:** public functions are entry points and configurable rules; use `private` or `internal` for helpers.
- **Checks:** test equations, update order and a complete run. Do not silently add clamping, fallbacks or defensive rules absent from the source.
- **Audit:** distinguish faithful rules, implementation choices and unsupported parts. Build success alone does not establish fidelity.
