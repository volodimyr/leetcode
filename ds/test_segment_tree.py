import unittest
from segment_tree import SegmentTree


class TestSegmentTree(unittest.TestCase):

    def test_build_single_element(self):
        st = SegmentTree([5])
        self.assertEqual(st.query(0, 0), 5)

    def test_build_multiple_elements_total_sum(self):
        nums = [1, 3, 5, 7, 9]
        st = SegmentTree(nums)
        self.assertEqual(st.query(0, 4), sum(nums))

    def test_query_full_range(self):
        nums = [2, 4, 6, 8]
        st = SegmentTree(nums)
        self.assertEqual(st.query(0, 3), 20)

    def test_query_partial_range(self):
        nums = [1, 2, 3, 4, 5]
        st = SegmentTree(nums)
        self.assertEqual(st.query(1, 3), 2 + 3 + 4)

    def test_query_single_index(self):
        nums = [10, 20, 30]
        st = SegmentTree(nums)
        self.assertEqual(st.query(2, 2), 30)

    def test_query_out_of_range(self):
        nums = [1, 2, 3]
        st = SegmentTree(nums)
        self.assertEqual(st.query(5, 10), 0)
        self.assertEqual(st.query(-10, -1), 0)

    def test_update_leaf(self):
        nums = [1, 2, 3]
        st = SegmentTree(nums)
        st.update(1, 10)
        self.assertEqual(st.query(1, 1), 10)

    def test_update_affects_parent_nodes(self):
        nums = [1, 2, 3, 4]
        st = SegmentTree(nums)
        st.update(2, 10)
        self.assertEqual(st.query(0, 3), 1 + 2 + 10 + 4)

    def test_multiple_updates(self):
        nums = [5, 5, 5, 5]
        st = SegmentTree(nums)
        st.update(0, 1)
        st.update(3, 9)
        self.assertEqual(st.query(0, 3), 1 + 5 + 5 + 9)

    def test_query_after_updates(self):
        nums = [1, 3, 5, 7]
        st = SegmentTree(nums)
        st.update(1, 10)
        st.update(3, 0)
        self.assertEqual(st.query(1, 3), 10 + 5 + 0)


if __name__ == "__main__":
    unittest.main()
