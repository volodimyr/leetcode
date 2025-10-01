// 707. Design Linked List
// Topics: 'Linked List', 'Design'

// Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
// A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
// If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

// Implement the MyLinkedList class:

//     MyLinkedList() Initializes the MyLinkedList object.
//     int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
//     void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
//     void addAtTail(int val) Append a node of value val as the last element of the linked list.
//     void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
//     void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.

// Example 1:

// Input
// ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
// [[], [1], [3], [1, 2], [1], [1], [1]]
// Output
// [null, null, null, null, 2, null, 3]

// Explanation
// MyLinkedList myLinkedList = new MyLinkedList();
// myLinkedList.addAtHead(1);
// myLinkedList.addAtTail(3);
// myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
// myLinkedList.get(1);              // return 2
// myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
// myLinkedList.get(1);              // return 3

// Constraints:

//     0 <= index, val <= 1000
//     Please do not use the built-in LinkedList library.
//     At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.

package designlinkedlist

type MyLinkedList struct {
	head *node
}

type node struct {
	val  int
	next *node
}

func Constructor() MyLinkedList {
	return MyLinkedList{}
}

func (m *MyLinkedList) Get(index int) int {
	if index < 0 {
		return -1
	}
	curr := m.head
	for i := 0; i < index && curr != nil; i++ {
		curr = curr.next
	}
	if curr == nil {
		return -1
	}
	return curr.val
}

func (m *MyLinkedList) AddAtHead(val int) {
	m.head = &node{val: val, next: m.head}
}

func (m *MyLinkedList) AddAtTail(val int) {
	if m.head == nil {
		m.head = &node{val: val}
		return
	}
	curr := m.head
	for curr.next != nil {
		curr = curr.next
	}
	curr.next = &node{val: val}
}

func (m *MyLinkedList) AddAtIndex(index int, val int) {
	if index == 0 {
		n := &node{val: val, next: m.head}
		m.head = n
		return
	}
	curr := m.head
	for i := 0; i < index-1 && curr != nil; i++ {
		curr = curr.next
	}
	if curr == nil {
		return
	}
	curr.next = &node{val: val, next: curr.next}
}

func (m *MyLinkedList) DeleteAtIndex(index int) {
	if m.head == nil {
		return
	}
	if index == 0 {
		m.head = m.head.next
		return
	}
	curr := m.head
	for i := 0; i < index-1 && curr != nil; i++ {
		curr = curr.next
	}
	if curr == nil || curr.next == nil {
		return
	}
	curr.next = curr.next.next
}

func (m *MyLinkedList) GetValues() []int {
	var arr []int
	curr := m.head
	for curr != nil {
		arr = append(arr, curr.val)
		curr = curr.next
	}
	return arr
}
