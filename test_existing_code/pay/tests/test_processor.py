from uuid import uuid4
import pytest
import os
from dotenv import load_dotenv
from pay.processor import PaymentProcessor
from pay.processor import luhn_checksum
from pay.credit_card import CreditCard


load_dotenv()

TEST_API_KEY: str = os.getenv("TEST_API_KEY", str(uuid4()))


def test_api_key_invalid(card: CreditCard) -> None:
    with pytest.raises(ValueError):
        processor = PaymentProcessor("")
        processor.charge(card, 100)


def test_card_valid_date(card: CreditCard) -> None:
    processor = PaymentProcessor(TEST_API_KEY)
    processor.charge(card, 100)


def test_card_invalid_date(card: CreditCard) -> None:
    with pytest.raises(ValueError):
        processor = PaymentProcessor(TEST_API_KEY)
        processor.charge(CreditCard(card.number, card.expiry_month, 1900), 100)


def test_card_number_invalid_luhn():
    assert not luhn_checksum("1249190007575068")


def test_card_number_invalid_luhn(card: CreditCard):
    assert luhn_checksum(card.number)


def test_charge_card_valid(card: CreditCard):
    payment_processor = PaymentProcessor(TEST_API_KEY)
    payment_processor.charge(card, 100)


def test_charge_card_invalid(card: CreditCard):
    with pytest.raises(ValueError):
        payment_processor = PaymentProcessor(TEST_API_KEY)
        payment_processor.charge(
            CreditCard("124919000757509", card.expiry_month, card.expiry_year), 100
        )
