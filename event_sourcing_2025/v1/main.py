from event_store import EventStore
from inventory import Inventory


def main() -> None:
    store = EventStore()
    inventory = Inventory(store)

    inventory.add_item("sword")
    inventory.add_item("potion")
    inventory.add_item("bow")
    inventory.add_item("shield")
    inventory.add_item("torch")

    print(inventory.get_items())
    print(inventory.get_count("shield"))

    inventory.remove_item("shield")

    print(inventory.get_items())
    print(inventory.get_count("shield"))

    inventory.remove_item("bow")
    inventory.add_item("banana")

    print(inventory.get_items())


if __name__ == "__main__":
    main()
