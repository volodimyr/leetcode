package sort

import (
	"reflect"
	"testing"
)

func TestInsertionSortEmptySlice(t *testing.T) {
	pairs := []Pair{}
	result := insertionSort(pairs)
	expected := [][]Pair{}
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestInsertionSortExample1(t *testing.T) {
	pairs := []Pair{{5, "apple"}, {2, "banana"}, {9, "cherry"}}
	result := insertionSort(pairs)
	expected := [][]Pair{
		{{5, "apple"}, {2, "banana"}, {9, "cherry"}},
		{{2, "banana"}, {5, "apple"}, {9, "cherry"}},
		{{2, "banana"}, {5, "apple"}, {9, "cherry"}},
	}
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestInsertionSortExample2(t *testing.T) {
	pairs := []Pair{{3, "cat"}, {3, "bird"}, {2, "dog"}}
	result := insertionSort(pairs)
	expected := [][]Pair{
		{{3, "cat"}, {3, "bird"}, {2, "dog"}},
		{{3, "cat"}, {3, "bird"}, {2, "dog"}},
		{{2, "dog"}, {3, "cat"}, {3, "bird"}},
	}
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestInsertionSortAlreadySorted(t *testing.T) {
	pairs := []Pair{{1, "a"}, {2, "b"}, {3, "c"}}
	result := insertionSort(pairs)
	expected := [][]Pair{
		{{1, "a"}, {2, "b"}, {3, "c"}},
		{{1, "a"}, {2, "b"}, {3, "c"}},
		{{1, "a"}, {2, "b"}, {3, "c"}},
	}
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestInsertionSortReverseSorted(t *testing.T) {
	pairs := []Pair{{3, "c"}, {2, "b"}, {1, "a"}}
	result := insertionSort(pairs)
	expected := [][]Pair{
		{{3, "c"}, {2, "b"}, {1, "a"}},
		{{2, "b"}, {3, "c"}, {1, "a"}},
		{{1, "a"}, {2, "b"}, {3, "c"}},
	}
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestInsertionSortTwoElements(t *testing.T) {
	pairs := []Pair{{2, "b"}, {1, "a"}}
	result := insertionSort(pairs)
	expected := [][]Pair{
		{{2, "b"}, {1, "a"}},
		{{1, "a"}, {2, "b"}},
	}
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestInsertionSortAllSameKeys(t *testing.T) {
	pairs := []Pair{{5, "first"}, {5, "second"}, {5, "third"}}
	result := insertionSort(pairs)
	expected := [][]Pair{
		{{5, "first"}, {5, "second"}, {5, "third"}},
		{{5, "first"}, {5, "second"}, {5, "third"}},
		{{5, "first"}, {5, "second"}, {5, "third"}},
	}
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestInsertionSortStabilityCheck(t *testing.T) {
	pairs := []Pair{{2, "first"}, {1, "a"}, {2, "second"}}
	result := insertionSort(pairs)
	expected := [][]Pair{
		{{2, "first"}, {1, "a"}, {2, "second"}},
		{{1, "a"}, {2, "first"}, {2, "second"}},
		{{1, "a"}, {2, "first"}, {2, "second"}},
	}
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}
