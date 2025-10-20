// 622. Desgin circular queue
// Topics: 'Design', 'Queue', 'Array', 'Linked List'
// Level: 'Medium'

// Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle, and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

// One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

// Implement the MyCircularQueue class:

//     MyCircularQueue(k) Initializes the object with the size of the queue to be k.
//     int Front() Gets the front item from the queue. If the queue is empty, return -1.
//     int Rear() Gets the last item from the queue. If the queue is empty, return -1.
//     boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
//     boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
//     boolean isEmpty() Checks whether the circular queue is empty or not.
//     boolean isFull() Checks whether the circular queue is full or not.

// You must solve the problem without using the built-in queue data structure in your programming language.

// Example 1:

// Input
// ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
// [[3], [1], [2], [3], [4], [], [], [], [4], []]
// Output
// [null, true, true, true, false, 3, true, true, true, 4]

// Explanation
// MyCircularQueue myCircularQueue = new MyCircularQueue(3);
// myCircularQueue.enQueue(1); // return True
// myCircularQueue.enQueue(2); // return True
// myCircularQueue.enQueue(3); // return True
// myCircularQueue.enQueue(4); // return False
// myCircularQueue.Rear();     // return 3
// myCircularQueue.isFull();   // return True
// myCircularQueue.deQueue();  // return True
// myCircularQueue.enQueue(4); // return True
// myCircularQueue.Rear();     // return 4

// Constraints:

//     1 <= k <= 1000
//     0 <= value <= 1000
//     At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull.

package designcircularqueue

type MyCircularQueue struct {
	arr         []int
	front, rear int
	max         int
	cap         int
}

func Constructor(k int) MyCircularQueue {
	arr := make([]int, 0, k)
	for range k {
		arr = append(arr, -1)
	}
	return MyCircularQueue{
		arr:   arr,
		front: -1,
		rear:  -1,
		cap:   0,
		max:   k,
	}
}

func (m *MyCircularQueue) EnQueue(value int) bool {
	if m.IsFull() {
		return false
	}
	if m.IsEmpty() {
		m.front++
		m.rear++
		m.arr[m.rear] = value
	} else {
		if (m.rear + 1) == m.max {
			// wrap around
			m.rear = 0
		} else {
			m.rear++
		}
		m.arr[m.rear] = value
	}
	m.cap++
	return true
}

func (m *MyCircularQueue) DeQueue() bool {
	if m.IsEmpty() {
		return false
	}
	m.arr[m.front] = -1
	m.cap--
	if m.IsEmpty() {
		m.front = -1
		m.rear = -1
	} else {
		m.front++
		if m.front == m.max {
			// wrap around
			m.front = 0
		}
	}
	return true
}

func (m *MyCircularQueue) Front() int {
	if m.front == -1 {
		return -1
	}
	return m.arr[m.front]
}

func (m *MyCircularQueue) Rear() int {
	if m.rear == -1 {
		return -1
	}
	return m.arr[m.rear]
}

func (m *MyCircularQueue) IsEmpty() bool {
	return m.cap == 0
}

func (m *MyCircularQueue) IsFull() bool {
	return m.cap == m.max
}
