# Solana account access

The [Blockchain infrastructure note](../Ethereum/Note.mdx#solanas-accounts-and-programs)
compares Solana with Bitcoin and Ethereum and presents this model.

The executable case asks whether two resolved transaction account lists conflict.
It studies `can_read_lock` and `can_write_lock` in Agave's
[`AccountLocks`](https://github.com/anza-xyz/agave/blob/39f386aadaf9a551eb690997e1d58769f165ea22/accounts-db/src/account_locks.rs).
The source was read on 2026-10-08. The public Solana documentation supplies the
account, instruction, fee, and transaction-lifetime explanations in the note.

`Model` stores read-only and writable addresses. `Spec` states the compatibility
condition; `Execution` decides it. `Examples` compares independent transfers
with transfers using a shared fee payer. `Checks` includes write/write,
read/write, and shared-read cases. `Verification` proves symmetry of the
compatibility relation.

Inputs stand for already resolved, validated account permissions, including the
fee payer and loaded addresses. This model does not validate a wire transaction,
execute a program, select a schedule, or establish consensus or throughput.
The source reference identifies the lock rule being studied; it is not a proof
of equivalence to the Rust implementation. Run `lake build` at the repository
root to check this case.
