# Reference models

These modules reproduce selected behaviors from external infrastructure in
Lean. They remain executable comparison cases alongside the project's native
implementation. They are partial models, not complete implementations of the
referenced facilities.

| Module | Implemented scope |
| --- | --- |
| Ethereum | Account balances, nonces, ETH transfers, and rejected replays |
| Solana | Read/write account-access compatibility and a symmetry proof |
| ERC20 | Ordinary token transfers; no allowance, minting, or redemption |
| X402 | Payment requirements and integer amount decoding |
| A2A | Agent Card fields, interface selection, and task-state classification |

The [blockchain note](Ethereum/Note.mdx) explains the Ethereum and Solana cases
and reviews Bitcoin. Solana examples include contention on a shared fee payer;
the model does not execute programs or implement a scheduler. The Ethereum fee
example uses supplied gas and price; the transfer rule does not charge gas or
execute contracts.

The [payment note](X402/Note.mdx) also discusses AP2, Circle Gateway, and
Nevermined. Those are source studies without executable models. Keep source
versions, omissions, and correspondence obligations with each case.

[Foundation](../Foundation/README.md) supplies shared identifiers and quantities.
The project's [wallet policy](../Native/Wallet/README.md) and
[paid-task case](../Cases/PaidTask/Note.mdx) are separate. The latter composes
local wallet, payment, ledger, and task rules; it does not yet compose the x402
and A2A models into a protocol implementation.

For task lifecycle background, see A2A's
[Life of a task](https://a2a-protocol.org/latest/topics/life-of-a-task/), consulted
on 2026-10-08. The A2A note pins the specification used by the current model.

See the [architecture](../../docs/ARCHITECTURE.md#reference-models-and-common-specifications)
for comparison through common specifications. Run `lake build` from the
repository root to check all reference modules.
