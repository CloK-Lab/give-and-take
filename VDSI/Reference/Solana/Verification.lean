import VDSI.Reference.Solana.Spec

namespace VDSI.Reference.Solana

/-- Compatibility does not depend on which transaction is named first. -/
theorem compatible_symm (left right : AccountAccess) :
    Compatible left right ↔ Compatible right left := by
  constructor
  · intro h
    exact ⟨h.2, h.1⟩
  · intro h
    exact ⟨h.2, h.1⟩

end VDSI.Reference.Solana
