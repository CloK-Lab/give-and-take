import GiveAndTake.Foundation.Identity
import GiveAndTake.Foundation.Network

open GiveAndTake.Foundation

namespace GiveAndTake.Cases.PaidTask

/-- One advertised endpoint and receiving account for this example agent. -/
structure Agent where
  id : AgentId
  endpoint : String
  services : List String
  payee : AccountId
  deriving DecidableEq, Repr

end GiveAndTake.Cases.PaidTask
