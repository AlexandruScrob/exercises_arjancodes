from decimal import Decimal

from statemachine import State, StateMachine


class PaymentMachine(StateMachine):
    pending = State("Pending", initial=True)
    authorized = State("Authorized")
    captured = State("Captured", final=True)
    cancelled = State("Cancelled", final=True)

    authorize = pending.to(authorized)
    capture = authorized.to(captured)
    cancel = pending.to(cancelled) | authorized.to(cancelled)

    def before_authorize(self, amount: Decimal) -> None:
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        print(f"Authorizing payment for €{amount}")

    def after_authorize(self, amount: Decimal) -> None:
        print(f"Payment authorized for €{amount}")

    def before_capture(self) -> None:
        print("Capturing payment...")

    def after_capture(self) -> None:
        print("Payment captured.")

    def after_cancel(self) -> None:
        print("Payment cancelled.")


def print_configuration(machine: PaymentMachine) -> None:
    active_states = ", ".join(state.id for state in machine.configuration)
    print(f"Active state(s): {active_states}")


def main() -> None:
    payment = PaymentMachine()

    print_configuration(payment)

    payment.authorize(Decimal("49.95"))
    print_configuration(payment)

    payment.capture()
    print_configuration(payment)

    # This would raise an exception because "captured" is a final state:
    # payment.cancel()


if __name__ == "__main__":
    main()
