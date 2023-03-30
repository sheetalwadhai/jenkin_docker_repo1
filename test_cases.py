import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(Calculator.Addition(2, 3), 5)
        self.assertEqual(Calculator.Addition(-1, 1), 0)
        self.assertEqual(Calculator.Addition(-1, -1), -2)

    def test_subtraction(self):
        self.assertEqual(Calculator.subtraction(4, 3), 1)


    def test_multiplication(self):
        self.assertEqual(Calculator.multiply(2, 3), 6)
        self.assertEqual(Calculator.multiply(-1, 1), -1)
        self.assertEqual(Calculator.multiply(-1, -1), 1)

    def test_division(self):
        self.assertEqual(Calculator.divide(4, 2), 2)
        self.assertRaises(ZeroDivisionError, Calculator.divide, 1, 0)

    def test_authentication(self):
        pass

if __name__ == '__main__':
    unittest.main()