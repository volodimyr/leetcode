import unittest
from moving import MovingAverage


class TestMovingAverage(unittest.TestCase):

    def test_example(self):
        ma = MovingAverage(3)
        self.assertAlmostEqual(ma.next(1), 1.0)
        self.assertAlmostEqual(ma.next(10), 5.5)
        self.assertAlmostEqual(ma.next(3), 14/3)
        self.assertAlmostEqual(ma.next(5), 6.0)

    def test_window_size_one(self):
        ma = MovingAverage(1)
        self.assertAlmostEqual(ma.next(5), 5.0)
        self.assertAlmostEqual(ma.next(10), 10.0)

    def test_window_larger_than_stream(self):
        ma = MovingAverage(5)
        self.assertAlmostEqual(ma.next(4), 4.0)
        self.assertAlmostEqual(ma.next(6), 5.0)

    def test_negative_values(self):
        ma = MovingAverage(2)
        self.assertAlmostEqual(ma.next(-5), -5.0)
        self.assertAlmostEqual(ma.next(5), 0.0)
        self.assertAlmostEqual(ma.next(-3), 1.0)


if __name__ == "__main__":
    unittest.main()
