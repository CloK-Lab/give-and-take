import GiveAndTake.Cases.PaidTask.Spec

open GiveAndTake.Foundation GiveAndTake.Native

namespace GiveAndTake.Cases.PaidTask

/-- Approve exact terms under a fixed wallet policy. No keys or signing IO. -/
def authorize (wallet : Wallet) (actor : AgentId) (terms : PaymentTerms)
    (nonce : Nat) : Option Authorization :=
  if CanAuthorize wallet actor terms then some ⟨terms, actor, nonce⟩ else none

private def moveFunds (balances : Balances) (terms : PaymentTerms) : Balances :=
  fun account asset =>
    if terms.payer = terms.payee then balances account asset
    else if asset ≠ terms.asset then balances account asset
    else if account = terms.payer then balances account asset - terms.amount.units
    else if account = terms.payee then balances account asset + terms.amount.units
    else balances account asset

/-- One atomic model transition: transfer funds, consume the nonce, mark paid. -/
def settle (wallet : Wallet) (provider : Agent) (task : Task)
    (ledger : Ledger) (authorization : Authorization) (now : Nat) :
    Option (Ledger × Task) :=
  if CanSettle wallet provider task ledger authorization now then
    let terms := authorization.terms
    some ({ balances := moveFunds ledger.balances terms,
            spent := (terms.payer, authorization.nonce) :: ledger.spent },
          { task with phase := .paid })
  else none

/-- Record a result reported by the provider after payment, without judging quality. -/
def complete (actor : AgentId) (task : Task) (result : String) : Option Task :=
  if actor = task.request.provider ∧ task.phase = .paid then
    some { task with phase := .completed result }
  else none

end GiveAndTake.Cases.PaidTask
