// 703. Kth largest element in a stream
// Topics: 'Tree', 'Design', 'Binary Search Tree', 'Heap (Priority Queue)', 'Binary Tree', 'Data Stream'

// You are part of a university admissions office and need to keep track of the kth highest test score from applicants in real-time. This helps to determine cut-off marks for interviews and admissions dynamically as new applicants submit their scores.

// You are tasked to implement a class which, for a given integer k, maintains a stream of test scores and continuously returns the kth highest test score after a new score has been submitted. More specifically, we are looking for the kth highest score in the sorted list of all scores.

// Implement the KthLargest class:

//     KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of test scores nums.
//     int add(int val) Adds a new test score val to the stream and returns the element representing the kth largest element in the pool of test scores so far.

// Example 1:

// Input:
// ["KthLargest", "add", "add", "add", "add", "add"]
// [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

// Output: [null, 4, 5, 5, 8, 8]

// Explanation:

// KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
// kthLargest.add(3); // return 4
// kthLargest.add(5); // return 5
// kthLargest.add(10); // return 5
// kthLargest.add(9); // return 8
// kthLargest.add(4); // return 8

// Example 2:

// Input:
// ["KthLargest", "add", "add", "add", "add"]
// [[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]]

// Output: [null, 7, 7, 7, 8]

// Explanation:
// KthLargest kthLargest = new KthLargest(4, [7, 7, 7, 7, 8, 3]);
// kthLargest.add(2); // return 7
// kthLargest.add(10); // return 7
// kthLargest.add(9); // return 7
// kthLargest.add(9); // return 8

// Constraints:

//     0 <= nums.length <= 104
//     1 <= k <= nums.length + 1
//     -104 <= nums[i] <= 104
//     -104 <= val <= 104
//     At most 104 calls will be made to add.

package kthlargestelementinastream

type KthLargest struct {
	arr []int
	max int
}

func Constructor(k int, nums []int) KthLargest {
	kth := KthLargest{
		arr: []int{},
		max: k,
	}
	for _, n := range nums {
		kth.Add(n)
	}

	return kth
}

func (k *KthLargest) Add(val int) int {
	if k.max > len(k.arr) {
		k.arr = append(k.arr, val)
		k.heapifyUp()
	} else if val > k.arr[0] {
		k.arr[0] = val
		k.heapifyDown()
	}
	return k.arr[0]
}

func (k *KthLargest) heapifyUp() {
	i := len(k.arr) - 1
	for i > 0 && k.arr[i] < k.arr[(i-1)/2] {
		k.arr[i], k.arr[(i-1)/2] = k.arr[(i-1)/2], k.arr[i]
		i = (i - 1) / 2
	}
}

func (k *KthLargest) heapifyDown() {
	i := 0
	for (2*i + 1) < len(k.arr) {
		if 2*i+2 < len(k.arr) && k.arr[2*i+2] < k.arr[2*i+1] && k.arr[i] > k.arr[2*i+2] {
			k.arr[2*i+2], k.arr[i] = k.arr[i], k.arr[2*i+2]
			i = 2*i + 2
		} else if k.arr[2*i+1] < k.arr[i] {
			k.arr[2*i+1], k.arr[i] = k.arr[i], k.arr[2*i+1]
			i = 2*i + 1
		} else {
			break
		}
	}
}
