import GiveAndTake.PaidCall.Execution

open GiveAndTake.PaidCall

def main : IO Unit := do
  let start := initial 100 20
  IO.println "Give and take — one paid call"
  IO.println s!"Initial: {reprStr start}"
  IO.println s!"Reserve 30, settle: {reprStr (run start [.reserve 30, .settle])}"
  IO.println s!"Reserve 30, refund: {reprStr (run start [.reserve 30, .refund])}"
  IO.println s!"Reserve 30, settle twice: {reprStr (run start [.reserve 30, .settle, .settle])}"
