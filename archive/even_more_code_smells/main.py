from even_more_code_smells.pos.costumer import Customer
from even_more_code_smells.pos.line_item import LineItem
from even_more_code_smells.pos.payment import StripePaymentProcessor
from pos.order import Order
from pos.system import POSSystem


def main() -> None:
    # create the POS system and setup the payment processor
    payment_processor = StripePaymentProcessor.create("https://api.stripe.com/v2")
    system = POSSystem(payment_processor)

    # create a customer
    customer = Customer(
        id=12345,
        name="Arjan",
        address="Sesame street 104",
        postal_code="1234",
        city="Amsterdam",
        email="hi@arjancodes.com",
    )

    # create the order
    order = Order(customer)

    order.add_line_item(LineItem(item="Keyboard", quantity=1, price=5000))
    order.add_line_item(LineItem(item="SSD", quantity=1, price=15000))
    order.add_line_item(LineItem(item="USB cable", quantity=2, price=500))

    # register and process the order
    system.register_order(order)
    system.process_order(order)


if __name__ == "__main__":
    main()
