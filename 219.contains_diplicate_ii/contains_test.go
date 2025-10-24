package containsdiplicateii

import "testing"

func TestContainsNearbyDuplicate(t *testing.T) {
	tests := []struct {
		name string
		nums []int
		k    int
		want bool
	}{
		{
			name: "Example 1",
			nums: []int{1, 2, 3, 1},
			k:    3,
			want: true,
		},
		{
			name: "Example 2",
			nums: []int{1, 0, 1, 1},
			k:    1,
			want: true,
		},
		{
			name: "Example 3",
			nums: []int{1, 2, 3, 1, 2, 3},
			k:    2,
			want: false,
		},
		{
			name: "No duplicates",
			nums: []int{1, 2, 3, 4, 5},
			k:    3,
			want: false,
		},
		{
			name: "Duplicate but too far apart",
			nums: []int{1, 2, 1},
			k:    1,
			want: false,
		},
		{
			name: "Single element",
			nums: []int{99},
			k:    10,
			want: false,
		},
		{
			name: "k is zero",
			nums: []int{1, 1},
			k:    0,
			want: false,
		},
		{
			name: "Large k covers whole array",
			nums: []int{5, 6, 7, 5},
			k:    10,
			want: true,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := containsNearbyDuplicate(tt.nums, tt.k)
			if got != tt.want {
				t.Errorf("containsNearbyDuplicate(%v, %d) = %v; want %v",
					tt.nums, tt.k, got, tt.want)
			}
		})
	}
}
