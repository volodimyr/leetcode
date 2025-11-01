// 215. Kth largest element in an array
// Topics: 'Heap (Priority Queue)', 'Sorting', 'Quickselect', 'Divide and Conquer', 'Array'
// Level: 'Medium'

// Given an integer array nums and an integer k, return the kth largest element in the array.

// Note that it is the kth largest element in the sorted order, not the kth distinct element.

// Can you solve it without sorting?

// Example 1:

// Input: nums = [3,2,1,5,6,4], k = 2
// Output: 5

// Example 2:

// Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
// Output: 4

// Constraints:

//     1 <= k <= nums.length <= 105
//     -104 <= nums[i] <= 104

package kthlargestelementinanarray

func findKthLargest(nums []int, max int) int {
	arr := []int{}
	for i, n := range nums {
		if i < max {
			arr = append(arr, n)
			j := len(arr) - 1
			for j > 0 && arr[j] < arr[(j-1)/2] {
				arr[j], arr[(j-1)/2] = arr[(j-1)/2], arr[j]
				j = (j - 1) / 2
			}
		} else if n > arr[0] {
			arr[0] = n
			j := 0
			for 2*j+1 < len(arr) {
				if 2*j+2 < len(arr) && arr[2*j+2] < arr[2*j+1] && arr[j] > arr[2*j+2] {
					arr[j], arr[2*j+2] = arr[2*j+2], arr[j]
					j = 2*j + 2
				} else if arr[j] > arr[2*j+1] {
					arr[j], arr[2*j+1] = arr[2*j+1], arr[j]
					j = 2*j + 1
				} else {
					break
				}
			}
		}
	}
	return arr[0]
}
