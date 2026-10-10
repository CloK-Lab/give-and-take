import VDSI.Native.Wallet.Spec

open VDSI.Foundation

namespace VDSI.Native.WalletExamples

-- Symbolic test identities and integer units; no chain client is involved.
def network : NetworkId := ⟨"vdsi", "wallet-test"⟩
def asset : AssetId := ⟨network, "native", "test"⟩
def owner : AgentId := ⟨"agent-a"⟩
def payer : AccountId := ⟨network, "buyer"⟩
def payee : AccountId := ⟨network, "provider"⟩
def wallet : Wallet := ⟨owner, payer, asset, ⟨30⟩, [payee]⟩
def request : SpendRequest := ⟨payer, payee, asset, ⟨30⟩⟩

#guard decide (CanSpend wallet owner request)
#guard !(decide (CanSpend wallet ⟨"agent-b"⟩ request))
#guard !(decide (CanSpend wallet owner { request with amount := ⟨31⟩ }))
#guard !(decide (CanSpend wallet owner { request with payee := payer }))
#guard !(decide (CanSpend wallet owner { request with payer := payee }))

end VDSI.Native.WalletExamples
