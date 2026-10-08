# Contributing

Give and Take grows through shared study. Contributions can start with a precise
question, a source reading, a model, an executable example, a counterexample, or
a theorem. Focus on one question, explain it through a concrete example, and
keep the change small enough to study together. Improve existing explanations
before opening more topics.

## A useful contribution

1. Describe the question and cite the relevant source, including its version
   or retrieval date when its meaning can change.
2. State the participants, observations, actions, units, and assumptions.
3. Define the model and executable behavior in Lean. Keep IO at the boundary.
4. State desired properties separately from the implementation. Include rejection
   and failure behavior where relevant.
5. Explain what the result establishes, what remains open, and how to reproduce it.

Use English for project documentation and code comments. Conversation and
discussion can use the participants' preferred language.

## Structure and evidence

Keep a case together under `GiveAndTake/<Case>/`. Separate model definitions,
specifications, execution, and proofs; execution must not import verification.
Extract shared abstractions when multiple concrete cases need them.

Write the explanation in `GiveAndTake/<Case>/Note.mdx` beside its code. Include
Lean declarations directly from the source files. Reading notes belong in
`docs/topics/`; `clok.json` supplies page discovery and project metadata. See the
[notebook guide](docs/README.md) for authoring and previewing documentation.

A runtime example is evidence about its inputs. A theorem establishes its stated
property under its hypotheses. Protocol conformance requires an explicit mapping
to a pinned specification. External services, facts, and non-Lean implementations
need their own correspondence arguments.

For strategic claims, define utilities, information, allowed deviations, and
environment assumptions. Record AI-generated behavior as reproducible traces;
one trace is not a theorem about every possible agent policy.

Do not use `sorry`, `admit`, custom axioms, or `native_decide` to complete proofs.
Leave unfinished claims in a written list of open questions. Add new public
theorems to the axiom audit.

## Checks

```sh
lake build
lake exe demo
lake env lean scripts/Audit.lean
```

Keep the toolchain pinned and add dependencies only when a concrete case needs
them. Update source notes and the README when the implemented scope changes.

For documentation changes, install dependencies once with `npm ci`, then run
`npm run build`. Inspect changed pages locally with `npm run dev`, including
navigation, source excerpts, and phone-width layout.
