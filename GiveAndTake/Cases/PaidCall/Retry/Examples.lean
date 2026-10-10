import GiveAndTake.Cases.PaidCall.Retry.Execution

namespace GiveAndTake.Cases.PaidCall.Retry.Examples

def approved : Call := ⟨7, 30, "report"⟩

def start : State := initial 100 20

def paid : State := execute approved start (.request approved)

def lost : State := execute approved paid .dropReply

def retried : State := execute approved lost (.request approved)

def delivered : State := execute approved retried .deliverReply

/-- Both attempts refer to purchase 7; only the reply is lost. -/
def trace : List (String × State) :=
  [("Initial", start), ("Request committed", paid), ("Reply lost", lost),
   ("Same request retried", retried), ("Reply delivered", delivered)]

end GiveAndTake.Cases.PaidCall.Retry.Examples
