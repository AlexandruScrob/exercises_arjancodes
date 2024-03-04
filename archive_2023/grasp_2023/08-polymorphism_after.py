from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Converter:
    """Apply a unit conversion according to the specified formula."""

    formula: formula

    def convert(self, input_value: float) -> None:
        self.formula.apply_conversion(input_value)


class Formula(ABC):
    """Interface for unit transformations."""

    @abstractmethod
    def apply_conversion(self, input_value: float) -> None:
        raise NotImplementedError("Subclass should implement calculate method.")


class InchesToCentimeters(Formula):
    """Inch to centimeter transformation."""

    def apply_conversion(self, input_value: float) -> None:
        """Print input value transformed from inches to centimeters."""
        output_value = input_value * 2.54
        print(f"{input_value} inches becomes {output_value:.4f} centimeters.")


class MilesToKilometers(Formula):
    """Miles to kilometers transformation."""

    def apply_conversion(self, input_value: float) -> None:
        """Print input value transformed from miles to km."""
        output_value = input_value * 1.609
        print(f"{input_value} miles becomes {output_value:.4f} kilometers.")


class PoundsToKilograms(Formula):
    """Pounds to kilograms transformation."""

    def apply_conversion(self, input_value: float) -> None:
        """Print input value transformed from pounds to kg."""
        output_value = input_value / 2.205
        print(f"{input_value} pounds becomes {output_value:.4f} kilograms.")


def main() -> None:
    input_value = 1

    inches_to_cm_conv = Converter(InchesToCentimeters())
    inches_to_cm_conv.convert(input_value)

    miles_to_km = Converter(MilesToKilometers())
    miles_to_km.convert(input_value)

    pounds_to_kg = Converter(PoundsToKilograms())
    pounds_to_kg.convert(input_value)


if __name__ == "__main__":
    main()
