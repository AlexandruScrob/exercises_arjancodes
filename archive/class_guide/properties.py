from functools import lru_cache

from dataclasses import dataclass

from email_tools.service import EmailService

SMTP_SERVER = "smtp.gmail.com"
PORT = 465
EMAIL = "hi@arjancodes.com"
PASSWORD = "password"


@lru_cache
def bmi(weight: float, height: float) -> float:
    return weight / (height**2)


@lru_cache
def bmi_category(bmi_value: float) -> str:
    if bmi_value < 18.5:
        return "Underweight"
    elif bmi_value < 25:
        return "Normal"
    elif bmi_value < 30:
        return "Overweight"
    else:
        return "Obese"


@dataclass
class Stats:
    gender: str
    height: float
    weight: float
    blood_type: str
    eye_color: str
    hair_color: str


@dataclass
class Address:
    address_line_1: str
    address_line_2: str
    city: str
    country: str
    postal_code: str

    def __str__(self) -> str:
        return f"{self.address_line_1}, {self.address_line_2}, {self.city}, {self.country}, {self.postal_code}"


@dataclass
class Person:
    name: str
    age: int
    email: str
    phone_number: str
    address: Address
    stats: Stats

    @property
    def split_name(self) -> tuple[str, str]:
        first_name, last_name = self.name.split(" ")
        return first_name, last_name

    def update_email(self, email: str) -> None:
        self.email = email
        # send email to the new address
        email_service = EmailService(SMTP_SERVER, PORT, EMAIL, PASSWORD)
        email_service.send_message(
            to_email=self.email,
            subject="Your email has been updated.",
            body="Your email has been updated. If this was not you, you have a problem.",
        )


def main() -> None:
    # create an address
    address = Address(
        address_line_1="123 Main St",
        address_line_2="Apt 1",
        city="New York",
        country="USA",
        postal_code="12345",
    )

    # create stats
    stats = Stats(
        gender="Male",
        height=1.8,
        weight=80,
        blood_type="A+",
        eye_color="Brown",
        hair_color="Black",
    )

    # create a person
    person = Person(
        name="John Doe",
        age=30,
        address=address,
        stats=stats,
        email="johndoe@gmail.com",
        phone_number="123-456-7890",
    )

    # compute the BMI
    bmi_value = bmi(stats.weight, stats.height)
    print(f"Your BMI is {bmi_value:.2f}")
    print(f"Your BMI category is {bmi_category(bmi_value)}")

    # update the email address
    person.update_email("johndoe@outlook.com")


if __name__ == "__main__":
    main()
