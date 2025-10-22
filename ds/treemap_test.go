package ds

import "testing"

func TestNewTreeMap(t *testing.T) {
	tm := NewTreeMap()
	if tm == nil {
		t.Fatal("NewTreeMap should return a non-nil TreeMap")
	}
}

func TestInsertSingleElement(t *testing.T) {
	tm := NewTreeMap()
	tm.Insert(5, 5)
	keys := tm.GetInorderKeys()
	if len(keys) != 1 {
		t.Errorf("Expected 1 key, got %d", len(keys))
	}
	if len(keys) > 0 && keys[0] != 5 {
		t.Errorf("Expected key 5, got %d", keys[0])
	}
}

func TestInsertMultipleElements(t *testing.T) {
	tm := NewTreeMap()
	tm.Insert(5, 5)
	tm.Insert(3, 3)
	tm.Insert(7, 7)
	keys := tm.GetInorderKeys()
	expected := []int{3, 5, 7}
	if len(keys) != len(expected) {
		t.Fatalf("Expected %d keys, got %d", len(expected), len(keys))
	}
	for i := range expected {
		if keys[i] != expected[i] {
			t.Errorf("At index %d: expected %d, got %d", i, expected[i], keys[i])
		}
	}
}

func TestInsertLeftSkewed(t *testing.T) {
	tm := NewTreeMap()
	tm.Insert(5, 5)
	tm.Insert(4, 4)
	tm.Insert(3, 3)
	tm.Insert(2, 2)
	keys := tm.GetInorderKeys()
	expected := []int{2, 3, 4, 5}
	if len(keys) != len(expected) {
		t.Fatalf("Expected %d keys, got %d", len(expected), len(keys))
	}
	for i := range expected {
		if keys[i] != expected[i] {
			t.Errorf("At index %d: expected %d, got %d", i, expected[i], keys[i])
		}
	}
}

func TestInsertRightSkewed(t *testing.T) {
	tm := NewTreeMap()
	tm.Insert(2, 2)
	tm.Insert(3, 3)
	tm.Insert(4, 4)
	tm.Insert(5, 5)
	keys := tm.GetInorderKeys()
	expected := []int{2, 3, 4, 5}
	if len(keys) != len(expected) {
		t.Fatalf("Expected %d keys, got %d", len(expected), len(keys))
	}
	for i := range expected {
		if keys[i] != expected[i] {
			t.Errorf("At index %d: expected %d, got %d", i, expected[i], keys[i])
		}
	}
}

func TestGetExistingKey(t *testing.T) {
	tm := NewTreeMap()
	tm.Insert(5, 50)
	tm.Insert(3, 30)
	tm.Insert(7, 70)

	val := tm.Get(5)
	if val != 50 {
		t.Errorf("Expected value 50, got %d", val)
	}

	val = tm.Get(3)
	if val != 30 {
		t.Errorf("Expected value 30, got %d", val)
	}

	val = tm.Get(7)
	if val != 70 {
		t.Errorf("Expected value 70, got %d", val)
	}
}

func TestGetNonExistingKey(t *testing.T) {
	tm := NewTreeMap()
	tm.Insert(5, 50)

	val := tm.Get(10)
	if val != -1 {
		t.Errorf("Expected -1 for non-existing key, got %d", val)
	}
}

func TestGetFromEmptyTree(t *testing.T) {
	tm := NewTreeMap()
	val := tm.Get(5)
	if val != -1 {
		t.Errorf("Expected -1 for empty tree, got %d", val)
	}
}

func TestGetMinSingleElement(t *testing.T) {
	tm := NewTreeMap()
	tm.Insert(5, 5)

	min := tm.GetMin()
	if min != 5 {
		t.Errorf("Expected min 5, got %d", min)
	}
}

func TestGetMinMultipleElements(t *testing.T) {
	tm := NewTreeMap()
	tm.Insert(5, 5)
	tm.Insert(3, 3)
	tm.Insert(7, 7)
	tm.Insert(1, 1)

	min := tm.GetMin()
	if min != 1 {
		t.Errorf("Expected min 1, got %d", min)
	}
}

func TestGetMinEmptyTree(t *testing.T) {
	tm := NewTreeMap()
	min := tm.GetMin()
	if min != -1 {
		t.Errorf("Expected -1 for empty tree, got %d", min)
	}
}

func TestGetMaxSingleElement(t *testing.T) {
	tm := NewTreeMap()
	tm.Insert(5, 5)

	max := tm.GetMax()
	if max != 5 {
		t.Errorf("Expected max 5, got %d", max)
	}
}

func TestGetMaxMultipleElements(t *testing.T) {
	tm := NewTreeMap()
	tm.Insert(5, 5)
	tm.Insert(3, 3)
	tm.Insert(7, 7)
	tm.Insert(9, 9)

	max := tm.GetMax()
	if max != 9 {
		t.Errorf("Expected max 9, got %d", max)
	}
}

func TestGetMaxEmptyTree(t *testing.T) {
	tm := NewTreeMap()
	max := tm.GetMax()
	if max != -1 {
		t.Errorf("Expected -1 for empty tree, got %d", max)
	}
}

func TestRemoveLeafNode(t *testing.T) {
	tm := NewTreeMap()
	tm.Insert(5, 5)
	tm.Insert(3, 3)
	tm.Insert(7, 7)

	tm.Remove(3)
	keys := tm.GetInorderKeys()
	expected := []int{5, 7}
	if len(keys) != len(expected) {
		t.Fatalf("Expected %d keys, got %d", len(expected), len(keys))
	}
	for i := range expected {
		if keys[i] != expected[i] {
			t.Errorf("At index %d: expected %d, got %d", i, expected[i], keys[i])
		}
	}
}

func TestRemoveNodeWithOneChild(t *testing.T) {
	tm := NewTreeMap()
	tm.Insert(5, 5)
	tm.Insert(3, 3)
	tm.Insert(2, 2)

	tm.Remove(3)
	keys := tm.GetInorderKeys()
	expected := []int{2, 5}
	if len(keys) != len(expected) {
		t.Fatalf("Expected %d keys, got %d", len(expected), len(keys))
	}
	for i := range expected {
		if keys[i] != expected[i] {
			t.Errorf("At index %d: expected %d, got %d", i, expected[i], keys[i])
		}
	}
}

func TestRemoveNodeWithTwoChildren(t *testing.T) {
	tm := NewTreeMap()
	tm.Insert(5, 5)
	tm.Insert(3, 3)
	tm.Insert(7, 7)
	tm.Insert(2, 2)
	tm.Insert(4, 4)

	tm.Remove(3)
	keys := tm.GetInorderKeys()
	expected := []int{2, 4, 5, 7}
	if len(keys) != len(expected) {
		t.Fatalf("Expected %d keys, got %d", len(expected), len(keys))
	}
	for i := range expected {
		if keys[i] != expected[i] {
			t.Errorf("At index %d: expected %d, got %d", i, expected[i], keys[i])
		}
	}
}

func TestRemoveRoot(t *testing.T) {
	tm := NewTreeMap()
	tm.Insert(5, 5)
	tm.Insert(3, 3)
	tm.Insert(7, 7)

	tm.Remove(5)
	keys := tm.GetInorderKeys()
	expected := []int{3, 7}
	if len(keys) != len(expected) {
		t.Fatalf("Expected %d keys, got %d", len(expected), len(keys))
	}
	for i := range expected {
		if keys[i] != expected[i] {
			t.Errorf("At index %d: expected %d, got %d", i, expected[i], keys[i])
		}
	}
}

func TestRemoveNonExistingKey(t *testing.T) {
	tm := NewTreeMap()
	tm.Insert(5, 5)
	tm.Insert(3, 3)

	tm.Remove(10)
	keys := tm.GetInorderKeys()
	expected := []int{3, 5}
	if len(keys) != len(expected) {
		t.Fatalf("Expected %d keys, got %d", len(expected), len(keys))
	}
	for i := range expected {
		if keys[i] != expected[i] {
			t.Errorf("At index %d: expected %d, got %d", i, expected[i], keys[i])
		}
	}
}

func TestRemoveFromEmptyTree(t *testing.T) {
	tm := NewTreeMap()
	tm.Remove(5)
	keys := tm.GetInorderKeys()
	if len(keys) != 0 {
		t.Errorf("Expected 0 keys, got %d", len(keys))
	}
}

func TestRemoveAllElements(t *testing.T) {
	tm := NewTreeMap()
	tm.Insert(5, 5)
	tm.Insert(3, 3)
	tm.Insert(7, 7)

	tm.Remove(5)
	tm.Remove(3)
	tm.Remove(7)

	keys := tm.GetInorderKeys()
	if len(keys) != 0 {
		t.Errorf("Expected 0 keys after removing all, got %d", len(keys))
	}
}

func TestInsertDuplicateKey(t *testing.T) {
	tm := NewTreeMap()
	tm.Insert(5, 50)
	tm.Insert(5, 100)

	val := tm.Get(5)
	if val != 100 {
		t.Errorf("Expected updated value 100, got %d", val)
	}

	keys := tm.GetInorderKeys()
	if len(keys) != 1 {
		t.Errorf("Expected 1 key after duplicate insert, got %d", len(keys))
	}
}

func TestComplexOperations(t *testing.T) {
	tm := NewTreeMap()
	tm.Insert(10, 10)
	tm.Insert(5, 5)
	tm.Insert(15, 15)
	tm.Insert(3, 3)
	tm.Insert(7, 7)
	tm.Insert(12, 12)
	tm.Insert(17, 17)

	min := tm.GetMin()
	if min != 3 {
		t.Errorf("Expected min 3, got %d", min)
	}

	max := tm.GetMax()
	if max != 17 {
		t.Errorf("Expected max 17, got %d", max)
	}

	tm.Remove(10)

	keys := tm.GetInorderKeys()
	expected := []int{3, 5, 7, 12, 15, 17}
	if len(keys) != len(expected) {
		t.Fatalf("Expected %d keys, got %d", len(expected), len(keys))
	}
	for i := range expected {
		if keys[i] != expected[i] {
			t.Errorf("At index %d: expected %d, got %d", i, expected[i], keys[i])
		}
	}
}

func TestGetInorderKeysEmptyTree(t *testing.T) {
	tm := NewTreeMap()
	keys := tm.GetInorderKeys()
	if len(keys) != 0 {
		t.Errorf("Expected 0 keys for empty tree, got %d", len(keys))
	}
}

func TestNegativeKeys(t *testing.T) {
	tm := NewTreeMap()
	tm.Insert(-5, -5)
	tm.Insert(-10, -10)
	tm.Insert(0, 0)
	tm.Insert(5, 5)

	keys := tm.GetInorderKeys()
	expected := []int{-10, -5, 0, 5}
	if len(keys) != len(expected) {
		t.Fatalf("Expected %d keys, got %d", len(expected), len(keys))
	}
	for i := range expected {
		if keys[i] != expected[i] {
			t.Errorf("At index %d: expected %d, got %d", i, expected[i], keys[i])
		}
	}

	min := tm.GetMin()
	if min != -10 {
		t.Errorf("Expected min -10, got %d", min)
	}
}
