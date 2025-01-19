import unittest
from datg.generator import generate_data


class TestGenerator(unittest.TestCase):
    def test_generate_data(self):
        fields = [('name', 'str'), ('age', 'int')]
        num_records = 5
        format = 'json'
        result = generate_data(fields, num_records, format)
        self.assertTrue(isinstance(result, str))


if __name__ == '__main__':
    unittest.main()
