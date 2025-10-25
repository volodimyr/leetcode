package ds

type DoublyLinkedList struct {
	head *Dnode
	tail *Dnode
}

type Dnode struct {
	val  int
	key  int
	freq int
	next *Dnode
	prev *Dnode
}

func NewDnode(key, val, freq int) *Dnode {
	return &Dnode{val: val, key: key, freq: freq}
}

func (d *Dnode) Val() int {
	return d.val
}

func (d *Dnode) SetVal(v int) {
	d.val = v
}

func (d *Dnode) Key() int {
	return d.key
}

func (d *Dnode) Freq() int {
	return d.freq
}

func (d *Dnode) FreqIncr() {
	d.freq++
}

func NewDoublyLinkedList() *DoublyLinkedList {
	return &DoublyLinkedList{}
}

func (d *DoublyLinkedList) InsertHeadWithKey(val, key int) *Dnode {
	node := &Dnode{val: val, key: key, prev: nil, next: d.head}
	if d.head != nil {
		d.head.prev = node
	} else {
		d.tail = node
	}
	d.head = node
	return d.head
}

func (d *DoublyLinkedList) InsertHeadByRef(node *Dnode) {
	if d.head != nil {
		d.head.prev, node.next = node, d.head
	} else {
		d.tail = node
	}
	d.head = node
}

func (d *DoublyLinkedList) InsertHead(val int) {
	node := &Dnode{val: val, prev: nil, next: d.head}
	if d.head != nil {
		d.head.prev, node.next = node, d.head
	} else {
		d.tail = node
	}
	d.head = node
}

func (d *DoublyLinkedList) InsertTail(val int) {
	node := &Dnode{val: val, next: nil, prev: d.tail}
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
	n := &Dnode{val: val, next: curr.next, prev: curr}
	curr.next = n
	if n.next != nil {
		n.next.prev = n
	}
	return true
}

func (d *DoublyLinkedList) Empty() bool {
	return d.head == nil
}

func (d *DoublyLinkedList) RemoveByRef(ref *Dnode) {
	if ref == d.head {
		d.RemoveHead()
		return
	}
	if ref == d.tail {
		d.RemoveTail()
		return
	}
	ref.prev.next = ref.next
	ref.next.prev = ref.prev
}

func (d *DoublyLinkedList) RemoveHead() {
	if d.head == nil {
		return
	}
	if d.head == d.tail {
		d.tail = nil
		d.head = nil
		return
	}
	d.head = d.head.next
	d.head.prev = nil
}

func (d *DoublyLinkedList) RemoveTailAndReturnKey() int {
	if d.tail == nil {
		return -1
	}
	key := d.tail.Key()
	d.RemoveTail()
	return key
}

func (d *DoublyLinkedList) RemoveTail() {
	if d.tail == nil {
		return
	}
	if d.tail == d.head {
		d.tail = nil
		d.head = nil
		return
	}
	d.tail = d.tail.prev
	d.tail.next = nil
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
