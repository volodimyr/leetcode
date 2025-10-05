//Design Double-ended Queue

// Design a Double-ended Queue class.

// Your Deque class should support the following operations:

//     Deque() will initialize an empty queue.
//     bool isEmpty() will return whether the queue is empty or not.
//     void append(int value) will insert value at the end of the queue.
//     void appendleft(int val) will insert value at the beginning of the queue.
//     int pop() will remove and return the value at the end of the queue. If the queue is empty, return -1.
//     int popleft() will remove and return the value at the beginning of the queue. If the queue is empty, return -1.

// Note: You should implement each operation in O(1)O(1) time complexity.

// Example 1:

// Input:
// ["isEmpty", "append", 10, "isEmpty", "appendLeft", 20, "popLeft", "pop", "pop", "append", 30, "pop", "isEmpty"]

// Output:
// [true, null, false, null, 20, 10, -1, null, 30, true]

package ds

type Deque struct {
	head *deqnode
	tail *deqnode
}

type deqnode struct {
	val  int
	next *deqnode
	prev *deqnode
}

func NewDeque() *Deque {
	return &Deque{}
}

func NewDequeInts(vals []int) *Deque {
	d := &Deque{}
	for _, val := range vals {
		d.Append(val)
	}
	return d
}

func (d *Deque) IsEmpty() bool {
	return d.head == nil
}

func (d *Deque) Append(value int) {
	n := &deqnode{val: value, prev: d.tail}
	if d.tail != nil {
		d.tail.next = n
	} else {
		d.head = n
	}
	d.tail = n
}

func (d *Deque) AppendLeft(value int) {
	n := &deqnode{val: value, next: d.head}
	if d.head != nil {
		d.head.prev = n
	} else {
		d.tail = n
	}
	d.head = n
}

func (d *Deque) Pop() int {
	if d.IsEmpty() {
		return -1
	}
	if d.head == d.tail {
		v := d.head.val
		d.head = nil
		d.tail = nil
		return v
	}
	v := d.tail.val
	d.tail = d.tail.prev
	d.tail.next = nil
	return v
}

func (d *Deque) GetArray() []int {
	var arr []int
	curr := d.head
	for curr != nil {
		arr = append(arr, curr.val)
		curr = curr.next
	}
	return arr
}

func (d *Deque) PopLeft() int {
	if d.IsEmpty() {
		return -1
	}
	if d.head == d.tail {
		v := d.head.val
		d.head = nil
		d.tail = nil
		return v
	}
	v := d.head.val
	d.head = d.head.next
	d.head.prev = nil
	return v
}
