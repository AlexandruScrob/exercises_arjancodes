"""
Basic example showing how to read and validate data from a file using Pydantic.
"""

import json
import pydantic
from typing import Optional, List


class ISBN10FormatError(Exception):
    """Custom error that is raised when ISBN10
    doesn't have the right format."""

    def __init__(self, value: str, message: str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)


class ISBNMissingError(Exception):
    """Custom error that is raised when both
    ISBN10 and ISBN10 are missing."""

    def __init__(self, title: str, message: str) -> None:
        self.title = title
        self.message = message
        super().__init__(message)


class Book(pydantic.BaseModel):
    title: str
    author: str
    publisher: str
    price: float
    isbn_10: Optional[str]
    isbn_13: Optional[str]
    subtitle: Optional[str]

    # before it converts values into a model or after
    @pydantic.root_validator(pre=True)
    @classmethod
    def check_isbn10_or_isbn13(cls, values):
        """Make sure there is either an isbn10 or isbn13 value defined."""
        if "isbn_10" not in values and "isbn13" not in values:
            raise ISBNMissingError(
                title=values["title"],
                message="Document should be either an ISBN10 or ISBN13"
            )
        return values

    @pydantic.validator("isbn_10")
    @classmethod
    def isbn_10_valid(cls, value):
        """Validator to check whether ISBN10 has a valid value."""
        chars = [c for c in value if c in "0123456789xX"]

        if len(chars) != 10:
            raise ISBN10FormatError(
                value=value, message="ISBN10 should be 10 digits.")

        def char_to_int(char: str) -> int:
            if char in "xX":
                return 10
            return int(char)

        weighted_sum = sum((10 - i) * char_to_int(x)
                           for i, x in enumerate(chars))

        if weighted_sum % 11 != 0:
            raise ISBN10FormatError(
                value=value, message="ISBN10 digit sum should be divisible "
                                     "by 11")

        return value

    class Config:
        """Pydantic config class"""

        allow_mutation = False  # books are now immutable objects
        anystr_lower = True


def main() -> None:
    """Main function."""

    # Read data from a JSON file
    with open("./data.json") as file:
        data = json.load(file)
        books: List[Book] = [Book(**item) for item in data]
        print(books[0].title)
        # books[0].title = "Example title"
        print(books[0].dict(include={"price"}))


if __name__ == "__main__":
    main()
