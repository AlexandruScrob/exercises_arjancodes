from enum import Enum, auto
from typing import Protocol


class PaymentMethod(str, Enum):
    PAYPAL = auto()
    CARD = auto()


class Payment:
    def pay(self, amount: int) -> None:
        ...


class PaypalPayment(Payment):
    def pay(self, amount: int) -> None:
        print(f"Paying ${amount/100:.2f} using Paypal")


class StripePayment(Payment):
    def pay(self, amount: int) -> None:
        print(f"Paying ${amount/100:.2f} using Stripe")


def create_payment(method: PaymentMethod) -> Payment:
    if method == PaymentMethod.PAYPAL:
        return PaypalPayment()
    elif method == PaymentMethod.CARD:
        return StripePayment()
    else:
        raise NotImplementedError()


def main() -> None:
    my_payment = create_payment(PaymentMethod.PAYPAL)
    my_payment.pay(1000)


if __name__ == "__main__":
    main()
