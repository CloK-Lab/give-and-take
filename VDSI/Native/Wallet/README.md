# Spending policy

`Model.lean` defines the project's wallet policy and a spending request.
`Spec.lean` defines the decidable `CanSpend` check over the actor, payer, network,
asset, per-call limit, and permitted recipient. `Checks.lean` uses symbolic local
identities and integer token units. It imports no reference infrastructure.

This is a spending policy, not a complete wallet with keys, signatures, custody,
or an aggregate budget. [The note](Note.mdx) discusses PASS as a reference; the
code here defines the project's own policy. The
[paid-task case](../../Cases/PaidTask/Note.mdx) connects it to local settlement.
Run `lake build` from the repository root to check the module and its cases.
