namespace GiveAndTake.Foundation

/-- An authenticated principal's identifier, separate from a chain account. -/
structure AgentId where
  value : String
  deriving DecidableEq, Repr

end GiveAndTake.Foundation
