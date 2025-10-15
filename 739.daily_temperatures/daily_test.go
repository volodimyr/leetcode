package dailytemperatures

import (
	"reflect"
	"testing"
)

func TestDailyTemperatures_Example1(t *testing.T) {
	temperatures := []int{73, 74, 75, 71, 69, 72, 76, 73}
	expected := []int{1, 1, 4, 2, 1, 1, 0, 0}
	result := dailyTemperatures(temperatures)

	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestDailyTemperatures_Example2(t *testing.T) {
	temperatures := []int{30, 40, 50, 60}
	expected := []int{1, 1, 1, 0}
	result := dailyTemperatures(temperatures)

	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestDailyTemperatures_Example3(t *testing.T) {
	temperatures := []int{30, 60, 90}
	expected := []int{1, 1, 0}
	result := dailyTemperatures(temperatures)

	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestDailyTemperatures_SingleElement(t *testing.T) {
	temperatures := []int{50}
	expected := []int{0}
	result := dailyTemperatures(temperatures)

	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestDailyTemperatures_AllDecreasing(t *testing.T) {
	temperatures := []int{90, 80, 70, 60, 50}
	expected := []int{0, 0, 0, 0, 0}
	result := dailyTemperatures(temperatures)

	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestDailyTemperatures_AllIncreasing(t *testing.T) {
	temperatures := []int{50, 60, 70, 80, 90}
	expected := []int{1, 1, 1, 1, 0}
	result := dailyTemperatures(temperatures)

	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestDailyTemperatures_AllSame(t *testing.T) {
	temperatures := []int{70, 70, 70, 70}
	expected := []int{0, 0, 0, 0}
	result := dailyTemperatures(temperatures)

	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestDailyTemperatures_TwoElements(t *testing.T) {
	temperatures := []int{30, 40}
	expected := []int{1, 0}
	result := dailyTemperatures(temperatures)

	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestDailyTemperatures_LargeGap(t *testing.T) {
	temperatures := []int{30, 35, 32, 33, 80}
	expected := []int{1, 3, 1, 1, 0}
	result := dailyTemperatures(temperatures)

	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}

func TestDailyTemperatures_MultipleWarmerDays(t *testing.T) {
	temperatures := []int{55, 38, 53, 81, 61, 93, 97}
	expected := []int{3, 1, 1, 2, 1, 1, 0}
	result := dailyTemperatures(temperatures)

	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Expected %v, got %v", expected, result)
	}
}
