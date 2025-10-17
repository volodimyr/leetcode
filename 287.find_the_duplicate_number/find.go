// 287. Find the duplicate number
// Topics: 'Array', 'Two Pointers', 'Binary Search', 'Bit Manipulation'
// Level: 'Medium'

// Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

// There is only one repeated number in nums, return this repeated number.

// You must solve the problem without modifying the array nums and using only constant extra space.

// Example 1:

// Input: nums = [1,3,4,2,2]
// Output: 2

// Example 2:

// Input: nums = [3,1,3,4,2]
// Output: 3

// Example 3:

// Input: nums = [3,3,3,3,3]
// Output: 3

// Constraints:

//     1 <= n <= 105
//     nums.length == n + 1
//     1 <= nums[i] <= n
//     All the integers in nums appear only once except for precisely one integer which appears two or more times.

package findtheduplicatenumber

func findDuplicate(nums []int) int {
	slow, fast := nums[0], nums[0]
	for {
		slow = nums[slow]
		fast = nums[nums[fast]]
		if fast == slow {
			break
		}
	}
	slow2 := nums[0]
	for slow2 != slow {
		slow = nums[slow]
		slow2 = nums[slow2]
	}
	return slow
}
