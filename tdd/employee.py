"""
Very advanced Employee management system.
"""
from dataclasses import dataclass


@dataclass
class Employee:
    """Basic representation of an employee."""

    name: str
    employee_id: int
    pay_rate: float = 100.0
    hours_worked: float = 0.0
    employer_cost: float = 1000.0
    employer_office_costs: float = 200.0
    employer_401k_costs: float = 400
    employer_support_costs: float = 400.0
    has_commission: bool = True
    commission: float = 100.0
    contracts_landed: int = 0

    def compute_payout(self) -> float:
        """Compute how much the employee should be paid."""
        employer_cost = (
                self.employer_401k_costs
                + self.employer_office_costs
                + self.employer_support_costs
        )
        payout = self.pay_rate * self.hours_worked + employer_cost

        if self.has_commission:
            payout += self.commission * self.contracts_landed
        return payout
