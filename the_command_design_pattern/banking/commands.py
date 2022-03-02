from dataclasses import dataclass, field
from typing import List
from banking.account import Account
from banking.transaction import Transaction


@dataclass
class Deposit:
    account: Account
    amount: int

    @property
    def transaction_details(self) -> str:
        return f"${self.amount / 100:.2f} to account {self.account.name}"

    def execute(self) -> None:
        self.account.deposit(self.amount)
        print(f"Deposited {self.transaction_details}")

    def undo(self) -> None:
        self.account.withdraw(self.amount)
        print(f"Undid deposit of {self.transaction_details}")

    def redo(self) -> None:
        self.account.deposit(self.amount)
        print(f"Redid deposit of {self.transaction_details}")


@dataclass
class Withdrawl:
    account: Account
    amount: int

    @property
    def transaction_details(self) -> str:
        return f"${self.amount / 100:.2f} to account {self.account.name}"

    def execute(self) -> None:
        self.account.withdraw(self.amount)
        print(f"Withdrawn {self.transaction_details}")

    def undo(self) -> None:
        self.account.deposit(self.amount)
        print(f"Undid withdrawal of {self.transaction_details}")

    def redo(self) -> None:
        self.account.withdraw(self.amount)
        print(f"Redid withdrawal of {self.transaction_details}")


@dataclass
class Transfer:
    from_account: Account
    to_account: Account
    amount: int

    @property
    def transaction_details(self) -> str:
        return (
            f"${self.amount/100:.2f} from account "
            f"{self.from_account.name} to account {self.to_account.name}"
        )

    def execute(self) -> None:
        self.from_account.withdraw(self.amount)
        self.to_account.deposit(self.amount)
        print(f"Transferred {self.transaction_details}")

    def undo(self) -> None:
        self.to_account.withdraw(self.amount)
        self.from_account.deposit(self.amount)
        print(f"Undid Transfer of {self.transaction_details}")

    def redo(self) -> None:
        self.from_account.withdraw(self.amount)
        self.to_account.deposit(self.amount)
        print(f"Redid Transfer of {self.transaction_details}")


@dataclass
class Batch:
    commands: List[Transaction] = field(default_factory=list)

    def execute(self) -> None:
        completed_commands: List[Transaction] = []

        try:
            for command in self.commands:
                command.execute()
                completed_commands.append(command)

        except ValueError:
            for command in reversed(completed_commands):
                command.undo()

    def undo(self) -> None:
        for command in reversed(self.commands):
            command.undo()

    def redo(self) -> None:
        for command in self.commands:
            command.redo()
