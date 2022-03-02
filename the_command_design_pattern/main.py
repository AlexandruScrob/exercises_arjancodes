from banking.bank import Bank
from banking.controller import BankController
from banking.commands import Deposit, Withdrawl, Transfer
from banking.commands import Batch


def main() -> None:

    # create a bank
    bank = Bank()

    # create a bank controller
    controller = BankController()

    # create some accounts
    account1 = bank.create_account("ArjanCodes")
    account2 = bank.create_account("Google")
    account3 = bank.create_account("Microsoft")

    controller.execute(Deposit(account1, 100000))

    controller.execute(
        Batch(
            commands=[
                Deposit(account2, 100000),
                Transfer(from_account=account2, to_account=account1, amount=50000),
            ]
        )
    )
    controller.undo()
    print(bank)
    controller.redo()

    controller.execute(Deposit(account3, 100000))

    controller.undo()
    controller.redo()

    controller.execute(Withdrawl(account1, 150000))

    controller.undo()

    print(bank)


if __name__ == "__main__":
    main()
