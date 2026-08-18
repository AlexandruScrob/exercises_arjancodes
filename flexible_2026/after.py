from dataclasses import dataclass
from decimal import Decimal
from enum import StrEnum

from pydantic import BaseModel, Field


class SeatType(StrEnum):
    STANDARD = "standard"
    EXTRA_LEGROOM = "extra_legroom"
    DUTCH = "dutch"


class FlightStatus(StrEnum):
    SCHEDULED = "scheduled"
    CANCELLED = "cancelled"


@dataclass(frozen=True)
class Money:
    amount: Decimal

    def __post_init__(self) -> None:
        if self.amount < Decimal("0"):
            raise ValueError("money cannot be negative.")

    def discounted(self, percentage: Decimal) -> "Money":
        return Money(self.amount * (Decimal("1") - percentage))

    def __str__(self) -> str:
        return f"{self.amount:.2f}"


@dataclass(frozen=True)
class Passenger:
    name: str
    loyalty: bool = False


@dataclass(frozen=True)
class Flight:
    number: str
    price: Money
    status: FlightStatus

    def ensure_bookable(self) -> None:
        if self.status == FlightStatus.CANCELLED:
            raise ValueError("Flight cancelled")


@dataclass(frozen=True)
class BookingRequest:
    passenger: Passenger
    flight: Flight
    seat: SeatType = SeatType.STANDARD


class BookingInput(BaseModel):
    passenger_name: str
    flight_number: str
    price: Decimal = Field(gt=0)
    status: FlightStatus
    loyalty: bool = False
    seat: SeatType = SeatType.STANDARD

    def to_domain(self) -> BookingRequest:
        return BookingRequest(
            passenger=Passenger(name=self.passenger_name, loyalty=self.loyalty),
            flight=Flight(
                number=self.flight_number, price=Money(self.price), status=self.status
            ),
            seat=self.seat,
        )


def create_booking(request: BookingRequest) -> None:
    flight = request.flight
    passenger = request.passenger

    flight.ensure_bookable()

    discount = Decimal("0.10") if passenger.loyalty is True else Decimal("0")
    total = flight.price.discounted(discount)

    print(
        f"Booked {flight.number} "
        f"for {passenger.name} "
        f"at €{total} "
        f"in seat {request.seat}"
    )


def main() -> None:
    raw_data = {
        "passenger_name": "Ada",
        "flight_number": "AC123",
        "price": "250.00",
        "status": "scheduled",
        "loyalty": True,
        "seat": "extra_legroom",
    }
    request = BookingInput.model_validate(raw_data).to_domain()
    # request = BookingRequest(
    #     passenger=Passenger(name="Ada", loyalty=True),
    #     flight=Flight(
    #         number="AC123",
    #         price=Money(amount=Decimal("250.00")),
    #         status=FlightStatus.SCHEDULED,
    #     ),
    #     seat=SeatType.EXTRA_LEGROOM,
    # )

    create_booking(request)


if __name__ == "__main__":
    main()
