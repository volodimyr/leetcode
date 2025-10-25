package lfucache

import (
	"testing"
)

func TestLFUCache_NilPointerDirect(t *testing.T) {
	lfu := Constructor(10)

	lfu.Put(7, 28)
	lfu.Put(7, 1)
	lfu.Put(8, 15)
	_ = lfu.Get(6)
	lfu.Put(10, 27)
	lfu.Put(8, 10)
	_ = lfu.Get(8)
	lfu.Put(6, 29)
	lfu.Put(1, 9)
	_ = lfu.Get(6)
	lfu.Put(10, 7)
	_ = lfu.Get(1)
	_ = lfu.Get(2)
	_ = lfu.Get(13)
	lfu.Put(8, 30)
	lfu.Put(1, 5)
	_ = lfu.Get(1)
	lfu.Put(13, 2)
	_ = lfu.Get(12)
}

func TestLFUCacheExample(t *testing.T) {
	lfu := Constructor(2)

	lfu.Put(1, 1)
	lfu.Put(2, 2)

	if v := lfu.Get(1); v != 1 {
		t.Fatalf("expected 1, got %d", v)
	}

	lfu.Put(3, 3)

	if v := lfu.Get(2); v != -1 {
		t.Fatalf("expected -1, got %d", v)
	}
	if v := lfu.Get(3); v != 3 {
		t.Fatalf("expected 3, got %d", v)
	}

	lfu.Put(4, 4)

	if v := lfu.Get(1); v != -1 {
		t.Fatalf("expected -1, got %d", v)
	}
	if v := lfu.Get(3); v != 3 {
		t.Fatalf("expected 3, got %d", v)
	}
	if v := lfu.Get(4); v != 4 {
		t.Fatalf("expected 4, got %d", v)
	}
}

func TestUpdateExistingKey(t *testing.T) {
	lfu := Constructor(2)

	lfu.Put(1, 1)
	lfu.Put(1, 10)

	if v := lfu.Get(1); v != 10 {
		t.Fatalf("expected 10, got %d", v)
	}
}

func TestEvictionOrder(t *testing.T) {
	lfu := Constructor(2)

	lfu.Put(1, 1)
	lfu.Put(2, 2)

	lfu.Get(1)
	lfu.Put(3, 3)

	if v := lfu.Get(2); v != -1 {
		t.Fatalf("expected -1, got %d", v)
	}
	if v := lfu.Get(1); v != 1 {
		t.Fatalf("expected 1, got %d", v)
	}
	if v := lfu.Get(3); v != 3 {
		t.Fatalf("expected 3, got %d", v)
	}
}

func TestLFUCache(t *testing.T) {
	// Basic test: capacity 2
	cache := Constructor(2)

	cache.Put(1, 1)                    // cache: {1:1}
	cache.Put(2, 2)                    // cache: {1:1, 2:2}
	if got := cache.Get(1); got != 1 { // 1 used once → freq increment
		t.Errorf("Get(1) = %d; want 1", got)
	}

	cache.Put(3, 3) // 2 is LFU → evict 2; cache: {1:1, 3:3}
	if got := cache.Get(2); got != -1 {
		t.Errorf("Get(2) = %d; want -1", got)
	}
	if got := cache.Get(3); got != 3 {
		t.Errorf("Get(3) = %d; want 3", got)
	}

	cache.Put(4, 4) // 1 and 3 both freq=2; 1 is LRU → evict 1; cache: {3:3, 4:4}
	if got := cache.Get(1); got != -1 {
		t.Errorf("Get(1) = %d; want -1", got)
	}
	if got := cache.Get(3); got != 3 {
		t.Errorf("Get(3) = %d; want 3", got)
	}
	if got := cache.Get(4); got != 4 {
		t.Errorf("Get(4) = %d; want 4", got)
	}

	// Test capacity 0
	cache0 := Constructor(0)
	cache0.Put(1, 1)
	if got := cache0.Get(1); got != -1 {
		t.Errorf("Capacity 0: Get(1) = %d; want -1", got)
	}

	// More complex test: frequency bumps and tie-breaking
	cache2 := Constructor(3)
	cache2.Put(1, 10) // freq 1
	cache2.Put(2, 20) // freq 1
	cache2.Put(3, 30) // freq 1
	cache2.Get(1)     // freq 2
	cache2.Get(2)     // freq 2
	cache2.Put(4, 40) // evict 3 (freq=1, LRU)
	if got := cache2.Get(3); got != -1 {
		t.Errorf("Get(3) = %d; want -1", got)
	}
	if got := cache2.Get(1); got != 10 {
		t.Errorf("Get(1) = %d; want 10", got)
	}
	if got := cache2.Get(2); got != 20 {
		t.Errorf("Get(2) = %d; want 20", got)
	}
	if got := cache2.Get(4); got != 40 {
		t.Errorf("Get(4) = %d; want 40", got)
	}

	// Edge case: repeated puts increase frequency
	cache2.Put(2, 25) // freq 3
	cache2.Put(5, 50) // evict 4 (freq 1)
	if got := cache2.Get(4); got != -1 {
		t.Errorf("Get(4) = %d; want -1", got)
	}
	if got := cache2.Get(2); got != 25 {
		t.Errorf("Get(2) = %d; want 25", got)
	}
	if got := cache2.Get(5); got != 50 {
		t.Errorf("Get(5) = %d; want 50", got)
	}
}
