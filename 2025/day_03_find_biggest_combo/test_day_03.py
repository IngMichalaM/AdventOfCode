import unittest
from day_03 import find_combo_lenght


class TestFindCombo(unittest.TestCase):
    def test_find_combo_1(self):
        result = find_combo_lenght(['12345'])
        self.assertEqual(45, result)

    def test_find_combo_2(self):
        result = find_combo_lenght(['5912345'])
        self.assertEqual(95, result)

    def test_find_combo_3(self):
        result = find_combo_lenght(['9812345'])
        self.assertEqual(98, result)

    def test_find_combo_4(self):
        result = find_combo_lenght(['912345'])
        self.assertEqual(95, result)

    def test_find_combo_5(self):
        result = find_combo_lenght(['55555'])
        self.assertEqual(55, result)

    def test_find_combo_6(self):
        result = find_combo_lenght(['9555559'])
        self.assertEqual(99, result)

    def test_find_combo_of_three_numbers(self):
        result = find_combo_lenght(['12345', '11', '291'])
        self.assertEqual(147, result)

    def test_find_combo_17(self):
        result = find_combo_lenght(['987654321111111'], 12)
        self.assertEqual(987654321111, result)

    def test_find_combo_18(self):
        result = find_combo_lenght(['811111111111119'], 12)
        self.assertEqual(811111111119, result)

    def test_find_combo_19(self):
        result = find_combo_lenght(['234234234234278'], 12)
        self.assertEqual(434234234278, result)

    def test_find_combo_20(self):
        result = find_combo_lenght(['818181911112111'], 12)
        self.assertEqual(888911112111, result)

    def test_find_combo_21(self):
        result = find_combo_lenght(['818111'], 12)
        self.assertEqual(0, result)

    def test_find_combo_22(self):
        result = find_combo_lenght(['111111111111'], 12)
        self.assertEqual(111111111111, result)

    def test_find_combo_7(self):
        result = find_combo_lenght(['1111111111119'], 12)
        self.assertEqual(111111111119, result)

    def test_find_combo_8(self):
        result = find_combo_lenght(['01111011111011109'], 12)
        self.assertEqual(111111111119, result)

    def test_find_combo_9(self):
        result = find_combo_lenght(['1234567891011'], 12)
        self.assertEqual(234567891011, result)

    def test_find_combo_10(self):
        result = find_combo_lenght(['123456789999999'], 12)
        self.assertEqual(456789999999, result)

    def test_find_combo_11(self):
        result = find_combo_lenght(['1234567899999990000'], 12)
        self.assertEqual(899999990000, result)

    def test_find_combo_12(self):
        result = find_combo_lenght(['123456', '789999', '9990000'], 2)
        self.assertEqual(254, result)

    def test_find_combo_13(self):
        result = find_combo_lenght(['009990000'], 2)
        self.assertEqual(99, result)

    def test_find_combo_14(self):
        result = find_combo_lenght(['555590'], 2)
        self.assertEqual(90, result)

    def test_find_combo_15(self):
        result = find_combo_lenght(['987654321', '1234567890', '009990000'], 2)
        self.assertEqual(287, result)

    def test_find_combo_16(self):
        result = find_combo_lenght(['3465793544554539453556366463344563446545344434374421565553674754454364545353445746344674866324626454'], 5)
        self.assertEqual(99866, result)

    def test_find_combo_23(self):
        result = find_combo_lenght(['987654321111111'], 2)
        self.assertEqual(98, result)

    def test_find_combo_24(self):
        result = find_combo_lenght(['811111111111119'], 2)
        self.assertEqual(89, result)

    def test_find_combo_25(self):
        result = find_combo_lenght(['234234234234278'], 2)
        self.assertEqual(78, result)

    def test_find_combo_26(self):
        result = find_combo_lenght(['818181911112111'], 2)
        self.assertEqual(92, result)

    def test_find_combo_example_input(self):
        result = find_combo_lenght(['234234234234278', '987654321111111', '818181911112111', '811111111111119'], 2)
        self.assertEqual(357, result)
