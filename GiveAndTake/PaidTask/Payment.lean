import GiveAndTake.Preliminaries.Asset
import GiveAndTake.PaidTask.Task

open GiveAndTake.Preliminaries

namespace GiveAndTake.PaidTask

/-- Bind this price and receiving account to the entire requested task. -/
structure PaymentTerms where
  task : TaskRequest
  payer : AccountId
  payee : AccountId
  asset : AssetId
  amount : Amount asset
  expiresAt : Nat
  deriving DecidableEq, Repr

/-- A model approval record, not a cryptographic signature. -/
structure Authorization where
  terms : PaymentTerms
  actor : AgentId
  nonce : Nat
  deriving DecidableEq, Repr

end GiveAndTake.PaidTask
