// Design heap
// Level: 'Medium'

// Design a Minimum Heap (aka a Priority Queue) class.

// Your MinHeap class should support the following operations:

//     MinHeap() will initialize an empty minimum heap.
//     void push(int val) will add val to the heap.
//     int pop() will remove and return the smallest element in the heap. If the heap is empty, return -1.
//     int top() will return the smallest element in the heap without removing it. If the heap is empty, return -1.
//     void heapify(int[] nums) will build a minimum heap from nums.

// Note: push and pop should be implemented in O(logn)O(logn) time complexity, while top should be implemented in O(1)O(1), and heapify should be implemented in O(n)O(n) time complexity.

// Example 1:

// Input:
// ["top", "push", 1, "top", "pop", "pop"]

// Output:
// [-1, null, 1, 1, -1]

// Example 2:

// Input:
// ["heapify", [1 2 3 4 5], "pop", "pop", "pop", "pop", "pop"]

// Output:
// [null, 1, 2, 3, 4, 5]

package ds

type MinHeap struct {
	arr []int
}

func NewMinHeap() *MinHeap {
	return &MinHeap{
		arr: []int{0},
	}
}

func (mh *MinHeap) Push(val int) {
	mh.arr = append(mh.arr, val)
	i := len(mh.arr) - 1
	for i > 1 && mh.arr[i] < mh.arr[i/2] {
		mh.arr[i/2], mh.arr[i] = mh.arr[i], mh.arr[i/2]
		i = i / 2
	}
}

func (mh *MinHeap) Pop() int {
	if len(mh.arr) == 1 {
		return -1
	}
	if len(mh.arr) == 2 {
		v := mh.arr[len(mh.arr)-1]
		mh.arr = mh.arr[:len(mh.arr)-1]
		return v
	}

	res := mh.arr[1]
	mh.arr[1] = mh.arr[len(mh.arr)-1]
	mh.arr = mh.arr[:len(mh.arr)-1]
	i := 1
	mh.percolate(i)

	return res
}

func (mh *MinHeap) Top() int {
	if len(mh.arr) == 1 {
		return -1
	}
	return mh.arr[1]
}

func (mh *MinHeap) Heapify(nums []int) {
	if len(nums) < 1 {
		return
	}
	nums = append(nums, nums[0])
	mh.arr = nums
	cur := (len(nums) - 1) / 2
	for cur > 0 {
		mh.percolate(cur)
		cur--
	}
}

func (mh *MinHeap) percolate(i int) {
	for 2*i < len(mh.arr) {
		if 2*i+1 < len(mh.arr) && mh.arr[2*i+1] < mh.arr[2*i] && mh.arr[i] > mh.arr[2*i+1] {
			mh.arr[2*i+1], mh.arr[i] = mh.arr[i], mh.arr[2*i+1]
			i = 2*i + 1
		} else if mh.arr[2*i] < mh.arr[i] {
			mh.arr[2*i], mh.arr[i] = mh.arr[i], mh.arr[2*i]
			i = 2 * i
		} else {
			break
		}
	}
}
