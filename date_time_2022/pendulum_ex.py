import pendulum


def main() -> None:
    some_date = pendulum.datetime(2022, 10, 9, 18, 0, tz="UTC")
    print(some_date)

    print(some_date.in_timezone("Australia/Sydney"))

    my_date = pendulum.datetime(2013, 3, 31, 1, 59, 59, 999999, tz="Europe/Paris")
    print(my_date)
    my_date = my_date.add(microseconds=1)
    print(my_date)
    my_date = my_date.subtract(microseconds=1)
    print(my_date)

    pendulum.set_locale("it")
    print(some_date.format("dddd DD MMMM YYYY"))
    print(some_date.format("dddd DD MMMM YYYY", locale="de"))
    print(
        some_date.format("LT"),
        some_date.format("LT", locale="en"),
        some_date.format("LLLL"),
    )

    pendulum.set_locale("en")
    print(pendulum.now().add(years=1).diff_for_humans())  # in 1 year

    print(pendulum.now().day_of_year, pendulum.now().day_of_week)
    print(pendulum.now().int_timestamp, pendulum.now().float_timestamp)

    print(pendulum.now().start_of("day"), pendulum.now().end_of("day"))

    duration = pendulum.duration(years=3, months=3)
    print(duration.days)


if __name__ == "__main__":
    main()
