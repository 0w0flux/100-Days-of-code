import requests
import dotenv
import os

dotenv.load_dotenv()
API = os.getenv("weather_api")
LATITUDE = 52.5244
LONGITUDE = 13.4105

response = requests.get(url=f"http://api.openweathermap.org/data/2.5/forecast?lat={LATITUDE}&lon={LONGITUDE}&cnt=4&units=metric&appid={API}")
response.raise_for_status()
data = response.json()

print(f"status code: {data["cod"]}")


for hour in data["list"]:
    if hour["weather"][0]["id"] < 300:
        print("maybe don't go outside.")
    elif hour["weather"][0]["id"] < 700:
        print("bring an umbrella.")
    elif hour["weather"][0]["id"] > 700 and hour["weather"][0]["id"] < 800:
        print("maybe don't go outside.")
    elif hour["weather"][0]["id"] == 800:
        print("weather should be good enough.")
    elif hour["weather"][0]["id"] > 800:
        print("some clouds nothing fancy")