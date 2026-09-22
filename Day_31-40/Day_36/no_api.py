import json
import os
import dotenv
import requests

dotenv.load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

def Get_News():
    with open("Day_36\\news.json", "r", encoding="utf-8") as data:
        news_data = json.load(data)

    print(f"Headline: {news_data["articles"][0]["title"]}")
    print(f"Brief: {news_data["articles"][0]["description"]}\n")

    print(f"Headline: {news_data["articles"][1]["title"]}")
    print(f"Brief: {news_data["articles"][1]["description"]}\n")

    print(f"Headline: {news_data["articles"][2]["title"]}")
    print(f"Brief: {news_data["articles"][2]["description"]}")


with open("Day_36\\stock.json", "r", encoding="utf-8") as data:
    stock_data = json.load(data)

stock_data = list(stock_data["Time Series (Daily)"].items())

if float(stock_data[1][1]["4. close"]) <= float(stock_data[2][1]["4. close"]) * 0.95 :
    print(f"Get News. {COMPANY_NAME} went down.🔻\n")
    Get_News()
elif float(stock_data[1][1]["4. close"]) >= float(stock_data[2][1]["4. close"]) * 1.05:
    print(f"Get News. {COMPANY_NAME} went up. 🔺\n")
    Get_News()

