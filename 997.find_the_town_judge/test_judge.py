import unittest
from collections import defaultdict
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        count_trust = defaultdict(int)
        people = set()

        for p, t in trust:
            count_trust[t] += 1
            people.add(p)

        for i in range(1, n + 1, 1):
            if i in people:
                continue
            trust_level = count_trust[i]
            if trust_level == n - 1:
                return i
        return -1


class TestFindJudge(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    # Basic examples from problem
    def test_example_1(self):
        """Example 1: Simple case with 2 people"""
        self.assertEqual(self.solution.findJudge(2, [[1, 2]]), 2)

    def test_example_2(self):
        """Example 2: 3 people, person 3 is judge"""
        self.assertEqual(self.solution.findJudge(3, [[1, 3], [2, 3]]), 3)

    def test_example_3(self):
        """Example 3: No judge (person 3 trusts person 1)"""
        self.assertEqual(self.solution.findJudge(3, [[1, 3], [2, 3], [3, 1]]), -1)

    # Edge cases
    def test_single_person(self):
        """Single person is the judge by default"""
        self.assertEqual(self.solution.findJudge(1, []), 1)

    def test_two_people_no_trust(self):
        """Two people but no trust relationships"""
        self.assertEqual(self.solution.findJudge(2, []), -1)

    def test_empty_trust_array(self):
        """No trust relationships with multiple people"""
        self.assertEqual(self.solution.findJudge(5, []), -1)

    # Judge validation tests
    def test_judge_trusts_someone(self):
        """Potential judge trusts someone - invalid"""
        self.assertEqual(self.solution.findJudge(3, [[1, 2], [2, 3], [3, 1]]), -1)

    def test_not_everyone_trusts_judge(self):
        """Not everyone trusts the potential judge"""
        self.assertEqual(self.solution.findJudge(4, [[1, 2], [3, 2]]), -1)

    def test_judge_at_beginning(self):
        """Judge is person 1"""
        self.assertEqual(self.solution.findJudge(3, [[2, 1], [3, 1]]), 1)

    def test_judge_in_middle(self):
        """Judge is in the middle of range"""
        self.assertEqual(self.solution.findJudge(5, [[1, 3], [2, 3], [4, 3], [5, 3]]), 3)

    def test_judge_at_end(self):
        """Judge is the last person"""
        self.assertEqual(
            self.solution.findJudge(4, [[1, 4], [2, 4], [3, 4]]), 4
        )

    # Larger test cases
    def test_large_town(self):
        """Larger town with judge at end"""
        n = 100
        trust = [[i, n] for i in range(1, n)]
        self.assertEqual(self.solution.findJudge(n, trust), n)

    def test_large_town_no_judge(self):
        """Larger town with no judge"""
        n = 100
        trust = [[i, n] for i in range(1, n)]
        trust.append([n, 1])  # Judge trusts someone
        self.assertEqual(self.solution.findJudge(n, trust), -1)

    # Multiple potential judges (but only one valid)
    def test_multiple_non_trusters(self):
        """Multiple people don't trust anyone, but only one is trusted by all"""
        # Person 2 and 3 don't trust anyone, but only 3 is trusted by all
        self.assertEqual(
            self.solution.findJudge(4, [[1, 3], [4, 3]]), -1
        )  # Person 2 and 3 both don't trust, but neither is trusted by n-1

    def test_everyone_trusts_but_one_person_missing(self):
        """Almost everyone trusts candidate, but one person doesn't"""
        self.assertEqual(
            self.solution.findJudge(5, [[1, 5], [2, 5], [3, 5]]), -1
        )  # Person 4 doesn't trust 5

    # Circular trust
    def test_circular_trust(self):
        """Circular trust pattern - no judge"""
        self.assertEqual(
            self.solution.findJudge(4, [[1, 2], [2, 3], [3, 4], [4, 1]]), -1
        )

    # Everyone trusts each other
    def test_everyone_trusts_everyone(self):
        """Everyone trusts everyone else - no judge"""
        trust = []
        n = 4
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i != j:
                    trust.append([i, j])
        self.assertEqual(self.solution.findJudge(n, trust), -1)

    # Duplicate-like scenarios (problem says all pairs are unique)
    def test_same_person_trusted_multiple_times(self):
        """Multiple people trust the same person (valid judge scenario)"""
        self.assertEqual(
            self.solution.findJudge(6, [[1, 6], [2, 6], [3, 6], [4, 6], [5, 6]]), 6
        )

    # Boundary tests
    def test_minimum_valid_judge(self):
        """Minimum case: n=2 with valid judge"""
        self.assertEqual(self.solution.findJudge(2, [[1, 2]]), 2)

    def test_maximum_n_constraint(self):
        """Test with n at upper constraint"""
        n = 1000
        trust = [[i, n] for i in range(1, n)]
        self.assertEqual(self.solution.findJudge(n, trust), n)


if __name__ == "__main__":
    # Run tests with verbose output
    unittest.main(verbosity=2)