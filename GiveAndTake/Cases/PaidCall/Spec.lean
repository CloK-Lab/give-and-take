import GiveAndTake.Cases.PaidCall.Model

namespace GiveAndTake.Cases.PaidCall

/-- All funds, including the reservation, remain in the two-party system. -/
def PreservesFunds (before after : State) : Prop :=
  totalFunds after = totalFunds before

/-- A finished call cannot be reused for another payment. -/
def Terminal (s : State) : Prop :=
  s.phase = .settled ∨ s.phase = .refunded

end GiveAndTake.Cases.PaidCall
