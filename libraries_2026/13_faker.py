from dataclasses import dataclass

from faker import Faker


@dataclass(frozen=True)
class Device:
    hostname: str
    owner: str
    company: str
    city: str


def create_device(fake: Faker) -> Device:
    return Device(
        hostname=fake.hostname(),
        owner=fake.name(),
        company=fake.company(),
        city=fake.city(),
    )


def main() -> None:
    us = Faker("en_US")
    nl = Faker("nl_NL")

    print("US")
    print(create_device(us))

    print()

    print("NL")
    print(create_device(nl))


if __name__ == "__main__":
    main()
