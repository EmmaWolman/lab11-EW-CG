#https://github.com/EmmaWolman/lab11-EW-CG
# Partner 1: Emma Wolman
# Partner 2: Connor Gionet
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    def test_multiply(self):
        self.assertEqual(multiply(3, 7), 21)
        self.assertEqual(multiply(-2, 4), -8)
        self.assertEqual(multiply(-5, -6), 30)

    def test_divide(self):
        # remember: divide(a, b) returns b / a
        self.assertEqual(divide(4, 20), 5)
        self.assertEqual(divide(-3, 9), -3)
        self.assertEqual(divide(2, -8), -4)

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################

    def logarithm(a, b):
        if a <= 0 or a == 1 or b <= 0:
            raise ValueError("Invalid values for logarithm.")
        return math.log(b, a)

    def log(a, b):
        return logarithm(a, b)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(8, 15), 17.0)
        self.assertAlmostEqual(hypotenuse(-6, 8), 10.0)

    def test_sqrt(self):
        self.assertRaises(ValueError, square_root, -9)
        self.assertAlmostEqual(square_root(4), 2.0)
        self.assertAlmostEqual(square_root(16), 4.0)


# Do not touch this
if __name__ == "__main__":
    unittest.main()