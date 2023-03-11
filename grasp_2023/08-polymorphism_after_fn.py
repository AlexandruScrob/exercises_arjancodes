from __future__ import annotations

from enum import Enum, auto
from typing import Callable


class ConversionType(Enum):
    """Types of unit conversion."""

    INCHES_TO_CM = auto()
    MILES_TO_KM = auto()
    POUNDS_TO_KG = auto()


ConversionFunc = Callable[[float], None]


def convert(input_value: float, converter: ConversionFunc) -> None:
    converter(input_value)


def inches_to_cm(input_value: float) -> None:
    """Print input value transformed from inches to centimeters."""
    output_value = input_value * 2.54
    print(f"{input_value} inches becomes {output_value:.4f} centimeters.")


def miles_to_km(input_value: float) -> None:
    """Print input value transformed from miles to km."""
    output_value = input_value * 1.609
    print(f"{input_value} miles becomes {output_value:.4f} kilometers.")


def pounds_to_kg(input_value: float) -> None:
    """Print input value transformed from pounds to kg."""
    output_value = input_value / 2.205
    print(f"{input_value} pounds becomes {output_value:.4f} kilograms.")


def main() -> None:
    input_value = 1

    convert(input_value, inches_to_cm)
    convert(input_value, miles_to_km)
    convert(input_value, pounds_to_kg)


if __name__ == "__main__":
    main()
