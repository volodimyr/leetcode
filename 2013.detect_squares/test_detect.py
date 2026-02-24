import unittest
from detect import CountSquares


class TestCountSquares(unittest.TestCase):

    def test_example_case(self):
        ds = CountSquares()
        ds.add([3, 10])
        ds.add([11, 2])
        ds.add([3, 2])

        self.assertEqual(ds.count([11, 10]), 1)
        self.assertEqual(ds.count([14, 8]), 0)

        ds.add([11, 2])  # duplicate
        self.assertEqual(ds.count([11, 10]), 2)

    def test_no_points(self):
        ds = CountSquares()
        self.assertEqual(ds.count([0, 0]), 0)

    def test_single_square(self):
        ds = CountSquares()
        ds.add([0, 0])
        ds.add([1, 0])
        ds.add([0, 1])
        ds.add([1, 1])

        self.assertEqual(ds.count([0, 0]), 1)
        self.assertEqual(ds.count([1, 1]), 1)

    def test_multiple_squares_different_sizes(self):
        ds = CountSquares()
        # small square
        ds.add([0, 0])
        ds.add([1, 0])
        ds.add([0, 1])
        ds.add([1, 1])

        # larger square
        ds.add([0, 0])
        ds.add([2, 0])
        ds.add([0, 2])
        ds.add([2, 2])

        self.assertEqual(ds.count([0, 0]), 2)

    def test_duplicates_multiplication(self):
        ds = CountSquares()
        ds.add([0, 0])
        ds.add([1, 0])
        ds.add([1, 0])
        ds.add([0, 1])
        ds.add([0, 1])
        ds.add([0, 1])
        ds.add([1, 1])
        ds.add([1, 1])
        ds.add([1, 1])
        ds.add([1, 1])

        # freq(1,0)=2
        # freq(0,1)=3
        # freq(1,1)=4
        # total = 2 * 3 * 4 = 24
        self.assertEqual(ds.count([0, 0]), 24)

    def test_query_point_not_added(self):
        ds = CountSquares()
        ds.add([0, 0])
        ds.add([1, 0])
        ds.add([0, 1])
        ds.add([1, 1])

        # query point not in structure — still valid
        self.assertEqual(ds.count([2, 2]), 0)


if __name__ == "__main__":
    unittest.main()