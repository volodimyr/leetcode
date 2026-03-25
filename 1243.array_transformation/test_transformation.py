from transformation import Solution

s = Solution()

assert s.transformArray([6,2,3,4]) == [6,3,3,4]
assert s.transformArray([1,6,3,4,3,5]) == [1,4,4,4,4,5]
assert s.transformArray([1,2,3]) == [1,2,3]          # already stable
assert s.transformArray([3,2,1]) == [3,2,1]          # already stable (first/last fixed, middle is local min)
assert s.transformArray([1,100,1]) == [1,1,1]       # local max shrinks to meet neighbors
assert s.transformArray([100,1,100]) == [100,100,100]  # local min grows to meet neighbors

print("All tests passed")
