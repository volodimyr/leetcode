// Design Singly Linked List
// Topics: 'Data structures'

// Design a Singly Linked List class.

// Your LinkedList class should support the following operations:

//     LinkedList() will initialize an empty linked list.
//     int get(int i) will return the value of the ith node (0-indexed). If the index is out of bounds, return -1.
//     void insertHead(int val) will insert a node with val at the head of the list.
//     void insertTail(int val) will insert a node with val at the tail of the list.
//     bool remove(int i) will remove the ith node (0-indexed). If the index is out of bounds, return false, otherwise return true.
//     int[] getValues() return an array of all the values in the linked list, ordered from head to tail.

// Example 1:

// Input:
// ["insertHead", 1, "insertTail", 2, "insertHead", 0, "remove", 1, "getValues"]

// Output:
// [null, null, null, true, [0, 2]]

// Example 2:

// Input:
// ["insertHead", 1, "insertHead", 2, "get", 5]

// Output:
// [null, null, -1]

// Note:

//     The index int i provided to get(int i) and remove(int i) is guaranteed to be greater than or equal to 0.

package ds

type LinkedList struct {
	head *node
}

type node struct {
	val  int
	next *node
}

func NewLinkedList() *LinkedList {
	return &LinkedList{}
}

func (ll *LinkedList) Get(index int) int {
	if ll.head == nil {
		return -1
	}
	curr := ll.head
	for i := 0; i < index; i++ {
		if curr == nil {
			return -1
		}
		curr = curr.next
	}
	if curr == nil {
		return -1
	}
	return curr.val
}

func (ll *LinkedList) InsertHead(val int) {
	ll.head = &node{val: val, next: ll.head}
}

func (ll *LinkedList) InsertTail(val int) {
	newTail := &node{val: val}
	if ll.head == nil {
		ll.head = newTail
		return
	}
	curr := ll.head
	for curr.next != nil {
		curr = curr.next
	}
	curr.next = newTail
}

func (ll *LinkedList) Remove(index int) bool {
	if ll.head == nil {
		return false
	}
	if index == 0 {
		ll.head = ll.head.next
		return true
	}

	curr := ll.head
	for i := 0; i < index-1 && curr != nil; i++ {
		curr = curr.next
	}
	if curr == nil || curr.next == nil {
		return false
	}
	curr.next = curr.next.next
	return true
}

func (ll *LinkedList) GetValues() []int {
	var arr []int
	curr := ll.head
	for curr != nil {
		arr = append(arr, curr.val)
		curr = curr.next
	}
	return arr
}
