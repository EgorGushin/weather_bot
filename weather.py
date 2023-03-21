import requests

API = 'Your APi key on openweathermap.org'


def weather_cheсk(lat, lon):
    URL = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&APPID={API}&units=metric&lang=ru'
    response = requests.get(URL)
    return response.json()
