import requests

from twilio.rest import Client

#openweather API properties
OWM_ENDPOINT = 'https://api.openweathermap.org/data/2.5/forecast'
API_KEY = 'mockupAPI_KEY'
#twilio API properties
ACCOUNT_SID = 'mockup_ACC_SID'
AUTH_TOKEN = 'mockup_AUTH_TOKEN'
FROM_NUMBER = 'mockup_FROM_NUMBER'
TO_NUMBER = 'mockup_TO_NUMBER'



weather_params = {
    'lat': 52.2298,
    'lon': 21.0118,
    'appid': API_KEY,
    'cnt': 4
}

will_rain = False

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
data = response.json()


for hour_data in data['list']:
    condition_code = hour_data['weather'][0]['id']
    if condition_code < 600 and condition_code >= 500:
        will_rain = True

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body="It will be raining today, please take an umbrella!",
        from_=FROM_NUMBER,
        to=TO_NUMBER,
    )
    print(message.status)