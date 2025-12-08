import unittest
from course import Solution

class TestCourseScheduleII(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        numCourses = 2
        prerequisites = [[1, 0]]
        result = self.sol.findOrder(numCourses, prerequisites)

        # Only valid order: 0 → 1
        self.assertEqual(result, [0, 1])

    def test_example2(self):
        numCourses = 4
        prerequisites = [[1,0],[2,0],[3,1],[3,2]]
        result = self.sol.findOrder(numCourses, prerequisites)

        # Valid topological orders:
        valid = [
            [0,1,2,3],
            [0,2,1,3]
        ]
        self.assertIn(result, valid)

    def test_example3(self):
        numCourses = 1
        prerequisites = []
        result = self.sol.findOrder(numCourses, prerequisites)
        self.assertEqual(result, [0])

    def test_no_prerequisites(self):
        numCourses = 4
        prerequisites = []
        result = self.sol.findOrder(numCourses, prerequisites)

        # Any permutation is valid
        self.assertEqual(set(result), {0,1,2,3})
        self.assertEqual(len(result), 4)

    def test_cycle_impossible(self):
        numCourses = 3
        prerequisites = [[0,1],[1,2],[2,0]]  # cycle
        result = self.sol.findOrder(numCourses, prerequisites)
        self.assertEqual(result, [])

    def test_long_chain(self):
        numCourses = 5
        prerequisites = [[1,0],[2,1],[3,2],[4,3]]
        result = self.sol.findOrder(numCourses, prerequisites)
        self.assertEqual(result, [0,1,2,3,4])


if __name__ == "__main__":
    unittest.main()
