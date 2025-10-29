package maximumfrequencystack

import (
	"testing"
)

func TestFreqStack(t *testing.T) {
	freqStack := Constructor()
	freqStack.Push(5)
	freqStack.Push(7)
	freqStack.Push(5)
	freqStack.Push(7)
	freqStack.Push(4)
	freqStack.Push(5)

	if got := freqStack.Pop(); got != 5 {
		t.Errorf("Pop() = %v, want %v", got, 5)
	}
	if got := freqStack.Pop(); got != 7 {
		t.Errorf("Pop() = %v, want %v", got, 7)
	}
	if got := freqStack.Pop(); got != 5 {
		t.Errorf("Pop() = %v, want %v", got, 5)
	}
	if got := freqStack.Pop(); got != 4 {
		t.Errorf("Pop() = %v, want %v", got, 4)
	}
}

func TestFreqStackSingleElement(t *testing.T) {
	freqStack := Constructor()
	freqStack.Push(1)

	if got := freqStack.Pop(); got != 1 {
		t.Errorf("Pop() = %v, want %v", got, 1)
	}
}

func TestFreqStackAllSameElement(t *testing.T) {
	freqStack := Constructor()
	freqStack.Push(3)
	freqStack.Push(3)
	freqStack.Push(3)

	if got := freqStack.Pop(); got != 3 {
		t.Errorf("Pop() = %v, want %v", got, 3)
	}
	if got := freqStack.Pop(); got != 3 {
		t.Errorf("Pop() = %v, want %v", got, 3)
	}
	if got := freqStack.Pop(); got != 3 {
		t.Errorf("Pop() = %v, want %v", got, 3)
	}
}

func TestFreqStackMultipleOperations(t *testing.T) {
	freqStack := Constructor()
	freqStack.Push(1)
	freqStack.Push(2)
	freqStack.Push(1)

	if got := freqStack.Pop(); got != 1 {
		t.Errorf("Pop() = %v, want %v", got, 1)
	}

	freqStack.Push(3)
	freqStack.Push(2)

	if got := freqStack.Pop(); got != 2 {
		t.Errorf("Pop() = %v, want %v", got, 2)
	}
	if got := freqStack.Pop(); got != 3 {
		t.Errorf("Pop() = %v, want %v", got, 3)
	}
	if got := freqStack.Pop(); got != 2 {
		t.Errorf("Pop() = %v, want %v", got, 2)
	}
	if got := freqStack.Pop(); got != 1 {
		t.Errorf("Pop() = %v, want %v", got, 1)
	}
}

func TestFreqStackTieBreaker(t *testing.T) {
	freqStack := Constructor()
	freqStack.Push(1)
	freqStack.Push(2)
	freqStack.Push(3)

	if got := freqStack.Pop(); got != 3 {
		t.Errorf("Pop() = %v, want %v", got, 3)
	}
	if got := freqStack.Pop(); got != 2 {
		t.Errorf("Pop() = %v, want %v", got, 2)
	}
	if got := freqStack.Pop(); got != 1 {
		t.Errorf("Pop() = %v, want %v", got, 1)
	}
}

func TestFreqStackComplexScenario(t *testing.T) {
	freqStack := Constructor()
	freqStack.Push(4)
	freqStack.Push(0)
	freqStack.Push(9)
	freqStack.Push(3)
	freqStack.Push(4)
	freqStack.Push(2)

	if got := freqStack.Pop(); got != 4 {
		t.Errorf("Pop() = %v, want %v", got, 4)
	}

	freqStack.Push(6)

	if got := freqStack.Pop(); got != 6 {
		t.Errorf("Pop() = %v, want %v", got, 6)
	}

	freqStack.Push(1)

	if got := freqStack.Pop(); got != 1 {
		t.Errorf("Pop() = %v, want %v", got, 1)
	}

	freqStack.Push(1)

	if got := freqStack.Pop(); got != 1 {
		t.Errorf("Pop() = %v, want %v", got, 1)
	}
}
