from dataclasses import dataclass, field
from enum import Enum


@dataclass
class LineItem:
    name: str
    price: int
    quantity: int = 1

    # properties should be simple and predictable
    @property
    def total_price(self) -> int:
        return self.price * self.quantity


class PaymentStatus(Enum):
    PENDING = "pending"
    PAID = "paid"
    FAILED = "failed"


class PaymentStatusError(Exception):
    pass


@dataclass
class Order:
    items: list[LineItem] = field(default_factory=list)
    _payment_status: PaymentStatus = PaymentStatus.PENDING

    def get_payment_status(self) -> PaymentStatus:
        return self._payment_status

    def set_payment_status(self, status: PaymentStatus) -> None:
        # here, using a (getter +) setter is ok, because we're doing
        # something more than just setting the value

        if self._payment_status == PaymentStatus.PAID:
            raise PaymentStatusError(
                "Can't change the status of an already" "paid order"
            )

        self._payment_status = status

    def add_item(self, item: LineItem):
        self.items.append(item)

    @property
    def total_price(self) -> int:
        return sum(item.total_price for item in self.items)
