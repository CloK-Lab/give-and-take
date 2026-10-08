import GiveAndTake.System.Examples
import GiveAndTake.PaidTask.Examples
import GiveAndTake.PaidCall.Execution

open GiveAndTake.PaidCall

def main : IO Unit := do
  let start := initial 100 20
  IO.println "Give and take — one paid call"
  IO.println s!"Initial: {reprStr start}"
  IO.println s!"Reserve 30, settle: {reprStr (run start [.reserve 30, .settle])}"
  IO.println s!"Reserve 30, refund: {reprStr (run start [.reserve 30, .refund])}"
  IO.println s!"Reserve 30, settle twice: {reprStr (run start [.reserve 30, .settle, .settle])}"

  IO.println "Give and take — paid echo task (balances in wei)"
  IO.println s!"Echo task: {reprStr GiveAndTake.PaidTask.Examples.demo}"

  IO.println "Give and take — system trace (balances in wei)"
  match GiveAndTake.System.Examples.demo with
  | none => IO.println "Rejected"
  | some states =>
    for state in states do
      IO.println (reprStr state)
