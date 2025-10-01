package designlinkedlist

import (
	"reflect"
	"testing"
)

func TestConstructor(t *testing.T) {
	ll := Constructor()
	if ll.head != nil {
		t.Error("Expected head to be nil for new list")
	}
}

func TestGetEmptyList(t *testing.T) {
	ll := Constructor()
	if got := ll.Get(0); got != -1 {
		t.Errorf("Get(0) on empty list = %d, want -1", got)
	}
}

func TestGetOutOfBounds(t *testing.T) {
	ll := Constructor()
	ll.AddAtHead(1)

	tests := []struct {
		name  string
		index int
	}{
		{"negative index", -1},
		{"index beyond list", 5},
		{"index at list size", 1},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := ll.Get(tt.index); got != -1 {
				t.Errorf("Get(%d) = %d, want -1", tt.index, got)
			}
		})
	}
}

func TestGetValidIndex(t *testing.T) {
	ll := Constructor()
	ll.AddAtHead(3)
	ll.AddAtHead(2)
	ll.AddAtHead(1)
	// List: [1, 2, 3]

	tests := []struct {
		index int
		want  int
	}{
		{0, 1},
		{1, 2},
		{2, 3},
	}

	for _, tt := range tests {
		t.Run("", func(t *testing.T) {
			if got := ll.Get(tt.index); got != tt.want {
				t.Errorf("Get(%d) = %d, want %d", tt.index, got, tt.want)
			}
		})
	}
}

func TestAddAtHead(t *testing.T) {
	ll := Constructor()

	ll.AddAtHead(1)
	if got := ll.GetValues(); !reflect.DeepEqual(got, []int{1}) {
		t.Errorf("After AddAtHead(1) = %v, want [1]", got)
	}

	ll.AddAtHead(2)
	if got := ll.GetValues(); !reflect.DeepEqual(got, []int{2, 1}) {
		t.Errorf("After AddAtHead(2) = %v, want [2, 1]", got)
	}

	ll.AddAtHead(3)
	if got := ll.GetValues(); !reflect.DeepEqual(got, []int{3, 2, 1}) {
		t.Errorf("After AddAtHead(3) = %v, want [3, 2, 1]", got)
	}
}

func TestAddAtTail(t *testing.T) {
	ll := Constructor()

	ll.AddAtTail(1)
	if got := ll.GetValues(); !reflect.DeepEqual(got, []int{1}) {
		t.Errorf("After AddAtTail(1) = %v, want [1]", got)
	}

	ll.AddAtTail(2)
	if got := ll.GetValues(); !reflect.DeepEqual(got, []int{1, 2}) {
		t.Errorf("After AddAtTail(2) = %v, want [1, 2]", got)
	}

	ll.AddAtTail(3)
	if got := ll.GetValues(); !reflect.DeepEqual(got, []int{1, 2, 3}) {
		t.Errorf("After AddAtTail(3) = %v, want [1, 2, 3]", got)
	}
}

func TestAddAtIndex(t *testing.T) {
	t.Run("add at head (index 0)", func(t *testing.T) {
		ll := Constructor()
		ll.AddAtIndex(0, 1)
		if got := ll.GetValues(); !reflect.DeepEqual(got, []int{1}) {
			t.Errorf("AddAtIndex(0, 1) = %v, want [1]", got)
		}
	})

	t.Run("add in middle", func(t *testing.T) {
		ll := Constructor()
		ll.AddAtHead(1)
		ll.AddAtTail(3)
		ll.AddAtIndex(1, 2)
		// List should be: [1, 2, 3]
		want := []int{1, 2, 3}
		if got := ll.GetValues(); !reflect.DeepEqual(got, want) {
			t.Errorf("GetValues() = %v, want %v", got, want)
		}
	})

	t.Run("add at tail (index = size)", func(t *testing.T) {
		ll := Constructor()
		ll.AddAtHead(1)
		ll.AddAtHead(2)
		ll.AddAtIndex(2, 3)
		// List should be: [2, 1, 3]
		want := []int{2, 1, 3}
		if got := ll.GetValues(); !reflect.DeepEqual(got, want) {
			t.Errorf("GetValues() = %v, want %v", got, want)
		}
	})

	t.Run("add out of bounds - no change", func(t *testing.T) {
		ll := Constructor()
		ll.AddAtHead(1)
		ll.AddAtIndex(5, 2)
		want := []int{1}
		if got := ll.GetValues(); !reflect.DeepEqual(got, want) {
			t.Errorf("GetValues() = %v, want %v", got, want)
		}
	})

	t.Run("add to empty list at index > 0", func(t *testing.T) {
		ll := Constructor()
		ll.AddAtIndex(1, 1)
		if ll.head != nil {
			t.Error("Adding at index > 0 to empty list should not change list")
		}
	})
}

func TestDeleteAtIndex(t *testing.T) {
	t.Run("delete from empty list", func(t *testing.T) {
		ll := Constructor()
		ll.DeleteAtIndex(0)
		if ll.head != nil {
			t.Error("Deleting from empty list should not crash")
		}
	})

	t.Run("delete head", func(t *testing.T) {
		ll := Constructor()
		ll.AddAtHead(1)
		ll.AddAtHead(2)
		ll.DeleteAtIndex(0)
		want := []int{1}
		if got := ll.GetValues(); !reflect.DeepEqual(got, want) {
			t.Errorf("After DeleteAtIndex(0) = %v, want %v", got, want)
		}
	})

	t.Run("delete middle", func(t *testing.T) {
		ll := Constructor()
		ll.AddAtTail(1)
		ll.AddAtTail(2)
		ll.AddAtTail(3)
		ll.DeleteAtIndex(1)
		want := []int{1, 3}
		if got := ll.GetValues(); !reflect.DeepEqual(got, want) {
			t.Errorf("After DeleteAtIndex(1) = %v, want %v", got, want)
		}
	})

	t.Run("delete tail", func(t *testing.T) {
		ll := Constructor()
		ll.AddAtTail(1)
		ll.AddAtTail(2)
		ll.AddAtTail(3)
		ll.DeleteAtIndex(2)
		want := []int{1, 2}
		if got := ll.GetValues(); !reflect.DeepEqual(got, want) {
			t.Errorf("After DeleteAtIndex(2) = %v, want %v", got, want)
		}
	})

	t.Run("delete out of bounds", func(t *testing.T) {
		ll := Constructor()
		ll.AddAtHead(1)
		ll.DeleteAtIndex(5)
		want := []int{1}
		if got := ll.GetValues(); !reflect.DeepEqual(got, want) {
			t.Errorf("After DeleteAtIndex(5) = %v, want %v", got, want)
		}
	})

	t.Run("delete only element", func(t *testing.T) {
		ll := Constructor()
		ll.AddAtHead(1)
		ll.DeleteAtIndex(0)
		if ll.head != nil {
			t.Error("After deleting only element, head should be nil")
		}
	})
}

func TestGetValues(t *testing.T) {
	t.Run("empty list", func(t *testing.T) {
		ll := Constructor()
		got := ll.GetValues()
		if len(got) != 0 {
			t.Errorf("GetValues() on empty list = %v, want []", got)
		}
	})

	t.Run("single element", func(t *testing.T) {
		ll := Constructor()
		ll.AddAtHead(42)
		want := []int{42}
		if got := ll.GetValues(); !reflect.DeepEqual(got, want) {
			t.Errorf("GetValues() = %v, want %v", got, want)
		}
	})

	t.Run("multiple elements", func(t *testing.T) {
		ll := Constructor()
		ll.AddAtTail(1)
		ll.AddAtTail(2)
		ll.AddAtTail(3)
		ll.AddAtTail(4)
		want := []int{1, 2, 3, 4}
		if got := ll.GetValues(); !reflect.DeepEqual(got, want) {
			t.Errorf("GetValues() = %v, want %v", got, want)
		}
	})
}

func TestComplexScenario(t *testing.T) {
	// Example from problem statement
	ll := Constructor()
	ll.AddAtHead(1)
	ll.AddAtTail(3)
	ll.AddAtIndex(1, 2)
	if got := ll.Get(1); got != 2 {
		t.Errorf("Get(1) = %d, want 2", got)
	}
	ll.DeleteAtIndex(1)
	if got := ll.Get(1); got != 3 {
		t.Errorf("After delete, Get(1) = %d, want 3", got)
	}

	// Verify final state
	want := []int{1, 3}
	if got := ll.GetValues(); !reflect.DeepEqual(got, want) {
		t.Errorf("Final state = %v, want %v", got, want)
	}
}

func TestEdgeCases(t *testing.T) {
	t.Run("multiple operations on single element", func(t *testing.T) {
		ll := Constructor()
		ll.AddAtHead(1)
		ll.DeleteAtIndex(0)
		ll.AddAtTail(2)
		want := []int{2}
		if got := ll.GetValues(); !reflect.DeepEqual(got, want) {
			t.Errorf("GetValues() = %v, want %v", got, want)
		}
	})

	t.Run("add and delete same index repeatedly", func(t *testing.T) {
		ll := Constructor()
		ll.AddAtHead(1)
		ll.AddAtHead(2)
		ll.DeleteAtIndex(0)
		ll.AddAtHead(3)
		want := []int{3, 1}
		if got := ll.GetValues(); !reflect.DeepEqual(got, want) {
			t.Errorf("GetValues() = %v, want %v", got, want)
		}
	})

	t.Run("negative values", func(t *testing.T) {
		ll := Constructor()
		ll.AddAtHead(-1)
		ll.AddAtTail(-2)
		want := []int{-1, -2}
		if got := ll.GetValues(); !reflect.DeepEqual(got, want) {
			t.Errorf("GetValues() = %v, want %v", got, want)
		}
	})
}
