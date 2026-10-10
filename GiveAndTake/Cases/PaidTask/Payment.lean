import GiveAndTake.Foundation.Asset
import GiveAndTake.Cases.PaidTask.Task

open GiveAndTake.Foundation

namespace GiveAndTake.Cases.PaidTask

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

end GiveAndTake.Cases.PaidTask
