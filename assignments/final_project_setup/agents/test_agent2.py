import unittest
import json
from agent2 import app

class Agent2TestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_addition(self):
        response = self.app.post('/calculate', data=json.dumps({
            'operation': 'add',
            'a': 5,
            'b': 3
        }), content_type='application/json')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['result'], 8)

    def test_subtraction(self):
        response = self.app.post('/calculate', data=json.dumps({
            'operation': 'subtract',
            'a': 10,
            'b': 4
        }), content_type='application/json')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['result'], 6)

    def test_multiplication(self):
        response = self.app.post('/calculate', data=json.dumps({
            'operation': 'multiply',
            'a': 7,
            'b': 6
        }), content_type='application/json')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['result'], 42)

    def test_division(self):
        response = self.app.post('/calculate', data=json.dumps({
            'operation': 'divide',
            'a': 8,
            'b': 2
        }), content_type='application/json')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['result'], 4)

    def test_division_by_zero(self):
        response = self.app.post('/calculate', data=json.dumps({
            'operation': 'divide',
            'a': 8,
            'b': 0
        }), content_type='application/json')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['result'], 'Infinity')

    def test_invalid_operation(self):
        response = self.app.post('/calculate', data=json.dumps({
            'operation': 'modulus',
            'a': 8,
            'b': 2
        }), content_type='application/json')
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('error', data)

    def test_missing_parameters(self):
        response = self.app.post('/calculate', data=json.dumps({
            'operation': 'add',
            'a': 5
        }), content_type='application/json')
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('error', data)

if __name__ == '__main__':
    unittest.main()
