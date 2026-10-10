import VDSI.Foundation.Asset

open VDSI.Foundation

namespace VDSI.Cases.PaidTask

/-- Available base units indexed by both account and asset. -/
abbrev Balances := AccountId → AssetId → Nat

/-- An abstract settlement state with account-scoped nonce tracking. -/
structure Ledger where
  balances : Balances
  spent : List (AccountId × Nat) := []

end VDSI.Cases.PaidTask
