package implementstackusingqueues

import "testing"

// Test Constructor
func TestConstructor(t *testing.T) {
	s := Constructor()
	if s.q == nil {
		t.Error("Constructor should initialize queue")
	}
	if s.size != 0 {
		t.Errorf("Expected size 0, got %d", s.size)
	}
	if !s.Empty() {
		t.Error("New stack should be empty")
	}
}

// Test Push single element
func TestPushSingleElement(t *testing.T) {
	s := Constructor()
	s.Push(1)

	if s.Empty() {
		t.Error("Stack should not be empty after push")
	}
	if s.size != 1 {
		t.Errorf("Expected size 1, got %d", s.size)
	}
	if s.Top() != 1 {
		t.Errorf("Expected top to be 1, got %d", s.Top())
	}
}

// Test Push multiple elements
func TestPushMultipleElements(t *testing.T) {
	s := Constructor()
	s.Push(1)
	s.Push(2)
	s.Push(3)

	if s.size != 3 {
		t.Errorf("Expected size 3, got %d", s.size)
	}
	if s.Top() != 3 {
		t.Errorf("Expected top to be 3, got %d", s.Top())
	}
}

// Test Pop single element
func TestPopSingleElement(t *testing.T) {
	s := Constructor()
	s.Push(1)

	val := s.Pop()
	if val != 1 {
		t.Errorf("Expected pop to return 1, got %d", val)
	}
	if !s.Empty() {
		t.Error("Stack should be empty after popping last element")
	}
	if s.size != 0 {
		t.Errorf("Expected size 0, got %d", s.size)
	}
}

// Test Pop multiple elements (LIFO order)
func TestPopLIFOOrder(t *testing.T) {
	s := Constructor()
	s.Push(1)
	s.Push(2)
	s.Push(3)

	if val := s.Pop(); val != 3 {
		t.Errorf("Expected first pop to return 3, got %d", val)
	}
	if val := s.Pop(); val != 2 {
		t.Errorf("Expected second pop to return 2, got %d", val)
	}
	if val := s.Pop(); val != 1 {
		t.Errorf("Expected third pop to return 1, got %d", val)
	}
	if !s.Empty() {
		t.Error("Stack should be empty after all pops")
	}
}

// Test Top doesn't remove element
func TestTopDoesNotRemove(t *testing.T) {
	s := Constructor()
	s.Push(1)
	s.Push(2)

	top1 := s.Top()
	top2 := s.Top()

	if top1 != 2 || top2 != 2 {
		t.Errorf("Expected both tops to be 2, got %d and %d", top1, top2)
	}
	if s.size != 2 {
		t.Errorf("Size should still be 2, got %d", s.size)
	}
}

// Test Empty on new stack
func TestEmptyOnNewStack(t *testing.T) {
	s := Constructor()
	if !s.Empty() {
		t.Error("New stack should be empty")
	}
}

// Test Empty after push
func TestEmptyAfterPush(t *testing.T) {
	s := Constructor()
	s.Push(1)
	if s.Empty() {
		t.Error("Stack should not be empty after push")
	}
}

// Test Empty after push and pop
func TestEmptyAfterPushAndPop(t *testing.T) {
	s := Constructor()
	s.Push(1)
	s.Pop()
	if !s.Empty() {
		t.Error("Stack should be empty after pushing and popping same element")
	}
}

// Test example from problem
func TestProblemExample(t *testing.T) {
	s := Constructor()
	s.Push(1)
	s.Push(2)

	if top := s.Top(); top != 2 {
		t.Errorf("Expected top to be 2, got %d", top)
	}
	if pop := s.Pop(); pop != 2 {
		t.Errorf("Expected pop to be 2, got %d", pop)
	}
	if empty := s.Empty(); empty {
		t.Error("Expected empty to be false")
	}
}

// Test alternating push and pop
func TestAlternatingPushPop(t *testing.T) {
	s := Constructor()
	s.Push(1)
	if val := s.Pop(); val != 1 {
		t.Errorf("Expected 1, got %d", val)
	}

	s.Push(2)
	s.Push(3)
	if val := s.Pop(); val != 3 {
		t.Errorf("Expected 3, got %d", val)
	}
	if val := s.Pop(); val != 2 {
		t.Errorf("Expected 2, got %d", val)
	}

	if !s.Empty() {
		t.Error("Stack should be empty")
	}
}

// Test with constraint boundaries (1 <= x <= 9)
func TestConstraintBoundaries(t *testing.T) {
	s := Constructor()
	s.Push(1) // minimum
	s.Push(9) // maximum

	if val := s.Pop(); val != 9 {
		t.Errorf("Expected 9, got %d", val)
	}
	if val := s.Pop(); val != 1 {
		t.Errorf("Expected 1, got %d", val)
	}
}

// Test many operations (up to 100 calls)
func TestManyOperations(t *testing.T) {
	s := Constructor()

	// Push 50 elements
	for i := 1; i <= 50; i++ {
		s.Push(i % 10) // values between 0-9
	}

	if s.size != 50 {
		t.Errorf("Expected size 50, got %d", s.size)
	}

	// Pop all elements
	for i := 0; i < 50; i++ {
		s.Pop()
	}

	if !s.Empty() {
		t.Error("Stack should be empty after all pops")
	}
}

// Test queue operations work correctly
func TestQueueInternals(t *testing.T) {
	q := &queue{}

	if !q.empty() {
		t.Error("New queue should be empty")
	}

	q.enqueue(1)
	if q.empty() {
		t.Error("Queue should not be empty")
	}

	if val := q.peek(); val != 1 {
		t.Errorf("Expected peek 1, got %d", val)
	}

	if val := q.dequeue(); val != 1 {
		t.Errorf("Expected dequeue 1, got %d", val)
	}

	if !q.empty() {
		t.Error("Queue should be empty after dequeue")
	}
}

// Test queue maintains FIFO order
func TestQueueFIFO(t *testing.T) {
	q := &queue{}
	q.enqueue(1)
	q.enqueue(2)
	q.enqueue(3)

	if val := q.dequeue(); val != 1 {
		t.Errorf("Expected 1, got %d", val)
	}
	if val := q.dequeue(); val != 2 {
		t.Errorf("Expected 2, got %d", val)
	}
	if val := q.dequeue(); val != 3 {
		t.Errorf("Expected 3, got %d", val)
	}
}

// Test size tracking
func TestSizeTracking(t *testing.T) {
	s := Constructor()

	sizes := []int{0, 1, 2, 3, 2, 1, 0}
	operations := []func(){
		func() {}, // initial
		func() { s.Push(1) },
		func() { s.Push(2) },
		func() { s.Push(3) },
		func() { s.Pop() },
		func() { s.Pop() },
		func() { s.Pop() },
	}

	for i, op := range operations {
		op()
		if s.size != sizes[i] {
			t.Errorf("After operation %d, expected size %d, got %d", i, sizes[i], s.size)
		}
	}
}
