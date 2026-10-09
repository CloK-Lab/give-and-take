import GiveAndTake.Preliminaries.Solana.Spec

namespace GiveAndTake.Preliminaries.Solana

/-- Decide access compatibility, without executing or scheduling a transaction. -/
def canRunTogether (left right : AccountAccess) : Bool :=
  decide (Compatible left right)

end GiveAndTake.Preliminaries.Solana
