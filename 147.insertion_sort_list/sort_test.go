package insertionsortlist

import "testing"

func TestInsertionSortList_Example1(t *testing.T) {
	// Input: [4,2,1,3]
	head := &ListNode{Val: 4, Next: &ListNode{Val: 2, Next: &ListNode{Val: 1, Next: &ListNode{Val: 3}}}}
	expected := "1->2->3->4"

	result := insertionSortList(head)
	actual := result.String()

	if actual != expected {
		t.Errorf("Expected %s, but got %s", expected, actual)
	}
}

func TestInsertionSortList_Example2(t *testing.T) {
	// Input: [-1,5,3,4,0]
	head := &ListNode{Val: -1, Next: &ListNode{Val: 5, Next: &ListNode{Val: 3, Next: &ListNode{Val: 4, Next: &ListNode{Val: 0}}}}}
	expected := "-1->0->3->4->5"

	result := insertionSortList(head)
	actual := result.String()

	if actual != expected {
		t.Errorf("Expected %s, but got %s", expected, actual)
	}
}

func TestInsertionSortList_SingleElement(t *testing.T) {
	// Input: [1]
	head := &ListNode{Val: 1}
	expected := "1"

	result := insertionSortList(head)
	actual := result.String()

	if actual != expected {
		t.Errorf("Expected %s, but got %s", expected, actual)
	}
}

func TestInsertionSortList_EmptyList(t *testing.T) {
	// Input: nil
	var head *ListNode = nil

	result := insertionSortList(head)

	if result != nil {
		t.Errorf("Expected nil, but got %v", result)
	}
}

func TestInsertionSortList_AlreadySorted(t *testing.T) {
	// Input: [1,2,3,4,5]
	head := &ListNode{Val: 1, Next: &ListNode{Val: 2, Next: &ListNode{Val: 3, Next: &ListNode{Val: 4, Next: &ListNode{Val: 5}}}}}
	expected := "1->2->3->4->5"

	result := insertionSortList(head)
	actual := result.String()

	if actual != expected {
		t.Errorf("Expected %s, but got %s", expected, actual)
	}
}

func TestInsertionSortList_ReverseSorted(t *testing.T) {
	// Input: [5,4,3,2,1]
	head := &ListNode{Val: 5, Next: &ListNode{Val: 4, Next: &ListNode{Val: 3, Next: &ListNode{Val: 2, Next: &ListNode{Val: 1}}}}}
	expected := "1->2->3->4->5"

	result := insertionSortList(head)
	actual := result.String()

	if actual != expected {
		t.Errorf("Expected %s, but got %s", expected, actual)
	}
}

func TestInsertionSortList_TwoElements(t *testing.T) {
	// Input: [2,1]
	head := &ListNode{Val: 2, Next: &ListNode{Val: 1}}
	expected := "1->2"

	result := insertionSortList(head)
	actual := result.String()

	if actual != expected {
		t.Errorf("Expected %s, but got %s", expected, actual)
	}
}

func TestInsertionSortList_TwoElementsAlreadySorted(t *testing.T) {
	// Input: [1,2]
	head := &ListNode{Val: 1, Next: &ListNode{Val: 2}}
	expected := "1->2"

	result := insertionSortList(head)
	actual := result.String()

	if actual != expected {
		t.Errorf("Expected %s, but got %s", expected, actual)
	}
}

func TestInsertionSortList_DuplicateValues(t *testing.T) {
	// Input: [3,1,2,1,3]
	head := &ListNode{Val: 3, Next: &ListNode{Val: 1, Next: &ListNode{Val: 2, Next: &ListNode{Val: 1, Next: &ListNode{Val: 3}}}}}
	expected := "1->1->2->3->3"

	result := insertionSortList(head)
	actual := result.String()

	if actual != expected {
		t.Errorf("Expected %s, but got %s", expected, actual)
	}
}

func TestInsertionSortList_AllSameValues(t *testing.T) {
	// Input: [2,2,2,2]
	head := &ListNode{Val: 2, Next: &ListNode{Val: 2, Next: &ListNode{Val: 2, Next: &ListNode{Val: 2}}}}
	expected := "2->2->2->2"

	result := insertionSortList(head)
	actual := result.String()

	if actual != expected {
		t.Errorf("Expected %s, but got %s", expected, actual)
	}
}

func TestInsertionSortList_NegativeNumbers(t *testing.T) {
	// Input: [-5,-1,-3,-2,-4]
	head := &ListNode{Val: -5, Next: &ListNode{Val: -1, Next: &ListNode{Val: -3, Next: &ListNode{Val: -2, Next: &ListNode{Val: -4}}}}}
	expected := "-5->-4->-3->-2->-1"

	result := insertionSortList(head)
	actual := result.String()

	if actual != expected {
		t.Errorf("Expected %s, but got %s", expected, actual)
	}
}

func TestInsertionSortList_MixedPositiveNegative(t *testing.T) {
	// Input: [3,-1,0,2,-2]
	head := &ListNode{Val: 3, Next: &ListNode{Val: -1, Next: &ListNode{Val: 0, Next: &ListNode{Val: 2, Next: &ListNode{Val: -2}}}}}
	expected := "-2->-1->0->2->3"

	result := insertionSortList(head)
	actual := result.String()

	if actual != expected {
		t.Errorf("Expected %s, but got %s", expected, actual)
	}
}
