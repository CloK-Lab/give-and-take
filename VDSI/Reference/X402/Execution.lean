import VDSI.Reference.X402.Model

open VDSI.Foundation

namespace VDSI.Reference.X402

/-- Decode decimal base units. This checks no signature, balance, or settlement. -/
def amountUnits (requirements : PaymentRequirements) : Option Nat :=
  requirements.amount.toNat?

end VDSI.Reference.X402
