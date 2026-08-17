from autoregistry import Registry

payment_providers = Registry()


@payment_providers
class StripePaymentProvider:
    name = "stripe"

    def charge(self, amount: float) -> str:
        return f"Paid {amount} with Stripe"


@payment_providers
class MolliePaymentProvider:
    name = "mollie"

    def charge(self, amount: float) -> str:
        return f"Paid {amount} with Mollie"


def main() -> None:
    provider_cls = payment_providers["StripePaymentProvider"]
    provider = provider_cls()

    result = provider.charge(49.95)
    print(result)


if __name__ == "__main__":
    main()
