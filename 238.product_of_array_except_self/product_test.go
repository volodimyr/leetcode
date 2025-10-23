package productofarrayexceptself

import (
	"reflect"
	"testing"
)

func TestProductExceptSelf(t *testing.T) {
	tests := []struct {
		name string
		nums []int
		want []int
	}{
		{
			name: "example 1 - basic positive numbers",
			nums: []int{1, 2, 3, 4},
			want: []int{24, 12, 8, 6},
		},
		{
			name: "example 2 - with zero in middle",
			nums: []int{-1, 1, 0, -3, 3},
			want: []int{0, 0, 9, 0, 0},
		},
		{
			name: "two elements",
			nums: []int{2, 3},
			want: []int{3, 2},
		},
		{
			name: "all ones",
			nums: []int{1, 1, 1, 1},
			want: []int{1, 1, 1, 1},
		},
		{
			name: "zero at start",
			nums: []int{0, 2, 3},
			want: []int{6, 0, 0},
		},
		{
			name: "zero at end",
			nums: []int{2, 3, 0},
			want: []int{0, 0, 6},
		},
		{
			name: "multiple zeros",
			nums: []int{0, 0, 2, 3},
			want: []int{0, 0, 0, 0},
		},
		{
			name: "negative numbers",
			nums: []int{-2, -3, -4},
			want: []int{12, 8, 6},
		},
		{
			name: "mixed positive and negative",
			nums: []int{2, -3, 4, -5},
			want: []int{60, -40, 30, -24},
		},
		{
			name: "single negative with positives",
			nums: []int{1, -2, 3, 4},
			want: []int{-24, 12, -8, -6},
		},
		{
			name: "larger array",
			nums: []int{1, 2, 3, 4, 5},
			want: []int{120, 60, 40, 30, 24},
		},
		{
			name: "array with one and zero",
			nums: []int{1, 0},
			want: []int{0, 1},
		},
		{
			name: "maximum negative value",
			nums: []int{-30, 2, 3},
			want: []int{6, -90, -60},
		},
		{
			name: "all negative ones",
			nums: []int{-1, -1, -1},
			want: []int{1, 1, 1},
		},
		{
			name: "even count of negatives",
			nums: []int{-1, -2, -3, -4},
			want: []int{-24, -12, -8, -6},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := productExceptSelf(tt.nums)
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("productExceptSelf(%v) = %v, want %v", tt.nums, got, tt.want)
			}
		})
	}
}

func TestProductExceptSelf_Properties(t *testing.T) {
	t.Run("output length equals input length", func(t *testing.T) {
		nums := []int{1, 2, 3, 4, 5}
		result := productExceptSelf(nums)
		if len(result) != len(nums) {
			t.Errorf("output length %d != input length %d", len(result), len(nums))
		}
	})

	t.Run("no mutation of input array", func(t *testing.T) {
		nums := []int{1, 2, 3, 4}
		original := make([]int, len(nums))
		copy(original, nums)
		productExceptSelf(nums)
		if !reflect.DeepEqual(nums, original) {
			t.Errorf("input array was mutated: got %v, want %v", nums, original)
		}
	})
}
