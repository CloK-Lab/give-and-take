import GiveAndTake.Preliminaries.X402.Model

namespace GiveAndTake.Preliminaries.X402

/-- Decode decimal base units. This checks no signature, balance, or settlement. -/
def amountUnits (requirements : PaymentRequirements) : Option Nat :=
  requirements.amount.toNat?

end GiveAndTake.Preliminaries.X402
