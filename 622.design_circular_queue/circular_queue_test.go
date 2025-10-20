package designcircularqueue

import (
	"testing"
)

func TestConstructor(t *testing.T) {
	q := Constructor(3)

	if q.max != 3 {
		t.Errorf("Expected maxSize 3, got %d", q.max)
	}

	if q.front != -1 {
		t.Errorf("Expected front -1, got %d", q.front)
	}

	if q.rear != -1 {
		t.Errorf("Expected rear -1, got %d", q.rear)
	}

	if !q.IsEmpty() {
		t.Error("Expected queue to be empty")
	}
}

func TestEnQueueSingleElement(t *testing.T) {
	q := Constructor(3)

	result := q.EnQueue(1)

	if !result {
		t.Error("Expected EnQueue to return true")
	}

	if q.IsEmpty() {
		t.Error("Expected queue to not be empty")
	}

	if q.Front() != 1 {
		t.Errorf("Expected Front() to return 1, got %d", q.Front())
	}

	if q.Rear() != 1 {
		t.Errorf("Expected Rear() to return 1, got %d", q.Rear())
	}
}

func TestEnQueueMultipleElements(t *testing.T) {
	q := Constructor(3)

	q.EnQueue(1)
	q.EnQueue(2)
	q.EnQueue(3)

	if q.Front() != 1 {
		t.Errorf("Expected Front() to return 1, got %d", q.Front())
	}

	if q.Rear() != 3 {
		t.Errorf("Expected Rear() to return 3, got %d", q.Rear())
	}

	if q.IsFull() != true {
		t.Error("Expected queue to be full")
	}
}

func TestEnQueueWhenFull(t *testing.T) {
	q := Constructor(3)

	q.EnQueue(1)
	q.EnQueue(2)
	q.EnQueue(3)
	result := q.EnQueue(4)

	if result {
		t.Error("Expected EnQueue to return false when queue is full")
	}

	if q.Rear() != 3 {
		t.Errorf("Expected Rear() to still return 3, got %d", q.Rear())
	}
}

func TestDeQueueSingleElement(t *testing.T) {
	q := Constructor(3)
	q.EnQueue(1)

	result := q.DeQueue()

	if !result {
		t.Error("Expected DeQueue to return true")
	}

	if !q.IsEmpty() {
		t.Error("Expected queue to be empty after dequeue")
	}

	if q.Front() != -1 {
		t.Errorf("Expected Front() to return -1, got %d", q.Front())
	}
}

func TestDeQueueMultipleElements(t *testing.T) {
	q := Constructor(3)
	q.EnQueue(1)
	q.EnQueue(2)
	q.EnQueue(3)

	q.DeQueue()

	if q.Front() != 2 {
		t.Errorf("Expected Front() to return 2, got %d", q.Front())
	}

	if q.Rear() != 3 {
		t.Errorf("Expected Rear() to return 3, got %d", q.Rear())
	}

	q.DeQueue()

	if q.Front() != 3 {
		t.Errorf("Expected Front() to return 3, got %d", q.Front())
	}
}

func TestDeQueueWhenEmpty(t *testing.T) {
	q := Constructor(3)

	result := q.DeQueue()

	if result {
		t.Error("Expected DeQueue to return false when queue is empty")
	}
}

func TestCircularBehavior(t *testing.T) {
	q := Constructor(3)

	// Fill the queue
	q.EnQueue(1)
	q.EnQueue(2)
	q.EnQueue(3)

	// Remove one element
	q.DeQueue()

	// Add element (should wrap around)
	result := q.EnQueue(4)

	if !result {
		t.Error("Expected EnQueue to return true after dequeue")
	}

	if q.Rear() != 4 {
		t.Errorf("Expected Rear() to return 4, got %d", q.Rear())
	}

	if q.Front() != 2 {
		t.Errorf("Expected Front() to return 2, got %d", q.Front())
	}
}

func TestExampleFromProblem(t *testing.T) {
	q := Constructor(3)

	if !q.EnQueue(1) {
		t.Error("Expected enQueue(1) to return true")
	}

	if !q.EnQueue(2) {
		t.Error("Expected enQueue(2) to return true")
	}

	if !q.EnQueue(3) {
		t.Error("Expected enQueue(3) to return true")
	}

	if q.EnQueue(4) {
		t.Error("Expected enQueue(4) to return false")
	}

	if q.Rear() != 3 {
		t.Errorf("Expected Rear() to return 3, got %d", q.Rear())
	}

	if !q.IsFull() {
		t.Error("Expected isFull() to return true")
	}

	if !q.DeQueue() {
		t.Error("Expected deQueue() to return true")
	}

	if !q.EnQueue(4) {
		t.Error("Expected enQueue(4) to return true")
	}

	if q.Rear() != 4 {
		t.Errorf("Expected Rear() to return 4, got %d", q.Rear())
	}
}

func TestIsEmpty(t *testing.T) {
	q := Constructor(3)

	if !q.IsEmpty() {
		t.Error("Expected new queue to be empty")
	}

	q.EnQueue(1)

	if q.IsEmpty() {
		t.Error("Expected queue with elements to not be empty")
	}

	q.DeQueue()

	if !q.IsEmpty() {
		t.Error("Expected queue to be empty after removing all elements")
	}
}

func TestIsFull(t *testing.T) {
	q := Constructor(2)

	if q.IsFull() {
		t.Error("Expected new queue to not be full")
	}

	q.EnQueue(1)

	if q.IsFull() {
		t.Error("Expected queue with 1 element to not be full")
	}

	q.EnQueue(2)

	if !q.IsFull() {
		t.Error("Expected queue to be full")
	}
}

func TestFrontAndRearWhenEmpty(t *testing.T) {
	q := Constructor(3)

	if q.Front() != -1 {
		t.Errorf("Expected Front() to return -1 when empty, got %d", q.Front())
	}

	if q.Rear() != -1 {
		t.Errorf("Expected Rear() to return -1 when empty, got %d", q.Rear())
	}
}

func TestMultipleEnqueueDequeueCycles(t *testing.T) {
	q := Constructor(3)

	// First cycle
	q.EnQueue(1)
	q.EnQueue(2)
	q.DeQueue()
	q.DeQueue()

	// Second cycle
	q.EnQueue(3)
	q.EnQueue(4)
	q.EnQueue(5)

	if q.Front() != 3 {
		t.Errorf("Expected Front() to return 3, got %d", q.Front())
	}

	if q.Rear() != 5 {
		t.Errorf("Expected Rear() to return 5, got %d", q.Rear())
	}

	if !q.IsFull() {
		t.Error("Expected queue to be full")
	}
}

func TestSingleElementQueue(t *testing.T) {
	q := Constructor(1)

	if !q.EnQueue(42) {
		t.Error("Expected enQueue to return true")
	}

	if !q.IsFull() {
		t.Error("Expected queue to be full")
	}

	if q.EnQueue(99) {
		t.Error("Expected enQueue to return false when full")
	}

	if q.Front() != 42 {
		t.Errorf("Expected Front() to return 42, got %d", q.Front())
	}

	if q.Rear() != 42 {
		t.Errorf("Expected Rear() to return 42, got %d", q.Rear())
	}

	if !q.DeQueue() {
		t.Error("Expected deQueue to return true")
	}

	if !q.IsEmpty() {
		t.Error("Expected queue to be empty")
	}
}

func TestLargeQueue(t *testing.T) {
	q := Constructor(1000)

	// Fill half the queue
	for i := 0; i < 500; i++ {
		if !q.EnQueue(i) {
			t.Errorf("Expected enQueue(%d) to succeed", i)
		}
	}

	if q.Front() != 0 {
		t.Errorf("Expected Front() to return 0, got %d", q.Front())
	}

	if q.Rear() != 499 {
		t.Errorf("Expected Rear() to return 499, got %d", q.Rear())
	}

	// Remove half
	for i := 0; i < 250; i++ {
		if !q.DeQueue() {
			t.Errorf("Expected deQueue to succeed at iteration %d", i)
		}
	}

	if q.Front() != 250 {
		t.Errorf("Expected Front() to return 250, got %d", q.Front())
	}
}
