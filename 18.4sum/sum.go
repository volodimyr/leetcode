// 18. 4Sum
// Topics: 'Array', 'Two Pointers', 'Sorting'
// Level: 'Medium'

// Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

//     0 <= a, b, c, d < n
//     a, b, c, and d are distinct.
//     nums[a] + nums[b] + nums[c] + nums[d] == target

// You may return the answer in any order.

// Example 1:

// Input: nums = [1,0,-1,0,-2,2], target = 0
// Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

// Example 2:

// Input: nums = [2,2,2,2,2], target = 8
// Output: [[2,2,2,2]]

// Constraints:

//     1 <= nums.length <= 200
//     -109 <= nums[i] <= 109
//     -109 <= target <= 109

package sum

import "sort"

func fourSum(nums []int, target int) [][]int {
	sort.Ints(nums)
	res := [][]int{}

	for i := range len(nums) - 3 {
		if i > 0 && nums[i-1] == nums[i] {
			continue
		}
		for L := i + 1; L < len(nums)-2; L++ {
			if L > i+1 && nums[L] == nums[L-1] {
				continue
			}
			L1 := L + 1
			R := len(nums) - 1
			for L1 < R {
				total := nums[i] + nums[L] + nums[L1] + nums[R]
				if total == target {
					res = append(res, []int{nums[i], nums[L], nums[L1], nums[R]})
					for L1 < R && nums[L1] == nums[L1+1] {
						L1++
					}
					for L1 < R && nums[R] == nums[R-1] {
						R--
					}
					L1++
					R--
				} else if total > target {
					R--
				} else {
					L1++
				}
			}
		}
	}
	return res
}
