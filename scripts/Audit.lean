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
