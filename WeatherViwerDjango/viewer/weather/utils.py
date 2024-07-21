import requests


def get_weather_forecast(city):
    # API URL для геокодирования
    api_key = 'eace2e11ceeacf99d7faa55193e739e1'
    geocode_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}"
    geocode_response = requests.get(geocode_url)
    geocode_data = geocode_response.json()

    if geocode_response.status_code != 200 or not geocode_data:
        return None

    latitude = geocode_data[0]['lat']
    longitude = geocode_data[0]['lon']

    weather_url = f"https://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&units=metric&appid={api_key}"
    weather_response = requests.get(weather_url)
    if weather_response.status_code == 200:
        return weather_response.json()
    else:
        return None
