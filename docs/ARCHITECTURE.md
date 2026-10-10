# Chain and stablecoin architecture

ν-DSI develops a verified decentralized superintelligence (DSI) system
for human-agent coordination and physical and computational resource allocation,
as described in the [overview](Overview.mdx). This document specifies its chain
and monetary subsystem. The planned implementation uses Lean for the chain,
stablecoin mechanisms, and agent protocols. External projects supply reference
designs and comparison cases. The implementation must execute the project's own
rules without relying on external chains, issued stablecoins, payment
facilitators, or their SDKs.

This contributor document specifies the development target and records what
exists. The chain and stablecoin described below are planned work. The first
milestone is one local node that records transfers, mints and redeems against
test reserves, and restores the same state after restart.

## Current implementation

| Component | What exists |
| --- | --- |
| Shared definitions | Network, asset, account, integer amount, and nonce types |
| Ledger studies | Ethereum balance/nonce transfers, token transfers, and Solana account-access compatibility |
| Wallet and tasks | Local spending checks and an executable paid echo task |
| Payment retry | A saved-receipt model with at-most-once payment and fund-conservation proofs under atomic local accounting |
| Chain node | Not implemented: no block production, node service, or persistent chain history |
| Stablecoin mechanism | Not implemented: no reserve deposits, issuance, or redemption |
| Task acceptance | Not implemented: completion currently records a provider's result without judging quality |

`lake exe demo` runs the local examples. The Base Sepolia probe under
`tools/reference/` is an optional external observation and does not contribute
to the native runtime. Its successful output establishes neither a project
chain nor a stablecoin implementation.

## Reference models and common specifications

Develop two bodies of executable Lean code in parallel: reference models of
selected external facilities, and the project's own chain and protocols. Keep
the existing reference models and their proofs. They provide concrete designs
and comparison cases as the native implementation develops. A common
specification states the behavior being compared independently of either body
of code.

| Part | Role in a comparison |
| --- | --- |
| Reference composition | Execute a selected combination of modeled protocols, with pinned versions, explicit adapters, and stated omissions |
| Common specification | Define inputs, permitted transitions, observable outcomes, and environment assumptions for one concrete case |
| Native implementation | Execute the project's own rules and relate their behavior to the same specification |

The current studies implement only parts of the reference facilities. For
example, the x402 code represents payment requirements and decodes amounts; it
does not execute authorization and settlement. `PaidTask` and `System` compose
local payment operations, not a complete x402/A2A stack. AP2, Gateway, and
Nevermined currently have source notes rather than executable models. A
reference composition and its correspondence proofs remain implementation work.
Select facilities that actually participate in a case; do not assume that every
referenced project is a successive stage in one protocol.

For each comparison, define input mappings and observations such as account
balances, authorized terms, committed payments, receipts, and rejection reasons.
Relate initial states and declare how account identities and integer asset units
correspond. Mapping test tokens to abstract units does not identify their
economic value or external backing. Internal message or block-processing steps
may leave the abstract state unchanged, but intermediate payment states and
failures visible to a participant must be included when they affect the contract.

The first proof target is refinement: every modeled execution, under the stated
assumptions, maps to an execution permitted by the common specification. Prove
initial-state correspondence and preservation of the state relation across
execution steps, allowing multiple internal steps where necessary. Keep the
abstract transition rules separate from the interpreters used by the demos.

If both implementations refine a specification, they both satisfy its safety
requirements. This does not establish identical behavior: an implementation
that never pays can satisfy an at-most-once property. A claim of behavioral
equivalence requires matching sets of observable behaviors in both directions
for corresponding inputs and initial states. State how termination, rejection,
and divergence are observed. Claims about eventual payment or recovery also
require progress proofs under explicit delivery, scheduling, and availability
assumptions; they do not follow from finite-trace safety alone.

Start the comparison when the native token transfer works. Relate
`Reference/ERC20/Execution.lean` and the native issued-token transfer to a
small transfer specification: for distinct valid accounts, sufficient funds
produce the exact debit and credit, preserve other balances and total supply,
and insufficient funds reject the transfer without changing state. Use matching
integer units and a fee-free, authorized context. This compares the transfer
operation; it makes no claim about signatures, issuance, redemption, fees, or
chain consensus. It requires no generic protocol framework or empty comparison
modules in advance.

Later payment comparisons can include authorization, settlement, lost replies,
and retries. Specify the queues, adapters, receipt storage, and ordering rules
that connect the reference components: properties of components alone do not
establish properties of their composition. In particular, do not attribute the
current retry model's atomic accounting-and-receipt assumption to an external
payment service without evidence.

A proof comparing Lean programs establishes a relation between those programs.
Relating a reference model to deployed infrastructure requires separate
specification mappings, source correspondence, and conformance evidence with
their own limits. Neither that relation nor functional equivalence establishes
equal throughput, cryptographic security, service quality, or monetary stability.
Those are separate claims with separate assumptions and evidence.

## Source layout

The existing modules have four locations:

```text
VDSI/
  Foundation/
    Network.lean
    Asset.lean
    Identity.lean
    Quantities/
  Reference/
    Ethereum/
    Solana/
    ERC20/
    X402/
    A2A/
  Native/
    Wallet/
  Cases/
    PaidCall/
      Retry/
    PaidTask/
      System/
```

`Foundation/` contains shared definitions and their operations and proofs.
`Reference/` contains executable models of selected external designs.
`Native/Wallet/` contains the project's own spending policy, currently without
key management or signing. `Cases/` runs concrete scenarios; `PaidTask/System/`
composes one task's authorization, settlement, and service execution. Its ETH
fixtures are part of the case, not a dependency of the native wallet module.

Add `Native/Chain/`, `Native/Stablecoin/`, and `Native/Node/` as the first
milestone acquires executable code. Add `Specs/Transfer/` for the common transfer
specification and `Comparisons/Transfer/` for the two observation mappings and
their correspondence proofs when both implementations can be compared. These
directories are not present yet. Agent payment modules follow concrete cases;
do not create placeholder protocol or experiment frameworks.

Imports follow these boundaries, including in checks:

- `Foundation/` does not import other project layers.
- `Reference/` and `Native/` use the foundation and their own modules, without
  importing each other, cases, or comparisons.
- `Specs/` uses foundation definitions independently of either implementation.
- `Comparisons/` may import the common specification and both implementations.
- `Cases/` may combine modules from the other layers for a concrete scenario.

Each module keeps its own `Model.lean`, `Spec.lean`, `Execution.lean`,
`Verification.lean`, and `Checks.lean` as needed, with `Examples.lean` for
reusable fixtures and `Note.mdx` for its explanation. Common comparison
specifications do not replace these local specifications. Execution never
imports its verification module.

The library facade exports definitions and proofs. Lake builds every module
through the `VDSI.*` glob, so checks remain part of the default build
without becoming facade imports. `Main.lean` imports and runs the concrete
cases. The axiom audit uses the exported theorem names.

Keep the website's Preliminaries and Examples reading groups and existing
slugs. They are independent of the source directories. Update relative note
links, source excerpts, and repository links whenever a module moves.

## Chain execution

Start with one designated block producer on one machine. This defines a useful
experimental execution environment with an explicit trust assumption. A
multi-node consensus protocol, fork choice, and fault tolerance remain separate
work; multiple copies of a process would not establish those properties.

The implementation should have three connected parts:

| Part | Responsibility |
| --- | --- |
| Chain core | Validate transactions and blocks, apply deterministic state transitions, and produce receipts |
| Stablecoin module | Apply reserve deposits, issuance, transfers, and redemption within the same chain state |
| Node | Accept requests, order transactions, persist accepted blocks, replay history, and answer queries |

A client submits a transaction to the node. The node invokes the Lean block
executor, persists the accepted block, and returns its receipt. Replay invokes
that same executor from the recorded genesis state. The proofs must concern
the executable definitions used by both paths.

Use finite account and asset collections so the state can be serialized,
replayed, and summed. The existing function-valued study ledgers need an
explicit representation change before they can serve this purpose. Give the
chain its own identity and asset units; retain Ethereum-specific types in their
reference cases.

A transaction binds the chain and protocol version, sender, nonce, and exact
operation. Its authorization must cover that complete encoding. A block binds
its height, predecessor, ordered transactions, and resulting state commitment.
Define canonical encoding before transaction IDs, signatures, and block hashes.
Reject incorrect nonces, unauthorized actions, insufficient balances, and
invalid parent links. The initial block rule should reject an invalid block
without partially committing it.

Keep wall-clock reads, randomness, and network responses outside deterministic
execution. Any such input that affects a transition must have explicit
validation rules and be recorded for replay. Use integer quantities with
declared units and check wire-format bounds during decoding.

Cryptographic operations are also implementation work. Implement selected
published algorithms in Lean and check their standard test vectors; specify
their security assumptions separately from functional correctness. Ordinary
language hashes and fixture identities cannot stand in for cryptographic
commitments or authenticated transactions. A trusted in-process fixture can
support early execution tests, but it cannot establish signed-node readiness.

## First stablecoin case

Use a unit-for-unit reserve mechanism as the initial experimental case. Let
`R` be a test reserve asset allocated at genesis and `S` be the issued token.
The initial case has no fees, interest, reserve yield, or external price feed.
This is a baseline for studying issuance and redemption, not a claim about a
dollar peg or a decision about all later monetary mechanisms.

For a valid positive integer amount, the operations are:

| Operation | State change |
| --- | --- |
| Deposit and mint | Move `n` units of `R` from the depositor into the module's reserve and issue `n` units of `S` to that depositor |
| Transfer | Move `n` units of `S` between accounts without changing its supply or the reserve |
| Burn and redeem | Burn `n` units of `S` from its current holder and release `n` units of `R` to that holder |

Each operation is one checked chain transition. Authorization, balances, and
nonce validation happen before any state update. Redemption belongs to the
current token holder, including someone who received the token by transfer.
The reserve is controlled by the module's rules; ordinary transfers cannot
withdraw its backing or mint either asset.

Starting from a valid genesis allocation, prove that the reserve equals the
outstanding `S` supply, that supply equals the sum of holder balances, and the
total quantity of `R` in wallets and the reserve remains its genesis quantity.
State the one-to-one conversion between these distinct asset units explicitly.
This initial case has no authority that can issue unbacked `S`.

The concrete milestone trace is: Alice deposits 100 units of `R`, receives 100
units of `S`, transfers 30 to Bob, and Bob redeems 30. Alice then holds 70 `S`,
Bob has received 30 `R`, and the reserve and `S` supply are both 70 units under
the specified conversion. Persist and replay that history after a node restart.

The test reserve has no external dollar backing. Accounting invariants alone
do not establish a market price, off-chain reserves, or a redemption service
outside this chain. Collateral prices, liquidations, and market participants
require their own concrete cases when those mechanisms are introduced.

## Node storage and interfaces

Write the node, transaction encoding, client commands, and persistence logic in
Lean using its standard IO facilities. Keep Node.js and Python tooling confined
to documentation and reference studies. The Lean compiler, runtime, operating
system, and IO behavior remain explicit execution dependencies and proof
boundaries.

Use an append-only block history with versioned framing and integrity checks.
Record genesis, including the chain identity and initial allocation. Rebuild
state by validating and replaying the accepted history; a snapshot is an
optimization whose state must agree with that history.

Specify how a complete block becomes committed and which storage operation
makes it durable before acknowledging it. Test interrupted writes and crashes
at that boundary. Distinguish an incomplete uncommitted tail from corruption of
committed history. A process-restart test does not establish recovery from
power loss; document and test the durability contract before claiming it.

Serialize state changes in the first node. Resubmitting the same signed
transaction should return its existing receipt without another debit. Persist
the transaction identity and receipt with the state change. A lost response
must not cause the client to construct a fresh transaction with a new nonce.

The planned interfaces submit transactions and query their receipts, account
balances, supply, reserve balances, and blocks. Implement a Lean command-line
client first, then a Lean network service when the local persistence path works.
These interfaces and commands do not exist yet. Keep local node data under
`.local/`, which is excluded from Git.

## Agent payments and proof boundaries

After the monetary operations work, express wallet authority and agent payment
rules as transactions on this chain. Extend the existing local payment cases
with actual chain receipts and durable purchase identifiers. Budget reservations
must account for concurrent purchases. Service delivery, acceptance evidence,
and payment settlement remain distinct states.

For delegated work, specify request, task, result, and retry identities, the
authority delegated to another agent, and the information each participant can
observe. Beyond the current single-purchase case, open modeling questions include
liquidity requirements for nested calls and the incentive effects of charging
per call, per unit of work, or per accepted result. Local rule compliance alone
does not establish progress of the composed system.

A2A, x402, AP2, PASS, Gateway, and Nevermined are references for comparing
semantics and failure cases. Implement the project's own messages and execution
rules in Lean. Any future compatibility claim requires a mapping to a pinned
specification and separate conformance evidence; no external SDK is the runtime
foundation.

The current retry proof assumes atomic local accounting and receipt storage.
Relate a new chain implementation to those assumptions through its actual
execution and persistence behavior. Do not infer verified persistence,
consensus, service quality, or economic stability from that proof.

## Implementation order

Keep the first milestone fixed: the single-node reserve, mint, transfer, and
redemption trace survives restart. Develop it in the following order:

1. Define and execute the chain state, transactions, and blocks; prove the
   chosen transition invariants using concrete fixtures.
2. Add the reserve and redemption operations and their accounting proofs.
3. Implement canonical encoding, cryptographic authorization, and a persistent
   node and client; test the complete trace and rejection paths.

Keep each case's definitions, specifications, execution, verification, checks,
and note together. Add `VDSI/Native/Chain/`,
`VDSI/Native/Stablecoin/`, and `VDSI/Native/Node/` only as they
acquire working implementations. Reuse shared
types where appropriate and keep reference models identifiable. Create no empty
framework modules or commands that merely print a planned workflow.

Run the Lean build, demo, and axiom audit for each change. Add recovery and
serialization tests at the IO boundary. The first version targets one local
writer; measure block execution and replay before setting throughput targets.
Revisit storage and scheduling when measured workloads require it. Agent
payment cases and multi-node consensus are subsequent milestones, each with
their own executable examples, assumptions, and verification obligations.
