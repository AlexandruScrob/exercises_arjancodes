from decimal import Decimal, getcontext


def main() -> None:
    print(1.1 + 2.2)

    print(Decimal("1.1") + Decimal("2.2"))

    getcontext().prec = 10  # set precision
    print(Decimal("1.1") + Decimal("2.2"))


if __name__ == "__main__":
    main()
