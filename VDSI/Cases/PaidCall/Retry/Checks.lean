import VDSI.Cases.PaidCall.Retry.Verification
import VDSI.Cases.PaidCall.Retry.Examples

namespace VDSI.Cases.PaidCall.Retry

open Examples

-- A successful payment followed by a lost reply and retry transfers only 30.
#guard delivered.funds = ⟨70, 50, .settled⟩
#guard delivered.commits = 1
#guard delivered.received = some (receiptFor approved)
#guard lost.received = none
#guard lost.pending = none
#guard lost.saved = some (receiptFor approved)
#guard retried.funds = paid.funds
#guard run approved start [.request approved, .dropReply, .request approved,
    .deliverReply] = delivered

-- Retrying an already delivered request is harmless, including after many losses.
#guard (run approved delivered (List.replicate 20 (.request approved))).commits = 1
#guard (run approved paid [.dropReply, .deliverReply, .dropReply]).funds = paid.funds

-- Matching an ID alone is insufficient: the complete approved call must match.
#guard request approved start { approved with price := 31 } = start
#guard request approved lost { approved with input := "different report" } = lost
#guard request approved lost { approved with id := 8 } = lost

-- Rejection leaves all state intact; reply delivery cannot invent a payment.
#guard request approved (initial 29 20) approved = initial 29 20
#guard execute approved start .deliverReply = start

-- Exact funding and zero-price calls still generate only one receipt and commit.
#guard (request approved (initial 30 20) approved).funds = ⟨0, 50, .settled⟩
#guard (run { approved with price := 0 } (initial 0 0)
    [.request { approved with price := 0 }, .request { approved with price := 0 }]).commits = 1

end VDSI.Cases.PaidCall.Retry
