from dataclasses import dataclass
from functools import partial
import timeit


@dataclass(slots=False)
class Person:
    name: str
    address: str
    email: str


@dataclass(slots=True)
class PersonSlots:
    name: str
    address: str
    email: str


@dataclass(slots=True)
class Employee:
    dept: str


# TypeError: multiple bases have instance lay-out conflict
# but you can combine a slots class with a regular class
# class PersonEmployee(PersonSlots, Employee):
#     pass


def get_set_delete(person: Person | PersonSlots):
    person.address = "123 Main St"
    _ = person.address
    del person.address


def main():
    person = Person("John", "123 Main St", "john@doe.com")
    person_slots = PersonSlots("John", "123 Main St", "john@doe.com")

    no_slots = min(timeit.repeat(partial(get_set_delete, person), number=1000000))
    slots = min(timeit.repeat(partial(get_set_delete, person_slots), number=1000000))
    print(f"no slots: {no_slots}")
    print(f"Slots: {slots}")
    print(f"% performance improvements: {(no_slots - slots) / no_slots:.2%}")


if __name__ == "__main__":
    main()


# no slots: 0.13213440001709387
# Slots: 0.1047205000068061
# % performance improvements: 20.75%
