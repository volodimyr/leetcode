package maximumtwinsumofalinkedlist

import "testing"

// Helper function to create linked list from slice
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

func TestPairSum_Example1(t *testing.T) {
	head := createList([]int{5, 4, 2, 1})
	result := pairSum(head)
	expected := 6
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestPairSum_Example2(t *testing.T) {
	head := createList([]int{4, 2, 2, 3})
	result := pairSum(head)
	expected := 7
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestPairSum_Example3(t *testing.T) {
	head := createList([]int{1, 100000})
	result := pairSum(head)
	expected := 100001
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestPairSum_MinimumSize(t *testing.T) {
	head := createList([]int{1, 2})
	result := pairSum(head)
	expected := 3
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestPairSum_AllSameValues(t *testing.T) {
	head := createList([]int{5, 5, 5, 5})
	result := pairSum(head)
	expected := 10
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestPairSum_IncreasingValues(t *testing.T) {
	head := createList([]int{1, 2, 3, 4})
	result := pairSum(head)
	expected := 5 // 1+4 or 2+3, max is 5
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestPairSum_DecreasingValues(t *testing.T) {
	head := createList([]int{10, 9, 8, 7})
	result := pairSum(head)
	expected := 17 // 10+7
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestPairSum_LargerList(t *testing.T) {
	head := createList([]int{1, 2, 3, 4, 5, 6})
	result := pairSum(head)
	expected := 7 // 1+6
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestPairSum_MaxValueAtEnds(t *testing.T) {
	head := createList([]int{100000, 1, 1, 100000})
	result := pairSum(head)
	expected := 200000
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestPairSum_EightNodes(t *testing.T) {
	head := createList([]int{5, 14, 3, 1, 2, 8, 7, 10})
	result := pairSum(head)
	// Twins: 5+10=15, 14+7=21, 3+8=11, 1+2=3
	expected := 21
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestPairSum_AlternatingHighLow(t *testing.T) {
	head := createList([]int{100, 1, 100, 1})
	result := pairSum(head)
	expected := 101 // 100+1
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}
