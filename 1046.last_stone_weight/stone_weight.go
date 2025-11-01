// 1046. Last stone weight
// Topics: 'Array', 'Heap (Priority Queue)'

// You are given an array of integers stones where stones[i] is the weight of the ith stone.

// We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

//     If x == y, both stones are destroyed, and
//     If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.

// At the end of the game, there is at most one stone left.

// Return the weight of the last remaining stone. If there are no stones left, return 0.

// Example 1:

// Input: stones = [2,7,4,1,8,1]
// Output: 1
// Explanation:
// We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
// we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
// we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
// we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

// Example 2:

// Input: stones = [1]
// Output: 1

// Constraints:

//     1 <= stones.length <= 30
//     1 <= stones[i] <= 1000

package laststoneweight

func lastStoneWeight(stones []int) int {
	heap := newMaxHeap(stones)

	for len(heap.stones) >= 2 {
		biggest1, biggest2 := heap.pop(), heap.pop()
		if biggest1 == biggest2 {
			continue
		}
		heap.push(biggest1 - biggest2)
	}
	if len(heap.stones) == 0 {
		return 0
	}
	return heap.stones[0]
}

type maxheap struct {
	stones []int
}

func newMaxHeap(stones []int) *maxheap {
	heap := &maxheap{stones: stones}
	i := (len(heap.stones) - 1) / 2
	for i >= 0 {
		heap.percolate(i)
		i--
	}
	return heap
}

func (m *maxheap) push(stone int) {
	m.stones = append(m.stones, stone)
	i := len(m.stones) - 1
	for i > 0 && m.stones[i] > m.stones[(i-1)/2] {
		m.stones[i], m.stones[(i-1)/2] = m.stones[(i-1)/2], m.stones[i]
		i = (i - 1) / 2
	}
}

func (m *maxheap) pop() int {
	if len(m.stones) == 0 {
		return -1
	}
	if len(m.stones) == 1 {
		v := m.stones[0]
		m.stones = []int{}
		return v
	}
	v := m.stones[0]
	m.stones[0] = m.stones[len(m.stones)-1]
	m.stones = m.stones[:len(m.stones)-1]
	m.percolate(0)
	return v
}

func (m *maxheap) percolate(i int) {
	for {
		largest := i
		left := 2*i + 1
		right := 2*i + 2
		if left < len(m.stones) && m.stones[left] > m.stones[largest] {
			largest = left
		}
		if right < len(m.stones) && m.stones[right] > m.stones[largest] {
			largest = right
		}

		if largest != i {
			m.stones[largest], m.stones[i] = m.stones[i], m.stones[largest]
			i = largest
		} else {
			break
		}
	}
}
