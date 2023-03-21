import requests

URL = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&APPID=7544d6bd11364e137f04555da356d101&units=metric&lang=ru'

def weather_cheсk(lat, lon):
    response = requests.get(URL.format(lat, lon))
    return response.json()
