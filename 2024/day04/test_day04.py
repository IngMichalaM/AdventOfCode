import unittest
from day04a import count_word_in_line
from day04b import opposite_direction, num_A_around_here


class TestCountWordInLine(unittest.TestCase):

    def test_count_word_1(self):
        self.assertEqual(count_word_in_line('MMMSXXMASM', "XMAS"), 1)

    def test_count_word_2(self):
        self.assertEqual(count_word_in_line('XMASMMMSXXMASM', "XMAS"), 2)

    def test_count_word_0(self):
        self.assertEqual(count_word_in_line('MMMSXXMAM', "XMAS"), 0)


class TestOppositeDirection(unittest.TestCase):

    def test_left_up(self):

        self.assertEqual(opposite_direction([-1,-1]), [1,1])

    def test_right_up(self):
        self.assertEqual(opposite_direction([-1, 1]), [1, -1])

    def test_left_down(self):
        self.assertEqual(opposite_direction([1, -1]), [-1, 1])

    def test_right_down(self):
        self.assertEqual(opposite_direction([1, 1]), [-1, -1])


class TestMSAroundA(unittest.TestCase):

    def test_find_mas_1(self):

        a = [['M','c','s'],['X','A','g'],['X','X','S']]
        self.assertEqual(num_A_around_here(a, 1, 1), 1)

    def test_find_mas_2(self):

        a = [['M','c','S'],['X','A','g'],['M','X','S']]
        self.assertEqual(num_A_around_here(a, 1, 1), 2)

if __name__ == '__main__':
    unittest.main()
