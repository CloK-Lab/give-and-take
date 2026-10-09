import GiveAndTake.Preliminaries.Solana.Spec

namespace GiveAndTake.Preliminaries.Solana

/-- Compatibility does not depend on which transaction is named first. -/
theorem compatible_symm (left right : AccountAccess) :
    Compatible left right ↔ Compatible right left := by
  constructor
  · intro h
    exact ⟨h.2, h.1⟩
  · intro h
    exact ⟨h.2, h.1⟩

end GiveAndTake.Preliminaries.Solana
