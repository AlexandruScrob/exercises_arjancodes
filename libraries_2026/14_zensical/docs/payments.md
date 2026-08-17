# Payments

The payment service supports multiple providers.

## Provider interface

```python
from typing import Protocol
from decimal import Decimal

class PaymentProvider(Protocol):
    def charge(self, amount: Decimal) -> str:
        ...
```

## Design note

We keep provider-specific code outside the domain model.
That keeps the core payment logic independent from Stripe, Mollie, or any other provider.
