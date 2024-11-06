
# agents/agent2.py

from flask import Flask, request, jsonify

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

app = Flask(__name__)

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
    return jsonify(calculation_result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
