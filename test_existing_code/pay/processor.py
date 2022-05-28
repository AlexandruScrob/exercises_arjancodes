from datetime import datetime
import re

from pay.credit_card import CreditCard


def _validate_api_key(api_key: str) -> str:
    uuid_pattern = r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
    if not re.match(uuid_pattern, api_key):
        raise ValueError("Invalid Api Key")

    return api_key


class PaymentProcessor:
    def __init__(self, api_key: str = "SOME_VALID_KEY") -> None:
        self.api_key = _validate_api_key(api_key)

    def charge(self, card: CreditCard, amount: int) -> None:
        if not self.validate_card(card):
            raise ValueError("Invalid card")
        print(f"Charging card number {card} for ${amount/100:.2f}")

    def validate_card(self, card: CreditCard) -> bool:
        return (
            luhn_checksum(card.number)
            and datetime(card.expiry_year, card.expiry_month, 1) > datetime.now()
        )


def luhn_checksum(card_number: str) -> bool:
    def digits_of(card_nr: str):
        return [int(d) for d in card_nr]

    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for digit in even_digits:
        checksum += sum(digits_of(str(digit * 2)))
    return checksum % 10 == 0
