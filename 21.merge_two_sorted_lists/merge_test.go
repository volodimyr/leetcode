package mergetwosortedlists

import (
	"testing"
)

func TestMergeTwoLists(t *testing.T) {
	tests := []struct {
		name  string
		list1 []int
		list2 []int
		want  []int
	}{
		{
			name:  "example 1: both lists have multiple elements",
			list1: []int{1, 2, 4},
			list2: []int{1, 3, 4},
			want:  []int{1, 1, 2, 3, 4, 4},
		},
		{
			name:  "example 2: both lists are empty",
			list1: []int{},
			list2: []int{},
			want:  []int{},
		},
		{
			name:  "example 3: list1 is empty, list2 has one element",
			list1: []int{},
			list2: []int{0},
			want:  []int{0},
		},
		{
			name:  "list2 is empty, list1 has elements",
			list1: []int{1, 2, 3},
			list2: []int{},
			want:  []int{1, 2, 3},
		},
		{
			name:  "all elements in list1 are smaller than list2",
			list1: []int{1, 2, 3},
			list2: []int{4, 5, 6},
			want:  []int{1, 2, 3, 4, 5, 6},
		},
		{
			name:  "all elements in list2 are smaller than list1",
			list1: []int{4, 5, 6},
			list2: []int{1, 2, 3},
			want:  []int{1, 2, 3, 4, 5, 6},
		},
		{
			name:  "lists with single elements",
			list1: []int{1},
			list2: []int{2},
			want:  []int{1, 2},
		},
		{
			name:  "lists with single elements reversed",
			list1: []int{2},
			list2: []int{1},
			want:  []int{1, 2},
		},
		{
			name:  "interleaved elements",
			list1: []int{1, 3, 5, 7},
			list2: []int{2, 4, 6, 8},
			want:  []int{1, 2, 3, 4, 5, 6, 7, 8},
		},
		{
			name:  "duplicate values",
			list1: []int{1, 1, 1},
			list2: []int{1, 1, 1},
			want:  []int{1, 1, 1, 1, 1, 1},
		},
		{
			name:  "different lengths",
			list1: []int{1, 2},
			list2: []int{1, 3, 4, 5},
			want:  []int{1, 1, 2, 3, 4, 5},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			list1 := buildList(tt.list1)
			list2 := buildList(tt.list2)
			got := mergeTwoLists(list1, list2)
			gotSlice := listToSlice(got)

			if !equal(gotSlice, tt.want) {
				t.Errorf("mergeTwoLists() = %v, want %v", gotSlice, tt.want)
			}
		})
	}
}

func buildList(vals []int) *ListNode {
	if len(vals) == 0 {
		return nil
	}
	head := &ListNode{Val: vals[0]}
	curr := head
	for i := 1; i < len(vals); i++ {
		curr.Next = &ListNode{Val: vals[i]}
		curr = curr.Next
	}
	return head
}

func listToSlice(head *ListNode) []int {
	var result []int
	curr := head
	for curr != nil {
		result = append(result, curr.Val)
		curr = curr.Next
	}
	return result
}

func equal(a, b []int) bool {
	if len(a) != len(b) {
		return false
	}
	for i := range a {
		if a[i] != b[i] {
			return false
		}
	}
	return true
}
