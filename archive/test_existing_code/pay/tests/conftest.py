from datetime import date
import pytest

from pay.credit_card import CreditCard


@pytest.fixture
def card() -> CreditCard:
    year = date.today().year + 2
    return CreditCard("1249190007575069", 12, year)
