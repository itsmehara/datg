import unittest
from datg.fields import define_field, get_supported_data_types


class TestFields(unittest.TestCase):
    def test_define_field(self):
        field = define_field('name', 'str')
        self.assertIn('value', field)

    def test_get_supported_data_types(self):
        data_types = get_supported_data_types()
        self.assertIn('int', data_types)


if __name__ == '__main__':
    unittest.main()
