package designhashmap

import "testing"

func TestConstructor(t *testing.T) {
	m := Constructor()
	if m.values == nil {
		t.Error("Expected values array to be initialized")
	}
	if len(m.values) != 11 {
		t.Errorf("Expected initial size of 10, got %d", len(m.values))
	}
	if m.size != 0 {
		t.Errorf("Expected initial size to be 0, got %d", m.size)
	}
}

func TestPutAndGet(t *testing.T) {
	m := Constructor()

	m.Put(1, 1)
	if got := m.Get(1); got != 1 {
		t.Errorf("Expected Get(1) = 1, got %d", got)
	}

	m.Put(2, 2)
	if got := m.Get(2); got != 2 {
		t.Errorf("Expected Get(2) = 2, got %d", got)
	}

	// Original value should still be there
	if got := m.Get(1); got != 1 {
		t.Errorf("Expected Get(1) = 1, got %d", got)
	}
}

func TestGetNonExistentKey(t *testing.T) {
	m := Constructor()

	if got := m.Get(3); got != -1 {
		t.Errorf("Expected Get(3) = -1, got %d", got)
	}

	m.Put(1, 1)
	if got := m.Get(99); got != -1 {
		t.Errorf("Expected Get(99) = -1, got %d", got)
	}
}

func TestPutUpdateExistingKey(t *testing.T) {
	m := Constructor()

	m.Put(2, 2)
	if got := m.Get(2); got != 2 {
		t.Errorf("Expected Get(2) = 2, got %d", got)
	}

	m.Put(2, 100)
	if got := m.Get(2); got != 100 {
		t.Errorf("Expected Get(2) = 100 after update, got %d", got)
	}
}

func TestRemove(t *testing.T) {
	m := Constructor()

	m.Put(2, 2)
	m.Remove(2)

	if got := m.Get(2); got != -1 {
		t.Errorf("Expected Get(2) = -1 after removal, got %d", got)
	}
}

func TestRemoveNonExistentKey(t *testing.T) {
	m := Constructor()

	// Should not panic
	m.Remove(999)

	m.Put(1, 1)
	m.Remove(999)

	// Original key should still be there
	if got := m.Get(1); got != 1 {
		t.Errorf("Expected Get(1) = 1, got %d", got)
	}
}

func TestExampleSequence(t *testing.T) {
	m := Constructor()

	m.Put(1, 1)
	m.Put(2, 2)

	if got := m.Get(1); got != 1 {
		t.Errorf("Expected Get(1) = 1, got %d", got)
	}

	if got := m.Get(3); got != -1 {
		t.Errorf("Expected Get(3) = -1, got %d", got)
	}

	m.Put(2, 1)

	if got := m.Get(2); got != 1 {
		t.Errorf("Expected Get(2) = 1, got %d", got)
	}

	m.Remove(2)

	if got := m.Get(2); got != -1 {
		t.Errorf("Expected Get(2) = -1 after removal, got %d", got)
	}
}

func TestMultipleKeys(t *testing.T) {
	m := Constructor()

	for i := 0; i < 100; i++ {
		m.Put(i, i*10)
	}

	for i := 0; i < 100; i++ {
		if got := m.Get(i); got != i*10 {
			t.Errorf("Expected Get(%d) = %d, got %d", i, i*10, got)
		}
	}
}

func TestCollisions(t *testing.T) {
	m := Constructor()

	// Keys that will collide (same hash in initial 10-bucket array)
	m.Put(1, 100)
	m.Put(11, 110)
	m.Put(21, 120)

	if got := m.Get(1); got != 100 {
		t.Errorf("Expected Get(1) = 100, got %d", got)
	}
	if got := m.Get(11); got != 110 {
		t.Errorf("Expected Get(11) = 110, got %d", got)
	}
	if got := m.Get(21); got != 120 {
		t.Errorf("Expected Get(21) = 120, got %d", got)
	}
}

func TestRemoveWithCollisions(t *testing.T) {
	m := Constructor()

	m.Put(1, 100)
	m.Put(11, 110)
	m.Put(21, 120)

	m.Remove(11)

	if got := m.Get(11); got != -1 {
		t.Errorf("Expected Get(11) = -1 after removal, got %d", got)
	}
	if got := m.Get(1); got != 100 {
		t.Errorf("Expected Get(1) = 100, got %d", got)
	}
	if got := m.Get(21); got != 120 {
		t.Errorf("Expected Get(21) = 120, got %d", got)
	}
}

func TestResizing(t *testing.T) {
	m := Constructor()
	initialLen := len(m.values)

	// Add enough elements to trigger resize
	for i := 0; i < 10; i++ {
		m.Put(i, i*10)
	}

	if len(m.values) <= initialLen {
		t.Errorf("Expected resize to occur, initial length: %d, current length: %d", initialLen, len(m.values))
	}

	// Verify all values are still accessible after resize
	for i := 0; i < 10; i++ {
		if got := m.Get(i); got != i*10 {
			t.Errorf("Expected Get(%d) = %d after resize, got %d", i, i*10, got)
		}
	}
}

func TestZeroValues(t *testing.T) {
	m := Constructor()

	m.Put(0, 0)
	if got := m.Get(0); got != 0 {
		t.Errorf("Expected Get(0) = 0, got %d", got)
	}

	m.Put(0, 100)
	if got := m.Get(0); got != 100 {
		t.Errorf("Expected Get(0) = 100 after update, got %d", got)
	}
}

func TestLargeValues(t *testing.T) {
	m := Constructor()

	m.Put(1000000, 1000000)
	if got := m.Get(1000000); got != 1000000 {
		t.Errorf("Expected Get(1000000) = 1000000, got %d", got)
	}
}

func TestRemoveHead(t *testing.T) {
	m := Constructor()

	m.Put(1, 100)
	m.Put(2, 200)

	m.Remove(2) // Remove most recently added (head)

	if got := m.Get(2); got != -1 {
		t.Errorf("Expected Get(2) = -1 after removal, got %d", got)
	}
	if got := m.Get(1); got != 100 {
		t.Errorf("Expected Get(1) = 100, got %d", got)
	}
}

func TestUpdateAfterRemove(t *testing.T) {
	m := Constructor()

	m.Put(1, 100)
	m.Remove(1)
	m.Put(1, 200)

	if got := m.Get(1); got != 200 {
		t.Errorf("Expected Get(1) = 200, got %d", got)
	}
}

func TestMultipleUpdates(t *testing.T) {
	m := Constructor()

	m.Put(5, 10)
	m.Put(5, 20)
	m.Put(5, 30)
	m.Put(5, 40)

	if got := m.Get(5); got != 40 {
		t.Errorf("Expected Get(5) = 40, got %d", got)
	}
}

func TestEmptyMapOperations(t *testing.T) {
	m := Constructor()

	if got := m.Get(1); got != -1 {
		t.Errorf("Expected Get(1) = -1 on empty map, got %d", got)
	}

	m.Remove(1) // Should not panic

	if got := m.Get(1); got != -1 {
		t.Errorf("Expected Get(1) = -1, got %d", got)
	}
}
