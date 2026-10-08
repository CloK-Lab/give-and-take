import GiveAndTake.Preliminaries.Identity
import GiveAndTake.Preliminaries.Network

open GiveAndTake.Preliminaries

namespace GiveAndTake.PaidTask

/-- One advertised endpoint and receiving account for this example agent. -/
structure Agent where
  id : AgentId
  endpoint : String
  services : List String
  payee : AccountId
  deriving DecidableEq, Repr

end GiveAndTake.PaidTask
