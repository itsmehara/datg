import unittest
from src.formatters import to_csv, to_json


class TestFormatters(unittest.TestCase):
    def test_to_csv(self):
        """
        Test CSV formatter function.
        """
        data = [{'name': 'Alice', 'age': 30}]
        result = to_csv(data)
        self.assertIn('name,age', result)

    def test_to_json(self):
        """
        Test JSON formatter function.
        """
        data = [{'name': 'Alice', 'age': 30}]
        result = to_json(data)
        self.assertIn('Alice', result)


if __name__ == '__main__':
    unittest.main()