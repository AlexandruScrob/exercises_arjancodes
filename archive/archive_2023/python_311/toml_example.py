import tomlib


def main() -> None:
    with open("settings.toml", "rb") as f:
        data = tomlib.load(f)
        print(data)


if __name__ == "__main__":
    main()
