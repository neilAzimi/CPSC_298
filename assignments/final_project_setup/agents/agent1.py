
# agents/agent1.py

import requests
import sys
import json
from config.settings import OPENWEATHERMAP_API_KEY

def get_weather(city_name):
    base_url = 'https://api.openweathermap.org/data/2.5/weather'

    params = {
        'q': city_name,
        'appid': OPENWEATHERMAP_API_KEY,
        'units': 'metric'
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        result = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'weather': data['weather'][0]['description']
        }
        return result
    else:
        error_message = data.get('message', 'Error fetching weather data.')
        return {'error': error_message}

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(json.dumps({'error': 'City name not provided.'}))
        sys.exit(1)

    city = sys.argv[1]
    weather_info = get_weather(city)
    print(json.dumps(weather_info))
