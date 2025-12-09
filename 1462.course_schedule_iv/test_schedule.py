import unittest
from schedule import Solution

class TestCourseScheduleIV(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_basic(self):
        numCourses = 4
        prerequisites = [[0,1],[1,2],[2,3]]
        queries = [[0,3],[1,3],[3,0],[0,2],[2,1]]
        expected = [True, True, False, True, False]
        self.assertEqual(self.s.checkIfPrerequisite(numCourses, prerequisites, queries), expected)

    def test_no_prerequisites(self):
        numCourses = 5
        prerequisites = []
        queries = [[0,1],[3,4],[2,2]]
        expected = [False, False, False]
        self.assertEqual(self.s.checkIfPrerequisite(numCourses, prerequisites, queries), expected)

    def test_disconnected_graph(self):
        numCourses = 6
        prerequisites = [[0,1],[2,3]]
        queries = [[0,1],[1,0],[2,3],[3,2],[0,3]]
        expected = [True, False, True, False, False]
        self.assertEqual(self.s.checkIfPrerequisite(numCourses, prerequisites, queries), expected)

    def test_multiple_paths(self):
        numCourses = 5
        prerequisites = [
            [0,1],[0,2],
            [1,3],[2,3],
            [3,4]
        ]
        queries = [[0,4],[1,4],[2,4],[0,3],[2,1]]
        expected = [True, True, True, True, False]
        self.assertEqual(self.s.checkIfPrerequisite(numCourses, prerequisites, queries), expected)

    def test_self_query(self):
        numCourses = 3
        prerequisites = [[0,1],[1,2]]
        queries = [[0,0],[1,1],[2,2]]
        expected = [False, False, False]
        self.assertEqual(self.s.checkIfPrerequisite(numCourses, prerequisites, queries), expected)

if __name__ == "__main__":
    unittest.main()
