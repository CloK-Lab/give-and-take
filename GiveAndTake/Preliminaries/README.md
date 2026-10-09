# Preliminaries

[Modules and interactions](../System/Note.mdx) introduces the environment of an
on-chain agent economy. [Quantities and units](Quantities/Note.mdx) supplies
shared definitions for energy, time, amounts, nonces, and execution fees. The
source studies then cover Ethereum, ERC-20, wallet authority, x402, and A2A.
Each directory contains its source reading, model, and executable checks.
The Ethereum study includes an ETH transfer rule over balances and nonces,
with examples of successful transfers and rejected replays.
`Quantities/` defines the nonce type used by those accounts, asset-indexed gas
pricing, and a constant-power energy calculation. Energy is a resource and a
cost input for the agent economy. The current implementation computes energy
from supplied power and duration; task-level measurement, electricity pricing,
and service value are not yet executable parts of the model. Gas usage and price
are supplied inputs; charging fees and executing contracts remain outside the
transfer rule. Its proofs cover nonce progression and fee aggregation at a
fixed price.
`Network.lean`, `Asset.lean`, and `Identity.lean` supply shared identifiers.

The combined case lives in [PaidTask](../PaidTask/Note.mdx).
Run `lake build` from the repository root to check every module.
