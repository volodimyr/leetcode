import unittest
from calendar import MyCalendar


class TestMyCalendar(unittest.TestCase):

    def test_example_from_prompt(self):
        cal = MyCalendar()
        self.assertTrue(cal.book(10, 20))
        self.assertFalse(cal.book(15, 25))
        self.assertTrue(cal.book(20, 30))

    def test_non_overlapping_sequential(self):
        cal = MyCalendar()
        self.assertTrue(cal.book(1, 5))
        self.assertTrue(cal.book(5, 10))
        self.assertTrue(cal.book(10, 15))

    def test_exact_overlap(self):
        cal = MyCalendar()
        self.assertTrue(cal.book(10, 20))
        self.assertFalse(cal.book(10, 20))

    def test_overlap_inside_existing(self):
        cal = MyCalendar()
        self.assertTrue(cal.book(10, 20))
        self.assertFalse(cal.book(12, 18))

    def test_overlap_covering_existing(self):
        cal = MyCalendar()
        self.assertTrue(cal.book(10, 20))
        self.assertFalse(cal.book(5, 25))

    def test_left_neighbor_overlap(self):
        cal = MyCalendar()
        self.assertTrue(cal.book(10, 20))
        self.assertTrue(cal.book(30, 40))
        self.assertFalse(cal.book(15, 35))  # overlaps left neighbor

    def test_right_neighbor_overlap(self):
        cal = MyCalendar()
        self.assertTrue(cal.book(10, 20))
        self.assertTrue(cal.book(30, 40))
        self.assertFalse(cal.book(25, 35))  # overlaps right neighbor

    def test_zero_index_insertion(self):
        cal = MyCalendar()
        self.assertTrue(cal.book(20, 30))
        self.assertFalse(cal.book(10, 25))  # must detect overlap at index 0

    def test_many_small_intervals(self):
        cal = MyCalendar()
        for i in range(0, 100, 2):
            self.assertTrue(cal.book(i, i + 1))
        self.assertFalse(cal.book(50, 51))

    def test_large_values(self):
        cal = MyCalendar()
        self.assertTrue(cal.book(0, 10**9))
        self.assertFalse(cal.book(1, 2))


if __name__ == "__main__":
    unittest.main()
