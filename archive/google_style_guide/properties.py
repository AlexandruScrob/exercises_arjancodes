from dataclasses import dataclass, field


@dataclass
class LineItem:
    name: str
    price: int
    quantity: int = 1

    # properties should be simple and predictable
    @property
    def total_price(self) -> int:
        return self.price * self.quantity


@dataclass
class Order:
    items: list[LineItem] = field(default_factory=list)

    def add_item(self, item: LineItem):
        self.items.append(item)

    @property
    def total_price(self) -> int:
        return sum(item.total_price for item in self.items)


def main():
    order = Order()
    order.add_item(LineItem("carrots", price=20, quantity=10))
    order.add_item(LineItem("eggs", price=20, quantity=5))

    print(f"Total price: ${order.total_price/100:.2f}")


if __name__ == "__main__":
    main()
