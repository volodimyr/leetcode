// 232. Implement queue using stacks
// Topics: 'Design', 'Stack', 'Queue'

// Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

// Implement the MyQueue class:

//     void push(int x) Pushes element x to the back of the queue.
//     int pop() Removes the element from the front of the queue and returns it.
//     int peek() Returns the element at the front of the queue.
//     boolean empty() Returns true if the queue is empty, false otherwise.

// Notes:

//     You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
//     Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

// Example 1:

// Input
// ["MyQueue", "push", "push", "peek", "pop", "empty"]
// [[], [1], [2], [], [], []]
// Output
// [null, null, null, 1, 1, false]

// Explanation
// MyQueue myQueue = new MyQueue();
// myQueue.push(1); // queue is: [1]
// myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
// myQueue.peek(); // return 1
// myQueue.pop(); // return 1, queue is [2]
// myQueue.empty(); // return false

// Constraints:

//     1 <= x <= 9
//     At most 100 calls will be made to push, pop, peek, and empty.
//     All the calls to pop and peek are valid.

package implementqueueusingstacks

type MyQueue struct {
	s1 *Stack[int]
	s2 *Stack[int]
}

func Constructor() MyQueue {
	return MyQueue{
		s1: &Stack[int]{},
		s2: &Stack[int]{},
	}
}

func (mq *MyQueue) Push(x int) {
	mq.s1.Push(x)
}

func (mq *MyQueue) Pop() int {
	if !mq.s2.Empty() {
		return mq.s2.Pop()
	}
	mq.reorder()
	return mq.s2.Pop()
}

func (mq *MyQueue) reorder() {
	for !mq.s1.Empty() {
		mq.s2.Push(mq.s1.Pop())
	}
}

func (mq *MyQueue) Peek() int {
	if !mq.s2.Empty() {
		return mq.s2.Peek()
	}
	mq.reorder()
	return mq.s2.Peek()
}

func (mq *MyQueue) Empty() bool {
	return mq.s2.Empty() && mq.s1.Empty()
}

type Stack[T any] struct {
	arr []T
}

func (s *Stack[T]) Pop() T {
	if s.Empty() {
		return s.zero()
	}
	v := s.arr[len(s.arr)-1]
	s.arr = s.arr[:len(s.arr)-1]
	return v
}

func (s *Stack[T]) Size() int {
	return len(s.arr)
}

func (s *Stack[T]) zero() T {
	var zero T
	return zero
}

func (s *Stack[T]) Push(v T) {
	s.arr = append(s.arr, v)
}

func (s *Stack[T]) Peek() T {
	return s.arr[len(s.arr)-1]
}

func (s *Stack[T]) Empty() bool {
	return len(s.arr) == 0
}
