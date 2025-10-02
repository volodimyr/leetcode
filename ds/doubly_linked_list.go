package ds

type DoublyLinkedList struct {
	head *dnode
	tail *dnode
}

type dnode struct {
	val  int
	next *dnode
	prev *dnode
}

func NewDoublyLinkedList() *DoublyLinkedList {
	return &DoublyLinkedList{}
}

func (d *DoublyLinkedList) InsertHead(val int) {
	node := &dnode{val: val, prev: nil, next: d.head}
	if d.head != nil {
		d.head.prev = node
	} else {
		d.tail = node
	}
	d.head = node
}

func (d *DoublyLinkedList) InsertTail(val int) {
	node := &dnode{val: val, next: nil, prev: d.tail}
	if d.tail != nil {
		d.tail.next = node
	} else {
		d.head = node
	}

	d.tail = node
}

func (d *DoublyLinkedList) Insert(index, val int) bool {
	if index < 0 {
		return false
	}
	if index == 0 {
		d.InsertHead(val)
		return true
	}
	curr := d.head
	for i := 0; i < index-1 && curr != nil; i++ {
		curr = curr.next
	}
	if curr == nil {
		return false
	}
	if curr.next == nil {
		d.InsertTail(val)
		return true
	}
	n := &dnode{val: val, next: curr.next, prev: curr}
	curr.next = n
	if n.next != nil {
		n.next.prev = n
	}
	return true
}

func (d *DoublyLinkedList) Remove(index int) bool {
	if d.head == nil {
		return false
	}
	if index == 0 {
		d.head = d.head.next
		if d.head != nil {
			d.head.prev = nil
		} else {
			d.tail = nil
		}
		return true
	}
	curr := d.head
	for i := 0; i < index-1 && curr != nil; i++ {
		curr = curr.next
	}
	if curr == nil || curr.next == nil {
		return false
	}
	curr.next = curr.next.next
	if curr.next != nil {
		curr.next.prev = curr
	} else {
		d.tail = curr
	}
	return true
}

func (d *DoublyLinkedList) Get(index int) int {
	if index < 0 {
		return -1
	}
	if d.head == nil {
		return -1
	}
	curr := d.head
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

func (d *DoublyLinkedList) Forward() []int {
	var arr []int
	curr := d.head
	for curr != nil {
		arr = append(arr, curr.val)
		curr = curr.next
	}
	return arr
}

func (d *DoublyLinkedList) Backward() []int {
	var arr []int
	curr := d.tail
	for curr != nil {
		arr = append(arr, curr.val)
		curr = curr.prev
	}
	return arr
}
