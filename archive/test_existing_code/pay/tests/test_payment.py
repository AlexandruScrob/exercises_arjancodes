from pay.order import Order, LineItem
from pay.payment import pay_order
import pytest

from pay.credit_card import CreditCard


class PaymentProcessorMock:
    def charge(self, card: CreditCard, amount: int):
        print(f"Charging {card.number} with amount ${amount/100:.2f}.")


def test_pay_order(card: CreditCard) -> None:
    order = Order()
    order.line_items.append(LineItem("Test", 100))
    pay_order(order, card, PaymentProcessorMock())


# def test_pay_order(monkeypatch: MonkeyPatch) -> None:

#     inputs = ["1249190007575069", "12", "2024"]
#     # NOTE using monkeypatch
#     monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
#     # monkeypatch.setattr("pay.processor._validate_api_key", lambda _: True)
#     # monkeypatch.setattr(PaymentProcessor, "charge", charge_mock)
#     order = Order()
#     order.line_items.append(LineItem("Test", 100))
#     pay_order(order, PaymentProcessorMock())


def test_pay_order_invalid(card: CreditCard) -> None:
    with pytest.raises(ValueError):
        order = Order()
        pay_order(order, card, PaymentProcessorMock())
