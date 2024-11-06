
# agents/agent1.py

import requests
import sys
import logging
import json
from config.settings import OPENWEATHERMAP_API_KEY

logging.basicConfig(level=logging.INFO)

def get_weather(city_name):
    base_url = 'https://api.openweathermap.org/data/2.5/weather'

    params = {
        'q': city_name,
        'appid': OPENWEATHERMAP_API_KEY,
        'units': 'metric'
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if response.status_code == 200:
            result = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'weather': data['weather'][0]['description']
            }
            logging.info(f"Weather data retrieved: {result}")
            return result
        else:
            error_message = data.get('message', 'Error fetching weather data.')
            logging.error(f"Error: {error_message}")
            return {'error': error_message}
    except Exception as e:
        logging.error(f"Exception occurred: {str(e)}")
        return {'error': 'An error occurred while fetching weather data.'}

if __name__ == '__main__':
    input_data = json.loads(sys.stdin.read())
    city = input_data.get('city_name')
    if not city:
        logging.error("City name not provided.")
        print(json.dumps({'error': 'City name not provided.'}))
        sys.exit(1)

    weather_info = get_weather(city)
    print(json.dumps(weather_info))
