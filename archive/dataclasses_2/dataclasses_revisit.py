from ast import alias
from dataclasses import dataclass, field
import random
import string
from typing import List


def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))


# kw_only makes so you initialize only using kw arguments
# match_args -> support pattern matching
# using slots makes that instances variables are accessed much faster
@dataclass(slots=True)  # (match_args=True)  # (kw_only=True)  # (frozen=True)
class Person:
    name: str
    address: str
    active: bool = True
    email_addresses: List[str] = field(default_factory=list)
    # with init=False the field won't be part of the initializer
    id: str = field(default_factory=generate_id, init=False)
    _search_string: str = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._search_string = f"{self.name} {self.address}"


def main() -> None:
    person = Person(name="John", address="123 Main St")
    # person.name = "Alex"
    # print(person.__dict__["name"])
    print(person)


if __name__ == "__main__":
    main()
