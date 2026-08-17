import msgspec


class User(msgspec.Struct):
    id: int
    name: str
    email: str
    is_admin: bool = False


def main() -> None:
    data = b"""
    {
        "id": 1,
        "name": "Arjan",
        "email": "arjan@example.com"
    }
    """

    user = msgspec.json.decode(data, type=User)

    print(user)

    encoded = msgspec.json.encode(user)
    print(encoded.decode())

    try:
        invalid_data = b"""
        {
            "id": "one",
            "name": "Arjan",
            "email": "arjan@example.com"
        }
        """

        msgspec.json.decode(invalid_data, type=User)

    except msgspec.ValidationError as e:
        print(e)


if __name__ == "__main__":
    main()
