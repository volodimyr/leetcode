import unittest
from eval import Solution

class TestEvaluateDivision(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def assertFloatListAlmostEqual(self, actual, expected, places=5):
        self.assertEqual(len(actual), len(expected))
        for a, e in zip(actual, expected):
            if e == -1.0:
                self.assertEqual(a, e)
            else:
                self.assertAlmostEqual(a, e, places=places)

    def test_example_1(self):
        equations = [["a", "b"], ["b", "c"]]
        values = [2.0, 3.0]
        queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
        expected = [6.0, 0.5, -1.0, 1.0, -1.0]

        result = self.solution.calcEquation(equations, values, queries)
        self.assertFloatListAlmostEqual(result, expected)

    def test_example_2(self):
        equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
        values = [1.5, 2.5, 5.0]
        queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
        expected = [3.75, 0.4, 5.0, 0.2]

        result = self.solution.calcEquation(equations, values, queries)
        self.assertFloatListAlmostEqual(result, expected)

    def test_example_3(self):
        equations = [["a", "b"]]
        values = [0.5]
        queries = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
        expected = [0.5, 2.0, -1.0, -1.0]

        result = self.solution.calcEquation(equations, values, queries)
        self.assertFloatListAlmostEqual(result, expected)

    def test_identity_defined_variable(self):
        equations = [["a", "b"]]
        values = [3.0]
        queries = [["a", "a"], ["b", "b"]]
        expected = [1.0, 1.0]

        result = self.solution.calcEquation(equations, values, queries)
        self.assertFloatListAlmostEqual(result, expected)

    def test_identity_undefined_variable(self):
        equations = [["a", "b"]]
        values = [2.0]
        queries = [["x", "x"]]
        expected = [-1.0]

        result = self.solution.calcEquation(equations, values, queries)
        self.assertFloatListAlmostEqual(result, expected)

    def test_disconnected_graph(self):
        equations = [["a", "b"], ["c", "d"]]
        values = [2.0, 4.0]
        queries = [["a", "d"], ["c", "b"]]
        expected = [-1.0, -1.0]

        result = self.solution.calcEquation(equations, values, queries)
        self.assertFloatListAlmostEqual(result, expected)

    def test_chain_longer_path(self):
        equations = [["a", "b"], ["b", "c"], ["c", "d"]]
        values = [2.0, 3.0, 4.0]
        queries = [["a", "d"], ["d", "a"]]
        expected = [24.0, 1 / 24.0]

        result = self.solution.calcEquation(equations, values, queries)
        self.assertFloatListAlmostEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
