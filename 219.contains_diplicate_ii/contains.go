// 219. Contains duplicate II
// Topics: 'Array', 'Hash Table', 'Sliding Window'

// Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

// Example 1:

// Input: nums = [1,2,3,1], k = 3
// Output: true

// Example 2:

// Input: nums = [1,0,1,1], k = 1
// Output: true

// Example 3:

// Input: nums = [1,2,3,1,2,3], k = 2
// Output: false

// Constraints:

// 1 <= nums.length <= 105
// -109 <= nums[i] <= 109
// 0 <= k <= 105

package containsdiplicateii

func containsNearbyDuplicate(nums []int, k int) bool {
	m := map[int]struct{}{}
	L := 0
	for R := range len(nums) {
		if R-L > k {
			delete(m, nums[L])
			L += 1
		}
		if _, ok := m[nums[R]]; ok {
			return true
		}
		m[nums[R]] = struct{}{}
	}
	return false
}
