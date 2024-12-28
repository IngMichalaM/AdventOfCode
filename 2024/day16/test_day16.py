import unittest
from day16a import calculate_price


class TestCalculatePrice(unittest.TestCase):

    def test_straight_path_east(self):
        path = [(0, 0), (0, 1), (0, 2), (0, 3)]
        self.assertEqual(calculate_price(path), 3)

    def test_straight_price_north(self):
        #  including one rotation
        path = [(4, 0), (3, 0), (2, 0), (1, 0)]
        self.assertEqual(calculate_price(path), 1003)

    def test_zig_zag_path(self):
        path = [(4, 0), (3, 0), (3, 1), (2, 1), (1, 1)]
        self.assertEqual(calculate_price(path), 3004)

