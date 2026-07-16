import httpx
from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: str
    name: str
    email: EmailStr

    @classmethod
    def find(cls, token: str) -> list["User"]:
        response = httpx.get(
            "http://localhost:8000/users",
            headers={"Authorization": f"Bearer {token}"},
        )
        return [cls(**user) for user in response.json()]


def main() -> None:
    # Initialize the API client with your API
    users = User.find("secret123")
    print(users)


if __name__ == "__main__":
    main()
