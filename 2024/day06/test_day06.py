import unittest
from day06a import find_starting_position, take_right_turn, go_and_turn


class TestFindStartingPosition(unittest.TestCase):

    def test_find_hash(self):

        a = [['.', '.', '.', '.', '#', '.', '.', '.', '.', '.']]

        self.assertEqual(find_starting_position(a, '#'), [0, 4])


class TestTakeRightTurn(unittest.TestCase):

    def test_take_right_turn_raise_error(self):
        with self.assertRaises(ValueError) as context:
            take_right_turn([0, 0])

        self.assertEqual(str(context.exception), "Unknown direction")

    def test_turn_go_down(self):
        self.assertEqual(take_right_turn([0, 1]), [1, 0])

    def test_turn_go_up(self):
        self.assertEqual(take_right_turn([0, -1]), [-1, 0])

    def test_turn_go_left(self):
        self.assertEqual(take_right_turn([1, 0]), [0, -1])

    def test_turn_go_right(self):
        self.assertEqual(take_right_turn([-1, 0]), [0, 1])

class TestGoAndTurn(unittest.TestCase):

    def test_go_up(self):
        print('----- ')
        a = [['.', '.', '.'], ['.', '.', '.'], ['.', '^', '.']]
        b = [['.', 'X', '.'], ['.', 'X', '.'], ['.', 'X', '.']]
        x, y = find_starting_position(a, '^')
        res_count, res_matrix = go_and_turn([-1, 0], x, y, a, len(a), len(a[0]))
        self.assertEqual(res_count, 3)
        self.assertEqual(res_matrix, b)

    def test_go_right(self):
        print('-- ')
        a = [['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['^', '.', '.', '.', '.']]
        b = [['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['X', 'X', 'X', 'X', 'X']]
        x, y = find_starting_position(a, '^')
        res_count, res_matrix = go_and_turn([0, 1], x, y, a, len(a), len(a[0]))
        self.assertEqual(res_count, 5)
        self.assertEqual(res_matrix, b)

    def test_go_down(self):
        print('------- ')
        a = [['.', '.', '.', '^', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.']]
        b = [['.', '.', '.', 'X', '.'], ['.', '.', '.', 'X', '.'], ['.', '.', '.', 'X', '.']]
        x, y = find_starting_position(a, '^')
        res_count, res_matrix = go_and_turn([1, 0], x, y, a, len(a), len(a[0]))
        self.assertEqual(res_count, 3)
        self.assertEqual(res_matrix, b)

    def test_go_left(self):
        print('---------- ')
        a = [['.', '^', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.']]
        b = [['X', 'X', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.']]
        x, y = find_starting_position(a, '^')
        res_count, res_matrix = go_and_turn([0, -1], x, y, a, len(a), len(a[0]))
        self.assertEqual(res_count, 2)
        self.assertEqual(res_matrix, b)

    def test_go_up_turn_right(self):
        print('---------- ')
        a = [['.', '.', '.', '.'], ['.', '#', '.', '.'], ['.', '.', '.', '.'], ['.', '^', '.', '.']]
        b = [['.', '.', '.', '.'], ['.', '#', '.', '.'], ['.', 'X', 'X', 'X'], ['.', 'X', '.', '.']]
        x, y = find_starting_position(a, '^')
        res_count, res_matrix = go_and_turn([-1, 0], x, y, a, len(a), len(a[0]))
        self.assertEqual(res_count, 4)
        self.assertEqual(res_matrix, b)

    def test_go_left_turn_right(self):
        print('---------- ')
        a = [['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.'], ['#', '^', '.', '.']]
        b = [['.', 'X', '.', '.'], ['.', 'X', '.', '.'], ['.', 'X', '.', '.'], ['#', 'X', '.', '.']]
        x, y = find_starting_position(a, '^')
        res_count, res_matrix = go_and_turn([-1, 0], x, y, a, len(a), len(a[0]))
        self.assertEqual(res_count, 4)
        self.assertEqual(res_matrix, b)

if __name__ == '__main__':
    unittest.main()
