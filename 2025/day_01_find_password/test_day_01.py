import unittest
from day_01_find_password import find_password


class TestFindPassword(unittest.TestCase):
    def test_dial_right_no_crossing_zero(self):
        zero_counter, position = find_password(['R5'])
        self.assertEqual(55, position)
        self.assertEqual(0, zero_counter)

    def test_dial_right_stop_at_zero(self):
        zero_counter, position = find_password(['R50'])
        self.assertEqual(0, position)
        self.assertEqual(1, zero_counter)

    def test_dial_right_one_crossing_zero(self):
        zero_counter, position = find_password(['R56'])
        self.assertEqual(6, position)
        self.assertEqual(0, zero_counter)

    def test_dial_right_two_crossing_zero(self):
        zero_counter, position = find_password(['R104'], 98)
        self.assertEqual(2, position)
        self.assertEqual(0, zero_counter)

    def test_dial_left_three_crossing_zero(self):
        zero_counter, position = find_password(['R150', 'R100'], 50)
        self.assertEqual(0, position)
        self.assertEqual(2, zero_counter)

    def test_dial_left_no_crossing_zero(self):
        zero_counter, position = find_password(['L5'])
        self.assertEqual(45, position)
        self.assertEqual(0, zero_counter)

    def test_dial_left_stop_at_zero(self):
        zero_counter, position = find_password(['L50'])
        self.assertEqual(0, position)
        self.assertEqual(1, zero_counter)

    def test_dial_left_one_crossing_zero(self):
        zero_counter, position = find_password(['L56'])
        self.assertEqual(94, position)
        self.assertEqual(0, zero_counter)

    def test_dial_left_two_crossing_zero(self):
        zero_counter, position = find_password(['L107'], 5)
        self.assertEqual(98, position)
        self.assertEqual(0, zero_counter)

    def test_dial_left_three_crossing_zero(self):
        zero_counter, position = find_password(['L207'], 5)
        self.assertEqual(98, position)
        self.assertEqual(0, zero_counter)

    def test_dial_left_three_crossing_zero_stop_at_zero(self):
        zero_counter, position = find_password(['L5', 'L100'], 5)
        self.assertEqual(0, position)
        self.assertEqual(2, zero_counter)

