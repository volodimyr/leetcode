package sumii

import "testing"

func TestFourSumCount(t *testing.T) {
	tests := []struct {
		name  string
		nums1 []int
		nums2 []int
		nums3 []int
		nums4 []int
		want  int
	}{
		{
			name:  "Example 1: Two tuples",
			nums1: []int{1, 2},
			nums2: []int{-2, -1},
			nums3: []int{-1, 2},
			nums4: []int{0, 2},
			want:  2,
		},
		{
			name:  "Example 2: Single element arrays",
			nums1: []int{0},
			nums2: []int{0},
			nums3: []int{0},
			nums4: []int{0},
			want:  1,
		},
		{
			name:  "No valid tuples",
			nums1: []int{1, 2},
			nums2: []int{3, 4},
			nums3: []int{5, 6},
			nums4: []int{7, 8},
			want:  0,
		},
		{
			name:  "All zeros",
			nums1: []int{0, 0, 0},
			nums2: []int{0, 0, 0},
			nums3: []int{0, 0, 0},
			nums4: []int{0, 0, 0},
			want:  81, // 3^4 = 81 combinations
		},
		{
			name:  "Negative and positive numbers",
			nums1: []int{-1, -1},
			nums2: []int{-1, 1},
			nums3: []int{-1, 1},
			nums4: []int{1, -1},
			want:  6,
		},
		{
			name:  "Mixed values with multiple solutions",
			nums1: []int{1, 1, 1},
			nums2: []int{-1, -1, -1},
			nums3: []int{0, 0, 0},
			nums4: []int{0, 0, 0},
			want:  81, // Each combination of 1 + (-1) + 0 + 0 = 0
		},
		{
			name:  "One element that sums to zero",
			nums1: []int{5},
			nums2: []int{-3},
			nums3: []int{-2},
			nums4: []int{0},
			want:  1,
		},
		{
			name:  "Multiple duplicates leading to same sum",
			nums1: []int{1, 1, 1, 1},
			nums2: []int{2, 2, 2, 2},
			nums3: []int{-1, -1, -1, -1},
			nums4: []int{-2, -2, -2, -2},
			want:  256, // 4^4 = 256 (each 1+2-1-2=0)
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := fourSumCount(tt.nums1, tt.nums2, tt.nums3, tt.nums4)
			if got != tt.want {
				t.Errorf("fourSumCount() = %v, want %v", got, tt.want)
			}
		})
	}
}
