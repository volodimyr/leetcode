import unittest
from remove import Solution


class TestRemoveSubfolders(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_basic_case(self):
        folders = ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]
        result = self.sol.removeSubfolders(folders)
        self.assertCountEqual(result, ["/a", "/c/d", "/c/f"])

    def test_single_folder(self):
        folders = ["/a"]
        result = self.sol.removeSubfolders(folders)
        self.assertEqual(result, ["/a"])

    def test_nested_only(self):
        folders = ["/a", "/a/b", "/a/b/c", "/a/b/c/d"]
        result = self.sol.removeSubfolders(folders)
        self.assertEqual(result, ["/a"])

    def test_no_subfolders(self):
        folders = ["/a", "/b", "/c"]
        result = self.sol.removeSubfolders(folders)
        self.assertCountEqual(result, ["/a", "/b", "/c"])

    def test_similar_prefix_not_subfolder(self):
        folders = ["/a", "/ab", "/a/b"]
        result = self.sol.removeSubfolders(folders)
        self.assertCountEqual(result, ["/a", "/ab"])

    def test_deep_tree(self):
        folders = [
            "/a/b/c",
            "/a/b",
            "/a",
            "/b/c/d",
            "/b/c",
            "/b"
        ]
        result = self.sol.removeSubfolders(folders)
        self.assertCountEqual(result, ["/a", "/b"])

    def test_unsorted_input(self):
        folders = ["/c/d/e", "/a/b", "/a", "/c/d", "/c/f"]
        result = self.sol.removeSubfolders(folders)
        self.assertCountEqual(result, ["/a", "/c/d", "/c/f"])


if __name__ == "__main__":
    unittest.main()
