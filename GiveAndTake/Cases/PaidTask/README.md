# A paid task

[Learning note](Note.mdx): a wallet authorizes 0.003 ETH for an echo task, a local
ledger updates balances in wei, and the provider returns the input. The model
omits gas and network execution. It does not implement the x402 EVM scheme.

`Spec.lean` states authorization and settlement conditions. `Execution.lean`
implements them. `Examples.lean` runs the task and checks accepted and rejected
paths.

`System/` composes the operations: `Config` fixes participants, wallet policy,
and the service; `State` holds the task, ledger, and pending approval. `step`
runs one action and `trace` records accepted states. Its examples reuse the
paid-task fixtures; no external protocols, wallets, or chain clients are called.
[Modules and interactions](System/Note.mdx) introduces the components, and
[the case note](Note.mdx#connect-the-modules) explains their execution.

Run `lake build`, `lake exe demo`, and `lake env lean scripts/Audit.lean` from
the repository root.
