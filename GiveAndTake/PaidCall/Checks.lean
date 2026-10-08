import GiveAndTake.PaidCall.Verification

namespace GiveAndTake.PaidCall

example : run (initial 100 20) [.reserve 30, .settle] =
    some ⟨70, 50, .settled⟩ := by decide

example : run (initial 100 20) [.reserve 30, .refund] =
    some ⟨100, 20, .refunded⟩ := by decide

example : run (initial 10 20) [.reserve 30] = none := by decide

example : run (initial 100 20) [.reserve 30, .settle, .settle] = none := by decide

example : run (initial 100 20) [.reserve 30, .refund, .settle] = none := by decide

example : run (initial 0 0) [.reserve 0, .settle] =
    some ⟨0, 0, .settled⟩ := by decide

end GiveAndTake.PaidCall
