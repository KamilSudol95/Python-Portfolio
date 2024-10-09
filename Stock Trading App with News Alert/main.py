import yfinance as yf
import pandas as pd
import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

#News API properties
NEWS_ENDPOINT = 'https://newsapi.org/v2/everything'
NEWS_API_KEY = 'mockup_API_KEY'

news_params = {
    'apiKey': 'mockup_API_KEY',
    'qInTitle': COMPANY_NAME,
}

#twilio API properties
ACCOUNT_SID = 'mockup_ACC_SID'
AUTH_TOKEN = 'mockup_AUTH_TOKEN'
FROM_NUMBER = 'mockup_from_number'
TO_NUMBER = 'mockup_to_number'

#pulling stock prices and manipulating data to get prices from yesterday and day before
data = yf.download(STOCK, period='5d', group_by='ticker')
data.head()
df = pd.DataFrame(data)
df.to_csv('price_movements.csv')
df = pd.read_csv('price_movements.csv')
df_temp = df.loc[2:3]
data = pd.DataFrame(df_temp)
day_before_value = round(data['Close'][2], 2)
yesterday_value = round(data['Close'][3], 2)

#checking if stock price rose/dropped by 5%
if (day_before_value / yesterday_value) < 0.95 or (day_before_value / yesterday_value) > 1.05:
    response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = response.json()['articles'][:3]
    formatted_articles = [f'Headline: {article['title']}.\n Description: {article['description']}'
                          for article in articles]

    #iterating through each formatted article and sending it via sms
    for article in formatted_articles:
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages.create(
            body= article,
            from_=FROM_NUMBER,
            to=TO_NUMBER,
        )

