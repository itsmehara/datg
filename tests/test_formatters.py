import unittest
from datg.formatters import to_csv, to_json


class TestFormatters(unittest.TestCase):
    def test_to_csv(self):
        data = [{'name': 'Alice', 'age': 30}]
        result = to_csv(data)
        self.assertIn('name,age', result)

    def test_to_json(self):
        data = [{'name': 'Alice', 'age': 30}]
        result = to_json(data)
        self.assertIn('Alice', result)


if __name__ == '__main__':
    unittest.main()
