from typing import List
import pytest


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l = len(nums)
        ans = [0] * (2 * l)
        for i, v in enumerate(nums):
            ans[i] = v
            ans[i + l] = v
        return ans

@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 1], [1, 2, 1, 1, 2, 1]),
    ([1, 3, 2, 1], [1, 3, 2, 1, 1, 3, 2, 1]),
    ([5], [5, 5]),
    ([7, 8], [7, 8, 7, 8]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]),
    ([9, 9, 9], [9, 9, 9, 9, 9, 9]),
])

def test_get_concatenation(nums, expected):
    sol = Solution()
    assert sol.getConcatenation(nums) == expected
