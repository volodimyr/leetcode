package ds

import "testing"

func TestDoublyLinkedList_FullFlow(t *testing.T) {
	dll := NewDoublyLinkedList()

	// 1. InsertHead on empty list
	dll.InsertHead(10) // [10]
	if !equalSlices(dll.Forward(), []int{10}) {
		t.Errorf("expected [10], got %v", dll.Forward())
	}
	if !equalSlices(dll.Backward(), []int{10}) {
		t.Errorf("expected [10], got %v", dll.Backward())
	}

	// 2. InsertTail
	dll.InsertTail(20) // [10,20]
	dll.InsertTail(30) // [10,20,30]
	if !equalSlices(dll.Forward(), []int{10, 20, 30}) {
		t.Errorf("expected [10,20,30], got %v", dll.Forward())
	}
	if !equalSlices(dll.Backward(), []int{30, 20, 10}) {
		t.Errorf("expected [30,20,10], got %v", dll.Backward())
	}

	// 3. Insert at index (middle)
	ok := dll.Insert(1, 15) // [10,15,20,30]
	if !ok {
		t.Error("Insert at index 1 should succeed")
	}
	if !equalSlices(dll.Forward(), []int{10, 15, 20, 30}) {
		t.Errorf("expected [10,15,20,30], got %v", dll.Forward())
	}

	// 4. Insert at index == length (append to tail)
	ok = dll.Insert(4, 40) // [10,15,20,30,40]
	if !ok {
		t.Error("Insert at tail should succeed")
	}
	if dll.tail.val != 40 {
		t.Errorf("expected tail=40, got %d", dll.tail.val)
	}

	// 5. Insert at invalid index (out of bounds)
	ok = dll.Insert(10, 99)
	if ok {
		t.Error("Insert out of bounds should fail")
	}

	// 6. Get values
	if dll.Get(0) != 10 || dll.Get(2) != 20 || dll.Get(4) != 40 {
		t.Errorf("Get returned wrong values: got [0]=%d [2]=%d [4]=%d",
			dll.Get(0), dll.Get(2), dll.Get(4))
	}
	if dll.Get(-1) != -1 || dll.Get(99) != -1 {
		t.Error("Get should return -1 for invalid indices")
	}

	// 7. Remove head
	ok = dll.Remove(0) // remove 10 → [15,20,30,40]
	if !ok {
		t.Error("Remove head should succeed")
	}
	if dll.head.val != 15 {
		t.Errorf("expected new head=15, got %d", dll.head.val)
	}

	// 8. Remove middle
	ok = dll.Remove(1) // remove 20 → [15,30,40]
	if !ok {
		t.Error("Remove middle should succeed")
	}
	if !equalSlices(dll.Forward(), []int{15, 30, 40}) {
		t.Errorf("expected [15,30,40], got %v", dll.Forward())
	}

	// 9. Remove tail
	ok = dll.Remove(2) // remove 40 → [15,30]
	if !ok {
		t.Error("Remove tail should succeed")
	}
	if dll.tail.val != 30 {
		t.Errorf("expected tail=30, got %d", dll.tail.val)
	}

	// 10. Remove out of bounds
	ok = dll.Remove(10)
	if ok {
		t.Error("Remove out of bounds should fail")
	}

	// Final state check
	expectedForward := []int{15, 30}
	expectedBackward := []int{30, 15}
	if !equalSlices(dll.Forward(), expectedForward) {
		t.Errorf("Forward final = %v, want %v", dll.Forward(), expectedForward)
	}
	if !equalSlices(dll.Backward(), expectedBackward) {
		t.Errorf("Backward final = %v, want %v", dll.Backward(), expectedBackward)
	}
}

func TestDoublyLinkedList_Insert(t *testing.T) {
	tests := []struct {
		name             string
		setup            func() *DoublyLinkedList
		index            int
		val              int
		expectedForward  []int
		expectedBackward []int
	}{
		{
			name: "insert at head when list empty",
			setup: func() *DoublyLinkedList {
				return NewDoublyLinkedList()
			},
			index:            0,
			val:              10,
			expectedForward:  []int{10},
			expectedBackward: []int{10},
		},
		{
			name: "insert at head when list not empty",
			setup: func() *DoublyLinkedList {
				ll := NewDoublyLinkedList()
				ll.InsertTail(20)
				ll.InsertTail(30)
				return ll
			},
			index:            0,
			val:              10,
			expectedForward:  []int{10, 20, 30},
			expectedBackward: []int{30, 20, 10},
		},
		{
			name: "insert at tail using insert with index == length",
			setup: func() *DoublyLinkedList {
				ll := NewDoublyLinkedList()
				ll.InsertTail(10)
				ll.InsertTail(20)
				return ll
			},
			index:            2,
			val:              30,
			expectedForward:  []int{10, 20, 30},
			expectedBackward: []int{30, 20, 10},
		},
		{
			name: "insert in middle of list",
			setup: func() *DoublyLinkedList {
				ll := NewDoublyLinkedList()
				ll.InsertTail(10)
				ll.InsertTail(30)
				return ll
			},
			index:            1,
			val:              20,
			expectedForward:  []int{10, 20, 30},
			expectedBackward: []int{30, 20, 10},
		},
		{
			name: "insert out of bounds (too large index) should do nothing",
			setup: func() *DoublyLinkedList {
				ll := NewDoublyLinkedList()
				ll.InsertTail(10)
				ll.InsertTail(20)
				return ll
			},
			index:            5,
			val:              99,
			expectedForward:  []int{10, 20},
			expectedBackward: []int{20, 10},
		},
		{
			name: "insert with negative index should do nothing",
			setup: func() *DoublyLinkedList {
				ll := NewDoublyLinkedList()
				ll.InsertTail(10)
				return ll
			},
			index:            -1,
			val:              99,
			expectedForward:  []int{10},
			expectedBackward: []int{10},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			ll := tt.setup()
			ll.Insert(tt.index, tt.val)

			gotForward := ll.Forward()
			gotBackward := ll.Backward()

			if !equalSlices(gotForward, tt.expectedForward) {
				t.Errorf("Forward() = %v, want %v", gotForward, tt.expectedForward)
			}
			if !equalSlices(gotBackward, tt.expectedBackward) {
				t.Errorf("Backward() = %v, want %v", gotBackward, tt.expectedBackward)
			}
		})
	}
}

func equalSlices(a, b []int) bool {
	if len(a) != len(b) {
		return false
	}
	for i := range a {
		if a[i] != b[i] {
			return false
		}
	}
	return true
}

func TestDoublyLinkedList_Remove(t *testing.T) {
	tests := []struct {
		name     string
		setup    func() *DoublyLinkedList
		index    int
		expected bool
		forward  []int
		backward []int
	}{
		{
			name: "remove from empty list returns false",
			setup: func() *DoublyLinkedList {
				return NewDoublyLinkedList()
			},
			index:    0,
			expected: false,
			forward:  []int{},
			backward: []int{},
		},
		{
			name: "remove only element in single-node list",
			setup: func() *DoublyLinkedList {
				dll := NewDoublyLinkedList()
				dll.InsertTail(10)
				return dll
			},
			index:    0,
			expected: true,
			forward:  []int{},
			backward: []int{},
		},
		{
			name: "remove head element in multi-node list",
			setup: func() *DoublyLinkedList {
				dll := NewDoublyLinkedList()
				dll.InsertTail(1)
				dll.InsertTail(2)
				dll.InsertTail(3)
				return dll
			},
			index:    0,
			expected: true,
			forward:  []int{2, 3},
			backward: []int{3, 2},
		},
		{
			name: "remove middle element",
			setup: func() *DoublyLinkedList {
				dll := NewDoublyLinkedList()
				dll.InsertTail(10)
				dll.InsertTail(20)
				dll.InsertTail(30)
				dll.InsertTail(40)
				return dll
			},
			index:    2,
			expected: true,
			forward:  []int{10, 20, 40},
			backward: []int{40, 20, 10},
		},
		{
			name: "remove last element (tail)",
			setup: func() *DoublyLinkedList {
				dll := NewDoublyLinkedList()
				dll.InsertTail(5)
				dll.InsertTail(6)
				dll.InsertTail(7)
				return dll
			},
			index:    2,
			expected: true,
			forward:  []int{5, 6},
			backward: []int{6, 5},
		},
		{
			name: "remove index out of range",
			setup: func() *DoublyLinkedList {
				dll := NewDoublyLinkedList()
				dll.InsertTail(100)
				dll.InsertTail(200)
				return dll
			},
			index:    5,
			expected: false,
			forward:  []int{100, 200},
			backward: []int{200, 100},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			dll := tt.setup()

			got := dll.Remove(tt.index)
			if got != tt.expected {
				t.Errorf("Remove(%d) = %v, expected %v", tt.index, got, tt.expected)
			}

			forward := dll.Forward()
			backward := dll.Backward()

			if len(forward) != len(tt.forward) {
				t.Errorf("Forward() = %v, expected %v", forward, tt.forward)
			}
			if len(backward) != len(tt.backward) {
				t.Errorf("Backward() = %v, expected %v", backward, tt.backward)
			}

			for i := range forward {
				if forward[i] != tt.forward[i] {
					t.Errorf("Forward() = %v, expected %v", forward, tt.forward)
					break
				}
			}
			for i := range backward {
				if backward[i] != tt.backward[i] {
					t.Errorf("Backward() = %v, expected %v", backward, tt.backward)
					break
				}
			}
		})
	}
}

func TestDoublyLinkedList_Get(t *testing.T) {
	tests := []struct {
		name     string
		setup    func() *DoublyLinkedList
		index    int
		expected int
	}{
		{
			name: "empty list returns -1",
			setup: func() *DoublyLinkedList {
				return NewDoublyLinkedList()
			},
			index:    0,
			expected: -1,
		},
		{
			name: "negative index returns -1",
			setup: func() *DoublyLinkedList {
				dll := NewDoublyLinkedList()
				dll.InsertTail(10)
				return dll
			},
			index:    -1,
			expected: -1,
		},
		{
			name: "index out of range returns -1",
			setup: func() *DoublyLinkedList {
				dll := NewDoublyLinkedList()
				dll.InsertTail(1)
				dll.InsertTail(2)
				return dll
			},
			index:    5,
			expected: -1,
		},
		{
			name: "get first element",
			setup: func() *DoublyLinkedList {
				dll := NewDoublyLinkedList()
				dll.InsertTail(42)
				dll.InsertTail(99)
				return dll
			},
			index:    0,
			expected: 42,
		},
		{
			name: "get middle element",
			setup: func() *DoublyLinkedList {
				dll := NewDoublyLinkedList()
				dll.InsertTail(10)
				dll.InsertTail(20)
				dll.InsertTail(30)
				return dll
			},
			index:    1,
			expected: 20,
		},
		{
			name: "get last element",
			setup: func() *DoublyLinkedList {
				dll := NewDoublyLinkedList()
				dll.InsertTail(5)
				dll.InsertTail(6)
				dll.InsertTail(7)
				return dll
			},
			index:    2,
			expected: 7,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			dll := tt.setup()
			got := dll.Get(tt.index)
			if got != tt.expected {
				t.Errorf("Get(%d) = %d, expected %d", tt.index, got, tt.expected)
			}
		})
	}
}

func TestInsertHead_EmptyList(t *testing.T) {
	dll := NewDoublyLinkedList()

	dll.InsertHead(5)

	// Head should point to new node
	if dll.head == nil {
		t.Fatal("head should not be nil after insert")
	}
	if dll.head.val != 5 {
		t.Errorf("expected head value 5, got %d", dll.head.val)
	}

	// Head's prev should be nil
	if dll.head.prev != nil {
		t.Error("head.prev should be nil")
	}

	// Head's next should be nil (only one element)
	if dll.head.next != nil {
		t.Error("head.next should be nil when list has one element")
	}

	// Tail should point to the same node as head (single element)
	if dll.tail == nil {
		t.Error("tail should not be nil after first insert")
	}
	if dll.tail != dll.head {
		t.Error("tail should equal head when list has one element")
	}
	if dll.tail.val != 5 {
		t.Errorf("expected tail value 5, got %d", dll.tail.val)
	}
}

func TestInsertHead_SingleElement(t *testing.T) {
	dll := NewDoublyLinkedList()
	dll.InsertHead(10)

	dll.InsertHead(20)

	// Head should be the new node
	if dll.head.val != 20 {
		t.Errorf("expected head value 20, got %d", dll.head.val)
	}

	// Head's prev should be nil
	if dll.head.prev != nil {
		t.Error("head.prev should be nil")
	}

	// Head's next should point to old head
	if dll.head.next == nil {
		t.Fatal("head.next should not be nil")
	}
	if dll.head.next.val != 10 {
		t.Errorf("expected head.next value 10, got %d", dll.head.next.val)
	}

	// Old head's prev should point back to new head
	if dll.head.next.prev != dll.head {
		t.Error("second node's prev should point to head")
	}

	// Tail should now be set to the old head
	if dll.tail == nil {
		t.Fatal("tail should be set after second insert")
	}
	if dll.tail.val != 10 {
		t.Errorf("expected tail value 10, got %d", dll.tail.val)
	}
}

func TestInsertHead_MultipleElements(t *testing.T) {
	dll := NewDoublyLinkedList()

	// Insert: 3, 2, 1
	dll.InsertHead(3)
	dll.InsertHead(2)
	dll.InsertHead(1)

	// Head should be 1
	if dll.head.val != 1 {
		t.Errorf("expected head value 1, got %d", dll.head.val)
	}

	// Verify forward traversal: 1 -> 2 -> 3
	result := dll.Forward()
	expected := []int{1, 2, 3}
	if len(result) != len(expected) {
		t.Fatalf("expected length %d, got %d", len(expected), len(result))
	}
	for i, v := range expected {
		if result[i] != v {
			t.Errorf("at index %d: expected %d, got %d", i, v, result[i])
		}
	}

	// Tail should be 3
	if dll.tail == nil {
		t.Fatal("tail should not be nil")
	}
	if dll.tail.val != 3 {
		t.Errorf("expected tail value 3, got %d", dll.tail.val)
	}

	// Tail's next should be nil
	if dll.tail.next != nil {
		t.Error("tail.next should be nil")
	}
}

func TestInsertHead_BackwardTraversal(t *testing.T) {
	dll := NewDoublyLinkedList()

	dll.InsertHead(30)
	dll.InsertHead(20)
	dll.InsertHead(10)

	// Traverse backward from tail: 30 -> 20 -> 10
	var backward []int
	curr := dll.tail
	for curr != nil {
		backward = append(backward, curr.val)
		curr = curr.prev
	}

	expected := []int{30, 20, 10}
	if len(backward) != len(expected) {
		t.Fatalf("expected length %d, got %d", len(expected), len(backward))
	}
	for i, v := range expected {
		if backward[i] != v {
			t.Errorf("at index %d: expected %d, got %d", i, v, backward[i])
		}
	}
}

func TestInsertHead_PrevPointers(t *testing.T) {
	dll := NewDoublyLinkedList()

	dll.InsertHead(1)
	dll.InsertHead(2)
	dll.InsertHead(3)

	// Verify all prev pointers
	// 3 -> 2 -> 1

	// Node 3 (head)
	if dll.head.prev != nil {
		t.Error("head prev should be nil")
	}

	// Node 2
	second := dll.head.next
	if second.prev != dll.head {
		t.Error("second node's prev should point to head")
	}

	// Node 1 (tail)
	third := second.next
	if third.prev != second {
		t.Error("third node's prev should point to second")
	}
}

func TestInsertHead_NextPointers(t *testing.T) {
	dll := NewDoublyLinkedList()

	dll.InsertHead(100)
	dll.InsertHead(200)
	dll.InsertHead(300)

	// Verify all next pointers
	// 300 -> 200 -> 100

	// Node 300 (head)
	if dll.head.next == nil {
		t.Fatal("head.next should not be nil")
	}
	if dll.head.next.val != 200 {
		t.Errorf("head.next should be 200, got %d", dll.head.next.val)
	}

	// Node 200
	second := dll.head.next
	if second.next == nil {
		t.Fatal("second.next should not be nil")
	}
	if second.next.val != 100 {
		t.Errorf("second.next should be 100, got %d", second.next.val)
	}

	// Node 100 (tail)
	third := second.next
	if third.next != nil {
		t.Error("tail.next should be nil")
	}
}

func TestInsertHead_AlternatingWithGet(t *testing.T) {
	dll := NewDoublyLinkedList()

	dll.InsertHead(5)
	if dll.Get(0) != 5 {
		t.Errorf("expected 5 at index 0, got %d", dll.Get(0))
	}

	dll.InsertHead(10)
	if dll.Get(0) != 10 {
		t.Errorf("expected 10 at index 0, got %d", dll.Get(0))
	}
	if dll.Get(1) != 5 {
		t.Errorf("expected 5 at index 1, got %d", dll.Get(1))
	}

	dll.InsertHead(15)
	if dll.Get(0) != 15 {
		t.Errorf("expected 15 at index 0, got %d", dll.Get(0))
	}
	if dll.Get(1) != 10 {
		t.Errorf("expected 10 at index 1, got %d", dll.Get(1))
	}
	if dll.Get(2) != 5 {
		t.Errorf("expected 5 at index 2, got %d", dll.Get(2))
	}
}

// NOTE: Bug in your InsertHead implementation!
// When inserting into an empty list, you don't set the tail.
// This test will FAIL with your current code:
func TestInsertHead_BugCheck_TailNotSetOnFirstInsert(t *testing.T) {
	dll := NewDoublyLinkedList()
	dll.InsertHead(42)

	// BUG: tail is nil, but should equal head when list has one element
	if dll.tail == nil {
		t.Log("BUG DETECTED: tail should be set to head on first insert")
		t.Log("Your code only sets tail when d.head != nil BEFORE insert")
		t.Log("But on first insert, d.head IS nil, so tail never gets set")
	}

	// Expected behavior for single element:
	// HEAD and TAIL should both point to the same node
	if dll.head != dll.tail {
		t.Error("head and tail should be same for single element")
	}
}

func TestInsertTail_EmptyList(t *testing.T) {
	dll := NewDoublyLinkedList()

	dll.InsertTail(5)

	// Tail should point to new node
	if dll.tail == nil {
		t.Fatal("tail should not be nil after insert")
	}
	if dll.tail.val != 5 {
		t.Errorf("expected tail value 5, got %d", dll.tail.val)
	}

	// Tail's next should be nil
	if dll.tail.next != nil {
		t.Error("tail.next should be nil")
	}

	// Tail's prev should be nil (only one element)
	if dll.tail.prev != nil {
		t.Error("tail.prev should be nil when list has one element")
	}

	// Head should point to the same node as tail (single element)
	if dll.head == nil {
		t.Error("head should not be nil after first insert")
	}
	if dll.head != dll.tail {
		t.Error("head should equal tail when list has one element")
	}
	if dll.head.val != 5 {
		t.Errorf("expected head value 5, got %d", dll.head.val)
	}
}

func TestInsertTail_SingleElement(t *testing.T) {
	dll := NewDoublyLinkedList()
	dll.InsertTail(10)

	dll.InsertTail(20)

	// Tail should be the new node
	if dll.tail.val != 20 {
		t.Errorf("expected tail value 20, got %d", dll.tail.val)
	}

	// Tail's next should be nil
	if dll.tail.next != nil {
		t.Error("tail.next should be nil")
	}

	// Tail's prev should point to old tail
	if dll.tail.prev == nil {
		t.Fatal("tail.prev should not be nil")
	}
	if dll.tail.prev.val != 10 {
		t.Errorf("expected tail.prev value 10, got %d", dll.tail.prev.val)
	}

	// Old tail's next should point to new tail
	if dll.tail.prev.next != dll.tail {
		t.Error("first node's next should point to tail")
	}

	// Head should still be the old tail
	if dll.head == nil {
		t.Fatal("head should not be nil")
	}
	if dll.head.val != 10 {
		t.Errorf("expected head value 10, got %d", dll.head.val)
	}
}

func TestInsertTail_MultipleElements(t *testing.T) {
	dll := NewDoublyLinkedList()

	// Insert: 1, 2, 3
	dll.InsertTail(1)
	dll.InsertTail(2)
	dll.InsertTail(3)

	// Tail should be 3
	if dll.tail.val != 3 {
		t.Errorf("expected tail value 3, got %d", dll.tail.val)
	}

	// Head should be 1
	if dll.head.val != 1 {
		t.Errorf("expected head value 1, got %d", dll.head.val)
	}

	// Verify forward traversal: 1 -> 2 -> 3
	result := dll.Forward()
	expected := []int{1, 2, 3}
	if len(result) != len(expected) {
		t.Fatalf("expected length %d, got %d", len(expected), len(result))
	}
	for i, v := range expected {
		if result[i] != v {
			t.Errorf("at index %d: expected %d, got %d", i, v, result[i])
		}
	}

	// Head's prev should be nil
	if dll.head.prev != nil {
		t.Error("head.prev should be nil")
	}

	// Tail's next should be nil
	if dll.tail.next != nil {
		t.Error("tail.next should be nil")
	}
}

func TestInsertTail_BackwardTraversal(t *testing.T) {
	dll := NewDoublyLinkedList()

	dll.InsertTail(10)
	dll.InsertTail(20)
	dll.InsertTail(30)

	// Traverse backward from tail: 30 -> 20 -> 10
	var backward []int
	curr := dll.tail
	for curr != nil {
		backward = append(backward, curr.val)
		curr = curr.prev
	}

	expected := []int{30, 20, 10}
	if len(backward) != len(expected) {
		t.Fatalf("expected length %d, got %d", len(expected), len(backward))
	}
	for i, v := range expected {
		if backward[i] != v {
			t.Errorf("at index %d: expected %d, got %d", i, v, backward[i])
		}
	}
}

func TestInsertTail_PrevPointers(t *testing.T) {
	dll := NewDoublyLinkedList()

	dll.InsertTail(1)
	dll.InsertTail(2)
	dll.InsertTail(3)

	// Verify all prev pointers
	// 1 -> 2 -> 3

	// Node 1 (head)
	if dll.head.prev != nil {
		t.Error("head prev should be nil")
	}

	// Node 2
	second := dll.head.next
	if second == nil {
		t.Fatal("second node should not be nil")
	}
	if second.prev != dll.head {
		t.Error("second node's prev should point to head")
	}

	// Node 3 (tail)
	third := second.next
	if third == nil {
		t.Fatal("third node should not be nil")
	}
	if third.prev != second {
		t.Error("tail's prev should point to second node")
	}
}

func TestInsertTail_NextPointers(t *testing.T) {
	dll := NewDoublyLinkedList()

	dll.InsertTail(100)
	dll.InsertTail(200)
	dll.InsertTail(300)

	// Verify all next pointers
	// 100 -> 200 -> 300

	// Node 100 (head)
	if dll.head.next == nil {
		t.Fatal("head.next should not be nil")
	}
	if dll.head.next.val != 200 {
		t.Errorf("head.next should be 200, got %d", dll.head.next.val)
	}

	// Node 200
	second := dll.head.next
	if second.next == nil {
		t.Fatal("second.next should not be nil")
	}
	if second.next.val != 300 {
		t.Errorf("second.next should be 300, got %d", second.next.val)
	}

	// Node 300 (tail)
	third := second.next
	if third.next != nil {
		t.Error("tail.next should be nil")
	}
}

func TestInsertTail_AlternatingWithGet(t *testing.T) {
	dll := NewDoublyLinkedList()

	dll.InsertTail(5)
	if dll.Get(0) != 5 {
		t.Errorf("expected 5 at index 0, got %d", dll.Get(0))
	}

	dll.InsertTail(10)
	if dll.Get(0) != 5 {
		t.Errorf("expected 5 at index 0, got %d", dll.Get(0))
	}
	if dll.Get(1) != 10 {
		t.Errorf("expected 10 at index 1, got %d", dll.Get(1))
	}

	dll.InsertTail(15)
	if dll.Get(0) != 5 {
		t.Errorf("expected 5 at index 0, got %d", dll.Get(0))
	}
	if dll.Get(1) != 10 {
		t.Errorf("expected 10 at index 1, got %d", dll.Get(1))
	}
	if dll.Get(2) != 15 {
		t.Errorf("expected 15 at index 2, got %d", dll.Get(2))
	}
}

func TestInsertTail_MixedWithInsertHead(t *testing.T) {
	dll := NewDoublyLinkedList()

	dll.InsertTail(2) // [2]
	dll.InsertHead(1) // [1, 2]
	dll.InsertTail(3) // [1, 2, 3]
	dll.InsertHead(0) // [0, 1, 2, 3]
	dll.InsertTail(4) // [0, 1, 2, 3, 4]

	// Verify forward traversal
	result := dll.Forward()
	expected := []int{0, 1, 2, 3, 4}
	if len(result) != len(expected) {
		t.Fatalf("expected length %d, got %d", len(expected), len(result))
	}
	for i, v := range expected {
		if result[i] != v {
			t.Errorf("at index %d: expected %d, got %d", i, v, result[i])
		}
	}

	// Verify head and tail
	if dll.head.val != 0 {
		t.Errorf("expected head value 0, got %d", dll.head.val)
	}
	if dll.tail.val != 4 {
		t.Errorf("expected tail value 4, got %d", dll.tail.val)
	}

	// Verify backward traversal
	var backward []int
	curr := dll.tail
	for curr != nil {
		backward = append(backward, curr.val)
		curr = curr.prev
	}
	expectedBackward := []int{4, 3, 2, 1, 0}
	if len(backward) != len(expectedBackward) {
		t.Fatalf("expected backward length %d, got %d", len(expectedBackward), len(backward))
	}
	for i, v := range expectedBackward {
		if backward[i] != v {
			t.Errorf("backward at index %d: expected %d, got %d", i, v, backward[i])
		}
	}
}

func TestInsertTail_LargeList(t *testing.T) {
	dll := NewDoublyLinkedList()

	// Insert 100 elements
	for i := 0; i < 100; i++ {
		dll.InsertTail(i)
	}

	// Verify head is 0
	if dll.head.val != 0 {
		t.Errorf("expected head value 0, got %d", dll.head.val)
	}

	// Verify tail is 99
	if dll.tail.val != 99 {
		t.Errorf("expected tail value 99, got %d", dll.tail.val)
	}

	// Verify all elements via Get
	for i := 0; i < 100; i++ {
		if dll.Get(i) != i {
			t.Errorf("at index %d: expected %d, got %d", i, i, dll.Get(i))
		}
	}
}

// Bug check for InsertTail
func TestInsertTail_BugCheck_HeadNotSetOnFirstInsert(t *testing.T) {
	dll := NewDoublyLinkedList()
	dll.InsertTail(42)

	// Check if head is properly set on first insert
	if dll.head == nil {
		t.Error("BUG DETECTED: head should be set on first InsertTail")
		t.Log("Your InsertTail never sets head, only tail!")
	}

	// For single element, head and tail should be the same
	if dll.head != dll.tail {
		t.Error("head and tail should be the same node for single element")
	}
}

func TestRemoveHead_EmptyList(t *testing.T) {
	dll := NewDoublyLinkedList()

	// Should not panic on empty list
	dll.RemoveHead()

	if dll.head != nil {
		t.Error("head should still be nil after RemoveHead on empty list")
	}
	if dll.tail != nil {
		t.Error("tail should still be nil after RemoveHead on empty list")
	}
}

func TestRemoveHead_SingleElement(t *testing.T) {
	dll := NewDoublyLinkedList()
	dll.InsertTail(42)

	dll.RemoveHead()

	// Both head and tail should be nil after removing the only element
	if dll.head != nil {
		t.Error("head should be nil after removing single element")
	}
	if dll.tail != nil {
		t.Error("tail should be nil after removing single element")
	}

	// Forward and Backward should return empty slices
	if len(dll.Forward()) != 0 {
		t.Errorf("Forward() should return empty slice, got %v", dll.Forward())
	}
	if len(dll.Backward()) != 0 {
		t.Errorf("Backward() should return empty slice, got %v", dll.Backward())
	}
}

func TestRemoveHead_TwoElements(t *testing.T) {
	dll := NewDoublyLinkedList()
	dll.InsertTail(10)
	dll.InsertTail(20)

	dll.RemoveHead()

	// Head should now be 20
	if dll.head == nil {
		t.Fatal("head should not be nil")
	}
	if dll.head.val != 20 {
		t.Errorf("expected head value 20, got %d", dll.head.val)
	}

	// Head's prev should be nil
	if dll.head.prev != nil {
		t.Error("head.prev should be nil")
	}

	// Tail should also be 20 (same node as head)
	if dll.tail == nil {
		t.Fatal("tail should not be nil")
	}
	if dll.tail != dll.head {
		t.Error("tail should equal head when list has one element")
	}

	// Check traversal
	if !equalSlices(dll.Forward(), []int{20}) {
		t.Errorf("Forward() = %v, want [20]", dll.Forward())
	}
}

func TestRemoveHead_MultipleElements(t *testing.T) {
	dll := NewDoublyLinkedList()
	dll.InsertTail(1)
	dll.InsertTail(2)
	dll.InsertTail(3)
	dll.InsertTail(4)

	dll.RemoveHead() // Remove 1

	// Head should be 2
	if dll.head.val != 2 {
		t.Errorf("expected head value 2, got %d", dll.head.val)
	}

	// Head's prev should be nil
	if dll.head.prev != nil {
		t.Error("new head's prev should be nil")
	}

	// Tail should still be 4
	if dll.tail.val != 4 {
		t.Errorf("expected tail value 4, got %d", dll.tail.val)
	}

	// Check forward traversal
	expected := []int{2, 3, 4}
	if !equalSlices(dll.Forward(), expected) {
		t.Errorf("Forward() = %v, want %v", dll.Forward(), expected)
	}

	// Check backward traversal
	expectedBack := []int{4, 3, 2}
	if !equalSlices(dll.Backward(), expectedBack) {
		t.Errorf("Backward() = %v, want %v", dll.Backward(), expectedBack)
	}
}

func TestRemoveHead_Consecutive(t *testing.T) {
	dll := NewDoublyLinkedList()
	dll.InsertTail(10)
	dll.InsertTail(20)
	dll.InsertTail(30)

	dll.RemoveHead() // Remove 10
	dll.RemoveHead() // Remove 20

	// Should have only 30 left
	if dll.head.val != 30 {
		t.Errorf("expected head value 30, got %d", dll.head.val)
	}
	if dll.tail.val != 30 {
		t.Errorf("expected tail value 30, got %d", dll.tail.val)
	}
	if dll.head != dll.tail {
		t.Error("head and tail should be the same for single element")
	}

	dll.RemoveHead() // Remove 30

	// Should be empty
	if dll.head != nil || dll.tail != nil {
		t.Error("list should be empty after removing all elements")
	}
}

// ============================================================================
// RemoveTail Tests
// ============================================================================

func TestRemoveTail_EmptyList(t *testing.T) {
	dll := NewDoublyLinkedList()

	// Should not panic on empty list
	dll.RemoveTail()

	if dll.head != nil {
		t.Error("head should still be nil after RemoveTail on empty list")
	}
	if dll.tail != nil {
		t.Error("tail should still be nil after RemoveTail on empty list")
	}
}

func TestRemoveTail_SingleElement(t *testing.T) {
	dll := NewDoublyLinkedList()
	dll.InsertTail(42)

	dll.RemoveTail()

	// Both head and tail should be nil after removing the only element
	if dll.head != nil {
		t.Error("head should be nil after removing single element")
	}
	if dll.tail != nil {
		t.Error("tail should be nil after removing single element")
	}

	// Forward and Backward should return empty slices
	if len(dll.Forward()) != 0 {
		t.Errorf("Forward() should return empty slice, got %v", dll.Forward())
	}
	if len(dll.Backward()) != 0 {
		t.Errorf("Backward() should return empty slice, got %v", dll.Backward())
	}
}

func TestRemoveTail_TwoElements(t *testing.T) {
	dll := NewDoublyLinkedList()
	dll.InsertTail(10)
	dll.InsertTail(20)

	dll.RemoveTail()

	// Tail should now be 10
	if dll.tail == nil {
		t.Fatal("tail should not be nil")
	}
	if dll.tail.val != 10 {
		t.Errorf("expected tail value 10, got %d", dll.tail.val)
	}

	// Tail's next should be nil
	if dll.tail.next != nil {
		t.Error("tail.next should be nil")
	}

	// Head should also be 10 (same node as tail)
	if dll.head == nil {
		t.Fatal("head should not be nil")
	}
	if dll.head != dll.tail {
		t.Error("head should equal tail when list has one element")
	}

	// Check traversal
	if !equalSlices(dll.Forward(), []int{10}) {
		t.Errorf("Forward() = %v, want [10]", dll.Forward())
	}
}

func TestRemoveTail_MultipleElements(t *testing.T) {
	dll := NewDoublyLinkedList()
	dll.InsertTail(1)
	dll.InsertTail(2)
	dll.InsertTail(3)
	dll.InsertTail(4)

	dll.RemoveTail() // Remove 4

	// Tail should be 3
	if dll.tail.val != 3 {
		t.Errorf("expected tail value 3, got %d", dll.tail.val)
	}

	// Tail's next should be nil
	if dll.tail.next != nil {
		t.Error("new tail's next should be nil")
	}

	// Head should still be 1
	if dll.head.val != 1 {
		t.Errorf("expected head value 1, got %d", dll.head.val)
	}

	// Check forward traversal
	expected := []int{1, 2, 3}
	if !equalSlices(dll.Forward(), expected) {
		t.Errorf("Forward() = %v, want %v", dll.Forward(), expected)
	}

	// Check backward traversal
	expectedBack := []int{3, 2, 1}
	if !equalSlices(dll.Backward(), expectedBack) {
		t.Errorf("Backward() = %v, want %v", dll.Backward(), expectedBack)
	}
}

func TestRemoveTail_Consecutive(t *testing.T) {
	dll := NewDoublyLinkedList()
	dll.InsertTail(10)
	dll.InsertTail(20)
	dll.InsertTail(30)

	dll.RemoveTail() // Remove 30
	dll.RemoveTail() // Remove 20

	// Should have only 10 left
	if dll.head.val != 10 {
		t.Errorf("expected head value 10, got %d", dll.head.val)
	}
	if dll.tail.val != 10 {
		t.Errorf("expected tail value 10, got %d", dll.tail.val)
	}
	if dll.head != dll.tail {
		t.Error("head and tail should be the same for single element")
	}

	dll.RemoveTail() // Remove 10

	// Should be empty
	if dll.head != nil || dll.tail != nil {
		t.Error("list should be empty after removing all elements")
	}
}

func TestRemoveTail_BugCheck_PrevNodeNextPointer(t *testing.T) {
	dll := NewDoublyLinkedList()
	dll.InsertTail(1)
	dll.InsertTail(2)
	dll.InsertTail(3)

	dll.RemoveTail() // Remove 3

	// BUG: Check if the implementation sets the new tail's next to nil
	if dll.tail.next != nil {
		t.Error("BUG DETECTED: tail.next should be set to nil after RemoveTail")
		t.Log("The current implementation only sets tail = tail.prev")
		t.Log("It should also set tail.next = nil")
	}
}

// ============================================================================
// RemoveByRef Tests
// ============================================================================

func TestRemoveByRef_RemoveHead(t *testing.T) {
	dll := NewDoublyLinkedList()
	dll.InsertTail(10)
	dll.InsertTail(20)
	dll.InsertTail(30)

	oldHead := dll.head
	dll.RemoveByRef(oldHead)

	// Head should now be 20
	if dll.head.val != 20 {
		t.Errorf("expected head value 20, got %d", dll.head.val)
	}

	// Head's prev should be nil
	if dll.head.prev != nil {
		t.Error("new head's prev should be nil")
	}

	expected := []int{20, 30}
	if !equalSlices(dll.Forward(), expected) {
		t.Errorf("Forward() = %v, want %v", dll.Forward(), expected)
	}
}

func TestRemoveByRef_RemoveTail(t *testing.T) {
	dll := NewDoublyLinkedList()
	dll.InsertTail(10)
	dll.InsertTail(20)
	dll.InsertTail(30)

	oldTail := dll.tail
	dll.RemoveByRef(oldTail)

	// Tail should now be 20
	if dll.tail.val != 20 {
		t.Errorf("expected tail value 20, got %d", dll.tail.val)
	}

	// Tail's next should be nil
	if dll.tail.next != nil {
		t.Error("new tail's next should be nil")
	}

	expected := []int{10, 20}
	if !equalSlices(dll.Forward(), expected) {
		t.Errorf("Forward() = %v, want %v", dll.Forward(), expected)
	}
}

func TestRemoveByRef_RemoveMiddle(t *testing.T) {
	dll := NewDoublyLinkedList()
	dll.InsertTail(10)
	dll.InsertTail(20)
	dll.InsertTail(30)
	dll.InsertTail(40)

	// Get reference to middle node (20)
	middle := dll.head.next
	dll.RemoveByRef(middle)

	// Should have 10, 30, 40
	expected := []int{10, 30, 40}
	if !equalSlices(dll.Forward(), expected) {
		t.Errorf("Forward() = %v, want %v", dll.Forward(), expected)
	}

	// Check backward traversal
	expectedBack := []int{40, 30, 10}
	if !equalSlices(dll.Backward(), expectedBack) {
		t.Errorf("Backward() = %v, want %v", dll.Backward(), expectedBack)
	}

	// Verify pointers are correctly linked
	// 10.next should be 30
	if dll.head.next.val != 30 {
		t.Errorf("head.next should be 30, got %d", dll.head.next.val)
	}

	// 30.prev should be 10
	if dll.head.next.prev.val != 10 {
		t.Errorf("second node's prev should be 10, got %d", dll.head.next.prev.val)
	}
}

func TestRemoveByRef_SingleElement(t *testing.T) {
	dll := NewDoublyLinkedList()
	dll.InsertTail(42)

	node := dll.head
	dll.RemoveByRef(node)

	// List should be empty
	if dll.head != nil {
		t.Error("head should be nil after removing single element")
	}
	if dll.tail != nil {
		t.Error("tail should be nil after removing single element")
	}
}

func TestRemoveByRef_RemoveSecondToLast(t *testing.T) {
	dll := NewDoublyLinkedList()
	dll.InsertTail(10)
	dll.InsertTail(20)
	dll.InsertTail(30)

	// Get reference to second node (20)
	secondNode := dll.head.next
	dll.RemoveByRef(secondNode)

	// Should have 10, 30
	expected := []int{10, 30}
	if !equalSlices(dll.Forward(), expected) {
		t.Errorf("Forward() = %v, want %v", dll.Forward(), expected)
	}

	// 10.next should be 30
	if dll.head.next.val != 30 {
		t.Errorf("head.next should be 30, got %d", dll.head.next.val)
	}

	// 30.prev should be 10
	if dll.tail.prev.val != 10 {
		t.Errorf("tail.prev should be 10, got %d", dll.tail.prev.val)
	}
}

func TestRemoveByRef_BugCheck_MiddleNodeNextPointer(t *testing.T) {
	dll := NewDoublyLinkedList()
	dll.InsertTail(10)
	dll.InsertTail(20)
	dll.InsertTail(30)

	// Get reference to middle node (20)
	middle := dll.head.next
	dll.RemoveByRef(middle)

	// BUG: The current implementation doesn't update the next pointer
	// when removing a middle node
	// 10.next should point to 30, not to the removed node
	if dll.head.next == middle {
		t.Error("BUG DETECTED: head.next still points to removed node")
		t.Log("RemoveByRef for middle nodes only updates prev.next")
		t.Log("It should also update next.prev")
	}

	// Also check if 30.prev points to 10
	thirdNode := dll.head.next
	if thirdNode.prev != dll.head {
		t.Error("BUG DETECTED: third node's prev doesn't point to head")
		t.Log("RemoveByRef doesn't update the next node's prev pointer")
	}
}

// ============================================================================
// Mixed Operations Tests
// ============================================================================

func TestMixedRemoveOperations(t *testing.T) {
	dll := NewDoublyLinkedList()

	// Build list: 1, 2, 3, 4, 5
	for i := 1; i <= 5; i++ {
		dll.InsertTail(i)
	}

	dll.RemoveHead()               // Remove 1 -> [2,3,4,5]
	dll.RemoveTail()               // Remove 5 -> [2,3,4]
	dll.RemoveByRef(dll.head.next) // Remove 3 -> [2,4]

	expected := []int{2, 4}
	if !equalSlices(dll.Forward(), expected) {
		t.Errorf("Forward() = %v, want %v", dll.Forward(), expected)
	}

	expectedBack := []int{4, 2}
	if !equalSlices(dll.Backward(), expectedBack) {
		t.Errorf("Backward() = %v, want %v", dll.Backward(), expectedBack)
	}
}

func TestRemoveAll_UsingRemoveHead(t *testing.T) {
	dll := NewDoublyLinkedList()
	dll.InsertTail(1)
	dll.InsertTail(2)
	dll.InsertTail(3)

	dll.RemoveHead()
	dll.RemoveHead()
	dll.RemoveHead()

	// List should be empty
	if dll.head != nil || dll.tail != nil {
		t.Error("list should be empty")
	}
	if len(dll.Forward()) != 0 {
		t.Error("Forward() should return empty slice")
	}
}

func TestRemoveAll_UsingRemoveTail(t *testing.T) {
	dll := NewDoublyLinkedList()
	dll.InsertTail(1)
	dll.InsertTail(2)
	dll.InsertTail(3)

	dll.RemoveTail()
	dll.RemoveTail()
	dll.RemoveTail()

	// List should be empty
	if dll.head != nil || dll.tail != nil {
		t.Error("list should be empty")
	}
	if len(dll.Forward()) != 0 {
		t.Error("Forward() should return empty slice")
	}
}

func TestRemoveByRef_InterleavedWithInserts(t *testing.T) {
	dll := NewDoublyLinkedList()

	dll.InsertTail(10)
	dll.InsertTail(20)

	middle := dll.head.next
	dll.InsertTail(30)

	dll.RemoveByRef(middle) // Remove 20

	expected := []int{10, 30}
	if !equalSlices(dll.Forward(), expected) {
		t.Errorf("Forward() = %v, want %v", dll.Forward(), expected)
	}

	dll.InsertTail(40)
	dll.InsertHead(5)

	expected = []int{5, 10, 30, 40}
	if !equalSlices(dll.Forward(), expected) {
		t.Errorf("Forward() = %v, want %v", dll.Forward(), expected)
	}
}
