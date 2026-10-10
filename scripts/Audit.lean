import VDSI

-- Fail if a theorem acquires a different axiom footprint.
/-- info: 'VDSI.Cases.PaidCall.execute_preservesFunds' depends on axioms: [propext, Quot.sound] -/
#guard_msgs in
#print axioms VDSI.Cases.PaidCall.execute_preservesFunds

/-- info: 'VDSI.Cases.PaidCall.run_preservesFunds' depends on axioms: [propext, Quot.sound] -/
#guard_msgs in
#print axioms VDSI.Cases.PaidCall.run_preservesFunds

/-- info: 'VDSI.Cases.PaidCall.terminal_rejects' depends on axioms: [propext] -/
#guard_msgs in
#print axioms VDSI.Cases.PaidCall.terminal_rejects

/-- info: 'VDSI.Cases.PaidCall.reserve_refund' depends on axioms: [propext, Quot.sound] -/
#guard_msgs in
#print axioms VDSI.Cases.PaidCall.reserve_refund

/-- info: 'VDSI.Foundation.Quantities.nonce_next_ne' does not depend on any axioms -/
#guard_msgs in
#print axioms VDSI.Foundation.Quantities.nonce_next_ne

/-- info: 'VDSI.Foundation.Quantities.fee_add' depends on axioms: [propext] -/
#guard_msgs in
#print axioms VDSI.Foundation.Quantities.fee_add

/-- info: 'VDSI.Reference.Solana.compatible_symm' does not depend on any axioms -/
#guard_msgs in
#print axioms VDSI.Reference.Solana.compatible_symm

/-- info: 'VDSI.Cases.PaidCall.Retry.execute_preservesInvariant' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms VDSI.Cases.PaidCall.Retry.execute_preservesInvariant

/-- info: 'VDSI.Cases.PaidCall.Retry.run_preservesInvariant' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms VDSI.Cases.PaidCall.Retry.run_preservesInvariant

/-- info: 'VDSI.Cases.PaidCall.Retry.initial_invariant' depends on axioms: [propext, Quot.sound] -/
#guard_msgs in
#print axioms VDSI.Cases.PaidCall.Retry.initial_invariant

/-- info: 'VDSI.Cases.PaidCall.Retry.run_atMostOnce' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms VDSI.Cases.PaidCall.Retry.run_atMostOnce

/-- info: 'VDSI.Cases.PaidCall.Retry.run_preservesFunds' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms VDSI.Cases.PaidCall.Retry.run_preservesFunds

/-- info: 'VDSI.Cases.PaidCall.Retry.run_receivedReceipt' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms VDSI.Cases.PaidCall.Retry.run_receivedReceipt

/-- info: 'VDSI.Cases.PaidCall.Retry.retry_usesReceipt' depends on axioms: [propext] -/
#guard_msgs in
#print axioms VDSI.Cases.PaidCall.Retry.retry_usesReceipt

/-- info: 'VDSI.Cases.PaidCall.Retry.changedTerms_rejected' depends on axioms: [propext] -/
#guard_msgs in
#print axioms VDSI.Cases.PaidCall.Retry.changedTerms_rejected

/-- info: 'VDSI.Cases.PaidCall.Retry.retry_deliversReceipt' depends on axioms: [propext] -/
#guard_msgs in
#print axioms VDSI.Cases.PaidCall.Retry.retry_deliversReceipt

/-- info: 'VDSI.Cases.PaidCall.Retry.lostReply_recovers' depends on axioms: [propext, Quot.sound] -/
#guard_msgs in
#print axioms VDSI.Cases.PaidCall.Retry.lostReply_recovers
