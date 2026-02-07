import unittest
from hit import HitCounter


class TestHitCounter(unittest.TestCase):

    def test_example_from_prompt(self):
        counter = HitCounter()

        counter.hit(1)
        counter.hit(2)
        counter.hit(3)

        self.assertEqual(counter.getHits(4), 3)

        counter.hit(300)
        self.assertEqual(counter.getHits(300), 4)
        self.assertEqual(counter.getHits(301), 3)

    def test_multiple_hits_same_timestamp(self):
        counter = HitCounter()

        counter.hit(10)
        counter.hit(10)
        counter.hit(10)

        self.assertEqual(counter.getHits(10), 3)
        self.assertEqual(counter.getHits(309), 3)
        self.assertEqual(counter.getHits(310), 0)

    def test_window_boundary(self):
        counter = HitCounter()

        counter.hit(1)
        counter.hit(2)
        counter.hit(300)

        # window is [timestamp-299, timestamp]
        self.assertEqual(counter.getHits(300), 3)
        self.assertEqual(counter.getHits(301), 2)

    def test_no_hits(self):
        counter = HitCounter()
        self.assertEqual(counter.getHits(100), 0)

    def test_large_timestamps(self):
        counter = HitCounter()

        counter.hit(1_000_000_000)
        counter.hit(1_000_000_100)

        self.assertEqual(counter.getHits(1_000_000_100), 2)
        self.assertEqual(counter.getHits(1_000_000_401), 0)


if __name__ == "__main__":
    unittest.main()
