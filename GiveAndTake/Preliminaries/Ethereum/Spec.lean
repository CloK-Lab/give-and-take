import GiveAndTake.Preliminaries.Ethereum.Model

namespace GiveAndTake.Preliminaries.Ethereum

/-- The two acceptance conditions of the balance-and-nonce model. -/
def ValidTransfer
    (state : State) (tx : Transfer) : Prop :=
  tx.nonce = (state tx.sender).nonce ∧
  tx.value.units ≤ (state tx.sender).balance.units

instance (state : State) (tx : Transfer) :
    Decidable (ValidTransfer state tx) := by
  unfold ValidTransfer
  infer_instance

end GiveAndTake.Preliminaries.Ethereum
