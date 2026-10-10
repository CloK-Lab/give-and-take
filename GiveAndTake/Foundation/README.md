# Shared definitions

`Network.lean`, `Asset.lean`, and `Identity.lean` define network, account, asset,
amount, and agent identifiers. They represent identities supplied to the model;
they do not authenticate principals or validate real network addresses.

[Quantities](Quantities/Note.mdx) defines nonces, asset-indexed gas pricing,
power, duration, and energy. Its executable operations advance a nonce, multiply
supplied gas by a unit price, and calculate energy at constant power. Its proofs
cover nonce progression and fee aggregation at a fixed price. Task measurement,
electricity pricing, and service value are outside this model.

This directory has no imports from the reference models, native implementation,
or cases. The ETH fee example used by the quantities note lives in
`../Reference/Ethereum/Checks.lean`; the note includes its source directly.
Run `lake build` and `lake env lean scripts/Audit.lean` from the repository root.
