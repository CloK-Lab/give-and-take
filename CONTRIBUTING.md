# Contributing

ν-DSI grows through shared study. Contributions can start with a precise
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
5. Explain what the result establishes and how to reproduce it.

Use English for project documentation and code comments. Conversation and
discussion can use the participants' preferred language.

## Structure and evidence

Keep shared definitions in `VDSI/Foundation/`, external facility models
in `Reference/`, the project's implementations in `Native/`, and executable
scenarios in `Cases/`. Keep each module's model, specification, execution,
verification, checks, and note together. Execution must not import verification.
Extract shared abstractions when multiple concrete cases need them.

`Foundation/` must not import the other project layers. `Reference/` and
`Native/` must not import each other or `Cases/`. Apply these boundaries to
checks as well as execution; place cross-layer fixtures in a case. Future
`Specs/` may depend on `Foundation/`; `Comparisons/` may import both
implementations and the common specification. Keep module-specific specifications
and proofs beside their implementations. Create the future directories only
with substantive code.

Implement the chain, stablecoin mechanisms, wallet and payment rules, and agent
protocols in Lean. Study external systems for their definitions and design
choices; the project runtime must execute its own rules without depending on
their chains, issued currencies, hosted services, or SDKs. Follow the scope and
implementation order in the [architecture](docs/ARCHITECTURE.md).

Keep protocol comparisons and external observations separate from runtime code.
Declare compiler, runtime, operating-system, and IO assumptions alongside the
proof boundaries. Writing a component in Lean does not itself verify it.

Preserve executable reference models while developing the native system. For a
comparison, select a concrete operation or protocol composition, pin its source
versions, and state a common specification independently of both implementations.
Define how each implementation's inputs, states, and outcomes map to that
specification. Prove refinement before claiming equivalence, and state which
observable behaviors must match in both directions. Shared invariants alone do
not establish equivalence. A correspondence between Lean models still needs
separate evidence relating each reference model to the external system.

Write the explanation in the module's `Note.mdx` beside its code. Include
Lean declarations directly from the source files. Reading notes belong in
`docs/topics/`; `clok.json` supplies page discovery and project metadata. See the
[notebook guide](docs/README.md) for authoring and previewing documentation.

A runtime example is evidence about its inputs. A theorem establishes its stated
property under its hypotheses. Protocol conformance requires an explicit mapping
to a pinned specification. External services, facts, and non-Lean implementations
need their own correspondence arguments.

For strategic claims, define utilities, information, allowed deviations, and
environment assumptions. Record SI-generated behavior as reproducible traces;
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
The library's `VDSI.*` Lake glob builds all modules, including checks and
examples. `VDSI.lean` exports definitions and proofs without importing
test fixtures; the demo imports its concrete cases directly.
For changes to the optional reference probe, run `npm run test:reference-chain`.
Its tests use mocked responses. Live `npm run check:reference-chain` is a
read-only observation of an external network and is not required by CI or the
project runtime.

For documentation changes, install dependencies once with `npm ci`, then run
`npm run build`. Inspect changed pages locally with `npm run dev`, including
navigation, source excerpts, and phone-width layout.
