
# agents/agent2.py

import logging
import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

def calculate(operation, a, b):
    try:
        a = float(a)
        b = float(b)
        if operation == 'add':
            result = a + b
        elif operation == 'subtract':
            result = a - b
        elif operation == 'multiply':
            result = a * b
        elif operation == 'divide':
            result = a / b if b != 0 else 'Infinity'
        else:
            logging.error("Unsupported operation.")
            return {'error': 'Unsupported operation.'}
        result_data = {'operation': operation, 'a': a, 'b': b, 'result': result}
        logging.info(f"Calculation result: {result_data}")
        return result_data
    except ValueError:
        logging.error("Invalid numbers provided.")
        return {'error': 'Invalid numbers provided.'}

DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL')

def send_discord_notification(message):
    if DISCORD_WEBHOOK_URL:
        data = {"content": message}
        try:
            response = requests.post(DISCORD_WEBHOOK_URL, json=data)
            if response.status_code == 204:
                logging.info("Notification sent to Discord successfully.")
            else:
                logging.error(f"Failed to send notification to Discord: {response.status_code}")
        except Exception as e:
            logging.error(f"Exception occurred while sending notification to Discord: {str(e)}")
    else:
        logging.warning("Discord webhook URL not set. Skipping notification.")

@app.route('/calculate', methods=['POST'])
def calculate_route():
    input_data = request.get_json()
    op = input_data.get('operation')
    num1 = input_data.get('a')
    num2 = input_data.get('b')
    if not op or num1 is None or num2 is None:
        logging.error("Operation and two numbers must be provided.")
        return jsonify({'error': 'Operation and two numbers must be provided.'}), 400

    calculation_result = calculate(op, num1, num2)
    if 'error' not in calculation_result:
        send_discord_notification(f"Calculation completed: {calculation_result}")
    return jsonify(calculation_result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
