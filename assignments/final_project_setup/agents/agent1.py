
# agents/agent1.py

import requests
import logging
import os
from flask import Flask, request, jsonify
from config.settings import OPENWEATHERMAP_API_KEY

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/weather', methods=['POST'])
def get_weather():
    input_data = request.get_json()
    city_name = input_data.get('city_name')
    if not city_name:
        logging.error("City name not provided.")
        return jsonify({'error': 'City name not provided.'}), 400

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
            return jsonify(result)
        else:
            error_message = data.get('message', 'Error fetching weather data.')
            logging.error(f"Error: {error_message}")
            return jsonify({'error': error_message}), response.status_code
    except Exception as e:
        logging.error(f"Exception occurred: {str(e)}")
        return jsonify({'error': 'An error occurred while fetching weather data.'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
