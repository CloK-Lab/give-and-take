import GiveAndTake.Cases.PaidTask.System.Examples
import GiveAndTake.Cases.PaidTask.Examples
import GiveAndTake.Cases.PaidCall.Execution
import GiveAndTake.Cases.PaidCall.Retry.Examples

open GiveAndTake.Cases.PaidCall

def main : IO Unit := do
  let start := initial 100 20
  IO.println "Give and take — one paid call"
  IO.println s!"Initial: {reprStr start}"
  IO.println s!"Reserve 30, settle: {reprStr (run start [.reserve 30, .settle])}"
  IO.println s!"Reserve 30, refund: {reprStr (run start [.reserve 30, .refund])}"
  IO.println s!"Reserve 30, settle twice: {reprStr (run start [.reserve 30, .settle, .settle])}"

  IO.println "Give and take — one purchase with a lost reply (integer base units)"
  for (label, state) in GiveAndTake.Cases.PaidCall.Retry.Examples.trace do
    IO.println s!"{label}: buyer={state.funds.buyer}, provider={state.funds.provider}, commits={state.commits}, pending={state.pending.isSome}, received={state.received.isSome}"

  IO.println "Give and take — paid echo task (balances in wei)"
  IO.println s!"Echo task: {reprStr GiveAndTake.Cases.PaidTask.Examples.demo}"

  IO.println "Give and take — system trace (balances in wei)"
  match GiveAndTake.Cases.PaidTask.System.Examples.demo with
  | none => IO.println "Rejected"
  | some states =>
    for state in states do
      IO.println (reprStr state)
