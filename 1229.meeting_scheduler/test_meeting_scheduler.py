import unittest
from meeting_scheduler import Solution

class TestMeetingScheduler(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.minAvailableDuration([[10,50],[60,120],[140,210]], [[0,15],[60,70]], 8), [60, 68])

    def test_example2(self):
        self.assertEqual(self.s.minAvailableDuration([[10,50],[60,120],[140,210]], [[0,15],[60,70]], 12), [])

    def test_overlap_at_start(self):
        self.assertEqual(self.s.minAvailableDuration([[0,30]], [[5,25]], 10), [5, 15])

    def test_exact_fit(self):
        self.assertEqual(self.s.minAvailableDuration([[0,10]], [[0,10]], 10), [0, 10])

    def test_no_overlap(self):
        self.assertEqual(self.s.minAvailableDuration([[0,10]], [[20,30]], 5), [])

    def test_overlap_too_short(self):
        self.assertEqual(self.s.minAvailableDuration([[0,10]], [[5,10]], 10), [])

if __name__ == "__main__":
    unittest.main()
