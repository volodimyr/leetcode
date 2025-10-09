package sortanarray

import (
	"reflect"
	"testing"
)

func TestSortArray_Example1(t *testing.T) {
	nums := []int{5, 2, 3, 1}
	expected := []int{1, 2, 3, 5}
	result := sortArray(nums)
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestSortArray_Example2(t *testing.T) {
	nums := []int{5, 1, 1, 2, 0, 0}
	expected := []int{0, 0, 1, 1, 2, 5}
	result := sortArray(nums)
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestSortArray_SingleElement(t *testing.T) {
	nums := []int{1}
	expected := []int{1}
	result := sortArray(nums)
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestSortArray_TwoElements(t *testing.T) {
	nums := []int{2, 1}
	expected := []int{1, 2}
	result := sortArray(nums)
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestSortArray_AlreadySorted(t *testing.T) {
	nums := []int{1, 2, 3, 4, 5}
	expected := []int{1, 2, 3, 4, 5}
	result := sortArray(nums)
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestSortArray_ReverseSorted(t *testing.T) {
	nums := []int{5, 4, 3, 2, 1}
	expected := []int{1, 2, 3, 4, 5}
	result := sortArray(nums)
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestSortArray_AllSameElements(t *testing.T) {
	nums := []int{3, 3, 3, 3}
	expected := []int{3, 3, 3, 3}
	result := sortArray(nums)
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestSortArray_NegativeNumbers(t *testing.T) {
	nums := []int{-1, -5, -3, -2, -4}
	expected := []int{-5, -4, -3, -2, -1}
	result := sortArray(nums)
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestSortArray_MixedPositiveNegative(t *testing.T) {
	nums := []int{3, -1, 2, -5, 0}
	expected := []int{-5, -1, 0, 2, 3}
	result := sortArray(nums)
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestSortArray_WithZeros(t *testing.T) {
	nums := []int{0, 0, 0, 1, -1}
	expected := []int{-1, 0, 0, 0, 1}
	result := sortArray(nums)
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestSortArray_LargeNumbers(t *testing.T) {
	nums := []int{50000, -50000, 25000, -25000, 0}
	expected := []int{-50000, -25000, 0, 25000, 50000}
	result := sortArray(nums)
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestSortArray_DuplicateElements(t *testing.T) {
	nums := []int{4, 2, 4, 1, 3, 2, 1}
	expected := []int{1, 1, 2, 2, 3, 4, 4}
	result := sortArray(nums)
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestSortArray_LargerArray(t *testing.T) {
	nums := []int{10, 7, 8, 9, 1, 5, 3, 6, 4, 2}
	expected := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	result := sortArray(nums)
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestSortArray_ThreeElements(t *testing.T) {
	nums := []int{3, 1, 2}
	expected := []int{1, 2, 3}
	result := sortArray(nums)
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestSortArray_AlternatingPattern(t *testing.T) {
	nums := []int{1, 3, 2, 4, 3, 5}
	expected := []int{1, 2, 3, 3, 4, 5}
	result := sortArray(nums)
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}
