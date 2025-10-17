import unittest
from pkg.calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        self.assertEqual(self.calculator.evaluate("3 + 2"), 5)

    def test_subtraction(self):
        self.assertEqual(self.calculator.evaluate("3 - 2"), 1)

    def test_multiplication(self):
        self.assertEqual(self.calculator.evaluate("3 * 2"), 6)

    def test_division(self):
        self.assertEqual(self.calculator.evaluate("6 / 2"), 3)

    def test_precedence(self):
        self.assertEqual(self.calculator.evaluate("3 + 7 * 2"), 17)

    def test_parentheses(self):
        self.assertEqual(self.calculator.evaluate("(3 + 7) * 2"), 20)

    def test_nested_parentheses(self):
        self.assertEqual(self.calculator.evaluate("(3 + (7 * 2)) * 2"), 40)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.evaluate("5 / 0")

    def test_invalid_expression(self):
        with self.assertRaises(ValueError):
            self.calculator.evaluate("3 + + 2")

    def test_empty_expression(self):
        self.assertIsNone(self.calculator.evaluate(""))


if __name__ == "__main__":
    unittest.main()
