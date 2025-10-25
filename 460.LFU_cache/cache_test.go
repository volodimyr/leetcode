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
