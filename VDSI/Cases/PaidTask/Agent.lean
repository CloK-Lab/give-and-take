import VDSI.Foundation.Identity
import VDSI.Foundation.Network

open VDSI.Foundation

namespace VDSI.Cases.PaidTask

/-- One advertised endpoint and receiving account for this example agent. -/
structure Agent where
  id : AgentId
  endpoint : String
  services : List String
  payee : AccountId
  deriving DecidableEq, Repr

end VDSI.Cases.PaidTask
