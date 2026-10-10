# External reference tools

These tools collect observations for protocol comparisons. The project's Lean
chain, stablecoin, and agent implementations do not depend on them.

## Base Sepolia observation

With Node.js 22.12 or newer, run from the repository root:

```sh
npm run check:reference-chain
```

The probe reads the chain ID, contract code, and decimal precision at the
configured USDC address. To inspect a balance, replace the placeholder with a
public EVM address:

```sh
npm run check:reference-chain -- --address 0xYOUR_PUBLIC_ADDRESS
```

This command was previously named `check:chain`. Its output now identifies the
observation as `external-reference`. It requires no private key and submits no
transaction. `GIVE_AND_TAKE_RPC_URL` selects an alternative Base Sepolia RPC.

Configuration sources, checked on 2026-10-09, are the
[Base network reference](https://docs.base.org/get-started/connect-to-base) and
[Circle contract registry](https://developers.circle.com/stablecoins/usdc-contract-addresses).
Test USDC has no financial value. The report depends on the RPC provider and
does not verify finality, contract correctness, or reserve backing. The token
reads use one block number, with a final check that its reported hash has not
changed.

Run the offline probe tests with `npm run test:reference-chain`. These tests
make no network requests.
