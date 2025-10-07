package sort

import (
	"reflect"
	"testing"
)

func TestInsertionEmptySlice(t *testing.T) {
	arr := []int{}
	result := insertion(arr)
	expected := []int{}
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestInsertionSingleElement(t *testing.T) {
	arr := []int{5}
	result := insertion(arr)
	expected := []int{5}
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestInsertionAlreadySorted(t *testing.T) {
	arr := []int{1, 2, 3, 4, 5}
	result := insertion(arr)
	expected := []int{1, 2, 3, 4, 5}
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestInsertionReverseSorted(t *testing.T) {
	arr := []int{5, 4, 3, 2, 1}
	result := insertion(arr)
	expected := []int{1, 2, 3, 4, 5}
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestInsertionRandomOrder(t *testing.T) {
	arr := []int{3, 1, 4, 1, 5, 9, 2, 6}
	result := insertion(arr)
	expected := []int{1, 1, 2, 3, 4, 5, 6, 9}
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestInsertionDuplicates(t *testing.T) {
	arr := []int{4, 2, 4, 2, 4}
	result := insertion(arr)
	expected := []int{2, 2, 4, 4, 4}
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestInsertionNegativeNumbers(t *testing.T) {
	arr := []int{-3, -1, -4, -1, -5}
	result := insertion(arr)
	expected := []int{-5, -4, -3, -1, -1}
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestInsertionMixedNumbers(t *testing.T) {
	arr := []int{-2, 0, 3, -5, 1}
	result := insertion(arr)
	expected := []int{-5, -2, 0, 1, 3}
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestInsertionTwoElements(t *testing.T) {
	arr := []int{2, 1}
	result := insertion(arr)
	expected := []int{1, 2}
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}
