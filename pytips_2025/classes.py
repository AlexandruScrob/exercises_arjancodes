# Use a class when you need to encapsulate behavior and data together. Classes are ideal for creating objects that have both state (attributes) and behavior (methods).

# from decimal import Decimal


# class ShoppingCart:
#     def __init__(self) -> None:
#         self.items = []

#     def add_item(self, item: str, price: Decimal) -> None:
#         self.items.append({"item": item, "price": price})

#     def total(self) -> Decimal:
#         return sum(item["price"] for item in self.items)


# cart = ShoppingCart()
# cart.add_item("apple", Decimal("1.5"))
# cart.add_item("banana", Decimal("2.0"))
# print(f"${cart.total():.2f}")

# $3.50

# A dataclass is a lightweight alternative to a class. It’s perfect for scenarios where you need to group related data but don’t need much behavior.

# from dataclasses import dataclass
# from decimal import Decimal


# @dataclass
# class Item:
#     name: str
#     price: Decimal


# item = Item(name="apple", price=Decimal("1.5"))
# print(item)
# print(f"${item.price:.2f}")

# Item(name='apple', price=Decimal('1.5'))
# $1.50

# Use a function for stateless operations: tasks that don’t require maintaining state over time and can be performed independently.


# def calculate_discounted_price(price: Decimal, discount: Decimal) -> Decimal:
#     return price - (price * discount / 100)


# discounted_price = calculate_discounted_price(Decimal("100"), Decimal("10"))
# print(f"${discounted_price:.2f}")

# $90.00

# Often, you’ll use these together for a complete solution.

from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Item:
    name: str
    price: Decimal


class ShoppingCart:
    def __init__(self) -> None:
        self.items: list[Item] = []

    def add_item(self, item: Item) -> None:
        self.items.append(item)

    def total(self) -> Decimal:
        return sum(item.price for item in self.items)


def calculate_discount(cart: ShoppingCart, discount: Decimal) -> Decimal:
    return cart.total() * (1 - discount / 100)


cart = ShoppingCart()
cart.add_item(Item("apple", Decimal("1.5")))
cart.add_item(Item("banana", Decimal("2.0")))

discounted_price = calculate_discount(cart, Decimal("10"))
print(f"${discounted_price:.2f}")

# $3.15
