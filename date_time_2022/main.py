import time
from datetime import datetime
from pytz import timezone


def main() -> None:
    print(time.time(), time.time_ns())

    some_date = datetime(2022, 10, 9, 18, 0, 0)
    print(some_date)

    some_date_iso = datetime.fromisoformat("2022-09-16T14:05:13")
    print(some_date_iso)

    print(some_date < datetime.now())

    some_date_iso = datetime.fromisoformat("2022-09-16T14:05:13")
    utc = timezone("UTC")
    loc = utc.localize(some_date_iso)
    print(loc)

    sydney = timezone("Australia/Sydney")
    print(loc.astimezone(sydney))

    amsterdam = timezone("europe/Amsterdam")
    print(loc.astimezone(amsterdam))


if __name__ == "__main__":
    main()
