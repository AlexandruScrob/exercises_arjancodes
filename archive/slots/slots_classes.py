from functools import partial
import timeit


class Person:
    def __init__(self, name: str, address: str, email: str) -> None:
        self.name = name
        self.address = address
        self.email = email


# Slots are aprox. 20% faster than dict generated dynamically (ex. Person class)
class PersonSlots:
    # NOTE you can add the dict to be able to add attributes
    __slots__ = (
        "name",
        "address",
        "email",
    )  # "__dict__"

    def __init__(self, name: str, address: str, email: str) -> None:
        self.name = name
        self.address = address
        self.email = email


class EmployeeSlots:
    __slots__ = ("dept",)

    def __init__(self, dept: str) -> None:
        self.dept = dept


def get_set_delete(person: Person | PersonSlots):
    person.address = "123 Main St"
    _ = person.address
    del person.address


def main():
    person = Person("John", "123 Main St", "john@doe.com")
    person_slots = PersonSlots("John", "123 Main St", "john@doe.com")

    no_slots = min(timeit.repeat(partial(get_set_delete, person), number=1000000))
    slots = min(timeit.repeat(partial(get_set_delete, person_slots), number=1000000))

    # person_slots.adding = "aaaa"
    print(f"no slots: {no_slots}")
    print(f"Slots: {slots}")
    print(f"% performance improvements: {(no_slots - slots) / no_slots:.2%}")


if __name__ == "__main__":
    main()

# NOTE: performance improvement with slots
# no slots: 0.13087920000543818
# Slots: 0.09896440000738949
# % performance improvements: 24.38%

# NOTE:
# it's not used as default because:
#  - it can interfere with mixins,
#  - may break older libaries,
#  - you can't add attributes dynamically (not recommended to do since it
#     causes ambiguity)
