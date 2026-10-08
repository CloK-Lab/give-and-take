import GiveAndTake.Preliminaries.Wallet.Spec
import GiveAndTake.Preliminaries.Ethereum.Model

namespace GiveAndTake.Preliminaries.WalletExamples

def owner : AgentId := ⟨"agent-a"⟩
def payer : AccountId := ⟨Ethereum.mainnet, "0x0000000000000000000000000000000000000001"⟩
def payee : AccountId := ⟨Ethereum.mainnet, "0x0000000000000000000000000000000000000002"⟩
def wallet : Wallet := ⟨owner, payer, Ethereum.ether, Ethereum.milliEther 3, [payee]⟩
def request : SpendRequest := ⟨payer, payee, Ethereum.ether, Ethereum.milliEther 3⟩

#guard decide (CanSpend wallet owner request)
#guard !(decide (CanSpend wallet ⟨"agent-b"⟩ request))
#guard !(decide (CanSpend wallet owner { request with amount := ⟨3000000000000001⟩ }))
#guard !(decide (CanSpend wallet owner { request with payee := payer }))
#guard !(decide (CanSpend wallet owner { request with payer := payee }))

end GiveAndTake.Preliminaries.WalletExamples
