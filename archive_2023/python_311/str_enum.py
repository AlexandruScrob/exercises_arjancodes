from enum import Enum, StrEnum, auto


class Color(StrEnum):
    WHITE = auto()
    BLACK = auto()


def main() -> None:
    print(Color.BLACK.value)


if __name__ == "__main__":
    main()
