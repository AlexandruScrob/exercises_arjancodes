from abc import ABC, abstractmethod
from dataclasses import dataclass


PAYOUT_HOLIDAY_DAYS = 5


@dataclass
class Employee:
    """Basic representation of an employee at the company."""

    name: str
    role: str
    vacation_days: int = 25

    def payout_holiday(self) -> None:
        """Let the employee pay out 5 holidays."""
        if self.vacation_days < PAYOUT_HOLIDAY_DAYS:
            raise ValueError(
                f"You don't have enough holidays left over for a payout.\
                    Remaining holidays: {self.vacation_days}."
            )
        self.vacation_days -= PAYOUT_HOLIDAY_DAYS
        print(f"Paying out a holiday. Holidays left: {self.vacation_days}")

    def take_a_single_holiday(self) -> None:
        """Let the employee take a single holiday."""
        # check whether the employee still has holidays left
        if self.vacation_days < 1:
            raise ValueError("You don't have any holidays left. Now back to work, you!")
        self.vacation_days -= 1
        print("Have fun on your holiday. Don't forget to check your emails!")


@dataclass
class HourlyEmployee(Employee):
    hourly_rate: float = 50
    amount: int = 10


@dataclass
class SalariedEmployee(Employee):
    monthly_salary: float = 5000


class Company:
    """Represents a company with employees."""

    def __init__(self) -> None:
        self.employees: list[Employee] = []

    def add_employee(self, employee: Employee) -> None:
        self.employees.append(employee)

    def find_by_role(self, role: str) -> list[Employee]:
        return [e for e in self.employees if e.role == role]

    def pay_employee(self, employee: Employee) -> None:
        if isinstance(employee, SalariedEmployee):
            print(
                f"Paying employee {employee.name} a monthly salary of ${employee.monthly_salary}."
            )
        elif isinstance(employee, HourlyEmployee):
            print(
                f"Paying employee {employee.name} a hourly rate of \
                ${employee.hourly_rate} for {employee.amount} hours."
            )


class Notification(ABC):
    """Abstract base class for notifications."""

    @abstractmethod
    def send(self, employee: Employee, message: str) -> None:
        pass


def send_email(employee: Employee, message: str) -> None:
    print(f"Sending email to {employee.name}: {message}")


def send_sms(employee: Employee, message: str) -> None:
    print(f"Sending SMS to {employee.name}: {message}")


def main() -> None:
    """Main function."""

    company = Company()

    louis = SalariedEmployee(name="Louis", role="manager")
    company.add_employee(louis)
    company.add_employee(HourlyEmployee(name="Brenda", role="president"))
    company.add_employee(HourlyEmployee(name="Tim", role="support"))

    print(company.find_by_role("vice-president"))
    print(company.find_by_role("manager"))
    print(company.find_by_role("support"))
    company.pay_employee(company.employees[0])
    company.employees[0].take_a_single_holiday()

    send_email(employee=louis, message="Your leave request is approved.")


if __name__ == "__main__":
    main()
