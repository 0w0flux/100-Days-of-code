import requests
import time
import smtplib
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
EMAIL = os.getenv("e-mail")
PASSWORD = os.getenv("app_key")
MY_LAT = 52.470809
MY_LONG = 13.395897

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
current_hour = time_now.hour

is_night = current_hour >= sunset or current_hour <= sunrise
is_close = (abs(MY_LAT - iss_latitude) <= 5 and abs(MY_LONG - iss_longitude) <= 5)

while True:
    if is_close and is_night:
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg="THE ISS IS ABOVE YOU!!!\n\nLOOK UP")
        connection.close()

    time.sleep(60)
