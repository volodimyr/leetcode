package lrucache

import "testing"

// ============================================================================
// Basic Functionality Tests
// ============================================================================

func TestLRUCache_Example1(t *testing.T) {
	// Example from the problem description
	lru := Constructor(2)

	lru.Put(1, 1) // cache is {1=1}
	lru.Put(2, 2) // cache is {1=1, 2=2}

	if got := lru.Get(1); got != 1 {
		t.Errorf("Get(1) = %d, want 1", got)
	}

	lru.Put(3, 3) // LRU key was 2, evicts key 2, cache is {1=1, 3=3}

	if got := lru.Get(2); got != -1 {
		t.Errorf("Get(2) = %d, want -1 (not found)", got)
	}

	lru.Put(4, 4) // LRU key was 1, evicts key 1, cache is {4=4, 3=3}

	if got := lru.Get(1); got != -1 {
		t.Errorf("Get(1) = %d, want -1 (not found)", got)
	}

	if got := lru.Get(3); got != 3 {
		t.Errorf("Get(3) = %d, want 3", got)
	}

	if got := lru.Get(4); got != 4 {
		t.Errorf("Get(4) = %d, want 4", got)
	}
}

func TestLRUCache_SingleCapacity(t *testing.T) {
	lru := Constructor(1)

	lru.Put(1, 10)
	if got := lru.Get(1); got != 10 {
		t.Errorf("Get(1) = %d, want 10", got)
	}

	lru.Put(2, 20) // Should evict key 1
	if got := lru.Get(1); got != -1 {
		t.Errorf("Get(1) = %d, want -1 (evicted)", got)
	}
	if got := lru.Get(2); got != 20 {
		t.Errorf("Get(2) = %d, want 20", got)
	}

	lru.Put(3, 30) // Should evict key 2
	if got := lru.Get(2); got != -1 {
		t.Errorf("Get(2) = %d, want -1 (evicted)", got)
	}
	if got := lru.Get(3); got != 30 {
		t.Errorf("Get(3) = %d, want 30", got)
	}
}

func TestLRUCache_GetNonExistentKey(t *testing.T) {
	lru := Constructor(2)

	if got := lru.Get(1); got != -1 {
		t.Errorf("Get(1) on empty cache = %d, want -1", got)
	}

	lru.Put(1, 10)
	if got := lru.Get(2); got != -1 {
		t.Errorf("Get(2) non-existent key = %d, want -1", got)
	}
}

// ============================================================================
// Update Existing Key Tests
// ============================================================================

func TestLRUCache_UpdateExistingKey(t *testing.T) {
	lru := Constructor(2)

	lru.Put(1, 10)
	lru.Put(2, 20)

	// Update key 1
	lru.Put(1, 100)

	if got := lru.Get(1); got != 100 {
		t.Errorf("Get(1) after update = %d, want 100", got)
	}

	// key 1 should now be most recently used
	// Adding key 3 should evict key 2 (not key 1)
	lru.Put(3, 30)

	if got := lru.Get(2); got != -1 {
		t.Errorf("Get(2) = %d, want -1 (should be evicted)", got)
	}
	if got := lru.Get(1); got != 100 {
		t.Errorf("Get(1) = %d, want 100 (should still exist)", got)
	}
	if got := lru.Get(3); got != 30 {
		t.Errorf("Get(3) = %d, want 30", got)
	}
}

func TestLRUCache_UpdateMovesToFront(t *testing.T) {
	lru := Constructor(3)

	lru.Put(1, 1)
	lru.Put(2, 2)
	lru.Put(3, 3)

	// Update key 1 (should move to front)
	lru.Put(1, 11)

	// Add key 4, should evict key 2 (oldest)
	lru.Put(4, 4)

	if got := lru.Get(2); got != -1 {
		t.Errorf("Get(2) = %d, want -1 (should be evicted)", got)
	}
	if got := lru.Get(1); got != 11 {
		t.Errorf("Get(1) = %d, want 11", got)
	}
	if got := lru.Get(3); got != 3 {
		t.Errorf("Get(3) = %d, want 3", got)
	}
	if got := lru.Get(4); got != 4 {
		t.Errorf("Get(4) = %d, want 4", got)
	}
}

// ============================================================================
// LRU Eviction Tests
// ============================================================================

func TestLRUCache_EvictionOrder(t *testing.T) {
	lru := Constructor(3)

	lru.Put(1, 1)
	lru.Put(2, 2)
	lru.Put(3, 3)

	// Access key 1 (moves to front)
	lru.Get(1)

	// Add key 4, should evict key 2 (least recently used)
	lru.Put(4, 4)

	if got := lru.Get(2); got != -1 {
		t.Errorf("Get(2) = %d, want -1 (should be evicted)", got)
	}
	if got := lru.Get(1); got != 1 {
		t.Errorf("Get(1) = %d, want 1", got)
	}
	if got := lru.Get(3); got != 3 {
		t.Errorf("Get(3) = %d, want 3", got)
	}
	if got := lru.Get(4); got != 4 {
		t.Errorf("Get(4) = %d, want 4", got)
	}
}

func TestLRUCache_EvictionWithGetAccess(t *testing.T) {
	lru := Constructor(2)

	lru.Put(1, 1)
	lru.Put(2, 2)

	// Access key 1 (moves to front, key 2 becomes LRU)
	lru.Get(1)

	// Add key 3, should evict key 2
	lru.Put(3, 3)

	if got := lru.Get(2); got != -1 {
		t.Errorf("Get(2) = %d, want -1 (should be evicted)", got)
	}
	if got := lru.Get(1); got != 1 {
		t.Errorf("Get(1) = %d, want 1", got)
	}
	if got := lru.Get(3); got != 3 {
		t.Errorf("Get(3) = %d, want 3", got)
	}
}

func TestLRUCache_MultipleEvictions(t *testing.T) {
	lru := Constructor(2)

	lru.Put(1, 1)
	lru.Put(2, 2)
	lru.Put(3, 3) // Evicts 1
	lru.Put(4, 4) // Evicts 2

	if got := lru.Get(1); got != -1 {
		t.Errorf("Get(1) = %d, want -1", got)
	}
	if got := lru.Get(2); got != -1 {
		t.Errorf("Get(2) = %d, want -1", got)
	}
	if got := lru.Get(3); got != 3 {
		t.Errorf("Get(3) = %d, want 3", got)
	}
	if got := lru.Get(4); got != 4 {
		t.Errorf("Get(4) = %d, want 4", got)
	}
}

// ============================================================================
// Edge Cases
// ============================================================================

func TestLRUCache_ZeroValues(t *testing.T) {
	lru := Constructor(2)

	lru.Put(0, 0)
	if got := lru.Get(0); got != 0 {
		t.Errorf("Get(0) = %d, want 0", got)
	}

	lru.Put(1, 0)
	if got := lru.Get(1); got != 0 {
		t.Errorf("Get(1) = %d, want 0", got)
	}
}

func TestLRUCache_LargeValues(t *testing.T) {
	lru := Constructor(2)

	lru.Put(10000, 100000)
	if got := lru.Get(10000); got != 100000 {
		t.Errorf("Get(10000) = %d, want 100000", got)
	}
}

func TestLRUCache_SameKeyMultiplePuts(t *testing.T) {
	lru := Constructor(1)

	lru.Put(1, 10)
	lru.Put(1, 20)
	lru.Put(1, 30)

	if got := lru.Get(1); got != 30 {
		t.Errorf("Get(1) = %d, want 30", got)
	}
}

// ============================================================================
// Complex Scenarios
// ============================================================================

func TestLRUCache_AlternatingPutGet(t *testing.T) {
	lru := Constructor(2)

	lru.Put(1, 1)
	lru.Get(1)
	lru.Put(2, 2)
	lru.Get(1)
	lru.Get(2)
	lru.Put(3, 3) // Should evict key 1? No! key 1 was accessed most recently

	// Actually, after Get(2), key 2 is most recent, then key 1
	// So key 1 should be evicted
	lru.Put(3, 3)

	// Wait, let me trace through:
	// Put(1,1): [1]
	// Get(1): [1] - accesses 1
	// Put(2,2): [2,1] - 2 is most recent
	// Get(1): [1,2] - 1 is most recent
	// Get(2): [2,1] - 2 is most recent
	// Put(3,3): evicts LRU which is 1, [3,2]

	if got := lru.Get(1); got != -1 {
		t.Errorf("Get(1) = %d, want -1 (should be evicted)", got)
	}
	if got := lru.Get(2); got != 2 {
		t.Errorf("Get(2) = %d, want 2", got)
	}
	if got := lru.Get(3); got != 3 {
		t.Errorf("Get(3) = %d, want 3", got)
	}
}

func TestLRUCache_SequentialAccess(t *testing.T) {
	lru := Constructor(3)

	lru.Put(1, 1)
	lru.Put(2, 2)
	lru.Put(3, 3)

	// Access in order: 3, 2, 1 (making 1 most recent)
	lru.Get(3)
	lru.Get(2)
	lru.Get(1)

	// Add key 4, should evict key 3 (least recently used)
	lru.Put(4, 4)

	if got := lru.Get(3); got != -1 {
		t.Errorf("Get(3) = %d, want -1 (should be evicted)", got)
	}
	if got := lru.Get(1); got != 1 {
		t.Errorf("Get(1) = %d, want 1", got)
	}
	if got := lru.Get(2); got != 2 {
		t.Errorf("Get(2) = %d, want 2", got)
	}
	if got := lru.Get(4); got != 4 {
		t.Errorf("Get(4) = %d, want 4", got)
	}
}

func TestLRUCache_UpdateDoesNotEvict(t *testing.T) {
	lru := Constructor(2)

	lru.Put(1, 1)
	lru.Put(2, 2)

	// Update key 1 (should NOT trigger eviction since we're at capacity but not exceeding)
	lru.Put(1, 11)

	if got := lru.Get(1); got != 11 {
		t.Errorf("Get(1) = %d, want 11", got)
	}
	if got := lru.Get(2); got != 2 {
		t.Errorf("Get(2) = %d, want 2 (should not be evicted)", got)
	}
}

// ============================================================================
// Stress Tests
// ============================================================================

func TestLRUCache_LargeCapacity(t *testing.T) {
	lru := Constructor(1000)

	// Insert 1000 items
	for i := 0; i < 1000; i++ {
		lru.Put(i, i*10)
	}

	// All should be retrievable
	for i := 0; i < 1000; i++ {
		if got := lru.Get(i); got != i*10 {
			t.Errorf("Get(%d) = %d, want %d", i, got, i*10)
		}
	}

	// Add one more, should evict key 0 (first inserted, now LRU)
	lru.Put(1000, 10000)

	if got := lru.Get(0); got != -1 {
		t.Errorf("Get(0) = %d, want -1 (should be evicted)", got)
	}
	if got := lru.Get(1000); got != 10000 {
		t.Errorf("Get(1000) = %d, want 10000", got)
	}
}

func TestLRUCache_ManyOperations(t *testing.T) {
	lru := Constructor(3)

	operations := []struct {
		op    string
		key   int
		value int
		want  int
	}{
		{"put", 1, 1, 0},
		{"put", 2, 2, 0},
		{"get", 1, 0, 1},
		{"put", 3, 3, 0},
		{"get", 2, 0, 2},
		{"put", 4, 4, 0},
		{"get", 1, 0, -1},
		{"get", 3, 0, 3}, // 3 was evicted
		{"get", 4, 0, 4},
	}

	for i, op := range operations {
		if op.op == "put" {
			lru.Put(op.key, op.value)
		} else {
			got := lru.Get(op.key)
			if got != op.want {
				t.Errorf("operation %d: Get(%d) = %d, want %d", i, op.key, got, op.want)
			}
		}
	}
}

// ============================================================================
// Capacity Tests
// ============================================================================

func TestLRUCache_CapacityOne(t *testing.T) {
	lru := Constructor(1)

	lru.Put(1, 1)
	if got := lru.Get(1); got != 1 {
		t.Errorf("Get(1) = %d, want 1", got)
	}

	lru.Put(2, 2)
	if got := lru.Get(1); got != -1 {
		t.Errorf("Get(1) = %d, want -1", got)
	}
	if got := lru.Get(2); got != 2 {
		t.Errorf("Get(2) = %d, want 2", got)
	}
}

func TestLRUCache_CapacityTwo_ComplexPattern(t *testing.T) {
	lru := Constructor(2)

	lru.Put(2, 1)
	lru.Put(1, 1)
	lru.Put(2, 3)
	lru.Put(4, 1)

	if got := lru.Get(1); got != -1 {
		t.Errorf("Get(1) = %d, want -1", got)
	}
	if got := lru.Get(2); got != 3 {
		t.Errorf("Get(2) = %d, want 3", got)
	}
}

// ============================================================================
// Order Verification Tests
// ============================================================================

func TestLRUCache_MRU_Order(t *testing.T) {
	lru := Constructor(3)

	// Insert in order: 1, 2, 3
	lru.Put(1, 1)
	lru.Put(2, 2)
	lru.Put(3, 3)

	// MRU order: 3, 2, 1 (3 is most recent)

	// Access 1 (moves to front)
	lru.Get(1)
	// MRU order: 1, 3, 2

	// Access 2 (moves to front)
	lru.Get(2)
	// MRU order: 2, 1, 3

	// Add 4, should evict 3
	lru.Put(4, 4)

	if got := lru.Get(3); got != -1 {
		t.Errorf("Get(3) = %d, want -1", got)
	}
	if got := lru.Get(2); got != 2 {
		t.Errorf("Get(2) = %d, want 2", got)
	}
	if got := lru.Get(1); got != 1 {
		t.Errorf("Get(1) = %d, want 1", got)
	}
	if got := lru.Get(4); got != 4 {
		t.Errorf("Get(4) = %d, want 4", got)
	}
}

// ============================================================================
// Special Pattern Tests
// ============================================================================

func TestLRUCache_GetMovesToFront(t *testing.T) {
	lru := Constructor(2)

	lru.Put(1, 1)
	lru.Put(2, 2)

	// Get 1 multiple times (should stay at front)
	lru.Get(1)
	lru.Get(1)
	lru.Get(1)

	// Add 3, should evict 2
	lru.Put(3, 3)

	if got := lru.Get(2); got != -1 {
		t.Errorf("Get(2) = %d, want -1", got)
	}
	if got := lru.Get(1); got != 1 {
		t.Errorf("Get(1) = %d, want 1", got)
	}
	if got := lru.Get(3); got != 3 {
		t.Errorf("Get(3) = %d, want 3", got)
	}
}

func TestLRUCache_PutSameKeyRepeatedly(t *testing.T) {
	lru := Constructor(2)

	lru.Put(1, 1)
	lru.Put(1, 2)
	lru.Put(1, 3)

	if got := lru.Get(1); got != 3 {
		t.Errorf("Get(1) = %d, want 3", got)
	}

	lru.Put(2, 2)
	lru.Put(3, 3) // Should evict 1? No, 1 was updated recently

	// After Put(1,3), order is [1]
	// After Put(2,2), order is [2,1]
	// After Put(3,3), should evict 1, order is [3,2]

	if got := lru.Get(1); got != -1 {
		t.Errorf("Get(1) = %d, want -1", got)
	}
	if got := lru.Get(2); got != 2 {
		t.Errorf("Get(2) = %d, want 2", got)
	}
	if got := lru.Get(3); got != 3 {
		t.Errorf("Get(3) = %d, want 3", got)
	}
}
