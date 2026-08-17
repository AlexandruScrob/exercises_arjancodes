from dataclasses import dataclass
from decimal import Decimal

from dishka import Provider, Scope, make_container, provide


@dataclass(frozen=True)
class Payment:
    customer_id: str
    amount: Decimal
    currency: str


class PaymentRepository:
    def save(self, payment: Payment) -> None:
        print(f"Saving payment for customer {payment.customer_id}")


class StripePaymentGateway:
    def charge(self, payment: Payment) -> str:
        print(f"Charging {payment.amount} {payment.currency} via Stripe")
        return "payment_123"


class PaymentService:
    def __init__(
        self,
        repository: PaymentRepository,
        gateway: StripePaymentGateway,
    ) -> None:
        self.repository = repository
        self.gateway = gateway

    def process_payment(self, payment: Payment) -> str:
        payment_id = self.gateway.charge(payment)
        self.repository.save(payment)
        return payment_id


class AppProvider(Provider):
    @provide(scope=Scope.APP)
    def payment_repository(self) -> PaymentRepository:
        return PaymentRepository()

    @provide(scope=Scope.APP)
    def payment_gateway(self) -> StripePaymentGateway:
        return StripePaymentGateway()

    @provide(scope=Scope.REQUEST)
    def payment_service(
        self,
        repository: PaymentRepository,
        gateway: StripePaymentGateway,
    ) -> PaymentService:
        return PaymentService(repository, gateway)


def process_checkout(
    customer_id: str,
    amount: Decimal,
    currency: str,
    service: PaymentService,
) -> str:
    payment = Payment(
        customer_id=customer_id,
        amount=amount,
        currency=currency,
    )

    return service.process_payment(payment)


def main() -> None:
    container = make_container(AppProvider())

    with container() as request_container:
        service = request_container.get(PaymentService)

        payment_id = process_checkout(
            customer_id="cust_123",
            amount=Decimal("49.95"),
            currency="EUR",
            service=service,
        )

    print(f"Payment completed: {payment_id}")


if __name__ == "__main__":
    main()
