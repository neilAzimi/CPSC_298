
# agents/agent2.py

import sys
import json
import logging

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

if __name__ == '__main__':
    input_data = json.loads(sys.stdin.read())
    op = input_data.get('operation')
    num1 = input_data.get('a')
    num2 = input_data.get('b')
    if not op or num1 is None or num2 is None:
        logging.error("Operation and two numbers must be provided.")
        print(json.dumps({'error': 'Operation and two numbers must be provided.'}))
        sys.exit(1)

    calculation_result = calculate(op, num1, num2)
    print(json.dumps(calculation_result))
