import unittest
from moves import Solution


class TestMinMovesToSeat(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        seats = [3, 1, 5]
        students = [2, 7, 4]
        self.assertEqual(self.solution.minMovesToSeat(seats, students), 4)

    def test_example_2(self):
        seats = [4, 1, 5, 9]
        students = [1, 3, 2, 6]
        self.assertEqual(self.solution.minMovesToSeat(seats, students), 7)

    def test_example_3(self):
        seats = [2, 2, 6, 6]
        students = [1, 3, 2, 6]
        self.assertEqual(self.solution.minMovesToSeat(seats, students), 4)

    def test_already_matching(self):
        seats = [1, 2, 3]
        students = [1, 2, 3]
        self.assertEqual(self.solution.minMovesToSeat(seats, students), 0)

    def test_single_element(self):
        seats = [10]
        students = [1]
        self.assertEqual(self.solution.minMovesToSeat(seats, students), 9)

    def test_all_same_positions(self):
        seats = [5, 5, 5]
        students = [5, 5, 5]
        self.assertEqual(self.solution.minMovesToSeat(seats, students), 0)

    def test_reverse_order(self):
        seats = [1, 2, 3, 4]
        students = [4, 3, 2, 1]
        self.assertEqual(self.solution.minMovesToSeat(seats, students), 0)


if __name__ == "__main__":
    unittest.main()