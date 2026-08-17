from pint import UnitRegistry

ureg = UnitRegistry()


def main() -> None:
    distance = 42 * ureg.kilometer
    duration = 2 * ureg.hour

    speed = distance / duration

    print(f"Speed: {speed}")
    print(f"Speed: {speed.to('meter / second'):.2f}")

    # Unit conversion
    print(f"Distance: {distance.to('mile'):.2f}")

    # Pint performs dimensional analysis
    force = 80 * ureg.kilogram * 9.81 * ureg.meter / ureg.second**2
    print(f"Weight force: {force.to('newton'):.1f}")

    # Invalid calculations are rejected
    try:
        result = distance + duration
        print(result)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
