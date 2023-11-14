import smtplib
import ssl

from asyncio import sleep
from random import randint
from email import message

from src.constants import ZEN
from src.settings import Settings


class EmailAPI:
    msg: message.Message
    _token: str

    def __init__(self) -> None:
        self.msg = message.Message()
        self._token = Settings().MAIL_TOKEN

    @staticmethod
    async def _exponential_backoff(retry: int, backoff_limit: int = 64):
        exponential_backoff = retry + (randint(1, 1000)/1000)
        wait = min(backoff_limit, exponential_backoff)

        await sleep(wait)

    def _configure_msg(self, first_name: str, second_name: str):
        self.msg["From"] = Settings().MAIL_FROM
        self.msg["Subject"] = f"{first_name}! O seu Zen do Python chegou!"
        self.msg.add_header("Content-Type", "text/html")

        self.msg.set_payload(ZEN.format(first_name, second_name))

    async def send_email(
        self, first_name: str, second_name: str, email: str, max_retry: int = 3
    ):
        RETRY = 0
        self._configure_msg(first_name, second_name)

        while True:
            try:
                with smtplib.SMTP("smtp.gmail.com", 587) as server:
                    server.starttls(context=ssl.create_default_context())
                    server.login(self.msg["From"], self._token)

                    server.sendmail(
                        self.msg["From"],
                        [email],
                        self.msg.as_string().encode("utf-8"),
                    )
                return True
            except smtplib.SMTPDataError as error:
                print(error)
                while RETRY <= max_retry:
                    RETRY += 1
                    await self._exponential_backoff(RETRY)

                return False
