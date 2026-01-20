import unittest
from lonely import Solution


class TestLonelyPixel(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        picture = [
            ["W", "W", "B"],
            ["W", "B", "W"],
            ["B", "W", "W"]
        ]
        self.assertEqual(self.solution.findLonelyPixel(picture), 3)

    def test_example_2(self):
        picture = [
            ["B", "B", "B"],
            ["B", "B", "W"],
            ["B", "B", "B"]
        ]
        self.assertEqual(self.solution.findLonelyPixel(picture), 0)

    def test_single_cell_black(self):
        picture = [["B"]]
        self.assertEqual(self.solution.findLonelyPixel(picture), 1)

    def test_single_cell_white(self):
        picture = [["W"]]
        self.assertEqual(self.solution.findLonelyPixel(picture), 0)

    def test_single_row(self):
        picture = [["W", "B", "W", "W"]]
        self.assertEqual(self.solution.findLonelyPixel(picture), 1)

    def test_single_column(self):
        picture = [
            ["W"],
            ["B"],
            ["W"]
        ]
        self.assertEqual(self.solution.findLonelyPixel(picture), 1)

    def test_multiple_black_same_row(self):
        picture = [
            ["B", "W", "B"]
        ]
        self.assertEqual(self.solution.findLonelyPixel(picture), 0)

    def test_multiple_black_same_column(self):
        picture = [
            ["B"],
            ["B"]
        ]
        self.assertEqual(self.solution.findLonelyPixel(picture), 0)

    def test_mixed_case(self):
        picture = [
            ["B", "W", "W"],
            ["W", "W", "W"],
            ["W", "W", "B"]
        ]
        self.assertEqual(self.solution.findLonelyPixel(picture), 2)


if __name__ == "__main__":
    unittest.main()
