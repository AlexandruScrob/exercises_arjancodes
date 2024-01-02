import timeit
from dataclasses import dataclass
from functools import partial


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
class EmployeeSlots:
    dept: str


def get_set_delete(person: Person | PersonSlots):
    person.address = "123 Main St"
    person.address
    del person.address


# NOTE: slots break when trying to use multiple inheritance
# class PersonEmployee(PersonSlots, EmployeeSlots):
#     pass
# TypeError: multiple bases have instance lay-out conflict


def main():
    person = Person("John", "123 Main St", "john@doe.com")
    person_slots = PersonSlots("John", "123 Main St", "john@doe.com")

    no_slots = min(timeit.repeat(partial(get_set_delete, person), number=1000))
    slots = min(timeit.repeat(partial(get_set_delete, person_slots), number=1000))

    print(f"No slots: {no_slots}.")
    print(f"Slots: {slots}.")


if __name__ == "__main__":
    main()

    # No slots: 0.0001444000517949462
    # Slots: 0.00010929990094155073
