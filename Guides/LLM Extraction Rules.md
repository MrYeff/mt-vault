This rules aim to ensure correctness, reproduceability and readability.

1. When information is not coppied instead transformed it has to be anotated using a comment like this:

```md 
## My Section
> XYZ extracted via LLM

Lorem ipsum dolorem ....
```

2. if the extraction is based on a described procedure it should also be referenced

```md 
## Model
> Model extracted via LLM acording to [[Model Notation]] 

Lorem ipsum dolorem ....
```

3. if required information is unavailable set the ⚠️-property to the apropriate error (e.g. ⚠️: - fulltext unavailable )
4. errors should be in this list:
	- not importet (default): import process was not preformed yet
	- not audited (default): imported but not proofread by independent audit agent
	- audit failed: apply if audit fails and add ## Audit Log to the bottom of the file (before ## LLM Justification)
	- fulltext unavailable: no accessible full text of the published paper
	- require reimport: paper was imported by a previous process and might have incomplete or faulty information 
5. if some step requires this information skip it entirely and mark it in ur note

```md 
## Model
> ⚠️ Model extraction skipped: full text unavailable; the abstract does not specify the model's rules.
```

6. each statement u create must be appended by a footnote linking to the LLM Justification section. For model claims, name the source section, equation, algorithm, table, or page. A citation alone is not enough: check that the passage supports the claim. Cite a notation or procedure block in the sentence introducing it.

```md 
## Text
- my statement[^r1]
  
## LLM Justification
[^r1]: ... 
```
7. before shortening a model, check: what it represents, who chooses each action, what each agent observes, update order, parameter values, control conditions, and measured outcomes. Do not hide a defining rule inside an unexplained helper function.
8. state what a simplification omits. If the paper's text and equations disagree, record both and flag the conflict; do not silently choose one.
9. extraction → independent audit → correction → independent re-audit. Use a cheap model for the first audit. The auditor must read the full text and check each claim against it, including missing mechanisms and conflicts between prose, equations, and algorithms. A valid template, references, and footnotes do not prove the claims are correct.
10. record failed audits and fixes in ## Audit Log. Keep `not audited` or `audit failed` until a re-audit passes. Store process details and import metadata in `vault/.automation`, not in the paper note.
11. use an expensive auditor when the cheap audit cannot resolve a source conflict, or when a model rule will directly determine the simulation design. Record what each auditor found; do not assume a more expensive audit is always necessary.
12. statements should be concise and readable. prefer: [[Model Notation]] > Bullet Points > text block
13. when u have a 