# 300. Longest Increasing Subsequence
# Topics: 'Array', 'Dynamic Programming', 'Binary Search'
# level: 'Medium'

# Given an integer array nums, return the length of the longest strictly increasing .

# Example 1:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

# Example 2:

# Input: nums = [0,1,0,3,2,3]
# Output: 4

# Example 3:

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1

 

# Constraints:

#     1 <= nums.length <= 2500
#     -104 <= nums[i] <= 104


# Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}
        def dfs(i, prev):
            if i == len(nums):
                return 0
            if (i, prev) in cache:
                return cache[(i,prev)]
            count = dfs(i+1, prev)
            if prev == -1 or nums[i] > nums[prev]:
                count = max(1+dfs(i+1, i), count)
            cache[(i,prev)] = count
            return count
        
        return dfs(0, -1)

        

# O(nlogn) solution in go
# func lengthOfLIS(nums []int) int {
# 	dp := []int{}
# 	dp = append(dp, nums[0])

# 	LIS := 1
# 	for i := 1; i < len(nums); i++ {
# 		if dp[len(dp)-1] < nums[i] {
# 			dp = append(dp, nums[i])
# 			LIS++
# 			continue
# 		}

# 		idx := sort.Search(len(dp), func(j int) bool {
# 			return dp[j] >= nums[i]
# 		})
# 		dp[idx] = nums[i]
# 	}

# 	return LIS
# }