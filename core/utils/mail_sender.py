from pydantic import EmailStr
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from core.config import get_settings

setting = get_settings()


async def mail_sending(mail_to: EmailStr, subject: str, html_body: str):
    msg = MIMEMultipart()

    msg["From"] = "tanujsingh@gmail.com <tanujsingh@gmail.com"
    msg["to"] = mail_to
    msg["subject"] = subject

    msg.attach(MIMEText(html_body, "html"))

    try:
        server = smtplib.SMTP(setting.EMAIL_HOST, setting.EMAIL_PORT)
        server.starttls()
        server.login(setting.EMAIL_HOST_USER, setting.EMAIL_HOST_PASSWORD)
        server.sendmail("tanuj@gmail.com", mail_to, msg.as_string())
        server.quit()
    except Exception as e:
        print(f"Failed to send the mail for mail:{mail_to}-Error:-{str(e)}")
