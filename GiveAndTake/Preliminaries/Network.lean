namespace GiveAndTake.Preliminaries

/-- Symbolic network identity, following the namespace/reference split in CAIP-2. -/
structure NetworkId where
  namespaceId : String
  reference : String
  deriving DecidableEq, Repr

/-- The same address on another network denotes another account. -/
structure AccountId where
  network : NetworkId
  address : String
  deriving DecidableEq, Repr

end GiveAndTake.Preliminaries
