import GiveAndTake.Reference.A2A.Execution

namespace GiveAndTake.Reference.A2A

def echoCard : AgentCard :=
  { name := "Echo"
    description := "Return the requested text."
    version := "0.1.0"
    supportedInterfaces :=
      [⟨"https://echo.example/a2a", "JSONRPC", "1.0"⟩,
       ⟨"https://echo.example/http", "HTTP+JSON", "1.0"⟩]
    skills := [⟨"echo", "Echo", "Return the requested text.", ["text"]⟩] }

#guard (selectInterface echoCard "JSONRPC" "1.0").map (·.url) =
  some "https://echo.example/a2a"
#guard (selectInterface echoCard "GRPC" "1.0").isNone
#guard (selectInterface echoCard "JSONRPC" "0.3").isNone
#guard isTerminal .completed
#guard isTerminal .failed
#guard !(isTerminal .inputRequired)
#guard !(isTerminal .authRequired)

end GiveAndTake.Reference.A2A
