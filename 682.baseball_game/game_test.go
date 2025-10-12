package baseballgame

import "testing"

func TestCalPoints_Example1(t *testing.T) {
	ops := []string{"5", "2", "C", "D", "+"}
	expected := 30
	result := calPoints(ops)
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestCalPoints_Example2(t *testing.T) {
	ops := []string{"5", "-2", "4", "C", "D", "9", "+", "+"}
	expected := 27
	result := calPoints(ops)
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestCalPoints_Example3(t *testing.T) {
	ops := []string{"1", "C"}
	expected := 0
	result := calPoints(ops)
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestCalPoints_SingleNumber(t *testing.T) {
	ops := []string{"10"}
	expected := 10
	result := calPoints(ops)
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestCalPoints_NegativeNumbers(t *testing.T) {
	ops := []string{"-10", "-5"}
	expected := -15
	result := calPoints(ops)
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestCalPoints_DoubleOperation(t *testing.T) {
	ops := []string{"3", "D"}
	expected := 9
	result := calPoints(ops)
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestCalPoints_DoubleNegative(t *testing.T) {
	ops := []string{"-5", "D"}
	expected := -15
	result := calPoints(ops)
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestCalPoints_SumOperation(t *testing.T) {
	ops := []string{"3", "4", "+"}
	expected := 14
	result := calPoints(ops)
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestCalPoints_SumWithNegatives(t *testing.T) {
	ops := []string{"3", "-4", "+"}
	expected := -2
	result := calPoints(ops)
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestCalPoints_CancelOperation(t *testing.T) {
	ops := []string{"5", "10", "C"}
	expected := 5
	result := calPoints(ops)
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestCalPoints_MultipleCancels(t *testing.T) {
	ops := []string{"5", "10", "15", "C", "C"}
	expected := 5
	result := calPoints(ops)
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestCalPoints_AllZeros(t *testing.T) {
	ops := []string{"0", "0", "+"}
	expected := 0
	result := calPoints(ops)
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestCalPoints_ComplexSequence(t *testing.T) {
	ops := []string{"1", "2", "+", "D", "C"}
	expected := 6
	result := calPoints(ops)
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestCalPoints_LargeNumbers(t *testing.T) {
	ops := []string{"30000", "-30000", "+"}
	expected := 0
	result := calPoints(ops)
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestCalPoints_DoubleAfterSum(t *testing.T) {
	ops := []string{"2", "3", "+", "D"}
	expected := 20
	result := calPoints(ops)
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestCalPoints_SumAfterDouble(t *testing.T) {
	ops := []string{"5", "D", "+"}
	expected := 30
	result := calPoints(ops)
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestCalPoints_CancelAfterSum(t *testing.T) {
	ops := []string{"1", "2", "+", "C"}
	expected := 3
	result := calPoints(ops)
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestCalPoints_CancelAfterDouble(t *testing.T) {
	ops := []string{"3", "D", "C"}
	expected := 3
	result := calPoints(ops)
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestCalPoints_AllOperations(t *testing.T) {
	ops := []string{"10", "5", "+", "D", "C", "10"}
	expected := 40
	result := calPoints(ops)
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}
