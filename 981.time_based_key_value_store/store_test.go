package timebasedkeyvaluestore

import "testing"

func TestTimeMap_BasicOperations(t *testing.T) {
	tm := Constructor()

	tm.Set("foo", "bar", 1)

	result := tm.Get("foo", 1)
	if result != "bar" {
		t.Errorf("Expected 'bar', got '%s'", result)
	}
}

func TestTimeMap_GetWithLargerTimestamp(t *testing.T) {
	tm := Constructor()

	tm.Set("foo", "bar", 1)

	result := tm.Get("foo", 3)
	if result != "bar" {
		t.Errorf("Expected 'bar', got '%s'", result)
	}
}

func TestTimeMap_MultipleValues(t *testing.T) {
	tm := Constructor()

	tm.Set("foo", "bar", 1)
	tm.Set("foo", "bar2", 4)

	result := tm.Get("foo", 4)
	if result != "bar2" {
		t.Errorf("Expected 'bar2', got '%s'", result)
	}

	result = tm.Get("foo", 5)
	if result != "bar2" {
		t.Errorf("Expected 'bar2', got '%s'", result)
	}
}

func TestTimeMap_GetNonExistentKey(t *testing.T) {
	tm := Constructor()

	result := tm.Get("foo", 1)
	if result != "" {
		t.Errorf("Expected empty string, got '%s'", result)
	}
}

func TestTimeMap_GetBeforeFirstTimestamp(t *testing.T) {
	tm := Constructor()

	tm.Set("foo", "bar", 5)

	result := tm.Get("foo", 3)
	if result != "" {
		t.Errorf("Expected empty string, got '%s'", result)
	}
}

func TestTimeMap_MultipleKeys(t *testing.T) {
	tm := Constructor()

	tm.Set("foo", "bar", 1)
	tm.Set("baz", "qux", 2)

	result := tm.Get("foo", 1)
	if result != "bar" {
		t.Errorf("Expected 'bar', got '%s'", result)
	}

	result = tm.Get("baz", 2)
	if result != "qux" {
		t.Errorf("Expected 'qux', got '%s'", result)
	}
}

func TestTimeMap_ComplexScenario(t *testing.T) {
	tm := Constructor()

	tm.Set("love", "high", 10)
	tm.Set("love", "low", 20)

	result := tm.Get("love", 5)
	if result != "" {
		t.Errorf("Expected empty string, got '%s'", result)
	}

	result = tm.Get("love", 10)
	if result != "high" {
		t.Errorf("Expected 'high', got '%s'", result)
	}

	result = tm.Get("love", 15)
	if result != "high" {
		t.Errorf("Expected 'high', got '%s'", result)
	}

	result = tm.Get("love", 20)
	if result != "low" {
		t.Errorf("Expected 'low', got '%s'", result)
	}

	result = tm.Get("love", 25)
	if result != "low" {
		t.Errorf("Expected 'low', got '%s'", result)
	}
}

func TestTimeMap_ManyTimestamps(t *testing.T) {
	tm := Constructor()

	tm.Set("key", "val1", 1)
	tm.Set("key", "val2", 3)
	tm.Set("key", "val3", 5)
	tm.Set("key", "val4", 7)
	tm.Set("key", "val5", 9)

	result := tm.Get("key", 2)
	if result != "val1" {
		t.Errorf("Expected 'val1', got '%s'", result)
	}

	result = tm.Get("key", 4)
	if result != "val2" {
		t.Errorf("Expected 'val2', got '%s'", result)
	}

	result = tm.Get("key", 6)
	if result != "val3" {
		t.Errorf("Expected 'val3', got '%s'", result)
	}

	result = tm.Get("key", 8)
	if result != "val4" {
		t.Errorf("Expected 'val4', got '%s'", result)
	}

	result = tm.Get("key", 10)
	if result != "val5" {
		t.Errorf("Expected 'val5', got '%s'", result)
	}
}

func TestTimeMap_EmptyMapGet(t *testing.T) {
	tm := Constructor()

	result := tm.Get("any", 100)
	if result != "" {
		t.Errorf("Expected empty string, got '%s'", result)
	}
}

func TestTimeMap_SingleValueMultipleGets(t *testing.T) {
	tm := Constructor()

	tm.Set("alpha", "beta", 50)

	result := tm.Get("alpha", 50)
	if result != "beta" {
		t.Errorf("Expected 'beta', got '%s'", result)
	}

	result = tm.Get("alpha", 100)
	if result != "beta" {
		t.Errorf("Expected 'beta', got '%s'", result)
	}

	result = tm.Get("alpha", 1000)
	if result != "beta" {
		t.Errorf("Expected 'beta', got '%s'", result)
	}
}

func TestTimeMap_ExactTimestampMatches(t *testing.T) {
	tm := Constructor()

	tm.Set("test", "a", 10)
	tm.Set("test", "b", 20)
	tm.Set("test", "c", 30)

	result := tm.Get("test", 10)
	if result != "a" {
		t.Errorf("Expected 'a', got '%s'", result)
	}

	result = tm.Get("test", 20)
	if result != "b" {
		t.Errorf("Expected 'b', got '%s'", result)
	}

	result = tm.Get("test", 30)
	if result != "c" {
		t.Errorf("Expected 'c', got '%s'", result)
	}
}
