# One paid call

This case studies accounting for a single service call between a buyer and a
provider. Balances are natural numbers in one abstract unit; zero-price calls
are allowed. A `reserved price` phase records funds unavailable to either party.

| Phase | Action | Result |
| --- | --- | --- |
| Ready | Reserve a price within the buyer's balance | Debit the buyer and reserve that price |
| Reserved | Settle | Credit the provider and finish the call |
| Reserved | Refund | Return the reservation to the buyer and finish the call |
| Any | Any other action | Reject |

The quantity being preserved is:

```text
buyer available balance + provider available balance + reserved funds
```

## Definitions and guarantees

- `Model.lean` defines phases, balances, actions, and the total.
- `Spec.lean` names fund conservation and terminal states.
- `Execution.lean` defines `execute` and `run`; `none` denotes rejection.
- `Verification.lean` proves conservation for every successful execution,
  rejection after a terminal state, and the result of reserve followed by refund.
- `Checks.lean` contains concrete boundary and lifecycle examples.

For example, buyer 100 and provider 20 become buyer 70 and provider 50 after
reserving and settling 30. Reserving and refunding 30 restores balances 100 and
20. The finished phase prevents reusing this call for another settlement.

`run` is a pure replay function. If any action rejects, the result is `none`;
this does not roll back effects in an external database, payment system, or chain.

## Boundaries and next questions

Settlement and refund are actions supplied to the model. There is no caller
identity, authentication, evidence of delivery, timeout rule, or adjudicator.
The case therefore establishes accounting behavior, not who is entitled to
settle or whether the service was delivered.

There is one call and no concurrency, persistence, fees, exchange rate, or
external wallet. There are no strategies or utility functions yet. Funds being
conserved does not establish that participants will cooperate or finish work.

Natural next questions include who may authorize each transition, what evidence
permits settlement, and whether a provider can fund a sub-call while its own
payment remains reserved. Each extension should introduce its assumptions and
desired properties explicitly.
