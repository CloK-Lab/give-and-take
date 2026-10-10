import GiveAndTake.Reference.X402.Model

open GiveAndTake.Foundation

namespace GiveAndTake.Reference.X402

/-- Decode decimal base units. This checks no signature, balance, or settlement. -/
def amountUnits (requirements : PaymentRequirements) : Option Nat :=
  requirements.amount.toNat?

end GiveAndTake.Reference.X402
