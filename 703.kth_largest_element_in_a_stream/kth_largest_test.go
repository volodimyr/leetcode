package kthlargestelementinastream

import (
	"testing"
)

func TestExample1(t *testing.T) {
	kth := Constructor(3, []int{4, 5, 8, 2})
	tests := []struct {
		val      int
		expected int
	}{
		{3, 4},
		{5, 5},
		{10, 5},
		{9, 8},
		{4, 8},
	}

	for i, tt := range tests {
		got := kth.Add(tt.val)
		if got != tt.expected {
			t.Errorf("Example1[%d]: Add(%d) = %d; expected %d", i, tt.val, got, tt.expected)
		}
	}
}

func TestExample2(t *testing.T) {
	kth := Constructor(4, []int{7, 7, 7, 7, 8, 3})

	tests := []struct {
		val      int
		expected int
	}{
		{2, 7},
		{10, 7},
		{9, 7},
		{9, 8},
	}

	for i, tt := range tests {
		got := kth.Add(tt.val)
		if got != tt.expected {
			t.Errorf("Example2[%d]: Add(%d) = %d; expected %d", i, tt.val, got, tt.expected)
		}
	}
}

func TestSingleElement(t *testing.T) {
	kth := Constructor(1, []int{5})

	tests := []struct {
		val      int
		expected int
	}{
		{2, 5},
		{10, 10},
		{1, 10},
	}

	for i, tt := range tests {
		got := kth.Add(tt.val)
		if got != tt.expected {
			t.Errorf("SingleElement[%d]: Add(%d) = %d; expected %d", i, tt.val, got, tt.expected)
		}
	}
}

func TestEmptyInit(t *testing.T) {
	kth := Constructor(2, []int{})

	tests := []struct {
		val      int
		expected int
	}{
		{3, 3},
		{5, 3},
		{10, 5},
		{9, 9},
	}

	for i, tt := range tests {
		got := kth.Add(tt.val)
		if got != tt.expected {
			t.Errorf("EmptyInit[%d]: Add(%d) = %d; expected %d", i, tt.val, got, tt.expected)
		}
	}
}
