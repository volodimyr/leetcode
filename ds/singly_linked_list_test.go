package ds

import "testing"

func TestLinkedList_Get(t *testing.T) {
	tests := []struct {
		name     string
		setup    func() *LinkedList
		index    int
		expected int
	}{
		{
			name: "empty list always returns -1",
			setup: func() *LinkedList {
				return NewLinkedList()
			},
			index:    0,
			expected: -1,
		},
		{
			name: "get head element",
			setup: func() *LinkedList {
				ll := NewLinkedList()
				ll.InsertHead(10)
				return ll
			},
			index:    0,
			expected: 10,
		},
		{
			name: "get second element",
			setup: func() *LinkedList {
				ll := NewLinkedList()
				ll.InsertHead(10)
				ll.InsertTail(20)
				return ll
			},
			index:    1,
			expected: 20,
		},
		{
			name: "index out of bounds > length",
			setup: func() *LinkedList {
				ll := NewLinkedList()
				ll.InsertHead(10)
				ll.InsertTail(20)
				return ll
			},
			index:    5,
			expected: -1,
		},
		{
			name: "get from single-element list index 1 (invalid)",
			setup: func() *LinkedList {
				ll := NewLinkedList()
				ll.InsertHead(42)
				return ll
			},
			index:    1,
			expected: -1,
		},
		{
			name: "get middle element in 3-node list",
			setup: func() *LinkedList {
				ll := NewLinkedList()
				ll.InsertTail(1)
				ll.InsertTail(2)
				ll.InsertTail(3)
				return ll
			},
			index:    1,
			expected: 2,
		},
		{
			name: "get last element in 3-node list",
			setup: func() *LinkedList {
				ll := NewLinkedList()
				ll.InsertTail(1)
				ll.InsertTail(2)
				ll.InsertTail(3)
				return ll
			},
			index:    2,
			expected: 3,
		},
		{
			name: "negative index not allowed (should return -1 by default behavior)",
			setup: func() *LinkedList {
				ll := NewLinkedList()
				ll.InsertTail(100)
				return ll
			},
			index:    -1,
			expected: -1,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			ll := tt.setup()
			got := ll.Get(tt.index)
			if got != tt.expected {
				t.Errorf("Get(%d) = %d; want %d", tt.index, got, tt.expected)
			}
		})
	}
}

func TestLinkedList(t *testing.T) {
	t.Run("Get from empty list", func(t *testing.T) {
		ll := NewLinkedList()
		if got := ll.Get(0); got != -1 {
			t.Errorf("expected -1, got %d", got)
		}
	})

	t.Run("InsertHead single element", func(t *testing.T) {
		ll := NewLinkedList()
		ll.InsertHead(10)
		if vals := ll.GetValues(); len(vals) != 1 || vals[0] != 10 {
			t.Errorf("expected [10], got %v", vals)
		}
	})

	t.Run("InsertTail appends element", func(t *testing.T) {
		ll := NewLinkedList()
		ll.InsertHead(1)
		ll.InsertTail(2)
		ll.InsertTail(3)
		expected := []int{1, 2, 3}
		if vals := ll.GetValues(); !equal(vals, expected) {
			t.Errorf("expected %v, got %v", expected, vals)
		}
	})

	t.Run("Insert at index", func(t *testing.T) {
		ll := NewLinkedList()
		ll.InsertTail(1)
		ll.InsertTail(3)
		ll.Insert(1, 2) // insert in middle
		expected := []int{1, 2, 3}
		if vals := ll.GetValues(); !equal(vals, expected) {
			t.Errorf("expected %v, got %v", expected, vals)
		}
	})

	t.Run("Insert at head using Insert(index=0)", func(t *testing.T) {
		ll := NewLinkedList()
		ll.InsertTail(2)
		ll.Insert(0, 1)
		expected := []int{1, 2}
		if vals := ll.GetValues(); !equal(vals, expected) {
			t.Errorf("expected %v, got %v", expected, vals)
		}
	})

	t.Run("Insert at out-of-range index does nothing", func(t *testing.T) {
		ll := NewLinkedList()
		ll.InsertTail(1)
		ll.Insert(5, 99) // should do nothing
		expected := []int{1}
		if vals := ll.GetValues(); !equal(vals, expected) {
			t.Errorf("expected %v, got %v", expected, vals)
		}
	})

	t.Run("Remove head element", func(t *testing.T) {
		ll := NewLinkedList()
		ll.InsertTail(1)
		ll.InsertTail(2)
		ok := ll.Remove(0)
		if !ok {
			t.Errorf("expected true, got false")
		}
		expected := []int{2}
		if vals := ll.GetValues(); !equal(vals, expected) {
			t.Errorf("expected %v, got %v", expected, vals)
		}
	})

	t.Run("Remove middle element", func(t *testing.T) {
		ll := NewLinkedList()
		ll.InsertTail(1)
		ll.InsertTail(2)
		ll.InsertTail(3)
		ok := ll.Remove(1) // remove 2
		if !ok {
			t.Errorf("expected true, got false")
		}
		expected := []int{1, 3}
		if vals := ll.GetValues(); !equal(vals, expected) {
			t.Errorf("expected %v, got %v", expected, vals)
		}
	})

	t.Run("Remove tail element", func(t *testing.T) {
		ll := NewLinkedList()
		ll.InsertTail(1)
		ll.InsertTail(2)
		ok := ll.Remove(1)
		if !ok {
			t.Errorf("expected true, got false")
		}
		expected := []int{1}
		if vals := ll.GetValues(); !equal(vals, expected) {
			t.Errorf("expected %v, got %v", expected, vals)
		}
	})

	t.Run("Remove out-of-range index returns false", func(t *testing.T) {
		ll := NewLinkedList()
		ll.InsertTail(1)
		if ok := ll.Remove(5); ok {
			t.Errorf("expected false, got true")
		}
	})
}

// helper for slices equality
func equal(a, b []int) bool {
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
