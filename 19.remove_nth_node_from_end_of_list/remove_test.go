package removenthnodefromendoflist

import (
	"reflect"
	"testing"
)

func TestRemoveNthFromEnd(t *testing.T) {
	tests := []struct {
		name string
		head *ListNode
		n    int
		want *ListNode
	}{
		{
			name: "remove 2nd from end in 5-node list",
			head: createList([]int{1, 2, 3, 4, 5}),
			n:    2,
			want: createList([]int{1, 2, 3, 5}),
		},
		{
			name: "remove only node",
			head: createList([]int{1}),
			n:    1,
			want: nil,
		},
		{
			name: "remove last node in 2-node list",
			head: createList([]int{1, 2}),
			n:    1,
			want: createList([]int{1}),
		},
		{
			name: "remove first node in 2-node list",
			head: createList([]int{1, 2}),
			n:    2,
			want: createList([]int{2}),
		},
		{
			name: "remove last node in long list",
			head: createList([]int{1, 2, 3, 4, 5, 6}),
			n:    1,
			want: createList([]int{1, 2, 3, 4, 5}),
		},
		{
			name: "remove first node in long list",
			head: createList([]int{1, 2, 3, 4, 5}),
			n:    5,
			want: createList([]int{2, 3, 4, 5}),
		},
		{
			name: "remove middle node 2",
			head: createList([]int{1, 2, 3, 4, 5}),
			n:    4,
			want: createList([]int{1, 3, 4, 5}),
		},
		{
			name: "remove middle node 3",
			head: createList([]int{1, 2, 3, 4, 5}),
			n:    3,
			want: createList([]int{1, 2, 4, 5}),
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := removeNthFromEnd(tt.head, tt.n)
			if !equalLists(got, tt.want) {
				t.Errorf("removeNthFromEnd() = %v, want %v", listToSlice(got), listToSlice(tt.want))
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
	for head != nil {
		result = append(result, head.Val)
		head = head.Next
	}
	return result
}

func equalLists(l1, l2 *ListNode) bool {
	return reflect.DeepEqual(listToSlice(l1), listToSlice(l2))
}
