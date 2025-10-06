// 347. Top K Frequent Elements
// Topics: 'Array', 'Hash Table', 'Divide and Conquer', 'Sorting', 'Heap (Priority Queue)', 'Bucket Sort', 'Counting', 'Quickselect'
// Level: 'Medium'

// Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

// Example 1:

// Input: nums = [1,1,1,2,2,3], k = 2

// Output: [1,2]

// Example 2:

// Input: nums = [1], k = 1

// Output: [1]

// Example 3:

// Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

// Output: [1,2]

// Constraints:

//     1 <= nums.length <= 105
//     -104 <= nums[i] <= 104
//     k is in the range [1, the number of unique elements in the array].
//     It is guaranteed that the answer is unique.

// Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

package topkfreqelements

import "sort"

func topKFrequent(nums []int, k int) []int {
	m := map[int]int{}

	for _, num := range nums {
		m[num]++
	}

	var sorted Sorted
	for k, v := range m {
		sorted = append(sorted, Counter{Val: k, Count: v})
	}
	sort.Sort(sorted)

	return sorted.TopK(k)
}

type Counter struct {
	Val   int
	Count int
}

type Sorted []Counter

func (s Sorted) TopK(k int) []int {
	var arr []int
	for i := range k {
		arr = append(arr, s[i].Val)
	}
	return arr
}
func (s Sorted) Len() int           { return len(s) }
func (s Sorted) Swap(i, j int)      { s[i], s[j] = s[j], s[i] }
func (s Sorted) Less(i, j int) bool { return s[i].Count > s[j].Count }
