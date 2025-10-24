package mergeksortedlists

import (
	"reflect"
	"testing"
)

func buildList(nums []int) *ListNode {
	if len(nums) == 0 {
		return nil
	}
	head := &ListNode{Val: nums[0]}
	cur := head
	for _, v := range nums[1:] {
		cur.Next = &ListNode{Val: v}
		cur = cur.Next
	}
	return head
}

func listToSlice(head *ListNode) []int {
	var res []int
	for head != nil {
		res = append(res, head.Val)
		head = head.Next
	}
	return res
}

func TestMergeKLists(t *testing.T) {
	tests := []struct {
		name   string
		input  [][]int
		expect []int
	}{
		{
			name:   "example1",
			input:  [][]int{{1, 4, 5}, {1, 3, 4}, {2, 6}},
			expect: []int{1, 1, 2, 3, 4, 4, 5, 6},
		},
		{
			name:   "single list",
			input:  [][]int{{1, 2, 3}},
			expect: []int{1, 2, 3},
		},
		{
			name:   "lists with duplicates",
			input:  [][]int{{1, 1, 2}, {1, 3}, {2, 2}},
			expect: []int{1, 1, 1, 2, 2, 2, 3},
		},
		{
			name:   "different lengths",
			input:  [][]int{{1}, {2, 3, 4}, {5, 6}},
			expect: []int{1, 2, 3, 4, 5, 6},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			var lists []*ListNode
			for _, arr := range tt.input {
				lists = append(lists, buildList(arr))
			}

			out := mergeKLists(lists)
			got := listToSlice(out)

			if !reflect.DeepEqual(got, tt.expect) {
				t.Fatalf("expected %v, got %v", tt.expect, got)
			}
		})
	}
}

func TestMerge(t *testing.T) {
	tests := []struct {
		name   string
		list1  []int
		list2  []int
		expect []int
	}{
		{
			name:   "both non-empty",
			list1:  []int{1, 3, 5},
			list2:  []int{2, 4, 6},
			expect: []int{1, 2, 3, 4, 5, 6},
		},
		{
			name:   "first list empty",
			list1:  []int{},
			list2:  []int{1, 2, 3},
			expect: []int{1, 2, 3},
		},
		{
			name:   "second list empty",
			list1:  []int{1, 2, 3},
			list2:  []int{},
			expect: []int{1, 2, 3},
		},
		{
			name:   "lists with duplicates",
			list1:  []int{1, 2, 2},
			list2:  []int{1, 2, 3},
			expect: []int{1, 1, 2, 2, 2, 3},
		},
		{
			name:   "different lengths",
			list1:  []int{1, 4, 7, 10},
			list2:  []int{2, 3},
			expect: []int{1, 2, 3, 4, 7, 10},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			l1 := buildList(tt.list1)
			l2 := buildList(tt.list2)

			out := merge(l1, l2)
			got := listToSlice(out)

			if !reflect.DeepEqual(got, tt.expect) {
				t.Fatalf("expected: %v, got: %v", tt.expect, got)
			}
		})
	}
}
