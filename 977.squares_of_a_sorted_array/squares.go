// Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
// Topics: 'Array' 'Two Pointers' 'Sorting'

// Example 1:

// Input: nums = [-4,-1,0,3,10]
// Output: [0,1,9,16,100]
// Explanation: After squaring, the array becomes [16,1,0,9,100].
// After sorting, it becomes [0,1,9,16,100].

// Example 2:

// Input: nums = [-7,-3,2,3,11]
// Output: [4,9,9,49,121]

package squaresofasortedarray

func sortedSquares(nums []int) []int {
	right := 0
	left := len(nums) - 1
	res := make([]int, len(nums))
	for i := left; i >= 0; i-- {
		rSq := sq(nums[right])
		lSq := sq(nums[left])
		if rSq > lSq {
			res[i] = rSq
			right++
		} else {
			res[i] = lSq
			left--
		}
	}
	return res
}

func sq(a int) int {
	return a * a
}
