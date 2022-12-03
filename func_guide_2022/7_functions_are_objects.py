import logging
from typing import Callable
from functools import partial


def handle_stripe_payment(amount: int) -> None:
    logging.info(f"Charging ${amount/100:.2f} using Stripe")


PRICES = {
    "burger": 10_00,
    "fries": 5_00,
    "drink": 2_00,
    "salad": 15_00,
}


HandlePaymentFn = Callable[[int], None]


def order_food(items: list[str], payment_handler: HandlePaymentFn) -> None:
    total = sum(PRICES[item] for item in items)
    logging.info(f"Order total is ${total/100:.2f}.")
    payment_handler(total)
    logging.info("Order completed.")


order_food_stripe = partial(order_food, payment_handler=handle_stripe_payment)


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    order_food_stripe(["burger", "fries", "drink"])


if __name__ == "__main__":
    main()
