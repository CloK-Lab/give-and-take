# A paid task

[Learning note](Note.mdx): a wallet authorizes 0.003 ETH for an echo task, a local
ledger updates balances in wei, and the provider returns the input. The model
omits gas and network execution. It does not implement the x402 EVM scheme.

`Spec.lean` states authorization and settlement conditions. `Execution.lean`
implements them. `Examples.lean` runs the task and checks accepted and rejected
paths. `../System/` composes these operations into the configuration, state, and
actions described in the note. Run `lake build` and `lake exe demo` from the
repository root.
