// Sort an Array

// You are given an array of integers nums, sort the array in ascending order and return it.

// You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

// Example 1:

// Input: nums = [10,9,1,1,1,2,3,1]

// Output: [1,1,1,1,2,3,9,10]

// Example 2:

// Input: nums = [5,10,2,1,3]

// Output: [1,2,3,5,10]

// Constraints:

//     1 <= nums.length <= 50,000.
//     -50,000 <= nums[i] <= 50,000

package sortanarray

func sortArray1(nums []int) []int {
	sort(nums, 0, len(nums)-1)
	return nums
}

func sort(nums []int, s, e int) {
	if e-s+1 <= 1 {
		return
	}

	pivot := nums[e]
	left := s

	for i := s; i < e; i++ {
		if nums[i] <= pivot {
			nums[left], nums[i] = nums[i], nums[left]
			left++
		}
	}
	nums[e] = nums[left]
	nums[left] = pivot

	sort(nums, s, left-1)
	sort(nums, left+1, e)
}
