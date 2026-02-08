import unittest
from reservation import SeatManager


class TestSeatManager(unittest.TestCase):

    def test_example_sequence(self):
        sm = SeatManager(5)

        self.assertEqual(sm.reserve(), 1)
        self.assertEqual(sm.reserve(), 2)

        sm.unreserve(2)

        self.assertEqual(sm.reserve(), 2)
        self.assertEqual(sm.reserve(), 3)
        self.assertEqual(sm.reserve(), 4)
        self.assertEqual(sm.reserve(), 5)

        sm.unreserve(5)

    def test_single_seat(self):
        sm = SeatManager(1)

        self.assertEqual(sm.reserve(), 1)
        sm.unreserve(1)
        self.assertEqual(sm.reserve(), 1)

    def test_unreserve_order(self):
        sm = SeatManager(5)

        seats = [sm.reserve() for _ in range(5)]
        self.assertEqual(seats, [1, 2, 3, 4, 5])

        sm.unreserve(3)
        sm.unreserve(1)

        self.assertEqual(sm.reserve(), 1)
        self.assertEqual(sm.reserve(), 3)

    def test_interleaved_operations(self):
        sm = SeatManager(4)

        self.assertEqual(sm.reserve(), 1)
        self.assertEqual(sm.reserve(), 2)

        sm.unreserve(1)

        self.assertEqual(sm.reserve(), 1)
        self.assertEqual(sm.reserve(), 3)

        sm.unreserve(2)

        self.assertEqual(sm.reserve(), 2)
        self.assertEqual(sm.reserve(), 4)


if __name__ == "__main__":
    unittest.main()
