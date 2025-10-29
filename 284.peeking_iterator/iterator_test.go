package peekingiterator

import "testing"

func TestPeekingIterator_Example1(t *testing.T) {
	// ["PeekingIterator", "next", "peek", "next", "next", "hasNext"]
	// [[[1, 2, 3]], [], [], [], [], []]
	// Expected: [null, 1, 2, 2, 3, false]

	iter := &Iterator[int]{arr: []int{1, 2, 3}, i: 0}
	pi := Constructor(iter)

	// next() should return 1
	if got := pi.next(); got != 1 {
		t.Errorf("next() = %v, want 1", got)
	}

	// peek() should return 2 without moving pointer
	if got := pi.peek(); got != 2 {
		t.Errorf("peek() = %v, want 2", got)
	}

	// next() should return 2 (peek didn't move pointer)
	if got := pi.next(); got != 2 {
		t.Errorf("next() = %v, want 2", got)
	}

	// next() should return 3
	if got := pi.next(); got != 3 {
		t.Errorf("next() = %v, want 3", got)
	}

	// hasNext() should return false
	if got := pi.hasNext(); got != false {
		t.Errorf("hasNext() = %v, want false", got)
	}
}

func TestPeekingIterator_SingleElement(t *testing.T) {
	iter := &Iterator[int]{arr: []int{42}, i: 0}
	pi := Constructor(iter)

	if !pi.hasNext() {
		t.Error("hasNext() should return true for single element")
	}

	if got := pi.peek(); got != 42 {
		t.Errorf("peek() = %v, want 42", got)
	}

	if got := pi.next(); got != 42 {
		t.Errorf("next() = %v, want 42", got)
	}

	if pi.hasNext() {
		t.Error("hasNext() should return false after consuming single element")
	}
}

func TestPeekingIterator_MultiplePeeks(t *testing.T) {
	iter := &Iterator[int]{arr: []int{1, 2, 3}, i: 0}
	pi := Constructor(iter)

	// Multiple peeks should return the same value
	for i := 0; i < 5; i++ {
		if got := pi.peek(); got != 1 {
			t.Errorf("peek() call %d = %v, want 1", i+1, got)
		}
	}

	// next() should still return 1
	if got := pi.next(); got != 1 {
		t.Errorf("next() = %v, want 1", got)
	}
}

func TestPeekingIterator_AlternatingPeekAndNext(t *testing.T) {
	iter := &Iterator[int]{arr: []int{10, 20, 30, 40}, i: 0}
	pi := Constructor(iter)

	// peek at 10
	if got := pi.peek(); got != 10 {
		t.Errorf("peek() = %v, want 10", got)
	}

	// consume 10
	if got := pi.next(); got != 10 {
		t.Errorf("next() = %v, want 10", got)
	}

	// peek at 20
	if got := pi.peek(); got != 20 {
		t.Errorf("peek() = %v, want 20", got)
	}

	// peek at 20 again
	if got := pi.peek(); got != 20 {
		t.Errorf("peek() = %v, want 20", got)
	}

	// consume 20
	if got := pi.next(); got != 20 {
		t.Errorf("next() = %v, want 20", got)
	}

	// consume 30 without peeking
	if got := pi.next(); got != 30 {
		t.Errorf("next() = %v, want 30", got)
	}

	// peek at 40
	if got := pi.peek(); got != 40 {
		t.Errorf("peek() = %v, want 40", got)
	}

	if !pi.hasNext() {
		t.Error("hasNext() should return true")
	}

	// consume 40
	if got := pi.next(); got != 40 {
		t.Errorf("next() = %v, want 40", got)
	}

	if pi.hasNext() {
		t.Error("hasNext() should return false")
	}
}

func TestPeekingIterator_OnlyNext(t *testing.T) {
	iter := &Iterator[int]{arr: []int{5, 10, 15}, i: 0}
	pi := Constructor(iter)

	expected := []int{5, 10, 15}
	for i, want := range expected {
		if !pi.hasNext() {
			t.Errorf("hasNext() should return true at position %d", i)
		}

		if got := pi.next(); got != want {
			t.Errorf("next() at position %d = %v, want %v", i, got, want)
		}
	}

	if pi.hasNext() {
		t.Error("hasNext() should return false after consuming all elements")
	}
}

func TestPeekingIterator_OnlyPeek(t *testing.T) {
	iter := &Iterator[int]{arr: []int{100, 200}, i: 0}
	pi := Constructor(iter)

	// Peek multiple times without consuming
	for i := 0; i < 10; i++ {
		if got := pi.peek(); got != 100 {
			t.Errorf("peek() call %d = %v, want 100", i+1, got)
		}

		if !pi.hasNext() {
			t.Errorf("hasNext() should return true after peek call %d", i+1)
		}
	}
}

func TestPeekingIterator_LargeArray(t *testing.T) {
	size := 1000
	arr := make([]int, size)
	for i := 0; i < size; i++ {
		arr[i] = i + 1
	}

	iter := &Iterator[int]{arr: arr, i: 0}
	pi := Constructor(iter)

	for i := 1; i <= size; i++ {
		if !pi.hasNext() {
			t.Errorf("hasNext() should return true at position %d", i)
		}

		if got := pi.peek(); got != i {
			t.Errorf("peek() at position %d = %v, want %v", i, got, i)
		}

		if got := pi.next(); got != i {
			t.Errorf("next() at position %d = %v, want %v", i, got, i)
		}
	}

	if pi.hasNext() {
		t.Error("hasNext() should return false after consuming all elements")
	}
}

func TestPeekingIterator_StringType(t *testing.T) {
	iter := &Iterator[string]{arr: []string{"hello", "world", "test"}, i: 0}
	pi := Constructor(iter)

	if got := pi.peek(); got != "hello" {
		t.Errorf("peek() = %v, want 'hello'", got)
	}

	if got := pi.next(); got != "hello" {
		t.Errorf("next() = %v, want 'hello'", got)
	}

	if got := pi.next(); got != "world" {
		t.Errorf("next() = %v, want 'world'", got)
	}

	if got := pi.peek(); got != "test" {
		t.Errorf("peek() = %v, want 'test'", got)
	}

	if !pi.hasNext() {
		t.Error("hasNext() should return true")
	}
}
