package implementqueueusingstacks

import "testing"

func TestMyQueue_BasicOperations(t *testing.T) {
	myQueue := Constructor()

	myQueue.Push(1)
	myQueue.Push(2)

	if got := myQueue.Peek(); got != 1 {
		t.Errorf("Peek() = %v, want %v", got, 1)
	}

	if got := myQueue.Pop(); got != 1 {
		t.Errorf("Pop() = %v, want %v", got, 1)
	}

	if got := myQueue.Empty(); got != false {
		t.Errorf("Empty() = %v, want %v", got, false)
	}
}

func TestMyQueue_Empty(t *testing.T) {
	myQueue := Constructor()

	if got := myQueue.Empty(); got != true {
		t.Errorf("Empty() = %v, want %v", got, true)
	}

	myQueue.Push(1)

	if got := myQueue.Empty(); got != false {
		t.Errorf("Empty() = %v, want %v", got, false)
	}

	myQueue.Pop()

	if got := myQueue.Empty(); got != true {
		t.Errorf("Empty() = %v, want %v", got, true)
	}
}

func TestMyQueue_SingleElement(t *testing.T) {
	myQueue := Constructor()

	myQueue.Push(5)

	if got := myQueue.Peek(); got != 5 {
		t.Errorf("Peek() = %v, want %v", got, 5)
	}

	if got := myQueue.Pop(); got != 5 {
		t.Errorf("Pop() = %v, want %v", got, 5)
	}

	if got := myQueue.Empty(); got != true {
		t.Errorf("Empty() = %v, want %v", got, true)
	}
}

func TestMyQueue_MultipleElements(t *testing.T) {
	myQueue := Constructor()

	for i := 1; i <= 5; i++ {
		myQueue.Push(i)
	}

	for i := 1; i <= 5; i++ {
		if got := myQueue.Peek(); got != i {
			t.Errorf("Peek() = %v, want %v", got, i)
		}
		if got := myQueue.Pop(); got != i {
			t.Errorf("Pop() = %v, want %v", got, i)
		}
	}

	if got := myQueue.Empty(); got != true {
		t.Errorf("Empty() = %v, want %v", got, true)
	}
}

func TestMyQueue_PushPopInterleaved(t *testing.T) {
	myQueue := Constructor()

	myQueue.Push(1)
	myQueue.Push(2)

	if got := myQueue.Pop(); got != 1 {
		t.Errorf("Pop() = %v, want %v", got, 1)
	}

	myQueue.Push(3)

	if got := myQueue.Pop(); got != 2 {
		t.Errorf("Pop() = %v, want %v", got, 2)
	}

	if got := myQueue.Pop(); got != 3 {
		t.Errorf("Pop() = %v, want %v", got, 3)
	}

	if got := myQueue.Empty(); got != true {
		t.Errorf("Empty() = %v, want %v", got, true)
	}
}

func TestMyQueue_PeekDoesNotRemove(t *testing.T) {
	myQueue := Constructor()

	myQueue.Push(1)
	myQueue.Push(2)

	if got := myQueue.Peek(); got != 1 {
		t.Errorf("Peek() = %v, want %v", got, 1)
	}

	if got := myQueue.Peek(); got != 1 {
		t.Errorf("Peek() = %v, want %v", got, 1)
	}

	if got := myQueue.Pop(); got != 1 {
		t.Errorf("Pop() = %v, want %v", got, 1)
	}
}

func TestMyQueue_BoundaryValues(t *testing.T) {
	myQueue := Constructor()

	myQueue.Push(1)
	myQueue.Push(9)

	if got := myQueue.Pop(); got != 1 {
		t.Errorf("Pop() = %v, want %v", got, 1)
	}

	if got := myQueue.Pop(); got != 9 {
		t.Errorf("Pop() = %v, want %v", got, 9)
	}
}

func TestMyQueue_LargeSequence(t *testing.T) {
	myQueue := Constructor()

	for i := 1; i <= 50; i++ {
		myQueue.Push(i)
	}

	for i := 1; i <= 50; i++ {
		if got := myQueue.Pop(); got != i {
			t.Errorf("Pop() = %v, want %v", got, i)
		}
	}

	if got := myQueue.Empty(); got != true {
		t.Errorf("Empty() = %v, want %v", got, true)
	}
}

func TestMyQueue_AlternatingPushPop(t *testing.T) {
	myQueue := Constructor()

	myQueue.Push(1)
	if got := myQueue.Pop(); got != 1 {
		t.Errorf("Pop() = %v, want %v", got, 1)
	}

	myQueue.Push(2)
	if got := myQueue.Pop(); got != 2 {
		t.Errorf("Pop() = %v, want %v", got, 2)
	}

	myQueue.Push(3)
	myQueue.Push(4)
	if got := myQueue.Pop(); got != 3 {
		t.Errorf("Pop() = %v, want %v", got, 3)
	}
	if got := myQueue.Pop(); got != 4 {
		t.Errorf("Pop() = %v, want %v", got, 4)
	}
}

func TestStack_Operations(t *testing.T) {
	s := &Stack[int]{}

	if got := s.Empty(); got != true {
		t.Errorf("Empty() = %v, want %v", got, true)
	}

	s.Push(10)
	s.Push(20)
	s.Push(30)

	if got := s.Peek(); got != 30 {
		t.Errorf("Peek() = %v, want %v", got, 30)
	}

	if got := s.Pop(); got != 30 {
		t.Errorf("Pop() = %v, want %v", got, 30)
	}

	if got := s.Pop(); got != 20 {
		t.Errorf("Pop() = %v, want %v", got, 20)
	}

	if got := s.Empty(); got != false {
		t.Errorf("Empty() = %v, want %v", got, false)
	}

	if got := s.Pop(); got != 10 {
		t.Errorf("Pop() = %v, want %v", got, 10)
	}

	if got := s.Empty(); got != true {
		t.Errorf("Empty() = %v, want %v", got, true)
	}
}
