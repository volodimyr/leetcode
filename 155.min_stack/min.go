// 155. Min Stack
// Topics: 'Stack'
// Level: 'Medium'

// Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

// Implement the MinStack class:

//     MinStack() initializes the stack object.
//     void push(int val) pushes the element val onto the stack.
//     void pop() removes the element on the top of the stack.
//     int top() gets the top element of the stack.
//     int getMin() retrieves the minimum element in the stack.

// You must implement a solution with O(1) time complexity for each function.

// Example 1:

// Input
// ["MinStack","push","push","push","getMin","pop","top","getMin"]
// [[],[-2],[0],[-3],[],[],[],[]]

// Output
// [null,null,null,null,-3,null,0,-2]

// Explanation
// MinStack minStack = new MinStack();
// minStack.push(-2);
// minStack.push(0);
// minStack.push(-3);
// minStack.getMin(); // return -3
// minStack.pop();
// minStack.top();    // return 0
// minStack.getMin(); // return -2

// Constraints:

//     -231 <= val <= 231 - 1
//     Methods pop, top and getMin operations will always be called on non-empty stacks.
//     At most 3 * 104 calls will be made to push, pop, top, and getMin.

package minstack

type value struct {
	val int
	min int
}

type MinStack struct {
	arr []value
}

func Constructor() MinStack {
	return MinStack{
		arr: make([]value, 0),
	}
}

func (m *MinStack) Push(val int) {
	if m.empty() {
		m.arr = append(m.arr, value{val: val, min: val})
		return
	}
	peeked := m.peek()
	if peeked.min < val {
		m.arr = append(m.arr, value{val: val, min: peeked.min})
	} else {
		m.arr = append(m.arr, value{val: val, min: val})
	}
}

func (m *MinStack) empty() bool {
	return len(m.arr) == 0
}

func (m *MinStack) Pop() {
	m.arr = m.arr[:len(m.arr)-1]
}

func (m *MinStack) peek() value {
	return m.arr[len(m.arr)-1]
}

func (m *MinStack) Top() int {
	return m.arr[len(m.arr)-1].val
}

func (m *MinStack) GetMin() int {
	return m.arr[len(m.arr)-1].min
}
