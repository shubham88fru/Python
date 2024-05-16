import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": "<apikey>"
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [v for (k, v) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
diff_percent = (difference / float(yesterday_closing_price))*100
if diff_percent > 5:
    news_params = {
        "apikey": "<apikey>",
        "qInTitle": COMPANY_NAME
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    client = Client("<acct_sid>", "auth_token")
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="",
            to=""
        )
