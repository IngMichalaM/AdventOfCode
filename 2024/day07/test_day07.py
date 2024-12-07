import unittest
from day07 import do_calculation, feasible_combination, my_concatenation


class TestDoCalculation(unittest.TestCase):

    def test_concatenation_only_ok(self):

        self.assertEqual(do_calculation(('||',), [15, 6]), 156)

    def test_concatenation_multiple_ok(self):
        self.assertEqual(do_calculation(('||', '||', '||'), [15, 6, 1, 5]), 15615)

    def test_all_operations_ok(self):
        self.assertEqual(do_calculation(('||', '*', '+'), [1, 1, 3, 5]), 38)

    def test_multiplication_1_ok(self):

        self.assertEqual(do_calculation(('*',), [9, 10]), 90)

    def test_addition_1_ok(self):

        self.assertTrue(do_calculation(('*',), [8, 10]), 80)

    def test_multiplication_3_ok(self):

        self.assertEqual(do_calculation(('*', '*', '*'), [1, 2, 3, 4]), 24)

    def test_addition_3_ok(self):

        self.assertEqual(do_calculation(('+', '+', '+'), [1, 2, 3, 4]), 10)


class TestFeasibleCombination(unittest.TestCase):

    def test_combination_short_ok(self):

        self.assertTrue(feasible_combination([55, 5, 11]))

    def test_combination_long_ok(self):

        self.assertTrue(feasible_combination([55, 10, 5, 5, 1]))

    def test_combination_short_nok(self):
        self.assertFalse(feasible_combination([55, 5, 110]))

    def test_combination_long_nok(self):
        self.assertFalse(feasible_combination([55, 10, 5, 555, 1]))


class TestMyConcatenation(unittest.TestCase):

    def test_concatenation_ok(self):

        self.assertEqual(my_concatenation(5, 8), 58)


if __name__ == '__main__':
    unittest.main()
