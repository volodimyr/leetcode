// 53. Maximum subarray
// Topics: 'Array', 'Divede and Conquer', 'Dynamic Programming'
// Level: 'Medium'

// Given an integer array nums, find the

// with the largest sum, and return its sum.

// Example 1:

// Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
// Output: 6
// Explanation: The subarray [4,-1,2,1] has the largest sum 6.

// Example 2:

// Input: nums = [1]
// Output: 1
// Explanation: The subarray [1] has the largest sum 1.

// Example 3:

// Input: nums = [5,4,-1,7,8]
// Output: 23
// Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

// Constraints:

//     1 <= nums.length <= 105
//     -104 <= nums[i] <= 104

// Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

package maximumsubarray

func maxSubArray(nums []int) int {
	_max := nums[0]
	cur := nums[0]
	for _, n := range nums[1:] {
		cur = max(n, cur+n)
		_max = max(_max, cur)
	}
	return _max
}

func maxSubArraySlidingWindow(nums []int) int {
	max := nums[0]
	var curSum int
	for R := range len(nums) {
		if curSum < 0 {
			curSum = 0
		}
		curSum += nums[R]
		if curSum > max {
			max = curSum
		}
	}
	return max
}
