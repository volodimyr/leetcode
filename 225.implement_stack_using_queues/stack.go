// 225. Implement stack using queues
// Topics: 'Stack', 'Design', 'Queue'

// Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

// Implement the MyStack class:

//     void push(int x) Pushes element x to the top of the stack.
//     int pop() Removes the element on the top of the stack and returns it.
//     int top() Returns the element on the top of the stack.
//     boolean empty() Returns true if the stack is empty, false otherwise.

// Notes:

//     You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
//     Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.

// Example 1:

// Input
// ["MyStack", "push", "push", "top", "pop", "empty"]
// [[], [1], [2], [], [], []]
// Output
// [null, null, null, 2, 2, false]

// Explanation
// MyStack myStack = new MyStack();
// myStack.push(1);
// myStack.push(2);
// myStack.top(); // return 2
// myStack.pop(); // return 2
// myStack.empty(); // return False

// Constraints:

//     1 <= x <= 9
//     At most 100 calls will be made to push, pop, top, and empty.
//     All the calls to pop and top are valid.

// Follow-up: Can you implement the stack using only one queue?

package implementstackusingqueues

type MyStack struct {
	q    *queue
	size int
}

func Constructor() MyStack {
	return MyStack{
		q: &queue{},
	}
}

func (s *MyStack) Push(x int) {
	s.q.enqueue(x)
	s.size += 1
	if s.size <= 1 {
		return
	}
	for i := 0; i < s.size-1; i++ {
		s.q.enqueue(s.q.dequeue())
	}
}

func (s *MyStack) Pop() int {
	x := s.q.dequeue()
	s.size -= 1

	return x
}

func (s *MyStack) Top() int {
	return s.q.peek()
}

func (s *MyStack) Empty() bool {
	return s.q.empty()
}

type queue struct {
	head *node
	tail *node
}

type node struct {
	val  int
	next *node
}

func (q *queue) empty() bool {
	return q.head == nil
}

func (q *queue) enqueue(val int) {
	n := &node{val: val}
	if q.head == nil {
		q.head = n
		q.tail = n
		return
	}
	q.tail.next = n
	q.tail = n
}

func (q *queue) dequeue() int {
	if q.head == nil {
		return -1
	}
	val := q.head.val
	if q.head == q.tail {
		q.tail = nil
	}
	q.head = q.head.next

	return val
}

func (q *queue) peek() int {
	if q.head == nil {
		return -1
	}
	return q.head.val
}
