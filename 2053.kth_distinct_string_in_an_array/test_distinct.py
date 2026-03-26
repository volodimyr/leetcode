from distinct import Solution

s = Solution()

assert s.kthDistinct(["d","b","c","b","c","a"], 2) == "a"
assert s.kthDistinct(["aaa","aa","a"], 1) == "aaa"
assert s.kthDistinct(["a","b","a"], 3) == ""
assert s.kthDistinct(["a"], 1) == "a"
assert s.kthDistinct(["a","a"], 1) == ""

print("All tests passed")
