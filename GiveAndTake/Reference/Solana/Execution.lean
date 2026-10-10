import GiveAndTake.Reference.Solana.Spec

namespace GiveAndTake.Reference.Solana

/-- Decide access compatibility, without executing or scheduling a transaction. -/
def canRunTogether (left right : AccountAccess) : Bool :=
  decide (Compatible left right)

end GiveAndTake.Reference.Solana
