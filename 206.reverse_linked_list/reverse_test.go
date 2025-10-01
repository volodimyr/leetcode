package reverselinkedlist

import (
	"reflect"
	"testing"
)

func TestReverseListEmpty(t *testing.T) {
	head := reverseList(nil)
	if head != nil {
		t.Error("Reversing empty list should return nil")
	}
}

func TestReverseListSingleNode(t *testing.T) {
	head := createList([]int{1})
	reversed := reverseList(head)

	want := []int{1}
	got := reversed.GetValues()

	if !reflect.DeepEqual(got, want) {
		t.Errorf("reverseList([1]) = %v, want %v", got, want)
	}
}

func TestReverseListTwoNodes(t *testing.T) {
	head := createList([]int{1, 2})
	reversed := reverseList(head)

	want := []int{2, 1}
	got := reversed.GetValues()

	if !reflect.DeepEqual(got, want) {
		t.Errorf("reverseList([1, 2]) = %v, want %v", got, want)
	}
}

func TestReverseListMultipleNodes(t *testing.T) {
	tests := []struct {
		name  string
		input []int
		want  []int
	}{
		{
			name:  "three nodes",
			input: []int{1, 2, 3},
			want:  []int{3, 2, 1},
		},
		{
			name:  "five nodes",
			input: []int{1, 2, 3, 4, 5},
			want:  []int{5, 4, 3, 2, 1},
		},
		{
			name:  "four nodes",
			input: []int{1, 2, 3, 4},
			want:  []int{4, 3, 2, 1},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			head := createList(tt.input)
			reversed := reverseList(head)
			got := reversed.GetValues()

			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("reverseList(%v) = %v, want %v", tt.input, got, tt.want)
			}
		})
	}
}

func TestReverseListNegativeValues(t *testing.T) {
	head := createList([]int{-1, -2, -3})
	reversed := reverseList(head)

	want := []int{-3, -2, -1}
	got := reversed.GetValues()

	if !reflect.DeepEqual(got, want) {
		t.Errorf("reverseList([-1, -2, -3]) = %v, want %v", got, want)
	}
}

func TestReverseListMixedValues(t *testing.T) {
	head := createList([]int{0, -5, 10, -3, 7})
	reversed := reverseList(head)

	want := []int{7, -3, 10, -5, 0}
	got := reversed.GetValues()

	if !reflect.DeepEqual(got, want) {
		t.Errorf("reverseList([0, -5, 10, -3, 7]) = %v, want %v", got, want)
	}
}

func TestReverseListDuplicateValues(t *testing.T) {
	head := createList([]int{1, 2, 2, 1})
	reversed := reverseList(head)

	want := []int{1, 2, 2, 1}
	got := reversed.GetValues()

	if !reflect.DeepEqual(got, want) {
		t.Errorf("reverseList([1, 2, 2, 1]) = %v, want %v", got, want)
	}
}

func TestReverseListAllSameValues(t *testing.T) {
	head := createList([]int{5, 5, 5, 5})
	reversed := reverseList(head)

	want := []int{5, 5, 5, 5}
	got := reversed.GetValues()

	if !reflect.DeepEqual(got, want) {
		t.Errorf("reverseList([5, 5, 5, 5]) = %v, want %v", got, want)
	}
}

func TestReverseListTwice(t *testing.T) {
	// Reversing twice should give original list
	original := []int{1, 2, 3, 4}
	head := createList(original)

	reversed := reverseList(head)
	doubleReversed := reverseList(reversed)

	got := doubleReversed.GetValues()

	if !reflect.DeepEqual(got, original) {
		t.Errorf("Reversing twice: got %v, want %v", got, original)
	}
}

func TestReverseListPreservesStructure(t *testing.T) {
	// Verify that reversal maintains proper linked structure
	head := createList([]int{1, 2, 3})
	reversed := reverseList(head)

	// Check each node manually
	if reversed.Val != 3 {
		t.Errorf("First node value = %d, want 3", reversed.Val)
	}
	if reversed.Next.Val != 2 {
		t.Errorf("Second node value = %d, want 2", reversed.Next.Val)
	}
	if reversed.Next.Next.Val != 1 {
		t.Errorf("Third node value = %d, want 1", reversed.Next.Next.Val)
	}
	if reversed.Next.Next.Next != nil {
		t.Error("Last node should point to nil")
	}
}

func TestReverseListLargeList(t *testing.T) {
	// Test with a larger list
	size := 100
	input := make([]int, size)
	want := make([]int, size)

	for i := 0; i < size; i++ {
		input[i] = i
		want[size-1-i] = i
	}

	head := createList(input)
	reversed := reverseList(head)
	got := reversed.GetValues()

	if !reflect.DeepEqual(got, want) {
		t.Errorf("Large list reversal failed")
	}
}

func createList(values []int) *ListNode {
	if len(values) == 0 {
		return nil
	}

	head := &ListNode{Val: values[0]}
	curr := head
	for i := 1; i < len(values); i++ {
		curr.Next = &ListNode{Val: values[i]}
		curr = curr.Next
	}

	return head
}
