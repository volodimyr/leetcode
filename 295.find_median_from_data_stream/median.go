// 295. Find median from Data Stream
// Topics: 'Two Pointers', 'Design', 'Sorting', 'Heap (Priority Queue)', 'Data Stream'
// Level: 'Hard'

// The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

//     For example, for arr = [2,3,4], the median is 3.
//     For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

// Implement the MedianFinder class:

//     MedianFinder() initializes the MedianFinder object.
//     void addNum(int num) adds the integer num from the data stream to the data structure.
//     double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

// Example 1:

// Input
// ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
// [[], [1], [2], [], [3], []]
// Output
// [null, null, null, 1.5, null, 2.0]

// Explanation
// MedianFinder medianFinder = new MedianFinder();
// medianFinder.addNum(1);    // arr = [1]
// medianFinder.addNum(2);    // arr = [1, 2]
// medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
// medianFinder.addNum(3);    // arr[1, 2, 3]
// medianFinder.findMedian(); // return 2.0

// Constraints:

//     -105 <= num <= 105
//     There will be at least one element in the data structure before calling findMedian.
//     At most 5 * 104 calls will be made to addNum and findMedian.

// Follow up:

//     If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
//     If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?

package findmedianfromdatastream

import "container/heap"

type MedianFinder struct {
	finder *medianHeap
}

func Constructor() MedianFinder {
	return MedianFinder{
		finder: &medianHeap{
			largest:  minheap{},
			smallest: maxheap{},
		},
	}
}

func (m *MedianFinder) AddNum(num int) {
	m.finder.Add(num)
}

func (m *MedianFinder) FindMedian() float64 {
	return m.finder.Median()
}

type medianHeap struct {
	smallest maxheap
	largest  minheap
}

func (m *medianHeap) Len() int {
	return m.smallest.Len() + m.largest.Len()
}

func (m *medianHeap) Median() float64 {
	if m.smallest.Len() > m.largest.Len() {
		return float64(m.smallest[0])
	}
	return (float64(m.largest[0]) + float64(m.smallest[0])) / 2
}

func (m *medianHeap) Add(num int) {
	if m.smallest.Len() == 0 || num <= m.smallest[0] {
		heap.Push(&m.smallest, num)
	} else {
		heap.Push(&m.largest, num)
	}
	if m.smallest.Len() > m.largest.Len()+1 {
		heap.Push(&m.largest, heap.Pop(&m.smallest).(int))
	} else if m.largest.Len() > m.smallest.Len() {
		heap.Push(&m.smallest, heap.Pop(&m.largest).(int))
	}
}

type (
	maxheap []int
	minheap []int
)

func (m maxheap) Len() int {
	return len(m)
}

func (m maxheap) Swap(i, j int) {
	m[i], m[j] = m[j], m[i]
}

func (m maxheap) Less(i, j int) bool {
	return m[i] > m[j]
}

func (m *maxheap) Push(v interface{}) {
	*m = append(*m, v.(int))
}

func (m *maxheap) Pop() interface{} {
	old := *m
	x := old[len(old)-1]
	*m = old[:len(old)-1]
	return x
}

// min heap
func (m minheap) Len() int {
	return len(m)
}

func (m minheap) Swap(i, j int) {
	m[i], m[j] = m[j], m[i]
}

func (m minheap) Less(i, j int) bool {
	return m[i] < m[j]
}

func (m *minheap) Push(v interface{}) {
	*m = append(*m, v.(int))
}

func (m *minheap) Pop() interface{} {
	old := *m
	x := old[len(old)-1]
	*m = old[:len(old)-1]
	return x
}
