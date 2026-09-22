import requests


data_dict = requests.get(url="https://opentdb.com/api.php?amount=20&category=18&type=boolean")
data_dict.raise_for_status()
data_dict = data_dict.json()

