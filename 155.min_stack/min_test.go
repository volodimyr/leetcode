package minstack

import "testing"

func TestExample1(t *testing.T) {
	minStack := Constructor()

	minStack.Push(-2)
	minStack.Push(0)
	minStack.Push(-3)

	min := minStack.GetMin()
	if min != -3 {
		t.Errorf("Expected GetMin() = -3, got %d", min)
	}

	minStack.Pop()

	top := minStack.Top()
	if top != 0 {
		t.Errorf("Expected Top() = 0, got %d", top)
	}

	min = minStack.GetMin()
	if min != -2 {
		t.Errorf("Expected GetMin() = -2, got %d", min)
	}
}

func TestPushSingleElement(t *testing.T) {
	minStack := Constructor()

	minStack.Push(5)

	if minStack.Top() != 5 {
		t.Errorf("Expected Top() = 5, got %d", minStack.Top())
	}

	if minStack.GetMin() != 5 {
		t.Errorf("Expected GetMin() = 5, got %d", minStack.GetMin())
	}
}

func TestPushMultipleAscending(t *testing.T) {
	minStack := Constructor()

	minStack.Push(1)
	minStack.Push(2)
	minStack.Push(3)

	if minStack.Top() != 3 {
		t.Errorf("Expected Top() = 3, got %d", minStack.Top())
	}

	if minStack.GetMin() != 1 {
		t.Errorf("Expected GetMin() = 1, got %d", minStack.GetMin())
	}
}

func TestPushMultipleDescending(t *testing.T) {
	minStack := Constructor()

	minStack.Push(3)
	minStack.Push(2)
	minStack.Push(1)

	if minStack.Top() != 1 {
		t.Errorf("Expected Top() = 1, got %d", minStack.Top())
	}

	if minStack.GetMin() != 1 {
		t.Errorf("Expected GetMin() = 1, got %d", minStack.GetMin())
	}
}

func TestPopSingleElement(t *testing.T) {
	minStack := Constructor()

	minStack.Push(10)
	minStack.Pop()

	// After popping the only element, stack should be empty
	// Note: we can't test this directly without checking length
}

func TestPopMultipleTimes(t *testing.T) {
	minStack := Constructor()

	minStack.Push(5)
	minStack.Push(10)
	minStack.Push(3)

	minStack.Pop()

	if minStack.Top() != 10 {
		t.Errorf("Expected Top() = 10 after first pop, got %d", minStack.Top())
	}

	if minStack.GetMin() != 5 {
		t.Errorf("Expected GetMin() = 5 after first pop, got %d", minStack.GetMin())
	}

	minStack.Pop()

	if minStack.Top() != 5 {
		t.Errorf("Expected Top() = 5 after second pop, got %d", minStack.Top())
	}

	if minStack.GetMin() != 5 {
		t.Errorf("Expected GetMin() = 5 after second pop, got %d", minStack.GetMin())
	}
}

func TestGetMinAfterPoppingMinimum(t *testing.T) {
	minStack := Constructor()

	minStack.Push(0)
	minStack.Push(1)
	minStack.Push(0)

	if minStack.GetMin() != 0 {
		t.Errorf("Expected GetMin() = 0, got %d", minStack.GetMin())
	}

	minStack.Pop()

	if minStack.GetMin() != 0 {
		t.Errorf("Expected GetMin() = 0 after pop, got %d", minStack.GetMin())
	}
}

func TestNegativeNumbers(t *testing.T) {
	minStack := Constructor()

	minStack.Push(-5)
	minStack.Push(-10)
	minStack.Push(-3)

	if minStack.GetMin() != -10 {
		t.Errorf("Expected GetMin() = -10, got %d", minStack.GetMin())
	}

	if minStack.Top() != -3 {
		t.Errorf("Expected Top() = -3, got %d", minStack.Top())
	}
}

func TestMixedPositiveNegative(t *testing.T) {
	minStack := Constructor()

	minStack.Push(5)
	minStack.Push(-5)
	minStack.Push(10)
	minStack.Push(-10)

	if minStack.GetMin() != -10 {
		t.Errorf("Expected GetMin() = -10, got %d", minStack.GetMin())
	}

	minStack.Pop()

	if minStack.GetMin() != -5 {
		t.Errorf("Expected GetMin() = -5 after pop, got %d", minStack.GetMin())
	}
}

func TestDuplicateValues(t *testing.T) {
	minStack := Constructor()

	minStack.Push(2)
	minStack.Push(2)
	minStack.Push(2)

	if minStack.GetMin() != 2 {
		t.Errorf("Expected GetMin() = 2, got %d", minStack.GetMin())
	}

	minStack.Pop()

	if minStack.GetMin() != 2 {
		t.Errorf("Expected GetMin() = 2 after pop, got %d", minStack.GetMin())
	}
}

func TestDuplicateMinimums(t *testing.T) {
	minStack := Constructor()

	minStack.Push(1)
	minStack.Push(2)
	minStack.Push(1)

	if minStack.GetMin() != 1 {
		t.Errorf("Expected GetMin() = 1, got %d", minStack.GetMin())
	}

	minStack.Pop()

	if minStack.GetMin() != 1 {
		t.Errorf("Expected GetMin() = 1 after pop, got %d", minStack.GetMin())
	}

	minStack.Pop()

	if minStack.GetMin() != 1 {
		t.Errorf("Expected GetMin() = 1 after second pop, got %d", minStack.GetMin())
	}
}

func TestZeroValues(t *testing.T) {
	minStack := Constructor()

	minStack.Push(0)
	minStack.Push(0)
	minStack.Push(0)

	if minStack.GetMin() != 0 {
		t.Errorf("Expected GetMin() = 0, got %d", minStack.GetMin())
	}

	if minStack.Top() != 0 {
		t.Errorf("Expected Top() = 0, got %d", minStack.Top())
	}
}

func TestLargeNumbers(t *testing.T) {
	minStack := Constructor()

	minStack.Push(2147483647)  // Max int32
	minStack.Push(-2147483648) // Min int32

	if minStack.GetMin() != -2147483648 {
		t.Errorf("Expected GetMin() = -2147483648, got %d", minStack.GetMin())
	}

	minStack.Pop()

	if minStack.GetMin() != 2147483647 {
		t.Errorf("Expected GetMin() = 2147483647, got %d", minStack.GetMin())
	}
}

func TestPushPopSequence(t *testing.T) {
	minStack := Constructor()

	minStack.Push(1)
	minStack.Push(2)
	minStack.Pop()
	minStack.Push(3)
	minStack.Pop()
	minStack.Push(4)

	if minStack.Top() != 4 {
		t.Errorf("Expected Top() = 4, got %d", minStack.Top())
	}

	if minStack.GetMin() != 1 {
		t.Errorf("Expected GetMin() = 1, got %d", minStack.GetMin())
	}
}

func TestMinChangesAfterMultiplePops(t *testing.T) {
	minStack := Constructor()

	minStack.Push(5)
	minStack.Push(1)
	minStack.Push(10)
	minStack.Push(2)

	if minStack.GetMin() != 1 {
		t.Errorf("Expected GetMin() = 1, got %d", minStack.GetMin())
	}

	minStack.Pop() // Remove 2
	minStack.Pop() // Remove 10
	minStack.Pop() // Remove 1

	if minStack.GetMin() != 5 {
		t.Errorf("Expected GetMin() = 5 after pops, got %d", minStack.GetMin())
	}
}

func TestTopDoesNotChangeMin(t *testing.T) {
	minStack := Constructor()

	minStack.Push(3)
	minStack.Push(1)
	minStack.Push(5)

	top1 := minStack.Top()
	min1 := minStack.GetMin()
	top2 := minStack.Top()
	min2 := minStack.GetMin()

	if top1 != top2 || top1 != 5 {
		t.Errorf("Expected Top() to remain 5, got %d and %d", top1, top2)
	}

	if min1 != min2 || min1 != 1 {
		t.Errorf("Expected GetMin() to remain 1, got %d and %d", min1, min2)
	}
}

func TestComplexSequence(t *testing.T) {
	minStack := Constructor()

	minStack.Push(512)
	minStack.Push(-1024)
	minStack.Push(-1024)
	minStack.Push(512)

	minStack.Pop()

	if minStack.GetMin() != -1024 {
		t.Errorf("Expected GetMin() = -1024, got %d", minStack.GetMin())
	}

	minStack.Pop()

	if minStack.GetMin() != -1024 {
		t.Errorf("Expected GetMin() = -1024, got %d", minStack.GetMin())
	}

	minStack.Pop()

	if minStack.GetMin() != 512 {
		t.Errorf("Expected GetMin() = 512, got %d", minStack.GetMin())
	}
}

func TestSingleElementOperations(t *testing.T) {
	minStack := Constructor()

	minStack.Push(100)

	if minStack.Top() != 100 {
		t.Errorf("Expected Top() = 100, got %d", minStack.Top())
	}

	if minStack.GetMin() != 100 {
		t.Errorf("Expected GetMin() = 100, got %d", minStack.GetMin())
	}

	minStack.Pop()
	minStack.Push(200)

	if minStack.Top() != 200 {
		t.Errorf("Expected Top() = 200, got %d", minStack.Top())
	}

	if minStack.GetMin() != 200 {
		t.Errorf("Expected GetMin() = 200, got %d", minStack.GetMin())
	}
}
