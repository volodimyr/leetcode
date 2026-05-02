import unittest
from log import LogSystem


class TestLogSystem(unittest.TestCase):

    def setUp(self):
        self.ls = LogSystem()
        self.ls.put(1, "2017:01:01:23:59:59")
        self.ls.put(2, "2017:01:01:22:59:59")
        self.ls.put(3, "2016:01:01:00:00:00")

    def test_retrieve_year(self):
        result = self.ls.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year")
        self.assertCountEqual(result, [1, 2, 3])

    def test_retrieve_hour(self):
        result = self.ls.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour")
        self.assertCountEqual(result, [1, 2])

    def test_retrieve_minute(self):
        result = self.ls.retrieve("2017:01:01:22:59:00", "2017:01:01:23:59:00", "Minute")
        self.assertCountEqual(result, [1, 2])

    def test_retrieve_second(self):
        result = self.ls.retrieve("2017:01:01:23:59:59", "2017:01:01:23:59:59", "Second")
        self.assertCountEqual(result, [1])

    def test_retrieve_no_match(self):
        result = self.ls.retrieve("2015:01:01:00:00:00", "2015:12:31:23:59:59", "Year")
        self.assertEqual(result, [])

    def test_retrieve_day_boundary(self):
        result = self.ls.retrieve("2016:01:01:00:00:00", "2016:01:01:00:00:00", "Day")
        self.assertCountEqual(result, [3])

    def test_put_and_retrieve_new_log(self):
        self.ls.put(4, "2015:06:15:12:30:00")
        result = self.ls.retrieve("2015:01:01:00:00:00", "2015:12:31:23:59:59", "Month")
        self.assertCountEqual(result, [4])


if __name__ == "__main__":
    unittest.main()
