package evaluatereversepolishnotation

import "testing"

func TestEvalRPN_Example1(t *testing.T) {
	tokens := []string{"2", "1", "+", "3", "*"}
	want := 9
	got := evalRPN(tokens)
	if got != want {
		t.Errorf("evalRPN(%v) = %v, want %v", tokens, got, want)
	}
}

func TestEvalRPN_Example2(t *testing.T) {
	tokens := []string{"4", "13", "5", "/", "+"}
	want := 6
	got := evalRPN(tokens)
	if got != want {
		t.Errorf("evalRPN(%v) = %v, want %v", tokens, got, want)
	}
}

func TestEvalRPN_Example3(t *testing.T) {
	tokens := []string{"10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"}
	want := 22
	got := evalRPN(tokens)
	if got != want {
		t.Errorf("evalRPN(%v) = %v, want %v", tokens, got, want)
	}
}

func TestEvalRPN_SingleNumber(t *testing.T) {
	tokens := []string{"42"}
	want := 42
	got := evalRPN(tokens)
	if got != want {
		t.Errorf("evalRPN(%v) = %v, want %v", tokens, got, want)
	}
}

func TestEvalRPN_NegativeNumber(t *testing.T) {
	tokens := []string{"-42"}
	want := -42
	got := evalRPN(tokens)
	if got != want {
		t.Errorf("evalRPN(%v) = %v, want %v", tokens, got, want)
	}
}

func TestEvalRPN_SimpleAddition(t *testing.T) {
	tokens := []string{"1", "2", "+"}
	want := 3
	got := evalRPN(tokens)
	if got != want {
		t.Errorf("evalRPN(%v) = %v, want %v", tokens, got, want)
	}
}

func TestEvalRPN_SimpleSubtraction(t *testing.T) {
	tokens := []string{"5", "3", "-"}
	want := 2
	got := evalRPN(tokens)
	if got != want {
		t.Errorf("evalRPN(%v) = %v, want %v", tokens, got, want)
	}
}

func TestEvalRPN_SimpleMultiplication(t *testing.T) {
	tokens := []string{"6", "7", "*"}
	want := 42
	got := evalRPN(tokens)
	if got != want {
		t.Errorf("evalRPN(%v) = %v, want %v", tokens, got, want)
	}
}

func TestEvalRPN_SimpleDivision(t *testing.T) {
	tokens := []string{"10", "2", "/"}
	want := 5
	got := evalRPN(tokens)
	if got != want {
		t.Errorf("evalRPN(%v) = %v, want %v", tokens, got, want)
	}
}

func TestEvalRPN_DivisionTruncatesTowardZero_Positive(t *testing.T) {
	tokens := []string{"7", "2", "/"}
	want := 3
	got := evalRPN(tokens)
	if got != want {
		t.Errorf("evalRPN(%v) = %v, want %v", tokens, got, want)
	}
}

func TestEvalRPN_DivisionTruncatesTowardZero_Negative(t *testing.T) {
	tokens := []string{"7", "-2", "/"}
	want := -3
	got := evalRPN(tokens)
	if got != want {
		t.Errorf("evalRPN(%v) = %v, want %v", tokens, got, want)
	}
}

func TestEvalRPN_NegativeResults(t *testing.T) {
	tokens := []string{"3", "5", "-"}
	want := -2
	got := evalRPN(tokens)
	if got != want {
		t.Errorf("evalRPN(%v) = %v, want %v", tokens, got, want)
	}
}

func TestEvalRPN_MultipleOperations(t *testing.T) {
	tokens := []string{"15", "7", "1", "1", "+", "-", "/", "3", "*", "2", "1", "1", "+", "+", "-"}
	// ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1))
	// ((15 / (7 - 2)) * 3) - (2 + 2)
	// ((15 / 5) * 3) - 4
	// (3 * 3) - 4
	// 9 - 4
	// 5
	want := 5
	got := evalRPN(tokens)
	if got != want {
		t.Errorf("evalRPN(%v) = %v, want %v", tokens, got, want)
	}
}

func TestEvalRPN_WithZeroOperand(t *testing.T) {
	tokens := []string{"0", "3", "+"}
	want := 3
	got := evalRPN(tokens)
	if got != want {
		t.Errorf("evalRPN(%v) = %v, want %v", tokens, got, want)
	}
}

func TestEvalRPN_ResultIsZero(t *testing.T) {
	tokens := []string{"5", "5", "-"}
	want := 0
	got := evalRPN(tokens)
	if got != want {
		t.Errorf("evalRPN(%v) = %v, want %v", tokens, got, want)
	}
}

func TestEvalRPN_LargeNumbers(t *testing.T) {
	tokens := []string{"100", "200", "+"}
	want := 300
	got := evalRPN(tokens)
	if got != want {
		t.Errorf("evalRPN(%v) = %v, want %v", tokens, got, want)
	}
}

func TestEvalRPN_BoundaryValues(t *testing.T) {
	tokens := []string{"-200", "200", "+"}
	want := 0
	got := evalRPN(tokens)
	if got != want {
		t.Errorf("evalRPN(%v) = %v, want %v", tokens, got, want)
	}
}

func TestEvalRPN_ConsecutiveOperations(t *testing.T) {
	tokens := []string{"1", "2", "+", "3", "+", "4", "+"}
	// ((1 + 2) + 3) + 4 = 10
	want := 10
	got := evalRPN(tokens)
	if got != want {
		t.Errorf("evalRPN(%v) = %v, want %v", tokens, got, want)
	}
}

func TestEvalRPN_AllOperators(t *testing.T) {
	tokens := []string{"2", "3", "+", "4", "*", "5", "/", "6", "-"}
	// (((2 + 3) * 4) / 5) - 6
	// ((5 * 4) / 5) - 6
	// (20 / 5) - 6
	// 4 - 6
	// -2
	want := -2
	got := evalRPN(tokens)
	if got != want {
		t.Errorf("evalRPN(%v) = %v, want %v", tokens, got, want)
	}
}

func TestEvalRPN_ComplexExpression(t *testing.T) {
	tokens := []string{"-78", "-33", "196", "+", "-19", "-", "115", "+", "-", "-99", "/", "-18", "8", "*", "-86", "-", "-", "16", "/", "26", "-14", "-", "-", "47", "-", "101", "-", "163", "*", "143", "-", "0", "-", "171", "+", "120", "*", "-60", "+", "156", "/", "173", "/", "-24", "11", "+", "21", "/", "*", "44", "*", "180", "70", "-40", "-", "*", "86", "132", "-84", "+", "*", "-", "38", "/", "/", "21", "28", "/", "+", "83", "/", "-31", "156", "-", "+", "28", "/", "95", "-", "120", "+", "8", "*", "90", "-", "-94", "*", "-73", "/", "-62", "/", "93", "*", "196", "-", "-59", "+", "187", "-", "143", "/", "-79", "-89", "+", "-"}
	want := 165
	got := evalRPN(tokens)
	if got != want {
		t.Errorf("evalRPN(%v) = %v, want %v", tokens, got, want)
	}
}
