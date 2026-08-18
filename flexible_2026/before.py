from decimal import Decimal
from typing import Any


def create_booking(data: dict[str, Any], **kwargs: Any) -> None:
    if data["status"] == "cancelled":
        raise ValueError("Flight cancelled")

    price = Decimal(data["price"])

    discount = Decimal("0.10") if data.get("loyalty") else Decimal("0")
    total = price * (Decimal("1") - discount)

    print(
        f"Booked {data['flight_number']} "
        f"for {data['passenger_name']} "
        f"at €{total} "
        f"in seat {kwargs.get('seat', 'standard')}"
    )


def main() -> None:
    booking = {
        "passenger_name": "Ada",
        "flight_number": "AC123",
        "price": "250.00",
        "status": "scheduled",
        "loyalty": True,
    }

    create_booking(
        booking,
        seat="extra_legroom",
    )


if __name__ == "__main__":
    main()
