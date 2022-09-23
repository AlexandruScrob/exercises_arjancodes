import datetime
from dataclasses import dataclass
from string import Template
from timeit import timeit


@dataclass
class User:
    first_name: str
    last_name: str

    # __str__ -> user friendly
    # __repr__ -> dev friendly
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


def main():
    # numbers
    number = 800
    print(f"The number is hex: {number:x}, octo: {number:o}, scientific: {number:e}.")
    print(f"Number: {number:06}")  # 000800, this type filling works only with numbers
    print(f"Decimal places with rounding: {100.21612321:.2f}")  # 100.22
    print(f"{44000000000:,.2f}")  # 44,000,000,000.00
    # percentages
    print(f"{0.34567:.2%}")  # 34.57%

    # for number in range(5, 15):
    #     print(f"The number is {number:4}.")  # default value for filling " "

    # strings
    greet = "Hi"
    print(f"{greet:>10}")  # works with strings, align to the right
    print(f"{greet:^10}")  # align to the center
    print(f"{greet:<10}")  # align to the center, align to the left
    print(f"{greet:_>10}")  # ________Hi
    print(f"{greet:_<10}")  # Hi________

    # dataclasses, str, repr
    user = User("Elon", "Musk")
    # it first tries to find a __str__ then it uses the __repr__
    print(f"User: {user}. using repr: {user!r}")  # or use repr(user)
    name = "Elon"
    print(f"Who wants to buy Twitter? {name!r}")  # 'Elon'

    # dates and times
    today = datetime.datetime.now()
    print(f"{today:%Y-%m-%d %H:%M:%S.%f}")
    print(f"{today:%D}")  # 09/12/22
    print(f"{today:%T}")  # 14:42:58
    print(f"{today:%A, %B %d, %Y}")  # Monday, September 12, 2022
    print(f"{today:%x} {today:%X}")  # x for current locale, and X for adjusted time

    # special characters
    print(f"{{single braces}}, {{{{double braces}}}}")  # {single braces}, {{double braces}}
    print(f"{'single qutoes'}, {{\"double quotes\"}} ")

    dictionary = {"hello": "world"}
    print(f"Hello, {dictionary['hello']}")

    # debugging variables
    x = 45
    y = 75
    print(f"{x = }, {y=}")  # x=45, y=75

    name = "Arjan"
    country = "The Netherlands"
    channel = "ArjanCodes"
    sentence = (
        f"Hi, I'm {name}." f"I'm from a beautiful country called {country}." f"I run a YT channel called {channel}."
    )

    print(sentence)


def perc_format():
    name = "Arjan"
    country = "The Netherlands"
    _ = "%s is from %s." % (name, country)


def str_format():
    name = "Arjan"
    country = "The Netherlands"
    _ = "{} is from {}".format(name, country)


def f_strings():
    name = "Arjan"
    country = "The Netherlands"
    _ = f"{name} is from {country}."


TEMPLATE = Template("$name is from $country.")


def template():
    name = "Arjan"
    country = "The Netherlands"
    _ = TEMPLATE.substitute(name=name, country=country)


if __name__ == "__main__":
    main()

    print("perc_format:", timeit(perc_format, number=100000))
    print("str_format:", timeit(str_format, number=100000))
    print("f_strings:", timeit(f_strings, number=100000))
    print("template:", timeit(template, number=100000))

    # perc_format: 0.018680499997572042
    # str_format: 0.017827600000600796
    # f_strings: 0.011517200000525918
    # template: 0.15447370000038063
