import os
import aiosmtplib

from email.message import EmailMessage
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from constants import BOOKING_SERVICE_BASE_URL, EMAIL_SENDING_ID

class EmailService:

    def __init__(self):
        template_dir = (
            Path(__file__).resolve().parent.parent
            / "templates"
            / "email"
        )

        self.template_env = Environment(
            loader=FileSystemLoader(template_dir)
        )

        self.smtp_host = os.getenv("SMTP_HOST")
        self.smtp_port = int(os.getenv("SMTP_PORT", "587"))
        self.smtp_username = os.getenv("SMTP_USERNAME")
        self.smtp_password = os.getenv("SMTP_PASSWORD")

    async def _send_email(
        self,
        sender: str,
        receiver: str,
        subject: str,
        html_content: str,
    ):
        message = EmailMessage()

        message["From"] = sender
        message["To"] = receiver
        message["Subject"] = subject

        message.set_content(
            "Please open this email in an HTML-compatible email client."
        )

        message.add_alternative(
            html_content,
            subtype="html",
        )

        await aiosmtplib.send(
            message,
            hostname=self.smtp_host,
            port=self.smtp_port,
            username=self.smtp_username,
            password=self.smtp_password,
            start_tls=True,
        )

    async def send_verification_email(
        self,
        receiver: str,
        verification_token: str
    ):

        template = self.template_env.get_template(
            "email_verification_email_template.html"
        )

        verification_url = (
            f"{BOOKING_SERVICE_BASE_URL}"
            f"/verify-email?token={verification_token}"
        )

        html_content = template.render(
            verification_url=verification_url,
        )

        await self._send_email(
            sender=EMAIL_SENDING_ID,
            receiver=receiver,
            subject="Verify your email address",
            html_content=html_content,
        )

    async def send_reset_password_email(
        self,
        receiver: str,
        reset_token: str
    ):
        template = self.template_env.get_template(
            "reset_password_email_template.html"
        )

        reset_url = (
            f"{BOOKING_SERVICE_BASE_URL}"
            f"/reset-password?token={reset_token}"
        )

        html_content = template.render(
            reset_url=reset_url
        )

        await self._send_email(
            sender=EMAIL_SENDING_ID,
            receiver=receiver,
            subject="Reset your password",
            html_content=html_content,
        )