import GiveAndTake.Preliminaries.Asset

namespace GiveAndTake.Preliminaries.Ethereum

def mainnet : NetworkId := ⟨"eip155", "1"⟩

/-- Native ETH on Ethereum mainnet, using CAIP-19's native-asset reference. -/
def ether : AssetId := ⟨mainnet, "slip44", "60"⟩

/-- Each unit is one wei, not one ETH. -/
abbrev Wei := Amount ether

def weiPerEther : Nat := 10 ^ 18

/-- An exact integer conversion: one milli-ETH is 10^15 wei. -/
def milliEther (n : Nat) : Wei := ⟨n * 10 ^ 15⟩

/-- Projection of execution-specs Account onto nonce and native balance. -/
structure Account where
  nonce : Nat
  balance : Wei
  deriving DecidableEq, Repr

end GiveAndTake.Preliminaries.Ethereum
