import unittest
from scheduling import Solution


class TestTwoCitySchedCost(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]), 110)

    def test_example2(self):
        self.assertEqual(self.solution.twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]), 1859)

    def test_example3(self):
        self.assertEqual(self.solution.twoCitySchedCost([[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]), 3086)

    def test_two_people(self):
        self.assertEqual(self.solution.twoCitySchedCost([[1,2],[2,1]]), 2)

    def test_equal_costs(self):
        self.assertEqual(self.solution.twoCitySchedCost([[5,5],[5,5]]), 10)


if __name__ == "__main__":
    unittest.main()
