// 81. Search in rotated sorted array II
// Topics: 'Array', 'Binary Search'

// There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

// Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

// Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

// You must decrease the overall operation steps as much as possible.

// Example 1:

// Input: nums = [2,5,6,0,0,1,2], target = 0
// Output: true

// Example 2:

// Input: nums = [2,5,6,0,0,1,2], target = 3
// Output: false

// Constraints:

//     1 <= nums.length <= 5000
//     -104 <= nums[i] <= 104
//     nums is guaranteed to be rotated at some pivot.
//     -104 <= target <= 104

package searchinrotatedsortedarrayii

func search(nums []int, target int) bool {
	L, R := 0, len(nums)-1
	for L <= R {
		L, R = skipDuplicates(nums, L, R)

		m := (L + R) / 2
		if target == nums[m] {
			return true
		}
		if nums[L] <= nums[m] {
			if target < nums[m] && target >= nums[L] {
				//sorted
				R = m - 1
			} else {
				L = m + 1
			}
		} else {
			if target > nums[m] && target <= nums[R] {
				//sorted
				L = m + 1
			} else {
				R = m - 1
			}
		}
	}
	return false
}

func skipDuplicates(nums []int, L, R int) (int, int) {
	for L < R {
		if nums[L] == nums[L+1] {
			L++
			continue
		}
		if nums[R] == nums[R-1] {
			R--
			continue
		}
		if nums[R] == nums[L] {
			R--
			continue
		}
		break
	}
	return L, R
}
