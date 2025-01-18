import unittest
from datg.utils import validate_format


class TestUtils(unittest.TestCase):
    def test_validate_format(self):
        self.assertTrue(validate_format('csv'))
        self.assertFalse(validate_format('xml'))


if __name__ == '__main__':
    unittest.main()
