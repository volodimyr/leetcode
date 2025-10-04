package ds

import "testing"

func TestDeque_IsEmpty(t *testing.T) {
	d := NewDeque()
	if !d.IsEmpty() {
		t.Error("New deque should be empty")
	}
}

func TestDeque_IsEmptyAfterAppend(t *testing.T) {
	d := NewDeque()
	d.Append(10)
	if d.IsEmpty() {
		t.Error("Deque should not be empty after append")
	}
}

func TestDeque_AppendAndPop(t *testing.T) {
	d := NewDeque()
	d.Append(10)
	val := d.Pop()
	if val != 10 {
		t.Errorf("Expected 10, got %d", val)
	}
}

func TestDeque_AppendLeftAndPopLeft(t *testing.T) {
	d := NewDeque()
	d.AppendLeft(20)
	val := d.PopLeft()
	if val != 20 {
		t.Errorf("Expected 20, got %d", val)
	}
}

func TestDeque_PopEmptyReturnsNegativeOne(t *testing.T) {
	d := NewDeque()
	val := d.Pop()
	if val != -1 {
		t.Errorf("Expected -1, got %d", val)
	}
}

func TestDeque_PopLeftEmptyReturnsNegativeOne(t *testing.T) {
	d := NewDeque()
	val := d.PopLeft()
	if val != -1 {
		t.Errorf("Expected -1, got %d", val)
	}
}

func TestDeque_IsEmptyAfterPopAll(t *testing.T) {
	d := NewDeque()
	d.Append(10)
	d.Pop()
	if !d.IsEmpty() {
		t.Error("Deque should be empty after popping all elements")
	}
}

func TestDeque_ExampleSequence(t *testing.T) {
	d := NewDeque()

	if !d.IsEmpty() {
		t.Error("Expected isEmpty to return true")
	}

	d.Append(10)

	if d.IsEmpty() {
		t.Error("Expected isEmpty to return false")
	}

	d.AppendLeft(20)

	val := d.PopLeft()
	if val != 20 {
		t.Errorf("Expected 20, got %d", val)
	}

	val = d.Pop()
	if val != 10 {
		t.Errorf("Expected 10, got %d", val)
	}

	val = d.Pop()
	if val != -1 {
		t.Errorf("Expected -1, got %d", val)
	}

	d.Append(30)

	val = d.Pop()
	if val != 30 {
		t.Errorf("Expected 30, got %d", val)
	}

	if !d.IsEmpty() {
		t.Error("Expected isEmpty to return true")
	}
}

func TestDeque_MultipleAppends(t *testing.T) {
	d := NewDeque()
	d.Append(1)
	d.Append(2)
	d.Append(3)

	if d.Pop() != 3 {
		t.Error("Expected 3")
	}
	if d.Pop() != 2 {
		t.Error("Expected 2")
	}
	if d.Pop() != 1 {
		t.Error("Expected 1")
	}
}

func TestDeque_MultipleAppendLefts(t *testing.T) {
	d := NewDeque()
	d.AppendLeft(1)
	d.AppendLeft(2)
	d.AppendLeft(3)

	if d.PopLeft() != 3 {
		t.Error("Expected 3")
	}
	if d.PopLeft() != 2 {
		t.Error("Expected 2")
	}
	if d.PopLeft() != 1 {
		t.Error("Expected 1")
	}
}

func TestDeque_MixedOperations(t *testing.T) {
	d := NewDeque()
	d.Append(1)
	d.AppendLeft(2)
	d.Append(3)
	d.AppendLeft(4)

	// Expected order: 4, 2, 1, 3
	if d.PopLeft() != 4 {
		t.Error("Expected 4")
	}
	if d.Pop() != 3 {
		t.Error("Expected 3")
	}
	if d.PopLeft() != 2 {
		t.Error("Expected 2")
	}
	if d.Pop() != 1 {
		t.Error("Expected 1")
	}
}

func TestDeque_AlternatingAppendPop(t *testing.T) {
	d := NewDeque()
	d.Append(1)
	if d.Pop() != 1 {
		t.Error("Expected 1")
	}
	d.Append(2)
	if d.Pop() != 2 {
		t.Error("Expected 2")
	}
	if !d.IsEmpty() {
		t.Error("Expected deque to be empty")
	}
}

func TestDeque_SingleElementPopLeft(t *testing.T) {
	d := NewDeque()
	d.Append(42)
	val := d.PopLeft()
	if val != 42 {
		t.Errorf("Expected 42, got %d", val)
	}
	if !d.IsEmpty() {
		t.Error("Expected deque to be empty")
	}
}

func TestDeque_SingleElementPop(t *testing.T) {
	d := NewDeque()
	d.AppendLeft(42)
	val := d.Pop()
	if val != 42 {
		t.Errorf("Expected 42, got %d", val)
	}
	if !d.IsEmpty() {
		t.Error("Expected deque to be empty")
	}
}

func TestDeque_AppendPopLeftOrder(t *testing.T) {
	d := NewDeque()
	d.Append(1)
	d.Append(2)
	d.Append(3)

	if d.PopLeft() != 1 {
		t.Error("Expected 1")
	}
	if d.PopLeft() != 2 {
		t.Error("Expected 2")
	}
	if d.PopLeft() != 3 {
		t.Error("Expected 3")
	}
}

func TestDeque_AppendLeftPopOrder(t *testing.T) {
	d := NewDeque()
	d.AppendLeft(1)
	d.AppendLeft(2)
	d.AppendLeft(3)

	if d.Pop() != 1 {
		t.Error("Expected 1")
	}
	if d.Pop() != 2 {
		t.Error("Expected 2")
	}
	if d.Pop() != 3 {
		t.Error("Expected 3")
	}
}
