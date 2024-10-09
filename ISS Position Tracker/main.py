import smtplib
import time
import requests
from datetime import datetime

MY_LON = 52.22977
MY_LAT = 21.01178

MY_EMAIL = 'mockupemail@gmail.com'
MY_PASSWORD = 'mockuppassword123!'

def is_iss_above():
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    data = response.json()

    iss_longitude = float(data['iss_position']['longitude'])
    iss_latitude = float(data['iss_position']['latitude'])
    #checking whether ISS is within 5degrees of Warsaw
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LON - 5 <= iss_longitude <= MY_LON + 5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LON,
        'formatted': 0,
    }

    response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
    data = response.json()
    sunrise = data['results']['sunrise'][11:13]
    sunset = data['results']['sunset'][11:13]
    time_now = datetime.now().hour
    #check whether it's already dark outside, otherwise you won't see the ISS
    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(6000)
    if is_iss_above() and is_night():
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg='Subject: Look up! \n\n The ISS should be visible on the sky'
        )