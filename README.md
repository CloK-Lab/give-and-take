# Give and Take

Building formal models, specifications, and executable code in Lean to study
agent protocols, payments, and tokenized assets.

A [CloK](https://www.clok.tech/about) community project. We learn by reading
protocols, making assumptions explicit, implementing small models, and studying
their properties. Questions about incentives, strategic behavior, and AI safety
guide the work.

## Start here

The first case models the accounting for one paid service call: reserve a price,
then settle or refund. The demo runs the same Lean functions that the theorems
describe. It requires no wallet, network access, or real funds.

Requires Lean **4.34.0**, pinned in `lean-toolchain`; no external Lean packages.

```sh
lake build
lake exe demo
lake env lean scripts/Audit.lean
```

The library proves conservation for every successful action sequence, rejection
of further actions after settlement or refund, and restoration of available
balances after a funded reservation is refunded. Build-time examples exercise
successful payment, refund, insufficient funds, repeated settlement, and a
zero-price call.

This is an accounting model. It does not yet represent caller authentication,
service execution or quality, deadlines, fees, concurrent calls, or external
settlement. Its proofs do not establish those properties. Read the
[case guide](GiveAndTake/PaidCall/README.md) for the precise scope.

## Study topics

| Topic | Questions | Current material |
| --- | --- | --- |
| [Agent interaction](docs/topics/agent-interaction.md) | How are capabilities, requests, delegation, and results specified? | A2A reading notes and modeling questions |
| [Payments](docs/topics/payments.md) | What authorizes payment, and how do delivery and settlement relate? | x402 reading notes and the local paid-call case |
| [Tokenized assets](docs/topics/tokenized-assets.md) | What does a token represent, and what connects it to an external claim? | RWA reading notes and modeling questions |

The topic notes are starting points for study. No A2A or x402 implementation,
RWA backing mechanism, or game-theoretic safety result is claimed yet. A token
may be an internal accounting unit; a particular blockchain is not required.

## Organization

```text
GiveAndTake/
  PaidCall/
    Model.lean          States, actions, and accounting quantities
    Spec.lean           Properties to establish
    Execution.lean      Executable state transitions and replay
    Verification.lean   Proofs about that execution
    Checks.lean         Small concrete examples
docs/topics/            Reading notes, sources, and open questions
scripts/Audit.lean      Theorem assumption audit
Main.lean               Runnable demonstration
```

New cases can introduce multiple agents, nested calls, observations, strategies,
and utilities. Each should identify its assumptions and the question it answers.
Operational correctness, strategic incentives, and observed AI behavior require
their own statements and evidence.

See [CONTRIBUTING.md](CONTRIBUTING.md) to add a study or case.

Licensed under [Apache-2.0](LICENSE).
