#https://github.com/EmmaWolman/lab11-EW-CG
# Partner 1: Emma Wolman
# Partner 2: Connor Gionet
import calculator
import unittest

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(2,2), 4)
        self.assertEqual(calculator.add(2,-2), 0)
        self.assertEqual(calculator.add(0,0), 0)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(8,2), 6)
        self.assertEqual(calculator.subtract(0,1), -1)
        self.assertEqual(calculator.subtract(-2, -2), 0)


    def test_multiply(self):
        self.assertEqual(calculator.mul(3, 7), 21)
        self.assertEqual(calculator.mul(-2, 4), -8)
        self.assertEqual(calculator.mul(-5, -6), 30)

    def test_divide(self):
        # remember: divide(a, b) returns b / a
        self.assertEqual(calculator.div(4, 20), 5)
        self.assertEqual(calculator.div(-3, 9), -3)
        self.assertEqual(calculator.div(2, -8), -4)

    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 5)

    def test_logarithm(self):
        self.assertEqual(calculator.logarithm(1, 10), 0)
        self.assertEqual(calculator.logarithm(10, 10), 1)
        self.assertEqual(calculator.logarithm(8, 2), 3)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.log(10, 1)


    def logarithm(a, b):
        if a <= 0 or a == 1 or b <= 0:
            raise ValueError("Invalid values for logarithm.")
        return math.log(b, a)

    def test_log_invalid_base(self):
        self.assertRaises(ValueError, calculator.log, 10, 1)

    def test_log_invalid_argument(self):
        self.assertRaises(ValueError, calculator.log, 10, -1)


    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(calculator.hypotenuse(8, 15), 17.0)
        self.assertAlmostEqual(calculator.hypotenuse(-6, 8), 10.0)

    def test_sqrt(self):
        self.assertRaises(ValueError, calculator.square_root, -9)
        self.assertAlmostEqual(calculator.square_root(4), 2.0)
        self.assertAlmostEqual(calculator.square_root(16), 4.0)


# Do not touch this
if __name__ == "__main__":
    unittest.main()