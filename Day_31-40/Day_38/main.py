import os
import dotenv
import requests
import time


base_url = "https://app.100daysofpython.dev/"

query_params = {
  "query": "", # running/jogging, swimming, walking, cycling, weightlifting (include duration/repetitions)
  "weight_kg": 68,                 
  "height_cm": 172,                 
  "age": 19,                        
  "gender": "male"                  
}

dotenv.load_dotenv()

date = time.localtime()
date = time.strftime("20%y/%m/%d")
date_h = time.strftime("%X")

nutrition_app_key = os.getenv("nutrition_app_key")
nutrition_app_id = os.getenv("nutrition_app_id")
sheety_api = os.getenv("sheety_workouts_api")
sheety_workout_url = os.getenv("sheety_workout_url")


def get_sheet():

    response = requests.get(url="https://api.sheety.co/fea5b80e569c2046bff19b5c6ea28288/myWorkouts/workouts", json=query_params)
    print(response.text)


def add_row(inputs):



    response = requests.post(url=sheety_workout_url, json=inputs, auth=("ocgit", sheety_api))
    print(response.text)


def get_calories_burned():

    headers = {
    "x-app-id": nutrition_app_id,
    "x-app-key": nutrition_app_key
    }

    exercise = "v1/nutrition/natural/exercise"
    
    request = requests.post(url=f"{base_url}{exercise}", json=query_params, headers=headers)
    data = request.json()

    inputs = {
        "workout" : {
            "date": date,
            "time": date_h,
            "exercise": data["exercises"][0]["name"].capitalize(),
            "duration": data["exercises"][0]["duration_min"],
            "calories": data["exercises"][0]["nf_calories"]
        }
    }

    add_row(inputs)


def ask():
    global query_params

    idk = str(input("Tell me which exercises you did: "))
    query_params["query"] = idk

    get_calories_burned()

ask()