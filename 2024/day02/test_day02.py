import unittest
from day02a import set_direction, keep_direction, level_difference


class TestSetDirection(unittest.TestCase):

    def test_increasing(self):
        self.assertEqual(set_direction(1, 10), 1)

    def test_decreasing(self):
        self.assertEqual(set_direction(9, 7), -1)

    def test_steady(self):
        self.assertEqual(set_direction(5, 5), 0)


class TestKeepDirection(unittest.TestCase):

    def test_increasing_ok(self):
        self.assertTrue(keep_direction(4, 9, 1))

    def test_increasing_nok(self):
        self.assertFalse(keep_direction(8, 3, 1))

    def test_increasing_negative_ok(self):
        self.assertTrue(keep_direction(-9, -4, 1))

    def test_increasing_negative_nok(self):
        self.assertFalse(keep_direction(-2, -30, 1))

    def test_decreasing_ok(self):
        self.assertTrue(keep_direction(5, 4, -1))

    def test_decreasing_nok(self):
        self.assertFalse(keep_direction(0, 5, -1))

    def test_decreasing_negative_ok(self):
        self.assertTrue(keep_direction(-5, -40, -1))

    def test_decreasing_negative_nok(self):
        self.assertFalse(keep_direction(-20, -10, -1))

    def test_increasing_a_equal_b_ok(self):
        self.assertFalse(keep_direction(10, 10, 1))

    def test_decreasing_a_equal_b_ok(self):
        self.assertFalse(keep_direction(10, 10, -1))

    def test_steady_a_equal_b_ok(self):
        self.assertFalse(keep_direction(10, 10, 0))

    def test_unsupported_direction_slope(self):
        with self.assertRaises(ValueError) as context:
            keep_direction(10, 9, 0)
        self.assertEqual(str(context.exception), "Unsuported direction")

    # def test_unsupported_direction(self):
    #     with self.assertRaises(ValueError) as context:
    #         keep_direction(10, 10, 1)
    #     self.assertEqual(str(context.exception), "A and B cannot equal - unsuported direction")


class TestLevelDifference(unittest.TestCase):

    def test_level_difference_ok(self):
        self.assertTrue(level_difference(3, 5))

    def test_level_difference_boundary_ok(self):
        self.assertTrue(level_difference(3, 6))

    def test_level_difference_nok(self):
        self.assertFalse(level_difference(3, 7))

    def test_level_difference_negative_num_ok(self):
        self.assertTrue(level_difference(-5, -4))

    def test_level_difference_negative_num_nok(self):
        self.assertFalse(level_difference(-15, -4))


if __name__ == '__main__':
    unittest.main()
