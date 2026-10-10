import GiveAndTake.Cases.PaidTask.Agent

open GiveAndTake.Foundation

namespace GiveAndTake.Cases.PaidTask

structure TaskId where
  value : Nat
  deriving DecidableEq, Repr

structure TaskRequest where
  id : TaskId
  caller : AgentId
  provider : AgentId
  service : String
  input : String
  deriving DecidableEq, Repr

/-- Local study phases, not the A2A task-state enumeration. -/
inductive TaskPhase where
  | requested
  | paid
  | completed (result : String)
  deriving DecidableEq, Repr

structure Task where
  request : TaskRequest
  phase : TaskPhase := .requested
  deriving DecidableEq, Repr

end GiveAndTake.Cases.PaidTask
