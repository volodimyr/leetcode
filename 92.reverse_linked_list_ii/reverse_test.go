package reverselinkedlistii

import (
	"reflect"
	"testing"
)

func createList(vals []int) *ListNode {
	if len(vals) == 0 {
		return nil
	}
	head := &ListNode{Val: vals[0]}
	current := head
	for i := 1; i < len(vals); i++ {
		current.Next = &ListNode{Val: vals[i]}
		current = current.Next
	}
	return head
}

func listToSlice(head *ListNode) []int {
	result := []int{}
	current := head
	for current != nil {
		result = append(result, current.Val)
		current = current.Next
	}
	return result
}

func TestReverseBetween(t *testing.T) {
	tests := []struct {
		name  string
		head  []int
		left  int
		right int
		want  []int
	}{
		{
			name:  "reverse middle portion",
			head:  []int{1, 2, 3, 4, 5},
			left:  2,
			right: 4,
			want:  []int{1, 4, 3, 2, 5},
		},
		{
			name:  "single node",
			head:  []int{5},
			left:  1,
			right: 1,
			want:  []int{5},
		},
		{
			name:  "reverse from beginning",
			head:  []int{1, 2, 3, 4, 5},
			left:  1,
			right: 3,
			want:  []int{3, 2, 1, 4, 5},
		},
		{
			name:  "reverse to end",
			head:  []int{1, 2, 3, 4, 5},
			left:  3,
			right: 5,
			want:  []int{1, 2, 5, 4, 3},
		},
		{
			name:  "reverse entire list",
			head:  []int{1, 2, 3, 4, 5},
			left:  1,
			right: 5,
			want:  []int{5, 4, 3, 2, 1},
		},
		{
			name:  "two nodes reverse both",
			head:  []int{1, 2},
			left:  1,
			right: 2,
			want:  []int{2, 1},
		},
		{
			name:  "reverse two adjacent nodes in middle",
			head:  []int{1, 2, 3, 4, 5},
			left:  3,
			right: 4,
			want:  []int{1, 2, 4, 3, 5},
		},
		{
			name:  "left equals right at position 1",
			head:  []int{1, 2, 3},
			left:  1,
			right: 1,
			want:  []int{1, 2, 3},
		},
		{
			name:  "left equals right in middle",
			head:  []int{1, 2, 3},
			left:  2,
			right: 2,
			want:  []int{1, 2, 3},
		},
		{
			name:  "left equals right at end",
			head:  []int{1, 2, 3},
			left:  3,
			right: 3,
			want:  []int{1, 2, 3},
		},
		{
			name:  "three nodes reverse all",
			head:  []int{1, 2, 3},
			left:  1,
			right: 3,
			want:  []int{3, 2, 1},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			head := createList(tt.head)
			result := reverseBetween(head, tt.left, tt.right)
			got := listToSlice(result)
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("reverseBetween() = %v, want %v", got, tt.want)
			}
		})
	}
}
