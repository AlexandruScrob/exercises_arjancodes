from email.message import Message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# from smtplib import SMTP
from typing import Protocol

DEFAULT_EMAIL = "support@arjancodes.com"
LOGIN = "test"
PASSWORD = "my_password"


def create_mime_multipart(
    from_address: str, to_address: str | None = None, subject: str = "No subject", message: str = ""
) -> Message:
    msg = MIMEMultipart()
    msg["From"] = from_address
    msg["To"] = to_address
    msg["Subject"] = subject
    mime = MIMEText(
        message,
        "html" if message.lower().startswith("<!doctype html>") else "plain",
    )
    msg.attach(mime)
    return msg


# depend on structural typing
class EmailServer(Protocol):
    @property
    def _host(self) -> str:
        ...

    def connect(self, host: str, port: int) -> None:
        ...

    def starttls(self) -> None:
        ...

    def login(self, login: str, password: str) -> None:
        ...

    def quit(self) -> None:
        ...

    def sendmail(self, from_address: str, to_address: str, message: str) -> None:
        ...


class EmailClient:
    def __init__(
        self,
        smtp_server: EmailServer,
        login: str | None = None,
        password: str | None = None,
        name: str = "",
        to_address: str = DEFAULT_EMAIL,
    ):
        self._server = smtp_server
        host, port = str(smtp_server._host).split(":")  # type: ignore
        self._host = host
        self._port = int(port)

        if not login or not password:
            self._login, self._password = LOGIN, PASSWORD
        else:
            self._login, self._password = login, password

        self.name = name
        self.to_address = to_address

    def _connect(self) -> None:
        self._server.connect(self._host, self._port)
        self._server.starttls()
        self._server.login(self._login, self._password)

    def _quit(self) -> None:
        self._server.quit()

    def send_message(self, msg: Message) -> None:
        if not msg["To"]:
            msg["To"] = self.to_address

        self._connect()
        self._server.sendmail(msg["From"], msg["To"], msg.as_string())
        self._quit()
