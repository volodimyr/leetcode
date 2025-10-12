package kokoeatingbananas

import "testing"

func TestMinEatingSpeed_Example1(t *testing.T) {
	piles := []int{3, 6, 7, 11}
	h := 8
	result := minEatingSpeed(piles, h)
	expected := 4
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestMinEatingSpeed_Example2(t *testing.T) {
	piles := []int{30, 11, 23, 4, 20}
	h := 5
	result := minEatingSpeed(piles, h)
	expected := 30
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestMinEatingSpeed_Example3(t *testing.T) {
	piles := []int{30, 11, 23, 4, 20}
	h := 6
	result := minEatingSpeed(piles, h)
	expected := 23
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestMinEatingSpeed_SinglePile(t *testing.T) {
	piles := []int{10}
	h := 10
	result := minEatingSpeed(piles, h)
	expected := 1
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestMinEatingSpeed_SinglePileSingleHour(t *testing.T) {
	piles := []int{100}
	h := 1
	result := minEatingSpeed(piles, h)
	expected := 100
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestMinEatingSpeed_MultiplePilesExactHours(t *testing.T) {
	piles := []int{5, 10, 15, 20}
	h := 4
	result := minEatingSpeed(piles, h)
	expected := 20
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestMinEatingSpeed_AllPilesSameSize(t *testing.T) {
	piles := []int{5, 5, 5, 5}
	h := 8
	result := minEatingSpeed(piles, h)
	expected := 3
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestMinEatingSpeed_MinimumSpeed(t *testing.T) {
	piles := []int{1, 1, 1, 1}
	h := 10
	result := minEatingSpeed(piles, h)
	expected := 1
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestMinEatingSpeed_LargeH(t *testing.T) {
	piles := []int{10, 20, 30}
	h := 100
	result := minEatingSpeed(piles, h)
	expected := 1
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestMinEatingSpeed_TwoPilesMoreHours(t *testing.T) {
	piles := []int{3, 6}
	h := 5
	result := minEatingSpeed(piles, h)
	expected := 2
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestMinEatingSpeed_EdgeCaseRounding(t *testing.T) {
	piles := []int{312884470}
	h := 968709470
	result := minEatingSpeed(piles, h)
	expected := 1
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestMinEatingSpeed_MustEatFaster(t *testing.T) {
	piles := []int{1000000000}
	h := 2
	result := minEatingSpeed(piles, h)
	expected := 500000000
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestMinEatingSpeed_VariedPileSizes(t *testing.T) {
	piles := []int{1, 2, 3, 4, 5}
	h := 10
	result := minEatingSpeed(piles, h)
	expected := 2
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestMinEatingSpeed_TightConstraint(t *testing.T) {
	piles := []int{100, 200, 300}
	h := 6
	result := minEatingSpeed(piles, h)
	expected := 100
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}
