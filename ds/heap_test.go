package ds

import (
	"testing"
)

func TestMinHeap_TopEmpty(t *testing.T) {
	mh := NewMinHeap()
	if got := mh.Top(); got != -1 {
		t.Errorf("Top() on empty heap = %d, want -1", got)
	}
}

func TestMinHeap_PopEmpty(t *testing.T) {
	mh := NewMinHeap()
	if got := mh.Pop(); got != -1 {
		t.Errorf("Pop() on empty heap = %d, want -1", got)
	}
}

func TestMinHeap_PushSingleElement(t *testing.T) {
	mh := NewMinHeap()
	mh.Push(5)
	if got := mh.Top(); got != 5 {
		t.Errorf("Top() = %d, want 5", got)
	}
}

func TestMinHeap_PushMultipleElements(t *testing.T) {
	mh := NewMinHeap()
	mh.Push(5)
	mh.Push(3)
	mh.Push(7)
	mh.Push(1)

	if got := mh.Top(); got != 1 {
		t.Errorf("Top() = %d, want 1", got)
	}
}

func TestMinHeap_PopSingleElement(t *testing.T) {
	mh := NewMinHeap()
	mh.Push(5)

	if got := mh.Pop(); got != 5 {
		t.Errorf("Pop() = %d, want 5", got)
	}

	if got := mh.Top(); got != -1 {
		t.Errorf("Top() after pop = %d, want -1", got)
	}
}

func TestMinHeap_PopMultipleElements(t *testing.T) {
	mh := NewMinHeap()
	values := []int{5, 3, 7, 1, 9, 2}
	for _, v := range values {
		mh.Push(v)
	}

	expected := []int{1, 2, 3, 5, 7, 9}
	for i, want := range expected {
		if got := mh.Pop(); got != want {
			t.Errorf("Pop() iteration %d = %d, want %d", i, got, want)
		}
	}

	if got := mh.Pop(); got != -1 {
		t.Errorf("Pop() on empty heap = %d, want -1", got)
	}
}

func TestMinHeap_PushPopInterleaved(t *testing.T) {
	mh := NewMinHeap()

	mh.Push(5)
	mh.Push(3)

	if got := mh.Pop(); got != 3 {
		t.Errorf("Pop() = %d, want 3", got)
	}

	mh.Push(1)
	mh.Push(7)

	if got := mh.Pop(); got != 1 {
		t.Errorf("Pop() = %d, want 1", got)
	}

	if got := mh.Pop(); got != 5 {
		t.Errorf("Pop() = %d, want 5", got)
	}

	if got := mh.Pop(); got != 7 {
		t.Errorf("Pop() = %d, want 7", got)
	}
}

func TestMinHeap_DuplicateValues(t *testing.T) {
	mh := NewMinHeap()
	mh.Push(5)
	mh.Push(5)
	mh.Push(3)
	mh.Push(3)
	mh.Push(3)

	expected := []int{3, 3, 3, 5, 5}
	for i, want := range expected {
		if got := mh.Pop(); got != want {
			t.Errorf("Pop() iteration %d = %d, want %d", i, got, want)
		}
	}
}

func TestMinHeap_LargeSequence(t *testing.T) {
	mh := NewMinHeap()

	// Push 100 elements in reverse order
	for i := 100; i > 0; i-- {
		mh.Push(i)
	}

	// Verify they come out in sorted order
	for i := 1; i <= 100; i++ {
		if got := mh.Pop(); got != i {
			t.Errorf("Pop() = %d, want %d", got, i)
			break
		}
	}
}

func TestMinHeap_AlternatingValues(t *testing.T) {
	mh := NewMinHeap()
	mh.Push(10)
	mh.Push(1)
	mh.Push(9)
	mh.Push(2)
	mh.Push(8)
	mh.Push(3)

	expected := []int{1, 2, 3, 8, 9, 10}
	for i, want := range expected {
		if got := mh.Pop(); got != want {
			t.Errorf("Pop() iteration %d = %d, want %d", i, got, want)
		}
	}
}

func TestMinHeap_EmptyHeap(t *testing.T) {
	mh := NewMinHeap()

	if got := mh.Top(); got != -1 {
		t.Errorf("Top() on empty heap = %v, want -1", got)
	}

	if got := mh.Pop(); got != -1 {
		t.Errorf("Pop() on empty heap = %v, want -1", got)
	}
}

func TestMinHeap_SingleElement(t *testing.T) {
	mh := NewMinHeap()
	mh.Push(5)

	if got := mh.Top(); got != 5 {
		t.Errorf("Top() = %v, want 5", got)
	}

	if got := mh.Pop(); got != 5 {
		t.Errorf("Pop() = %v, want 5", got)
	}

	if got := mh.Top(); got != -1 {
		t.Errorf("Top() after Pop() = %v, want -1", got)
	}
}

func TestMinHeap_MultipleElements(t *testing.T) {
	mh := NewMinHeap()
	mh.Push(3)
	mh.Push(1)
	mh.Push(4)
	mh.Push(2)

	if got := mh.Top(); got != 1 {
		t.Errorf("Top() = %v, want 1", got)
	}

	expected := []int{1, 2, 3, 4}
	for i, want := range expected {
		if got := mh.Pop(); got != want {
			t.Errorf("Pop() call %d = %v, want %v", i+1, got, want)
		}
	}

	if got := mh.Pop(); got != -1 {
		t.Errorf("Pop() on empty heap = %v, want -1", got)
	}
}

func TestMinHeap_DuplicateElements(t *testing.T) {
	mh := NewMinHeap()
	mh.Push(5)
	mh.Push(3)
	mh.Push(5)
	mh.Push(3)
	mh.Push(1)

	expected := []int{1, 3, 3, 5, 5}
	for i, want := range expected {
		if got := mh.Pop(); got != want {
			t.Errorf("Pop() call %d = %v, want %v", i+1, got, want)
		}
	}
}

func TestMinHeap_NegativeNumbers(t *testing.T) {
	mh := NewMinHeap()
	mh.Push(-5)
	mh.Push(10)
	mh.Push(-3)
	mh.Push(0)
	mh.Push(-10)

	expected := []int{-10, -5, -3, 0, 10}
	for i, want := range expected {
		if got := mh.Pop(); got != want {
			t.Errorf("Pop() call %d = %v, want %v", i+1, got, want)
		}
	}
}

func TestMinHeap_Heapify(t *testing.T) {
	mh := NewMinHeap()
	nums := []int{5, 3, 7, 1, 4, 6, 2}
	mh.Heapify(nums)

	expected := []int{1, 2, 3, 4, 5, 6, 7}
	for i, want := range expected {
		if got := mh.Pop(); got != want {
			t.Errorf("Pop() call %d after Heapify = %v, want %v", i+1, got, want)
		}
	}
}

func TestMinHeap_HeapifyEmpty(t *testing.T) {
	mh := NewMinHeap()
	mh.Heapify([]int{})

	if got := mh.Top(); got != -1 {
		t.Errorf("Top() after Heapify with empty array = %v, want -1", got)
	}
}

func TestMinHeap_HeapifySingleElement(t *testing.T) {
	mh := NewMinHeap()
	mh.Heapify([]int{42})

	if got := mh.Top(); got != 42 {
		t.Errorf("Top() = %v, want 42", got)
	}

	if got := mh.Pop(); got != 42 {
		t.Errorf("Pop() = %v, want 42", got)
	}
}

func TestMinHeap_MixedOperations(t *testing.T) {
	mh := NewMinHeap()

	// Push some elements
	mh.Push(10)
	mh.Push(5)
	mh.Push(15)

	if got := mh.Pop(); got != 5 {
		t.Errorf("First Pop() = %v, want 5", got)
	}

	// Push more elements
	mh.Push(3)
	mh.Push(20)

	if got := mh.Top(); got != 3 {
		t.Errorf("Top() = %v, want 3", got)
	}

	expected := []int{3, 10, 15, 20}
	for i, want := range expected {
		if got := mh.Pop(); got != want {
			t.Errorf("Pop() call %d = %v, want %v", i+1, got, want)
		}
	}
}

func TestMinHeap_Example1(t *testing.T) {
	mh := NewMinHeap()

	// "top"
	if got := mh.Top(); got != -1 {
		t.Errorf("Top() = %v, want -1", got)
	}

	// "push", 1
	mh.Push(1)

	// "top"
	if got := mh.Top(); got != 1 {
		t.Errorf("Top() = %v, want 1", got)
	}

	// "pop"
	if got := mh.Pop(); got != 1 {
		t.Errorf("Pop() = %v, want 1", got)
	}

	// "pop"
	if got := mh.Pop(); got != -1 {
		t.Errorf("Pop() = %v, want -1", got)
	}
}

func TestMinHeap_Example2(t *testing.T) {
	mh := NewMinHeap()

	// "heapify", [1 2 3 4 5]
	mh.Heapify([]int{1, 2, 3, 4, 5})

	expected := []int{1, 2, 3, 4, 5}
	for i, want := range expected {
		if got := mh.Pop(); got != want {
			t.Errorf("Pop() call %d = %v, want %v", i+1, got, want)
		}
	}
}

func TestMinHeap_HeapifyThenPush(t *testing.T) {
	mh := NewMinHeap()
	mh.Heapify([]int{5, 3, 7})
	mh.Push(1)
	mh.Push(10)

	expected := []int{1, 3, 5, 7, 10}
	for i, want := range expected {
		if got := mh.Pop(); got != want {
			t.Errorf("Pop() call %d = %v, want %v", i+1, got, want)
		}
	}
}

func TestMinHeap_LargeDataset(t *testing.T) {
	mh := NewMinHeap()

	// Push elements in reverse order
	for i := 100; i > 0; i-- {
		mh.Push(i)
	}

	// Should pop in ascending order
	for i := 1; i <= 100; i++ {
		if got := mh.Pop(); got != i {
			t.Errorf("Pop() = %v, want %v", got, i)
			break
		}
	}
}

func TestMinHeap_TopDoesNotRemove(t *testing.T) {
	mh := NewMinHeap()
	mh.Push(5)
	mh.Push(3)
	mh.Push(7)

	// Call Top multiple times
	for i := 0; i < 5; i++ {
		if got := mh.Top(); got != 3 {
			t.Errorf("Top() call %d = %v, want 3", i+1, got)
		}
	}

	// Verify element is still there
	if got := mh.Pop(); got != 3 {
		t.Errorf("Pop() = %v, want 3", got)
	}
}
