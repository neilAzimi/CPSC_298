
# agents/agent2.py

import sys
import json

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
            return {'error': 'Unsupported operation.'}
        return {'operation': operation, 'a': a, 'b': b, 'result': result}
    except ValueError:
        return {'error': 'Invalid numbers provided.'}

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print(json.dumps({'error': 'Operation and two numbers must be provided.'}))
        sys.exit(1)

    op, num1, num2 = sys.argv[1], sys.argv[2], sys.argv[3]
    calculation_result = calculate(op, num1, num2)
    print(json.dumps(calculation_result))
