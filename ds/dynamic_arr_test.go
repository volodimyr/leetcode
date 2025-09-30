package ds

import "testing"

func TestNewDynamicArray(t *testing.T) {
	da := NewDynamicArray(1)

	if da.GetSize() != 0 {
		t.Errorf("Expected size 0, got %d", da.GetSize())
	}

	if da.GetCapacity() != 1 {
		t.Errorf("Expected capacity 1, got %d", da.GetCapacity())
	}
}

func TestNewDynamicArrayWithDifferentCapacity(t *testing.T) {
	da := NewDynamicArray(5)

	if da.GetSize() != 0 {
		t.Errorf("Expected size 0, got %d", da.GetSize())
	}

	if da.GetCapacity() != 5 {
		t.Errorf("Expected capacity 5, got %d", da.GetCapacity())
	}
}

func TestPushback(t *testing.T) {
	da := NewDynamicArray(2)

	da.Pushback(1)

	if da.GetSize() != 1 {
		t.Errorf("Expected size 1, got %d", da.GetSize())
	}

	if da.Get(0) != 1 {
		t.Errorf("Expected element at index 0 to be 1, got %d", da.Get(0))
	}
}

func TestPushbackMultipleElements(t *testing.T) {
	da := NewDynamicArray(3)

	da.Pushback(1)
	da.Pushback(2)
	da.Pushback(3)

	if da.GetSize() != 3 {
		t.Errorf("Expected size 3, got %d", da.GetSize())
	}

	if da.Get(0) != 1 || da.Get(1) != 2 || da.Get(2) != 3 {
		t.Errorf("Elements not stored correctly")
	}
}

func TestPushbackWithResize(t *testing.T) {
	da := NewDynamicArray(1)

	da.Pushback(1)

	if da.GetCapacity() != 1 {
		t.Errorf("Expected capacity 1 after first push, got %d", da.GetCapacity())
	}

	da.Pushback(2)

	if da.GetCapacity() != 2 {
		t.Errorf("Expected capacity 2 after resize, got %d", da.GetCapacity())
	}

	if da.GetSize() != 2 {
		t.Errorf("Expected size 2, got %d", da.GetSize())
	}

	if da.Get(0) != 1 || da.Get(1) != 2 {
		t.Errorf("Elements not preserved after resize")
	}
}

func TestPushbackMultipleResizes(t *testing.T) {
	da := NewDynamicArray(1)

	da.Pushback(1)
	da.Pushback(2)
	da.Pushback(3)

	if da.GetCapacity() != 4 {
		t.Errorf("Expected capacity 4 after multiple resizes, got %d", da.GetCapacity())
	}

	if da.GetSize() != 3 {
		t.Errorf("Expected size 3, got %d", da.GetSize())
	}
}

func TestGet(t *testing.T) {
	da := NewDynamicArray(3)
	da.Pushback(10)
	da.Pushback(20)
	da.Pushback(30)

	if da.Get(0) != 10 {
		t.Errorf("Expected 10 at index 0, got %d", da.Get(0))
	}

	if da.Get(1) != 20 {
		t.Errorf("Expected 20 at index 1, got %d", da.Get(1))
	}

	if da.Get(2) != 30 {
		t.Errorf("Expected 30 at index 2, got %d", da.Get(2))
	}
}

func TestSet(t *testing.T) {
	da := NewDynamicArray(3)
	da.Pushback(1)
	da.Pushback(2)
	da.Pushback(3)

	da.Set(1, 20)

	if da.Get(1) != 20 {
		t.Errorf("Expected 20 at index 1 after set, got %d", da.Get(1))
	}

	if da.GetSize() != 3 {
		t.Errorf("Set should not change size, got %d", da.GetSize())
	}
}

func TestSetMultipleIndices(t *testing.T) {
	da := NewDynamicArray(5)
	da.Pushback(1)
	da.Pushback(2)
	da.Pushback(3)
	da.Pushback(4)

	da.Set(0, 100)
	da.Set(2, 300)
	da.Set(3, 400)

	if da.Get(0) != 100 {
		t.Errorf("Expected 100 at index 0, got %d", da.Get(0))
	}

	if da.Get(1) != 2 {
		t.Errorf("Expected 2 at index 1 (unchanged), got %d", da.Get(1))
	}

	if da.Get(2) != 300 {
		t.Errorf("Expected 300 at index 2, got %d", da.Get(2))
	}

	if da.Get(3) != 400 {
		t.Errorf("Expected 400 at index 3, got %d", da.Get(3))
	}
}

func TestPopback(t *testing.T) {
	da := NewDynamicArray(3)
	da.Pushback(1)
	da.Pushback(2)
	da.Pushback(3)

	val := da.Popback()

	if val != 3 {
		t.Errorf("Expected popback to return 3, got %d", val)
	}

	if da.GetSize() != 2 {
		t.Errorf("Expected size 2 after popback, got %d", da.GetSize())
	}

	if da.GetCapacity() != 3 {
		t.Errorf("Popback should not change capacity, got %d", da.GetCapacity())
	}
}

func TestPopbackMultipleTimes(t *testing.T) {
	da := NewDynamicArray(5)
	da.Pushback(10)
	da.Pushback(20)
	da.Pushback(30)

	val1 := da.Popback()
	val2 := da.Popback()

	if val1 != 30 {
		t.Errorf("Expected first popback to return 30, got %d", val1)
	}

	if val2 != 20 {
		t.Errorf("Expected second popback to return 20, got %d", val2)
	}

	if da.GetSize() != 1 {
		t.Errorf("Expected size 1 after two popbacks, got %d", da.GetSize())
	}

	if da.Get(0) != 10 {
		t.Errorf("Expected remaining element to be 10, got %d", da.Get(0))
	}
}

func TestExample1(t *testing.T) {
	da := NewDynamicArray(1)

	if da.GetSize() != 0 {
		t.Errorf("Expected size 0, got %d", da.GetSize())
	}

	if da.GetCapacity() != 1 {
		t.Errorf("Expected capacity 1, got %d", da.GetCapacity())
	}
}

func TestExample2(t *testing.T) {
	da := NewDynamicArray(1)

	da.Pushback(1)

	if da.GetCapacity() != 1 {
		t.Errorf("Expected capacity 1, got %d", da.GetCapacity())
	}

	da.Pushback(2)

	if da.GetCapacity() != 2 {
		t.Errorf("Expected capacity 2, got %d", da.GetCapacity())
	}
}

func TestExample3(t *testing.T) {
	da := NewDynamicArray(1)

	if da.GetSize() != 0 {
		t.Errorf("Expected size 0, got %d", da.GetSize())
	}

	if da.GetCapacity() != 1 {
		t.Errorf("Expected capacity 1, got %d", da.GetCapacity())
	}

	da.Pushback(1)

	if da.GetSize() != 1 {
		t.Errorf("Expected size 1, got %d", da.GetSize())
	}

	if da.GetCapacity() != 1 {
		t.Errorf("Expected capacity 1, got %d", da.GetCapacity())
	}

	da.Pushback(2)

	if da.GetSize() != 2 {
		t.Errorf("Expected size 2, got %d", da.GetSize())
	}

	if da.GetCapacity() != 2 {
		t.Errorf("Expected capacity 2, got %d", da.GetCapacity())
	}

	if da.Get(1) != 2 {
		t.Errorf("Expected 2 at index 1, got %d", da.Get(1))
	}

	da.Set(1, 3)

	if da.Get(1) != 3 {
		t.Errorf("Expected 3 at index 1, got %d", da.Get(1))
	}

	val := da.Popback()

	if val != 3 {
		t.Errorf("Expected popback to return 3, got %d", val)
	}

	if da.GetSize() != 1 {
		t.Errorf("Expected size 1, got %d", da.GetSize())
	}

	if da.GetCapacity() != 2 {
		t.Errorf("Expected capacity 2, got %d", da.GetCapacity())
	}
}

func TestPushbackAndPopbackSequence(t *testing.T) {
	da := NewDynamicArray(2)

	da.Pushback(5)
	da.Pushback(10)
	da.Pushback(15)

	if da.GetSize() != 3 {
		t.Errorf("Expected size 3, got %d", da.GetSize())
	}

	val1 := da.Popback()
	val2 := da.Popback()

	if val1 != 15 || val2 != 10 {
		t.Errorf("Expected popback sequence 15, 10, got %d, %d", val1, val2)
	}

	da.Pushback(25)
	da.Pushback(35)

	if da.GetSize() != 3 {
		t.Errorf("Expected size 3, got %d", da.GetSize())
	}

	if da.Get(0) != 5 || da.Get(1) != 25 || da.Get(2) != 35 {
		t.Errorf("Elements not as expected after push/pop sequence")
	}
}
