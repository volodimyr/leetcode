from diff import Solution

s = Solution()

assert s.maxDifference("aaaaabbc") == 3
assert s.maxDifference("abcabcab") == 1
assert s.maxDifference("aab") == -1  # odd: b=1, even: a=2 → 1-2=-1

print("All tests passed.")
