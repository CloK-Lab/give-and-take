# One paid call

Read [the learning note](Note.mdx) for a worked example, the modeling choices,
and the explanation of fund conservation. Its Lean source lives in this directory.

`Retry/` extends the accounting example with one approved purchase, a saved
receipt, and separate reply-loss and delivery actions. Its executable handler
and proofs use the same `PaidCall.run` payment interpreter. An invariant proves
that any finite trace commits at most once, preserves funds, and only delivers
the receipt for the approved purchase. A recovery theorem covers a lost reply
followed by a retry and successful delivery.

The case fixes one buyer, provider, asset, and authenticated client. Balance
changes and the saved receipt commit atomically in a local model. It does not
implement x402, signatures, external chain reconciliation, or a shared budget
across multiple purchases. `commits` counts model payments, not gas costs.

Definitions, specifications, execution, and verification live in separate files
under `Retry/`. `Examples.lean` supplies the trace used by the demo;
`Checks.lean` exercises rejection and boundary cases. Public theorems are audited
in `scripts/Audit.lean`.

From the repository root, run `lake build` and `lake exe demo`.
