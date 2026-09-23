import requests
import os
import dotenv
import time


dotenv.load_dotenv()

pixela_url = "https://pixe.la/v1/users"
pixela_token = os.getenv("pixela_token")
user_name = "ocgit"
graph_id = "graph1"

date = time.localtime()
date = time.strftime("%Y%m%d")

    # if time.struct_time(date)[1] < 10: 
    #     date = f"{time.struct_time(date)[0]}0{time.struct_time(date)[1]}{time.struct_time(date)[2]}"
    # else:
    #     date = f"{time.struct_time(date)[0]}{time.struct_time(date)[1]}{time.struct_time(date)[2]}"

headers = {
    "X-USER-TOKEN": pixela_token
}


def create_user():

    user_parameters = {
        "token" : pixela_token,
        "username" : user_name,
        "agreeTermsOfService" : "yes",
        "notMinor" : "yes"
    }

    response = requests.post(url=f"{pixela_url}", json=user_parameters)
    print(response.text)


def create_graph():
    global graph_config

    graph_config = {
        "id" : "graph1",
        "name" : "push ups",
        "unit" : "Push up",
        "type" : "int",
        "color" : "ajisai"
    }


    response = requests.post(url=f"{pixela_url}/{user_name}/graphs", json=graph_config, headers=headers)
    print(response.text)


def graph_change():

    change = {
        "date" : f"{date}", #yyyymmdd
        "quantity" : "10"
    }

    response = requests.post(url=f"{pixela_url}/{user_name}/graphs/{graph_id}", json=change, headers=headers)
    print(response.text)
    

def graph_add_pixel():

    add = {
        "quantity" : "5"
    }

    response = requests.put(url=f"{pixela_url}/{user_name}/graphs/{graph_id}/{date}", json=add, headers=headers)
    print(response.text)


def graph_delete():

    delete = {
        "quantity" : "1"
    }

    response = requests.delete(url=f"{pixela_url}/{user_name}/graphs/{graph_id}/{date}", json=delete, headers=headers)
    print(response.text)


graph_add_pixel()


