package reversenodeinkgroup

import (
	"reflect"
	"testing"
)

// Helper: convert slice to linked list
func sliceToList(nums []int) *ListNode {
	dummy := &ListNode{}
	cur := dummy
	for _, n := range nums {
		cur.Next = &ListNode{Val: n}
		cur = cur.Next
	}
	return dummy.Next
}

// Helper: convert linked list to slice
func listToSlice(head *ListNode) []int {
	var result []int
	for head != nil {
		result = append(result, head.Val)
		head = head.Next
	}
	return result
}

func TestReverseKGroup(t *testing.T) {
	tests := []struct {
		input []int
		k     int
		want  []int
	}{
		// Full reversal
		{[]int{1, 2, 3, 4, 5, 6}, 3, []int{3, 2, 1, 6, 5, 4}},
		// Last group less than k
		{[]int{1, 2, 3, 4, 5}, 3, []int{3, 2, 1, 4, 5}},
		// k = 1, list unchanged
		{[]int{1, 2, 3, 4}, 1, []int{1, 2, 3, 4}},
		// k = list length, whole list reversed
		{[]int{1, 2, 3, 4}, 4, []int{4, 3, 2, 1}},
		// k > list length, list unchanged
		{[]int{1, 2, 3}, 5, []int{1, 2, 3}},
		// Single element
		{[]int{1}, 2, []int{1}},
	}

	for _, tt := range tests {
		t.Run("", func(t *testing.T) {
			head := sliceToList(tt.input)
			got := reverseKGroup(head, tt.k)
			gotSlice := listToSlice(got)
			if !reflect.DeepEqual(gotSlice, tt.want) {
				t.Errorf("reverseKGroup(%v, %d) = %v; want %v", tt.input, tt.k, gotSlice, tt.want)
			}
		})
	}
}
