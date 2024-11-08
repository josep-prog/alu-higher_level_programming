import unittest
from 7-base_geometry import BaseGeometry

class TestBaseGeometry(unittest.TestCase):

    def setUp(self):
        self.bg = BaseGeometry()

    def test_integer_validator_valid(self):
        self.bg.integer_validator("my_int", 12)
        self.bg.integer_validator("width", 89)

    def test_integer_validator_type_error(self):
        with self.assertRaises(TypeError) as context:
            self.bg.integer_validator("name", "John")
        self.assertEqual(str(context.exception), "name must be an integer")

    def test_integer_validator_value_error_zero(self):
        with self.assertRaises(ValueError) as context:
            self.bg.integer_validator("age", 0)
        self.assertEqual(str(context.exception), "age must be greater than 0")

    def test_integer_validator_value_error_negative(self):
        with self.assertRaises(ValueError) as context:
            self.bg.integer_validator("distance", -4)
        self.assertEqual(str(context.exception), "distance must be greater than 0")

if __name__ == '__main__':
    unittest.main()
