import GiveAndTake

-- Fail if a theorem acquires a different axiom footprint.
/-- info: 'GiveAndTake.Cases.PaidCall.execute_preservesFunds' depends on axioms: [propext, Quot.sound] -/
#guard_msgs in
#print axioms GiveAndTake.Cases.PaidCall.execute_preservesFunds

/-- info: 'GiveAndTake.Cases.PaidCall.run_preservesFunds' depends on axioms: [propext, Quot.sound] -/
#guard_msgs in
#print axioms GiveAndTake.Cases.PaidCall.run_preservesFunds

/-- info: 'GiveAndTake.Cases.PaidCall.terminal_rejects' depends on axioms: [propext] -/
#guard_msgs in
#print axioms GiveAndTake.Cases.PaidCall.terminal_rejects

/-- info: 'GiveAndTake.Cases.PaidCall.reserve_refund' depends on axioms: [propext, Quot.sound] -/
#guard_msgs in
#print axioms GiveAndTake.Cases.PaidCall.reserve_refund

/-- info: 'GiveAndTake.Foundation.Quantities.nonce_next_ne' does not depend on any axioms -/
#guard_msgs in
#print axioms GiveAndTake.Foundation.Quantities.nonce_next_ne

/-- info: 'GiveAndTake.Foundation.Quantities.fee_add' depends on axioms: [propext] -/
#guard_msgs in
#print axioms GiveAndTake.Foundation.Quantities.fee_add

/-- info: 'GiveAndTake.Reference.Solana.compatible_symm' does not depend on any axioms -/
#guard_msgs in
#print axioms GiveAndTake.Reference.Solana.compatible_symm

/-- info: 'GiveAndTake.Cases.PaidCall.Retry.execute_preservesInvariant' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms GiveAndTake.Cases.PaidCall.Retry.execute_preservesInvariant

/-- info: 'GiveAndTake.Cases.PaidCall.Retry.run_preservesInvariant' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms GiveAndTake.Cases.PaidCall.Retry.run_preservesInvariant

/-- info: 'GiveAndTake.Cases.PaidCall.Retry.initial_invariant' depends on axioms: [propext, Quot.sound] -/
#guard_msgs in
#print axioms GiveAndTake.Cases.PaidCall.Retry.initial_invariant

/-- info: 'GiveAndTake.Cases.PaidCall.Retry.run_atMostOnce' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms GiveAndTake.Cases.PaidCall.Retry.run_atMostOnce

/-- info: 'GiveAndTake.Cases.PaidCall.Retry.run_preservesFunds' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms GiveAndTake.Cases.PaidCall.Retry.run_preservesFunds

/-- info: 'GiveAndTake.Cases.PaidCall.Retry.run_receivedReceipt' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms GiveAndTake.Cases.PaidCall.Retry.run_receivedReceipt

/-- info: 'GiveAndTake.Cases.PaidCall.Retry.retry_usesReceipt' depends on axioms: [propext] -/
#guard_msgs in
#print axioms GiveAndTake.Cases.PaidCall.Retry.retry_usesReceipt

/-- info: 'GiveAndTake.Cases.PaidCall.Retry.changedTerms_rejected' depends on axioms: [propext] -/
#guard_msgs in
#print axioms GiveAndTake.Cases.PaidCall.Retry.changedTerms_rejected

/-- info: 'GiveAndTake.Cases.PaidCall.Retry.retry_deliversReceipt' depends on axioms: [propext] -/
#guard_msgs in
#print axioms GiveAndTake.Cases.PaidCall.Retry.retry_deliversReceipt

/-- info: 'GiveAndTake.Cases.PaidCall.Retry.lostReply_recovers' depends on axioms: [propext, Quot.sound] -/
#guard_msgs in
#print axioms GiveAndTake.Cases.PaidCall.Retry.lostReply_recovers
