import smtplib
from dotenv import load_dotenv
import os
from datetime import datetime 
import pandas
import pathlib
import random


def send_email(name, birthday_email, msg):
    load_dotenv()
    my_email = os.getenv("e-mail")
    key = os.getenv("app_key")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=key)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_email, 
                            msg=f"Subject: Happy birthday {name}! :D \n\n{msg}")

def get_birthday():
    birthdays = pandas.read_csv("Day_32/birthdays.csv")
    return birthdays

if __name__ == "__main__":
        
    now = datetime.now()
    month = now.month
    day = now.day

    birthday = get_birthday()

    for i, row in birthday.iterrows():
        if month == row["month"] and day == row["day"]:
            folder = pathlib.Path("Day_32/letter_templates")
            random_file = random.choice(list(folder.iterdir()))

            with open(random_file, "r") as file:
                lines = file.readlines()

                lines[0] = lines[0].replace("[NAME]", row["name"])
                message = "".join(lines)
                print(message)
            send_email(name=row["name"], birthday_email=row["email"], msg=message)
            
        print(row["name"], row["month"], row["day"], row["email"])
        