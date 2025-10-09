// 912. Sort an Array
// Topics: Array', 'Divide and Conquer', 'Sorting', 'Heap (Priority Queue)', 'Merge Sort', 'Bucket Sort', 'Radix Sort', 'Counting Sort'
// Given an array of integers nums, sort the array in ascending order and return it.

// You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

// Example 1:

// Input: nums = [5,2,3,1]
// Output: [1,2,3,5]
// Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).

// Example 2:

// Input: nums = [5,1,1,2,0,0]
// Output: [0,0,1,1,2,5]
// Explanation: Note that the values of nums are not necessarily unique.

// Constraints:

//     1 <= nums.length <= 5 * 104
//     -5 * 104 <= nums[i] <= 5 * 104

package sortanarray

func sortArray(nums []int) []int {
	return mergeSort(nums, 0, len(nums)-1)
}

func mergeSort(nums []int, l, r int) []int {
	if l < r {
		m := (l + r) / 2
		mergeSort(nums, l, m)
		mergeSort(nums, m+1, r)

		merge(nums, l, m, r)
	}

	return nums
}

func merge(nums []int, l, m, r int) {
	L := make([]int, m-l+1)
	R := make([]int, r-m)
	copy(L, nums[l:m+1])
	copy(R, nums[m+1:r+1])

	var i, j int
	k := l

	for i < len(L) && j < len(R) {
		if L[i] < R[j] {
			nums[k] = L[i]
			i++
		} else {
			nums[k] = R[j]
			j++
		}
		k++
	}

	for i < len(L) {
		nums[k] = L[i]
		k++
		i++
	}
	for j < len(R) {
		nums[k] = R[j]
		k++
		j++
	}
}
