package findmedianfromdatastream

import (
	"testing"
)

func TestMedianFinder(t *testing.T) {
	mf := Constructor()
	mf.AddNum(1)
	mf.AddNum(2)

	median := mf.FindMedian()
	expected := 1.5
	if median != expected {
		t.Errorf("Expected %v, got %v", expected, median)
	}

	mf.AddNum(3)
	median = mf.FindMedian()
	expected = 2.0
	if median != expected {
		t.Errorf("Expected %v, got %v", expected, median)
	}
}

func TestMedianFinderSingleElement(t *testing.T) {
	mf := Constructor()
	mf.AddNum(5)

	median := mf.FindMedian()
	expected := 5.0
	if median != expected {
		t.Errorf("Expected %v, got %v", expected, median)
	}
}

func TestMedianFinderNegativeNumbers(t *testing.T) {
	mf := Constructor()
	mf.AddNum(-1)
	mf.AddNum(-2)
	mf.AddNum(-3)

	median := mf.FindMedian()
	expected := -2.0
	if median != expected {
		t.Errorf("Expected %v, got %v", expected, median)
	}
}

func TestMedianFinderMixedNumbers(t *testing.T) {
	mf := Constructor()
	mf.AddNum(-1)
	mf.AddNum(5)
	mf.AddNum(3)
	mf.AddNum(-2)

	median := mf.FindMedian()
	expected := 1.0
	if median != expected {
		t.Errorf("Expected %v, got %v", expected, median)
	}
}

func TestMedianFinderLargeSequence(t *testing.T) {
	mf := Constructor()
	nums := []int{12, 10, 13, 11, 5, 15, 1, 2, 3, 6}

	for _, num := range nums {
		mf.AddNum(num)
	}

	median := mf.FindMedian()
	expected := 8.0
	if median != expected {
		t.Errorf("Expected %v, got %v", expected, median)
	}
}

func TestMedianFinderDuplicates(t *testing.T) {
	mf := Constructor()
	mf.AddNum(1)
	mf.AddNum(1)
	mf.AddNum(1)

	median := mf.FindMedian()
	expected := 1.0
	if median != expected {
		t.Errorf("Expected %v, got %v", expected, median)
	}
}

func TestMedianFinderAlternatingOddEven(t *testing.T) {
	mf := Constructor()

	mf.AddNum(1)
	if median := mf.FindMedian(); median != 1.0 {
		t.Errorf("After 1 element: expected 1.0, got %v", median)
	}

	mf.AddNum(2)
	if median := mf.FindMedian(); median != 1.5 {
		t.Errorf("After 2 elements: expected 1.5, got %v", median)
	}

	mf.AddNum(3)
	if median := mf.FindMedian(); median != 2.0 {
		t.Errorf("After 3 elements: expected 2.0, got %v", median)
	}

	mf.AddNum(4)
	if median := mf.FindMedian(); median != 2.5 {
		t.Errorf("After 4 elements: expected 2.5, got %v", median)
	}

	mf.AddNum(5)
	if median := mf.FindMedian(); median != 3.0 {
		t.Errorf("After 5 elements: expected 3.0, got %v", median)
	}
}

func TestMedianFinderDescendingOrder(t *testing.T) {
	mf := Constructor()
	mf.AddNum(5)
	mf.AddNum(4)
	mf.AddNum(3)
	mf.AddNum(2)
	mf.AddNum(1)

	median := mf.FindMedian()
	expected := 3.0
	if median != expected {
		t.Errorf("Expected %v, got %v", expected, median)
	}
}

func TestMedianFinderAllSameNumbers(t *testing.T) {
	mf := Constructor()
	for i := 0; i < 10; i++ {
		mf.AddNum(7)
	}

	median := mf.FindMedian()
	expected := 7.0
	if median != expected {
		t.Errorf("Expected %v, got %v", expected, median)
	}
}

func TestMedianFinderTwoElements(t *testing.T) {
	mf := Constructor()
	mf.AddNum(10)
	mf.AddNum(20)

	median := mf.FindMedian()
	expected := 15.0
	if median != expected {
		t.Errorf("Expected %v, got %v", expected, median)
	}
}
