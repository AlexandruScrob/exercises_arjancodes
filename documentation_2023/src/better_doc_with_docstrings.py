"""Bank account operations using OOP."""

# from __future__ import annotations  # * To allow type hints

from datetime import datetime
from enum import StrEnum, auto
from typing import Self


class TransactionType(StrEnum):
    DEPOSIT = auto()
    WITHDRAWAL = auto()
    TRANSFER = auto()


Transaction = tuple[TransactionType, datetime, int]


class InsufficientBalanceError(Exception):
    ...


class BankAccount:
    """Represents a bank account entity"""

    def __init__(self, initial_balance: int = 0) -> None:
        self._balance = initial_balance
        self._transaction_history: list[Transaction] = []

    def deposit(self, amount: int) -> None:
        """Send money to the account.

        Parameters
        ----------
        amount : int
             Amount sent in cents.
        """
        self._balance += amount
        self._transaction_history.append(
            (TransactionType.DEPOSIT, datetime.now(), amount)
        )

    def withdraw(self, amount: int) -> None:
        """Get money from the account in cash

        Parameters
        ----------
        amount : int
            Amount to get in cents.

        Raises
        ------
        InsufficientBalanceError
            When there is no balance to proceed with operation.
        """
        if self._sufficient_balance(amount):
            self._balance -= amount
            self._transaction_history.append(
                (TransactionType.WITHDRAWAL, datetime.now(), amount)
            )
        else:
            raise InsufficientBalanceError

    def transfer(self, other: Self, amount: int) -> None:
        if self._sufficient_balance(amount):
            timestamp: datetime = datetime.now()
            self._balance -= amount
            other._balance += amount
            # ! Can't append operation at other instance class
            self._transaction_history.append(
                (TransactionType.TRANSFER, timestamp, amount)
            )
        else:
            raise InsufficientBalanceError

    def _sufficient_balance(self, amount: int) -> bool:
        """Check if the balance is non-negative.

        Parameters
        ----------
        amount : int
           Amount to compare with balance.

        Returns
        -------
        bool
            True if resulting balance is non-negative, false otherwhise.
        """
        return amount <= self._balance

    @property
    def balance(self) -> int:
        """Account balance.

        Returns
        -------
        int
            Money within account.
        """
        return self._balance

    @property
    def transaction_history(self) -> list[Transaction]:
        """All the historical transactions from the account.

        Returns
        -------
        list[Transaction]
            List of transactions.
        """
        return self._transaction_history


def main() -> None:
    account1 = BankAccount(initial_balance=100)
    account2 = BankAccount(initial_balance=50)

    account1.transfer(account2, 50)

    print(account1.balance)


if __name__ == "__main__":
    main()
