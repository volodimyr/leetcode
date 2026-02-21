import unittest
from triplets import Solution


class TestMergeTriplets(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_true(self):
        triplets = [[2,5,3],[1,8,4],[1,7,5]]
        target = [2,7,5]
        self.assertTrue(self.solution.mergeTriplets(triplets, target))

    def test_example_false(self):
        triplets = [[3,4,5],[4,5,6]]
        target = [3,2,5]
        self.assertFalse(self.solution.mergeTriplets(triplets, target))

    def test_single_triplet_exact_match(self):
        triplets = [[1,2,3]]
        target = [1,2,3]
        self.assertTrue(self.solution.mergeTriplets(triplets, target))

    def test_single_triplet_not_match(self):
        triplets = [[1,2,3]]
        target = [3,2,1]
        self.assertFalse(self.solution.mergeTriplets(triplets, target))

    def test_multiple_needed_to_merge(self):
        triplets = [[1,3,1],[2,1,2],[3,2,3]]
        target = [3,3,3]
        self.assertTrue(self.solution.mergeTriplets(triplets, target))

    def test_triplets_exceed_target(self):
        triplets = [[5,5,5],[6,6,6]]
        target = [4,4,4]
        self.assertFalse(self.solution.mergeTriplets(triplets, target))

    def test_partial_match_not_complete(self):
        triplets = [[2,0,0],[0,2,0]]
        target = [2,2,2]
        self.assertFalse(self.solution.mergeTriplets(triplets, target))

    def test_large_values(self):
        triplets = [[1000,2000,3000],[2000,1000,3000],[3000,2000,1000]]
        target = [3000,2000,3000]
        self.assertTrue(self.solution.mergeTriplets(triplets, target))


if __name__ == "__main__":
    unittest.main()