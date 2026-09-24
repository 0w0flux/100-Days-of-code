import os
import dotenv
import requests
from twilio.rest import Client

dotenv.load_dotenv()

# for other companys look up (https://de.tradingview.com/markets/)
STOCK_NAME = "NVDA"
COMPANY_NAME = "NVIDIA Corporation"

def Get_News(msg):

    news_api = os.getenv("news_api")
    news_url = requests.get(f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&apiKey={news_api}")
    news_data = news_url.json()

    message = msg

    for article in news_data["articles"][:3]:
        message += (
            f"\nHeadline: {article['title']}\n"
            f"Brief: {article['description']}\n"
        )

    print(msg)
    return message

# doesn't work because: "Unable to create record: Invalid template name. Trial accounts can only use predefined SMS templates."
def Send_Message(msg):
    twilio_api = os.getenv("twilio_api")
    twilio_secret = os.getenv("twilio_secret")
    twilio_sid = os.getenv("twilio_account_sid")

    twilio = Client(twilio_api, twilio_secret, twilio_sid)

    num_from = os.getenv("twilio_phone_number")
    num_to = os.getenv("phone_number")

    message = twilio.messages.create(
        body=f"{Get_News(msg)}",
        from_=num_from,
        to=num_to
    )

def Check_Stock():

    stock_url_parameters = f"function=TIME_SERIES_DAILY&symbol={STOCK_NAME}&outputsize=compact"
    stock_api = os.getenv("alphavantage_api")

    stock_url = requests.get(f"https://www.alphavantage.co/query?{stock_url_parameters}&apikey={stock_api}")
    stock_data = stock_url.json()
    
    try:
        stock_data = list(stock_data["Time Series (Daily)"].items())
    except:
        raise KeyError("The Stock API limit of 25 is used up!")

    print(stock_data)

    if float(stock_data[0][1]["4. close"]) <= float(stock_data[1][1]["4. close"]) * 0.9999 : #change to 0.95
        Send_Message(f"Get News. {COMPANY_NAME} went down.🔻\n")
    elif float(stock_data[0][1]["4. close"]) >= float(stock_data[1][1]["4. close"]) * 1.0001: #change to 1.05
        Send_Message(msg=f"{COMPANY_NAME} went up. 🔺\n")

Check_Stock()




