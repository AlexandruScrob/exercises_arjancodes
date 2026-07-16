from dataclasses import dataclass


API_URL = "https://api.company.com"
API_VERSION_ID = "v2"
TOKEN = "a3f5c7e8d9b1c2e3f4a5b62e3f4a5b6c7d8e9f0a1"
ACCOUNT_ID = 98753244984

type JSONDict = dict[str, str | int | float | bool | None]


@dataclass
class APIClient:
    api_url: str
    api_version: str
    token: str
    account_id: int

    def make_request(
        self,
        path: str,
        data: JSONDict | None = None,
        method: str = "post",
    ) -> None:
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }
        fullpath = f"{self.api_url}/{self.api_version}/{self.account_id}/{path}"
        print(f"Making request to {fullpath}")
        print(f"Data: {data}")
        print(f"Method: {method}")
        print(f"Headers: {headers}")


# @dataclass
# class Invoice:
#     id: int
#     amount: float
#     customer_id: int
#     payment_due: str

#     def send_invoice(self, client: APIClient) -> None:
#         client.make_request(
#             "invoices",
#             data={
#                 "id": self.id,
#                 "amount": self.amount,
#                 "customer_id": self.customer_id,
#                 "payment_due": self.payment_due,
#             },
#         )


def main() -> None:
    client = APIClient(
        api_url=API_URL,
        api_version=API_VERSION_ID,
        token=TOKEN,
        account_id=ACCOUNT_ID,
    )

    client.make_request(path="invoices", data={"amount": 1000}, method="post")


if __name__ == "__main__":
    main()
