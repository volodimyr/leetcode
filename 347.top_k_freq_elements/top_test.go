package topkfreqelements

import (
	"reflect"
	"sort"
	"testing"
)

// Helper function to compare slices ignoring order
func containsSameElements(a, b []int) bool {
	if len(a) != len(b) {
		return false
	}
	aCopy := make([]int, len(a))
	bCopy := make([]int, len(b))
	copy(aCopy, a)
	copy(bCopy, b)
	sort.Ints(aCopy)
	sort.Ints(bCopy)
	return reflect.DeepEqual(aCopy, bCopy)
}

// Test Example 1: [1,1,1,2,2,3], k=2 -> [1,2]
func TestTopKFrequent_Example1(t *testing.T) {
	nums := []int{1, 1, 1, 2, 2, 3}
	k := 2
	expected := []int{1, 2}

	result := topKFrequent(nums, k)

	if !containsSameElements(result, expected) {
		t.Errorf("Expected %v (in any order), got %v", expected, result)
	}

	if len(result) != k {
		t.Errorf("Expected %d elements, got %d", k, len(result))
	}
}

// Test Example 2: [1], k=1 -> [1]
func TestTopKFrequent_Example2(t *testing.T) {
	nums := []int{1}
	k := 1
	expected := []int{1}

	result := topKFrequent(nums, k)

	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

// Test Example 3: [1,2,1,2,1,2,3,1,3,2], k=2 -> [1,2]
func TestTopKFrequent_Example3(t *testing.T) {
	nums := []int{1, 2, 1, 2, 1, 2, 3, 1, 3, 2}
	k := 2
	expected := []int{1, 2}

	result := topKFrequent(nums, k)

	if !containsSameElements(result, expected) {
		t.Errorf("Expected %v (in any order), got %v", expected, result)
	}
}

// Test with all elements having same frequency
func TestTopKFrequent_SameFrequency(t *testing.T) {
	nums := []int{1, 2, 3, 4}
	k := 2

	result := topKFrequent(nums, k)

	if len(result) != k {
		t.Errorf("Expected %d elements, got %d", k, len(result))
	}

	// All elements have frequency 1, so any 2 are valid
	for _, val := range result {
		found := false
		for _, num := range nums {
			if val == num {
				found = true
				break
			}
		}
		if !found {
			t.Errorf("Result contains invalid element %d", val)
		}
	}
}

// Test with k equals total unique elements
func TestTopKFrequent_KEqualsUniqueCount(t *testing.T) {
	nums := []int{1, 1, 2, 2, 3, 3}
	k := 3
	expected := []int{1, 2, 3}

	result := topKFrequent(nums, k)

	if !containsSameElements(result, expected) {
		t.Errorf("Expected %v (in any order), got %v", expected, result)
	}
}

// Test with negative numbers
func TestTopKFrequent_NegativeNumbers(t *testing.T) {
	nums := []int{-1, -1, -1, -2, -2, -3}
	k := 2
	expected := []int{-1, -2}

	result := topKFrequent(nums, k)

	if !containsSameElements(result, expected) {
		t.Errorf("Expected %v (in any order), got %v", expected, result)
	}
}

// Test with mixed positive and negative numbers
func TestTopKFrequent_MixedNumbers(t *testing.T) {
	nums := []int{-1, -1, 2, 2, 2, 3}
	k := 2
	expected := []int{2, -1}

	result := topKFrequent(nums, k)

	if !containsSameElements(result, expected) {
		t.Errorf("Expected %v (in any order), got %v", expected, result)
	}
}

// Test with k=1 and multiple elements
func TestTopKFrequent_SingleMostFrequent(t *testing.T) {
	nums := []int{5, 5, 5, 3, 3, 1}
	k := 1
	expected := []int{5}

	result := topKFrequent(nums, k)

	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

// Test with all same elements
func TestTopKFrequent_AllSameElements(t *testing.T) {
	nums := []int{7, 7, 7, 7, 7}
	k := 1
	expected := []int{7}

	result := topKFrequent(nums, k)

	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

// Test with larger dataset
func TestTopKFrequent_LargerDataset(t *testing.T) {
	nums := []int{1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 5, 5, 5, 5}
	k := 3
	expected := []int{5, 1, 2} // 5 appears 5 times, 1 appears 4 times, 2 appears 3 times

	result := topKFrequent(nums, k)

	if !containsSameElements(result, expected) {
		t.Errorf("Expected %v (in any order), got %v", expected, result)
	}
}

// Test boundary: minimum array size
func TestTopKFrequent_MinimumArraySize(t *testing.T) {
	nums := []int{100}
	k := 1
	expected := []int{100}

	result := topKFrequent(nums, k)

	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

// Test with zeros
func TestTopKFrequent_WithZeros(t *testing.T) {
	nums := []int{0, 0, 0, 1, 1, 2}
	k := 2
	expected := []int{0, 1}

	result := topKFrequent(nums, k)

	if !containsSameElements(result, expected) {
		t.Errorf("Expected %v (in any order), got %v", expected, result)
	}
}

// Test different frequencies with clear ordering
func TestTopKFrequent_ClearFrequencyOrder(t *testing.T) {
	nums := []int{4, 4, 4, 4, 3, 3, 3, 2, 2, 1}
	k := 3
	expected := []int{4, 3, 2}

	result := topKFrequent(nums, k)

	if !containsSameElements(result, expected) {
		t.Errorf("Expected %v (in any order), got %v", expected, result)
	}
}
