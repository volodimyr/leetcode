package sortanarray

import (
	"reflect"
	"testing"
)

func TestSortArray1_Example1(t *testing.T) {
	nums := []int{10, 9, 1, 1, 1, 2, 3, 1}
	expected := []int{1, 1, 1, 1, 2, 3, 9, 10}
	result := sortArray1(nums)

	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, but got %v", expected, result)
	}
}

func TestSortArray1_Example2(t *testing.T) {
	nums := []int{5, 10, 2, 1, 3}
	expected := []int{1, 2, 3, 5, 10}
	result := sortArray1(nums)

	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, but got %v", expected, result)
	}
}

func TestSortArray1_SingleElement(t *testing.T) {
	nums := []int{42}
	expected := []int{42}
	result := sortArray1(nums)

	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, but got %v", expected, result)
	}
}

func TestSortArray1_TwoElements(t *testing.T) {
	nums := []int{2, 1}
	expected := []int{1, 2}
	result := sortArray1(nums)

	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, but got %v", expected, result)
	}
}

func TestSortArray1_AlreadySorted(t *testing.T) {
	nums := []int{1, 2, 3, 4, 5}
	expected := []int{1, 2, 3, 4, 5}
	result := sortArray1(nums)

	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, but got %v", expected, result)
	}
}

func TestSortArray1_ReverseSorted(t *testing.T) {
	nums := []int{5, 4, 3, 2, 1}
	expected := []int{1, 2, 3, 4, 5}
	result := sortArray1(nums)

	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, but got %v", expected, result)
	}
}

func TestSortArray1_AllSameElements(t *testing.T) {
	nums := []int{3, 3, 3, 3, 3}
	expected := []int{3, 3, 3, 3, 3}
	result := sortArray1(nums)

	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, but got %v", expected, result)
	}
}

func TestSortArray1_NegativeNumbers(t *testing.T) {
	nums := []int{-5, -1, -10, -3, -2}
	expected := []int{-10, -5, -3, -2, -1}
	result := sortArray1(nums)

	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, but got %v", expected, result)
	}
}

func TestSortArray1_MixedPositiveNegative(t *testing.T) {
	nums := []int{3, -1, 0, -5, 2, 10, -3}
	expected := []int{-5, -3, -1, 0, 2, 3, 10}
	result := sortArray1(nums)

	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, but got %v", expected, result)
	}
}

func TestSortArray1_WithZeros(t *testing.T) {
	nums := []int{0, 5, 0, -2, 0, 3}
	expected := []int{-2, 0, 0, 0, 3, 5}
	result := sortArray1(nums)

	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, but got %v", expected, result)
	}
}

func TestSortArray1_BoundaryValues(t *testing.T) {
	nums := []int{50000, -50000, 0, 1, -1}
	expected := []int{-50000, -1, 0, 1, 50000}
	result := sortArray1(nums)

	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, but got %v", expected, result)
	}
}

func TestSortArray1_LargeArrayWithDuplicates(t *testing.T) {
	nums := []int{7, 2, 7, 1, 9, 2, 5, 7, 1, 9}
	expected := []int{1, 1, 2, 2, 5, 7, 7, 7, 9, 9}
	result := sortArray1(nums)

	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, but got %v", expected, result)
	}
}

func TestSortArray1_ThreeElements(t *testing.T) {
	nums := []int{3, 1, 2}
	expected := []int{1, 2, 3}
	result := sortArray1(nums)

	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, but got %v", expected, result)
	}
}

// Test that the function modifies the original array (in-place sorting)
func TestSortArray1_ModifiesOriginalArray(t *testing.T) {
	nums := []int{5, 2, 8, 1}
	originalPtr := &nums[0]
	result := sortArray1(nums)
	resultPtr := &result[0]

	if originalPtr != resultPtr {
		t.Error("Function should return the same array (in-place sorting)")
	}
}

// Edge case: alternating high-low values
func TestSortArray1_AlternatingValues(t *testing.T) {
	nums := []int{100, 1, 99, 2, 98, 3}
	expected := []int{1, 2, 3, 98, 99, 100}
	result := sortArray1(nums)

	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, but got %v", expected, result)
	}
}
