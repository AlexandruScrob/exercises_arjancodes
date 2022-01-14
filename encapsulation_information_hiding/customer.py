from dataclasses import dataclass


# TODO by encapsulating you provide boundaries to cohesion (increases cohesion)
#  to your software, and grouping things together
# TODO information hiding reduces coupling, introduces layers (abstraction)
@dataclass
class Customer:
    id: str
    name: str
    email_address: str
    address_line_1: str
    address_line_2: str
    postal_code: str
    city: str
    country: str

    def __post_init__(self):
        self._send_welcome_email()

    def _send_welcome_email(self):
        subject = "Welcome to our platform!"
        body = (
            f"Hi, {self.name}, bla bla bla."
            f"Cheers!"
        )
        send_email(self.email_address, subject, body)


def send_email(email_address, subject, body):
    print(f"Email sent to {email_address}, with subject: {subject}"
          f"and body: {body}")
