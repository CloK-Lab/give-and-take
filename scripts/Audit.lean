import GiveAndTake

-- Fail if a theorem acquires a different axiom footprint.
/-- info: 'GiveAndTake.PaidCall.execute_preservesFunds' depends on axioms: [propext, Quot.sound] -/
#guard_msgs in
#print axioms GiveAndTake.PaidCall.execute_preservesFunds

/-- info: 'GiveAndTake.PaidCall.run_preservesFunds' depends on axioms: [propext, Quot.sound] -/
#guard_msgs in
#print axioms GiveAndTake.PaidCall.run_preservesFunds

/-- info: 'GiveAndTake.PaidCall.terminal_rejects' depends on axioms: [propext] -/
#guard_msgs in
#print axioms GiveAndTake.PaidCall.terminal_rejects

/-- info: 'GiveAndTake.PaidCall.reserve_refund' depends on axioms: [propext, Quot.sound] -/
#guard_msgs in
#print axioms GiveAndTake.PaidCall.reserve_refund

/-- info: 'GiveAndTake.Preliminaries.Quantities.nonce_next_ne' does not depend on any axioms -/
#guard_msgs in
#print axioms GiveAndTake.Preliminaries.Quantities.nonce_next_ne

/-- info: 'GiveAndTake.Preliminaries.Quantities.fee_add' depends on axioms: [propext] -/
#guard_msgs in
#print axioms GiveAndTake.Preliminaries.Quantities.fee_add

/-- info: 'GiveAndTake.Preliminaries.Solana.compatible_symm' does not depend on any axioms -/
#guard_msgs in
#print axioms GiveAndTake.Preliminaries.Solana.compatible_symm
