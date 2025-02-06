# Abstraction using ABCs:

from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> None:
        pass


class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> None:
        print(f"Processing ${amount} payment via PayPal.")


class StripeProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> None:
        print(f"Processing ${amount} payment via Stripe.")


def process_order(amount: float, processor: PaymentProcessor) -> None:
    processor.process_payment(amount)


paypal = PayPalProcessor()
stripe = StripeProcessor()
process_order(100.0, paypal)
process_order(200.0, stripe)

# Processing $100.0 payment via PayPal.
# Processing $200.0 payment via Stripe.

# Abstracting a logger using a protocol:

from typing import Protocol


class Logger(Protocol):
    def log(self, message: str) -> None:
        pass


class ConsoleLogger:
    def log(self, message: str) -> None:
        print(f"LOG: {message}")


class FileLogger:
    def log(self, message: str) -> None:
        with open("log.txt", "a") as file:
            file.write(f"{message}\n")


def perform_task(logger: Logger) -> None:
    logger.log("Task started.")
    # Simulate a task
    logger.log("Task completed.")


console_logger = ConsoleLogger()
file_logger = FileLogger()
perform_task(console_logger)  # Output: LOG: Task started. LOG: Task completed.
perform_task(file_logger)  # Logs to a file.

# LOG: Task started.
# LOG: Task completed.
