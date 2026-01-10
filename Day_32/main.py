import smtplib
from dotenv import load_dotenv
import os


if __name__ == "__main__":
    load_dotenv()
    email = os.getenv("e-mail")
    key = os.getenv("app_key")

    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=email, password=key)
    connection.sendmail(from_addr=email, to_addrs=email, msg="Hello")
    connection.close()
    