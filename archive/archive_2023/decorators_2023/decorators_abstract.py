import logging
from abc import ABC, abstractmethod
from math import sqrt
from time import perf_counter


def is_prime(number: int) -> bool:
    if number < 2:
        return False

    return all(number % element != 0 for element in range(2, int(sqrt(number)) + 1))


class AbstractComponent(ABC):
    @abstractmethod
    def execute(self, upper_bound: int) -> int:
        pass


class ConcreteComponent(AbstractComponent):
    def execute(self, upper_bound: int) -> int:
        return sum(bool(is_prime(number)) for number in range(upper_bound))


class AbstractDecorator(AbstractComponent):
    def __init__(self, decorated: AbstractComponent) -> None:
        self._decorated = decorated


class BenchmarkDecorator(AbstractDecorator):
    def execute(self, upper_bound: int) -> int:
        start_time = perf_counter()
        value = self._decorated.execute(upper_bound)
        end_time = perf_counter()
        run_time = end_time - start_time
        logging.info(
            f"Execution of {self._decorated.__class__.__name__} took {run_time:.2f} seconds"
        )
        return value


class LoggingDecorator(AbstractDecorator):
    def execute(self, upper_bound: int) -> int:
        logging.info(f"Calling {self._decorated.__class__.__name__}")
        value = self._decorated.execute(upper_bound)
        logging.info(f"Finished calling {self._decorated.__class__.__name__}")
        return value


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    component = ConcreteComponent()
    benchmark_decorator = BenchmarkDecorator(component)
    logging_decorator = LoggingDecorator(benchmark_decorator)
    value = logging_decorator.execute(100000)
    logging.info(f"Found {value} prime numbers.")


if __name__ == "__main__":
    main()
