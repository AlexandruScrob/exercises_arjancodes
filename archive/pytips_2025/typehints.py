# Type hints help others (and future you) understand your code better.


def average(numbers: list[int]) -> float:
    return sum(numbers) / len(numbers)


print(average([10, 20, 30]))  # Output: 20.0

# 20.0

# Type hints also help you write code that's more generic:

# from typing import Iterable


# def average(numbers: Iterable[int]) -> float:
#     return sum(numbers) / len(numbers)


# print(average((10, 20, 30)))  # Output: 20.0

# 20.0
