import GiveAndTake.Preliminaries.Ethereum.Examples

namespace GiveAndTake.Preliminaries.Ethereum

def exampleAccount : Account := ⟨⟨0⟩, milliEther 10⟩

#guard (milliEther 3).units = 3000000000000000
#guard (milliEther 1000).units = weiPerEther
#guard exampleAccount.balance.units = 10000000000000000
#guard ether ≠ { ether with network := ⟨"eip155", "11155111"⟩ }

#guard transferExample = some {
  senderBalance := milliEther 7, recipientBalance := milliEther 5, senderNonce := ⟨8⟩ }
#guard (applyTransfer initialState { payment with nonce := ⟨8⟩ }).isNone
#guard (applyTransfer initialState { payment with value := milliEther 11 }).isNone

-- Once nonce 7 has been consumed, neither replay nor a conflicting spend is accepted.
#guard ((applyTransfer initialState payment).bind fun next =>
  applyTransfer next payment).isNone
#guard ((applyTransfer initialState payment).bind fun next =>
  applyTransfer next { payment with recipient := "Carol" }).isNone

-- A self-transfer preserves value while advancing the nonce.
#guard ((applyTransfer initialState { payment with recipient := "Alice" }).map
  fun next => next "Alice") = some ⟨⟨8⟩, milliEther 10⟩
#guard ((applyTransfer initialState { payment with value := ⟨0⟩ }).map
  fun next => next "Alice") = some ⟨⟨8⟩, milliEther 10⟩
#guard ((applyTransfer initialState { payment with recipient := "Carol" }).map
  fun next => next "Carol") = some ⟨⟨0⟩, milliEther 3⟩
#guard ((applyTransfer initialState payment).map fun next => next "Carol") =
  some (initialState "Carol")
#guard ((applyTransfer initialState payment).bind fun next =>
  (applyTransfer next { payment with nonce := ⟨8⟩ }).map fun final =>
    ((final "Alice").balance.units, (final "Bob").balance.units,
      (final "Alice").nonce.value)) = some (4000000000000000, 8000000000000000, 9)

end GiveAndTake.Preliminaries.Ethereum
