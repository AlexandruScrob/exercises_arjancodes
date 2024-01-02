class Order:
    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total

    def pay(self, payment_type, security_code):
        if payment_type == "debit":
            print("Processing debit payment type")
            print(f"Verifying security code: {security_code}")
            self.status = "paid"

        elif payment_type == "credit":
            print("Processing credit payment type")
            print(f"Verifying security code: {security_code}")
            self.status = "paid"

        else:
            raise Exception(f"Unknown payment type: {payment_type}")


class PaymentProcessor:
    @staticmethod
    def set_status(order_type):
        order.status = order_type

    def pay_credit(self, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        self.set_status("credit")

    def pay_debit(self, security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        self.set_status("debit")


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())

processor = PaymentProcessor()
processor.pay_credit("0372846")
