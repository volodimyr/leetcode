// 739. Daily temperatures
// Topics: 'Stack', 'Array', 'Monotonic Stack'

// Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

// Example 1:

// Input: temperatures = [73,74,75,71,69,72,76,73]
// Output: [1,1,4,2,1,1,0,0]

// Example 2:

// Input: temperatures = [30,40,50,60]
// Output: [1,1,1,0]

// Example 3:

// Input: temperatures = [30,60,90]
// Output: [1,1,0]

//	for !stack.empty() && temperatures[stack.peek()] <= temperatures[i] {
//
// stack.pop()
// }
package dailytemperatures

func dailyTemperatures(temperatures []int) []int {
	stack := newmstack()
	warmer := make([]int, len(temperatures))
	for i := len(temperatures) - 1; i >= 0; i-- {
		for !stack.empty() && temperatures[stack.peek()] <= temperatures[i] {
			stack.pop()
		}
		if stack.empty() {
			warmer[i] = 0
		} else {
			warmer[i] = stack.peek() - i
		}
		stack.push(i)
	}

	return warmer
}

type monotonicStack struct {
	arr []int
}

func newmstack() *monotonicStack {
	return &monotonicStack{}
}

func (m *monotonicStack) size() int {
	return len(m.arr)
}

func (m *monotonicStack) peek() int {
	if m.empty() {
		return -1
	}
	return m.arr[len(m.arr)-1]
}

func (m *monotonicStack) pop() int {
	if m.empty() {
		return -1
	}
	x := m.arr[len(m.arr)-1]
	m.arr = m.arr[:len(m.arr)-1]
	return x
}

func (m *monotonicStack) push(x int) {
	m.arr = append(m.arr, x)
}

func (m *monotonicStack) empty() bool {
	return len(m.arr) == 0
}
