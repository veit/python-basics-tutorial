import arithmetic
import unittest

class TestArithmetic(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(arithmetic.add(7, 6), 13)

    def test_subtraction(self):
        self.assertEqual(arithmetic.subtract(7, 6), 1)

    def test_multiplication(self):
        self.assertEqual(arithmetic.multiply(7, 6), 42)

    def test_division(self):
        self.assertEqual(arithmetic.divide(42, 7), 6)

# In order to use the file as a script as well as an importable module, the code
# that parses the command line only runs if the module is executed as the “main”
# file.
if __name__ == '__main__':
    unittest.main()
