import GiveAndTake.Preliminaries.Quantities.Verification
import GiveAndTake.Preliminaries.Ethereum.Model

namespace GiveAndTake.Preliminaries.Quantities

-- Illustrative inputs, not a live gas quote.
def transferGas : Gas := ⟨21000⟩
def effectivePrice : PricePerGas Ethereum.ether :=
  ⟨2 * 10 ^ 9⟩

#guard (fee transferGas effectivePrice).units = 42000000000000
#guard (fee ⟨0⟩ effectivePrice).units = 0
#guard energy ⟨100⟩ ⟨2⟩ = ⟨200⟩
#guard (Nonce.next ⟨7⟩).value = 8

-- Separate devices over the same two seconds; illustrative, not measured data.
def deviceEnergy : List Energy :=
  [energy ⟨60⟩ ⟨2⟩,   -- GPU
   energy ⟨25⟩ ⟨2⟩,   -- CPU
   energy ⟨15⟩ ⟨2⟩]   -- Network device

#guard deviceEnergy.map Energy.joules = [120, 50, 30]
#guard (deviceEnergy.map Energy.joules).sum =
  (energy ⟨100⟩ ⟨2⟩).joules

end GiveAndTake.Preliminaries.Quantities
