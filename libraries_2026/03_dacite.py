from dataclasses import dataclass
from decimal import Decimal
from enum import StrEnum

from dacite import Config, from_dict


class Currency(StrEnum):
    EUR = "EUR"
    USD = "USD"


@dataclass(frozen=True)
class Money:
    amount: Decimal
    currency: Currency


@dataclass(frozen=True)
class Customer:
    id: str
    name: str


@dataclass(frozen=True)
class Order:
    id: str
    customer: Customer
    total: Money


def main() -> None:
    data = {
        "id": "order_123",
        "customer": {
            "id": "cust_456",
            "name": "Arjan",
        },
        "total": {
            "amount": "49.95",
            "currency": "EUR",
        },
    }

    order = from_dict(
        data_class=Order,
        data=data,
        config=Config(
            cast=[Decimal, Currency],
        ),
    )

    print(order)
    print(order.total.amount + Decimal("10.00"))


if __name__ == "__main__":
    main()
