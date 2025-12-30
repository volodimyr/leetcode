import unittest

from typing import List
from flood import Solution

class TestFloodFill(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        image = [[1,1,1],[1,1,0],[1,0,1]]
        sr, sc, color = 1, 1, 2
        expected = [[2,2,2],[2,2,0],[2,0,1]]
        self.assertEqual(self.solution.floodFill(image, sr, sc, color), expected)

    def test_example2(self):
        image = [[0,0,0],[0,0,0]]
        sr, sc, color = 0, 0, 0
        expected = [[0,0,0],[0,0,0]]
        self.assertEqual(self.solution.floodFill(image, sr, sc, color), expected)

    def test_single_pixel(self):
        image = [[1]]
        sr, sc, color = 0, 0, 2
        expected = [[2]]
        self.assertEqual(self.solution.floodFill(image, sr, sc, color), expected)

    def test_no_change_needed(self):
        image = [[2,2,2],[2,2,2]]
        sr, sc, color = 1, 1, 2
        expected = [[2,2,2],[2,2,2]]
        self.assertEqual(self.solution.floodFill(image, sr, sc, color), expected)

    def test_non_rectangular_fill_area(self):
        image = [
            [1,1,1,1],
            [1,1,0,0],
            [1,0,1,1]
        ]
        sr, sc, color = 0, 0, 9
        expected = [
            [9,9,9,9],
            [9,9,0,0],
            [9,0,1,1]
        ]
        self.assertEqual(self.solution.floodFill(image, sr, sc, color), expected)

if __name__ == '__main__':
    unittest.main()
