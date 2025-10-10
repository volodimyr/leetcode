// 35. Search insert position
// Topics: 'Binary Search', 'Array'

// Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

// You must write an algorithm with O(log n) runtime complexity.

// Example 1:

// Input: nums = [1,3,5,6], target = 5
// Output: 2

// Example 2:

// Input: nums = [1,3,5,6], target = 2
// Output: 1

// Example 3:

// Input: nums = [1,3,5,6], target = 7
// Output: 4

// Constraints:

//     1 <= nums.length <= 104
//     -104 <= nums[i] <= 104
//     nums contains distinct values sorted in ascending order.

package searchinsertposition

func searchInsert(nums []int, target int) int {
	var index int
	low, high := 0, len(nums)-1
	for low <= high {
		mid := low + (high-low)/2
		v := nums[mid]
		if v == target {
			return mid
		}
		if v < target {
			if mid+1 > index {
				index = mid + 1
			}
			low = mid + 1
		} else {
			high = mid - 1
		}
	}
	return index
}
