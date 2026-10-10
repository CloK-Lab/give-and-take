import VDSI.Cases.PaidTask.System.Execution
import VDSI.Cases.PaidTask.Examples

open VDSI.Foundation VDSI.Cases.PaidTask
open VDSI.Reference

namespace VDSI.Cases.PaidTask.System.Examples

def config : Config :=
  { wallet := PaidTask.Examples.wallet
    provider := PaidTask.Examples.provider
    service := fun name input => if name = "echo" then some input else none }

def initial : State := ⟨PaidTask.Examples.task, PaidTask.Examples.initialLedger, none⟩

def actions : List Action :=
  [.authorize PaidTask.Examples.buyer PaidTask.Examples.terms 0,
   .settle 10, .execute PaidTask.Examples.provider.id]

structure Snapshot where
  phase : TaskPhase
  approved : Bool
  buyerWei : Nat
  providerWei : Nat
  deriving DecidableEq, Repr

def snapshot (state : State) : Snapshot :=
  ⟨state.task.phase, state.approval.isSome,
   state.ledger.balances PaidTask.Examples.buyerAccount Ethereum.ether,
   state.ledger.balances PaidTask.Examples.providerAccount Ethereum.ether⟩

def demo : Option (List Snapshot) :=
  (trace config initial actions).map (List.map snapshot)

#guard demo = some
  [⟨.requested, false, 10000000000000000, 2000000000000000⟩,
   ⟨.requested, true, 10000000000000000, 2000000000000000⟩,
   ⟨.paid, false, 7000000000000000, 5000000000000000⟩,
   ⟨.completed "hello", false, 7000000000000000, 5000000000000000⟩]

-- The composed system enforces ordering, even if an action is submitted directly.
#guard (step config initial (.settle 10)).isNone
#guard (step config initial (.execute PaidTask.Examples.provider.id)).isNone
#guard (trace config initial (actions ++ [.settle 11])).isNone

-- A service that returns no result rejects the execution action.
#guard (trace { config with service := fun _ _ => none } initial actions).isNone

end VDSI.Cases.PaidTask.System.Examples
