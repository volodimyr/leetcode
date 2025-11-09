import unittest
from ipo import Solution

class TestFindMaximizedCapital(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    # Example test cases
    def test_example_1(self):
        k = 2
        w = 0
        profits = [1, 2, 3]
        capital = [0, 1, 1]
        expected = 4
        self.assertEqual(self.solution.findMaximizedCapital(k, w, profits, capital), expected)
    
    def test_example_2(self):
        k = 3
        w = 0
        profits = [1, 2, 3]
        capital = [0, 1, 2]
        expected = 6
        self.assertEqual(self.solution.findMaximizedCapital(k, w, profits, capital), expected)
    
    # Edge cases
    def test_single_project(self):
        k = 1
        w = 0
        profits = [1]
        capital = [0]
        expected = 1
        self.assertEqual(self.solution.findMaximizedCapital(k, w, profits, capital), expected)
    
    def test_cannot_afford_any_project(self):
        k = 2
        w = 0
        profits = [1, 2, 3]
        capital = [1, 2, 3]
        expected = 0
        self.assertEqual(self.solution.findMaximizedCapital(k, w, profits, capital), expected)
    
    def test_can_do_all_projects(self):
        k = 5
        w = 10
        profits = [1, 2, 3]
        capital = [0, 1, 2]
        expected = 16
        self.assertEqual(self.solution.findMaximizedCapital(k, w, profits, capital), expected)
    
    def test_k_larger_than_n(self):
        k = 10
        w = 0
        profits = [1, 2, 3]
        capital = [0, 0, 0]
        expected = 6
        self.assertEqual(self.solution.findMaximizedCapital(k, w, profits, capital), expected)
    
    def test_high_initial_capital(self):
        k = 2
        w = 100
        profits = [1, 2, 3, 4, 5]
        capital = [0, 1, 10, 50, 99]
        expected = 109
        self.assertEqual(self.solution.findMaximizedCapital(k, w, profits, capital), expected)
    
    def test_zero_profits(self):
        k = 2
        w = 5
        profits = [0, 0, 0]
        capital = [0, 1, 2]
        expected = 5
        self.assertEqual(self.solution.findMaximizedCapital(k, w, profits, capital), expected)
    
    def test_all_projects_same_capital(self):
        k = 2
        w = 1
        profits = [5, 10, 15, 20]
        capital = [1, 1, 1, 1]
        expected = 36
        self.assertEqual(self.solution.findMaximizedCapital(k, w, profits, capital), expected)
    
    def test_sequential_unlocking(self):
        k = 3
        w = 0
        profits = [1, 5, 10]
        capital = [0, 1, 6]
        expected = 16
        self.assertEqual(self.solution.findMaximizedCapital(k, w, profits, capital), expected)
    
    def test_large_capital_requirements(self):
        k = 1
        w = 1000000000
        profits = [10000, 10000]
        capital = [999999999, 1000000000]
        expected = 1000010000
        self.assertEqual(self.solution.findMaximizedCapital(k, w, profits, capital), expected)
    
    def test_k_equals_zero(self):
        k = 0
        w = 10
        profits = [1, 2, 3]
        capital = [0, 0, 0]
        expected = 10
        self.assertEqual(self.solution.findMaximizedCapital(k, w, profits, capital), expected)
    
    def test_multiple_affordable_projects_choose_best(self):
        k = 1
        w = 5
        profits = [1, 10, 100]
        capital = [0, 1, 2]
        expected = 105
        self.assertEqual(self.solution.findMaximizedCapital(k, w, profits, capital), expected)
    
    def test_greedy_choice_matters(self):
        k = 2
        w = 0
        profits = [10, 1, 1, 100]
        capital = [0, 0, 0, 10]
        expected = 110
        self.assertEqual(self.solution.findMaximizedCapital(k, w, profits, capital), expected)

if __name__ == '__main__':
    unittest.main()