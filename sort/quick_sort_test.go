package sort

import (
	"testing"
)

func TestQuickSort_Example1(t *testing.T) {
	pairs := []Pair{
		{3, "cat"},
		{2, "dog"},
		{3, "bird"},
	}

	result := QuickSort(pairs)

	if len(result) != 3 {
		t.Errorf("Expected length 3, got %d", len(result))
	}

	// Verify sorting by key
	if result[0].Key != 2 || result[0].Value != "dog" {
		t.Errorf("Expected (2, dog), got (%d, %s)", result[0].Key, result[0].Value)
	}
	if result[1].Key != 3 {
		t.Errorf("Expected key 3 at index 1, got %d", result[1].Key)
	}
	if result[2].Key != 3 {
		t.Errorf("Expected key 3 at index 2, got %d", result[2].Key)
	}
}

func TestQuickSort_Example2(t *testing.T) {
	pairs := []Pair{
		{5, "apple"},
		{9, "banana"},
		{9, "cherry"},
		{1, "date"},
		{9, "elderberry"},
	}

	result := QuickSort(pairs)

	if len(result) != 5 {
		t.Errorf("Expected length 5, got %d", len(result))
	}

	// Verify sorting by key
	expectedKeys := []int{1, 5, 9, 9, 9}
	for i, expectedKey := range expectedKeys {
		if result[i].Key != expectedKey {
			t.Errorf("At index %d: expected key %d, got %d", i, expectedKey, result[i].Key)
		}
	}

	// Verify first two elements
	if result[0].Key != 1 || result[0].Value != "date" {
		t.Errorf("Expected (1, date), got (%d, %s)", result[0].Key, result[0].Value)
	}
	if result[1].Key != 5 || result[1].Value != "apple" {
		t.Errorf("Expected (5, apple), got (%d, %s)", result[1].Key, result[1].Value)
	}
}

func TestQuickSort_EmptyArray(t *testing.T) {
	pairs := []Pair{}

	result := QuickSort(pairs)

	if len(result) != 0 {
		t.Errorf("Expected empty array, got length %d", len(result))
	}
}

func TestQuickSort_SingleElement(t *testing.T) {
	pairs := []Pair{{5, "single"}}

	result := QuickSort(pairs)

	if len(result) != 1 {
		t.Errorf("Expected length 1, got %d", len(result))
	}
	if result[0].Key != 5 || result[0].Value != "single" {
		t.Errorf("Expected (5, single), got (%d, %s)", result[0].Key, result[0].Value)
	}
}

func TestQuickSort_TwoElements(t *testing.T) {
	pairs := []Pair{
		{10, "second"},
		{5, "first"},
	}

	result := QuickSort(pairs)

	if len(result) != 2 {
		t.Errorf("Expected length 2, got %d", len(result))
	}
	if result[0].Key != 5 || result[0].Value != "first" {
		t.Errorf("Expected (5, first), got (%d, %s)", result[0].Key, result[0].Value)
	}
	if result[1].Key != 10 || result[1].Value != "second" {
		t.Errorf("Expected (10, second), got (%d, %s)", result[1].Key, result[1].Value)
	}
}

func TestQuickSort_AlreadySorted(t *testing.T) {
	pairs := []Pair{
		{1, "a"},
		{2, "b"},
		{3, "c"},
		{4, "d"},
		{5, "e"},
	}

	result := QuickSort(pairs)

	expectedKeys := []int{1, 2, 3, 4, 5}
	for i, expectedKey := range expectedKeys {
		if result[i].Key != expectedKey {
			t.Errorf("At index %d: expected key %d, got %d", i, expectedKey, result[i].Key)
		}
	}
}

func TestQuickSort_ReverseSorted(t *testing.T) {
	pairs := []Pair{
		{5, "e"},
		{4, "d"},
		{3, "c"},
		{2, "b"},
		{1, "a"},
	}

	result := QuickSort(pairs)

	expectedKeys := []int{1, 2, 3, 4, 5}
	for i, expectedKey := range expectedKeys {
		if result[i].Key != expectedKey {
			t.Errorf("At index %d: expected key %d, got %d", i, expectedKey, result[i].Key)
		}
	}
}

func TestQuickSort_AllSameKeys(t *testing.T) {
	pairs := []Pair{
		{7, "first"},
		{7, "second"},
		{7, "third"},
		{7, "fourth"},
	}

	result := QuickSort(pairs)

	if len(result) != 4 {
		t.Errorf("Expected length 4, got %d", len(result))
	}

	for i, pair := range result {
		if pair.Key != 7 {
			t.Errorf("At index %d: expected key 7, got %d", i, pair.Key)
		}
	}
}

func TestQuickSort_NegativeKeys(t *testing.T) {
	pairs := []Pair{
		{-5, "negative"},
		{0, "zero"},
		{5, "positive"},
		{-10, "more negative"},
	}

	result := QuickSort(pairs)

	expectedKeys := []int{-10, -5, 0, 5}
	for i, expectedKey := range expectedKeys {
		if result[i].Key != expectedKey {
			t.Errorf("At index %d: expected key %d, got %d", i, expectedKey, result[i].Key)
		}
	}
}

func TestQuickSort_LargerArray(t *testing.T) {
	pairs := []Pair{
		{15, "o"},
		{3, "c"},
		{9, "i"},
		{1, "a"},
		{12, "l"},
		{7, "g"},
		{5, "e"},
		{20, "t"},
		{2, "b"},
		{18, "r"},
	}

	result := QuickSort(pairs)

	// Verify that result is sorted by key
	for i := 0; i < len(result)-1; i++ {
		if result[i].Key > result[i+1].Key {
			t.Errorf("Array not sorted: at index %d, key %d > key %d at index %d",
				i, result[i].Key, result[i+1].Key, i+1)
		}
	}
}

func TestQuickSort_DuplicateKeysWithDifferentValues(t *testing.T) {
	pairs := []Pair{
		{5, "first5"},
		{3, "first3"},
		{5, "second5"},
		{3, "second3"},
		{1, "first1"},
	}

	result := QuickSort(pairs)

	expectedKeys := []int{1, 3, 3, 5, 5}
	for i, expectedKey := range expectedKeys {
		if result[i].Key != expectedKey {
			t.Errorf("At index %d: expected key %d, got %d", i, expectedKey, result[i].Key)
		}
	}

	// Verify first element
	if result[0].Key != 1 || result[0].Value != "first1" {
		t.Errorf("Expected (1, first1), got (%d, %s)", result[0].Key, result[0].Value)
	}
}

func TestQuickSort_VerifySortedOrder(t *testing.T) {
	pairs := []Pair{
		{42, "z"},
		{17, "y"},
		{8, "x"},
		{99, "w"},
		{3, "v"},
	}

	result := QuickSort(pairs)

	// General test: verify the array is sorted
	for i := 0; i < len(result)-1; i++ {
		if result[i].Key > result[i+1].Key {
			t.Errorf("Array not properly sorted at index %d: %d > %d",
				i, result[i].Key, result[i+1].Key)
		}
	}
}

func TestQuickSort_MixedPositiveNegativeZero(t *testing.T) {
	pairs := []Pair{
		{10, "ten"},
		{-3, "neg three"},
		{0, "zero"},
		{-15, "neg fifteen"},
		{7, "seven"},
		{-3, "neg three again"},
	}

	result := QuickSort(pairs)

	// Verify sorted order
	for i := 0; i < len(result)-1; i++ {
		if result[i].Key > result[i+1].Key {
			t.Errorf("Array not sorted at index %d: %d > %d",
				i, result[i].Key, result[i+1].Key)
		}
	}
}
