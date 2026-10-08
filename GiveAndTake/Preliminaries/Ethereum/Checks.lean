import GiveAndTake.Preliminaries.Ethereum.Model

namespace GiveAndTake.Preliminaries.Ethereum

def exampleAccount : Account := ⟨0, milliEther 10⟩

#guard (milliEther 3).units = 3000000000000000
#guard (milliEther 1000).units = weiPerEther
#guard exampleAccount.balance.units = 10000000000000000
#guard ether ≠ { ether with network := ⟨"eip155", "11155111"⟩ }

end GiveAndTake.Preliminaries.Ethereum
