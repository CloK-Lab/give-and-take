import VDSI.Reference.Solana.Examples
import VDSI.Reference.Solana.Verification

namespace VDSI.Reference.Solana

-- Independent transfers share a read-only program; a shared fee payer conflicts.
#guard paymentAccessExample = (true, false)

-- A competing debit from Alice conflicts even when the recipient is different.
#guard !canRunTogether aliceToBob {
  readOnly := ["SystemProgram"], writable := ["Alice", "Carol"] }

-- Reading a balance conflicts with a transaction that writes it, in either order.
#guard !canRunTogether aliceToBob {
  readOnly := ["Bob"], writable := ["ReaderFeePayer"] }
#guard !canRunTogether {
  readOnly := ["Bob"], writable := ["ReaderFeePayer"] } aliceToBob

-- Two readers can share the same data account if their fee payers differ.
#guard canRunTogether {
  readOnly := ["PriceData"], writable := ["Alice"] } {
  readOnly := ["PriceData"], writable := ["Carol"] }

-- One transfer cannot run concurrently with another copy of itself.
#guard !canRunTogether aliceToBob aliceToBob

end VDSI.Reference.Solana
