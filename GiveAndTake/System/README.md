# System model

[Modules and interactions](Note.mdx) introduces the components and infrastructure
references. [A paid task](../PaidTask/Note.mdx#connect-the-modules) explains their
executable composition: `Config` fixes participants, wallet policy, and the
service; `State` holds the task, ledger, and pending approval. `step` runs one
action; `trace` records accepted states.

`Examples.lean` supplies the echo service and a 0.003 ETH payment, using the same
fixtures as `PaidTask`. No external protocols, wallets, or chain clients are called.
Run `lake build`, `lake exe demo`, and `lake env lean scripts/Audit.lean`.
