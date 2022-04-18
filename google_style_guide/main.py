import logging
from typing import List

from my_package import module


# careful with too many default arguments
def compute_total_price(unit_price: int, quantity: int = 1, discount_perc: float = 0):
    total = unit_price * quantity
    return int((1 - discount_perc) * total)


# TODO never use mutable arguments as default value
# ex. my_list: List[int] = []
# print(oops())
# print(oops())
# [30]
# [30, 30]
# correct way ->
# [30]
# [30]
def oops(my_list: List[int] = None):
    if my_list is None:
        my_list = []
    my_list.append(30)
    return my_list


# TODO main function helps limit global vars
#  to local vars = keeps env less polluted
def main():
    price = 340_00
    discount = 0.15
    print(
        f"Total price minus discount: $"
        f"{compute_total_price(price, discount_perc=discount)/100:.2f}"
    )

    print(oops())
    print(oops())

    logging.basicConfig(level=logging.INFO)

    # TODO as imports is better to reference the package so
    #  it is easier to follow back to the source
    module.my_function()


if __name__ == "__main__":
    main()
