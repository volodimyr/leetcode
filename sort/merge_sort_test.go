package sort

import (
	"reflect"
	"testing"
)

func TestMergeSort_Example1(t *testing.T) {
	pairs := []Pair{
		{5, "apple"},
		{2, "banana"},
		{9, "cherry"},
		{1, "date"},
		{9, "elderberry"},
	}
	expected := []Pair{
		{1, "date"},
		{2, "banana"},
		{5, "apple"},
		{9, "cherry"},
		{9, "elderberry"},
	}
	result := mergeSort(pairs)
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestMergeSort_Example2(t *testing.T) {
	pairs := []Pair{
		{3, "cat"},
		{2, "dog"},
		{3, "bird"},
	}
	expected := []Pair{
		{2, "dog"},
		{3, "cat"},
		{3, "bird"},
	}
	result := mergeSort(pairs)
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestMergeSort_Empty(t *testing.T) {
	pairs := []Pair{}
	expected := []Pair{}
	result := mergeSort(pairs)
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestMergeSort_SingleElement(t *testing.T) {
	pairs := []Pair{{1, "single"}}
	expected := []Pair{{1, "single"}}
	result := mergeSort(pairs)
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestMergeSort_TwoElements(t *testing.T) {
	pairs := []Pair{
		{2, "second"},
		{1, "first"},
	}
	expected := []Pair{
		{1, "first"},
		{2, "second"},
	}
	result := mergeSort(pairs)
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestMergeSort_AlreadySorted(t *testing.T) {
	pairs := []Pair{
		{1, "one"},
		{2, "two"},
		{3, "three"},
		{4, "four"},
	}
	expected := []Pair{
		{1, "one"},
		{2, "two"},
		{3, "three"},
		{4, "four"},
	}
	result := mergeSort(pairs)
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestMergeSort_ReverseSorted(t *testing.T) {
	pairs := []Pair{
		{5, "five"},
		{4, "four"},
		{3, "three"},
		{2, "two"},
		{1, "one"},
	}
	expected := []Pair{
		{1, "one"},
		{2, "two"},
		{3, "three"},
		{4, "four"},
		{5, "five"},
	}
	result := mergeSort(pairs)
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestMergeSort_AllSameKeys(t *testing.T) {
	pairs := []Pair{
		{5, "first"},
		{5, "second"},
		{5, "third"},
		{5, "fourth"},
	}
	expected := []Pair{
		{5, "first"},
		{5, "second"},
		{5, "third"},
		{5, "fourth"},
	}
	result := mergeSort(pairs)
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestMergeSort_StabilityCheck(t *testing.T) {
	pairs := []Pair{
		{2, "a"},
		{1, "x"},
		{2, "b"},
		{1, "y"},
		{2, "c"},
	}
	expected := []Pair{
		{1, "x"},
		{1, "y"},
		{2, "a"},
		{2, "b"},
		{2, "c"},
	}
	result := mergeSort(pairs)
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestMergeSort_NegativeKeys(t *testing.T) {
	pairs := []Pair{
		{-1, "negative"},
		{0, "zero"},
		{-5, "very negative"},
		{3, "positive"},
	}
	expected := []Pair{
		{-5, "very negative"},
		{-1, "negative"},
		{0, "zero"},
		{3, "positive"},
	}
	result := mergeSort(pairs)
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestMergeSort_ManyDuplicates(t *testing.T) {
	pairs := []Pair{
		{3, "first"},
		{1, "a"},
		{3, "second"},
		{2, "b"},
		{3, "third"},
		{1, "c"},
	}
	expected := []Pair{
		{1, "a"},
		{1, "c"},
		{2, "b"},
		{3, "first"},
		{3, "second"},
		{3, "third"},
	}
	result := mergeSort(pairs)
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestMergeSort_LargeRange(t *testing.T) {
	pairs := []Pair{
		{100, "hundred"},
		{-100, "negative hundred"},
		{0, "zero"},
		{50, "fifty"},
		{-50, "negative fifty"},
	}
	expected := []Pair{
		{-100, "negative hundred"},
		{-50, "negative fifty"},
		{0, "zero"},
		{50, "fifty"},
		{100, "hundred"},
	}
	result := mergeSort(pairs)
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestMergeSort_ThreeElementsWithDuplicates(t *testing.T) {
	pairs := []Pair{
		{2, "x"},
		{1, "y"},
		{2, "z"},
	}
	expected := []Pair{
		{1, "y"},
		{2, "x"},
		{2, "z"},
	}
	result := mergeSort(pairs)
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestMergeSort_AlternatingKeys(t *testing.T) {
	pairs := []Pair{
		{1, "a"},
		{2, "b"},
		{1, "c"},
		{2, "d"},
		{1, "e"},
	}
	expected := []Pair{
		{1, "a"},
		{1, "c"},
		{1, "e"},
		{2, "b"},
		{2, "d"},
	}
	result := mergeSort(pairs)
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestMergeSort_SevenElements(t *testing.T) {
	pairs := []Pair{
		{7, "g"},
		{3, "c"},
		{9, "i"},
		{1, "a"},
		{5, "e"},
		{2, "b"},
		{8, "h"},
	}
	expected := []Pair{
		{1, "a"},
		{2, "b"},
		{3, "c"},
		{5, "e"},
		{7, "g"},
		{8, "h"},
		{9, "i"},
	}
	result := mergeSort(pairs)
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}
