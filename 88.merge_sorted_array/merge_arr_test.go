package mergesortedarray

import (
	"reflect"
	"testing"
)

func TestMergeBasicCases(t *testing.T) {
	tests := []struct {
		name   string
		nums1  []int
		m      int
		nums2  []int
		n      int
		expect []int
	}{
		{
			name:   "example 1 - merge equal sized arrays",
			nums1:  []int{1, 2, 3, 0, 0, 0},
			m:      3,
			nums2:  []int{2, 5, 6},
			n:      3,
			expect: []int{1, 2, 2, 3, 5, 6},
		},
		{
			name:   "example 2 - nums2 is empty",
			nums1:  []int{1},
			m:      1,
			nums2:  []int{},
			n:      0,
			expect: []int{1},
		},
		{
			name:   "example 3 - nums1 is empty",
			nums1:  []int{0},
			m:      0,
			nums2:  []int{1},
			n:      1,
			expect: []int{1},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			merge(tt.nums1, tt.m, tt.nums2, tt.n)
			if !reflect.DeepEqual(tt.nums1, tt.expect) {
				t.Errorf("merge() = %v, want %v", tt.nums1, tt.expect)
			}
		})
	}
}

func TestMergeEdgeCases(t *testing.T) {
	tests := []struct {
		name   string
		nums1  []int
		m      int
		nums2  []int
		n      int
		expect []int
	}{
		{
			name:   "all elements from nums2 come first",
			nums1:  []int{4, 5, 6, 0, 0, 0},
			m:      3,
			nums2:  []int{1, 2, 3},
			n:      3,
			expect: []int{1, 2, 3, 4, 5, 6},
		},
		{
			name:   "all elements from nums1 come first",
			nums1:  []int{1, 2, 3, 0, 0, 0},
			m:      3,
			nums2:  []int{4, 5, 6},
			n:      3,
			expect: []int{1, 2, 3, 4, 5, 6},
		},
		{
			name:   "single element in each array",
			nums1:  []int{1, 0},
			m:      1,
			nums2:  []int{2},
			n:      1,
			expect: []int{1, 2},
		},
		{
			name:   "single element nums2 into empty nums1",
			nums1:  []int{0},
			m:      0,
			nums2:  []int{1},
			n:      1,
			expect: []int{1},
		},
		{
			name:   "nums1 much larger than nums2",
			nums1:  []int{1, 2, 3, 4, 5, 0},
			m:      5,
			nums2:  []int{6},
			n:      1,
			expect: []int{1, 2, 3, 4, 5, 6},
		},
		{
			name:   "nums2 much larger than nums1",
			nums1:  []int{1, 0, 0, 0, 0, 0},
			m:      1,
			nums2:  []int{2, 3, 4, 5, 6},
			n:      5,
			expect: []int{1, 2, 3, 4, 5, 6},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			merge(tt.nums1, tt.m, tt.nums2, tt.n)
			if !reflect.DeepEqual(tt.nums1, tt.expect) {
				t.Errorf("merge() = %v, want %v", tt.nums1, tt.expect)
			}
		})
	}
}

func TestMergeDuplicates(t *testing.T) {
	tests := []struct {
		name   string
		nums1  []int
		m      int
		nums2  []int
		n      int
		expect []int
	}{
		{
			name:   "duplicate elements in both arrays",
			nums1:  []int{1, 1, 2, 0, 0, 0},
			m:      3,
			nums2:  []int{1, 2, 3},
			n:      3,
			expect: []int{1, 1, 1, 2, 2, 3},
		},
		{
			name:   "all same elements",
			nums1:  []int{1, 1, 1, 0, 0},
			m:      3,
			nums2:  []int{1, 1},
			n:      2,
			expect: []int{1, 1, 1, 1, 1},
		},
		{
			name:   "multiple duplicates interleaved",
			nums1:  []int{1, 3, 5, 0, 0, 0},
			m:      3,
			nums2:  []int{1, 3, 5},
			n:      3,
			expect: []int{1, 1, 3, 3, 5, 5},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			merge(tt.nums1, tt.m, tt.nums2, tt.n)
			if !reflect.DeepEqual(tt.nums1, tt.expect) {
				t.Errorf("merge() = %v, want %v", tt.nums1, tt.expect)
			}
		})
	}
}

func TestMergeNegativeNumbers(t *testing.T) {
	tests := []struct {
		name   string
		nums1  []int
		m      int
		nums2  []int
		n      int
		expect []int
	}{
		{
			name:   "negative and positive numbers",
			nums1:  []int{-3, 0, 3, 0, 0, 0},
			m:      3,
			nums2:  []int{-2, 1, 4},
			n:      3,
			expect: []int{-3, -2, 0, 1, 3, 4},
		},
		{
			name:   "all negative numbers",
			nums1:  []int{-5, -3, -1, 0, 0, 0},
			m:      3,
			nums2:  []int{-6, -4, -2},
			n:      3,
			expect: []int{-6, -5, -4, -3, -2, -1},
		},
		{
			name:   "negative in nums1, positive in nums2",
			nums1:  []int{-3, -2, -1, 0, 0, 0},
			m:      3,
			nums2:  []int{1, 2, 3},
			n:      3,
			expect: []int{-3, -2, -1, 1, 2, 3},
		},
		{
			name:   "positive in nums1, negative in nums2",
			nums1:  []int{1, 2, 3, 0, 0, 0},
			m:      3,
			nums2:  []int{-3, -2, -1},
			n:      3,
			expect: []int{-3, -2, -1, 1, 2, 3},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			merge(tt.nums1, tt.m, tt.nums2, tt.n)
			if !reflect.DeepEqual(tt.nums1, tt.expect) {
				t.Errorf("merge() = %v, want %v", tt.nums1, tt.expect)
			}
		})
	}
}

func TestMergeLargerArrays(t *testing.T) {
	tests := []struct {
		name   string
		nums1  []int
		m      int
		nums2  []int
		n      int
		expect []int
	}{
		{
			name:   "larger merged array",
			nums1:  []int{1, 3, 5, 7, 9, 0, 0, 0, 0, 0},
			m:      5,
			nums2:  []int{2, 4, 6, 8, 10},
			n:      5,
			expect: []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10},
		},
		{
			name:   "sequential numbers",
			nums1:  []int{1, 2, 3, 4, 0, 0, 0, 0},
			m:      4,
			nums2:  []int{5, 6, 7, 8},
			n:      4,
			expect: []int{1, 2, 3, 4, 5, 6, 7, 8},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			merge(tt.nums1, tt.m, tt.nums2, tt.n)
			if !reflect.DeepEqual(tt.nums1, tt.expect) {
				t.Errorf("merge() = %v, want %v", tt.nums1, tt.expect)
			}
		})
	}
}
