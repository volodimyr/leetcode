package addtwonumbers

import (
	"reflect"
	"testing"
)

func TestAddTwoNumbers(t *testing.T) {
	tests := []struct {
		name string
		l1   *ListNode
		l2   *ListNode
		want *ListNode
	}{
		{
			name: "example 1: 342 + 465 = 807",
			l1:   createList([]int{2, 4, 3}),
			l2:   createList([]int{5, 6, 4}),
			want: createList([]int{7, 0, 8}),
		},
		{
			name: "example 2: 0 + 0 = 0",
			l1:   createList([]int{0}),
			l2:   createList([]int{0}),
			want: createList([]int{0}),
		},
		{
			name: "example 3: 9999999 + 9999 = 10009998",
			l1:   createList([]int{9, 9, 9, 9, 9, 9, 9}),
			l2:   createList([]int{9, 9, 9, 9}),
			want: createList([]int{8, 9, 9, 9, 0, 0, 0, 1}),
		},
		{
			name: "different lengths: 123 + 4567 = 4690",
			l1:   createList([]int{3, 2, 1}),
			l2:   createList([]int{7, 6, 5, 4}),
			want: createList([]int{0, 9, 6, 4}),
		},
		{
			name: "carry propagation: 99 + 1 = 100",
			l1:   createList([]int{9, 9}),
			l2:   createList([]int{1}),
			want: createList([]int{0, 0, 1}),
		},
		{
			name: "single digit with carry: 5 + 5 = 10",
			l1:   createList([]int{5}),
			l2:   createList([]int{5}),
			want: createList([]int{0, 1}),
		},
		{
			name: "no carry: 1 + 2 = 3",
			l1:   createList([]int{1}),
			l2:   createList([]int{2}),
			want: createList([]int{3}),
		},
		{
			name: "l1 longer: 12345 + 67 = 12412",
			l1:   createList([]int{5, 4, 3, 2, 1}),
			l2:   createList([]int{7, 6}),
			want: createList([]int{2, 1, 4, 2, 1}),
		},
		{
			name: "l2 longer: 12 + 3456 = 3468",
			l1:   createList([]int{2, 1}),
			l2:   createList([]int{6, 5, 4, 3}),
			want: createList([]int{8, 6, 4, 3}),
		},
		{
			name: "multiple carries: 999 + 999 = 1998",
			l1:   createList([]int{9, 9, 9}),
			l2:   createList([]int{9, 9, 9}),
			want: createList([]int{8, 9, 9, 1}),
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := addTwoNumbers(tt.l1, tt.l2)
			if !equalLists(got, tt.want) {
				t.Errorf("addTwoNumbers() = %v, want %v", listToSlice(got), listToSlice(tt.want))
			}
		})
	}
}

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
	var result []int
	current := head
	for current != nil {
		result = append(result, current.Val)
		current = current.Next
	}
	return result
}

func equalLists(l1, l2 *ListNode) bool {
	return reflect.DeepEqual(listToSlice(l1), listToSlice(l2))
}
