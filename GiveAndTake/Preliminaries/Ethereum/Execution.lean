import GiveAndTake.Preliminaries.Ethereum.Spec
import GiveAndTake.Preliminaries.Quantities.Execution

namespace GiveAndTake.Preliminaries.Ethereum

/-- Evaluate the transfer rule against one immutable account-state snapshot. -/
def applyTransfer : Transition State Transfer :=
  fun state tx =>
    if ValidTransfer state tx then
      some fun address =>
        let account := state address
        let debit :=
          if address = tx.sender then tx.value.units else 0
        let credit :=
          if address = tx.recipient then tx.value.units else 0
        let nextNonce :=
          if address = tx.sender then account.nonce.next
          else account.nonce
        { balance :=
            ⟨account.balance.units - debit + credit⟩
          nonce := nextNonce }
    else none

end GiveAndTake.Preliminaries.Ethereum
