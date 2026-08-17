from whenever import ZonedDateTime


def main() -> None:
    bedtime = ZonedDateTime(
        2023,
        3,
        25,
        22,
        tz="Europe/Paris",
    )

    print(f"Bedtime: {bedtime}")

    # Correctly accounts for the DST transition
    wake_up = bedtime.add(hours=8)

    print(f"Wake up: {wake_up}")

    duration = wake_up - bedtime
    print(f"Actual sleep: {duration}")

    # Convert to another timezone
    amsterdam = wake_up.to_tz("Europe/Amsterdam")
    print(f"Amsterdam: {amsterdam}")

    new_york = wake_up.to_tz("America/New_York")
    print(f"New York: {new_york}")


if __name__ == "__main__":
    main()
