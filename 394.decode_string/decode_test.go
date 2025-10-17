package decodestring

import "testing"

func TestDecodeString_SimpleRepeat(t *testing.T) {
	input := "eb10[a]"
	expected := "ebaaaaaaaaaa"
	result := decodeString(input)
	if result != expected {
		t.Errorf("decodeString(%q) = %q; want %q", input, result, expected)
	}
}

func TestDecodeString_Complex(t *testing.T) {
	input := "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
	expected := "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"
	result := decodeString(input)
	if result != expected {
		t.Errorf("decodeString(%q) = %q; want %q", input, result, expected)
	}
}

func TestDecodeString_MultipleSimpleRepeats(t *testing.T) {
	input := "3[a]2[bc]"
	expected := "aaabcbc"
	result := decodeString(input)
	if result != expected {
		t.Errorf("decodeString(%q) = %q; want %q", input, result, expected)
	}
}

func TestDecodeString_NestedBrackets(t *testing.T) {
	input := "e3[a2[c]]"
	expected := "eaccaccacc"
	result := decodeString(input)
	if result != expected {
		t.Errorf("decodeString(%q) = %q; want %q", input, result, expected)
	}
}

func TestDecodeString_WithTrailingLetters(t *testing.T) {
	input := "2[abc]3[cd]ef1[f]"
	expected := "abcabccdcdcdeff"
	result := decodeString(input)
	if result != expected {
		t.Errorf("decodeString(%q) = %q; want %q", input, result, expected)
	}
}

func TestDecodeString_SingleLetter(t *testing.T) {
	input := "a"
	expected := "a"
	result := decodeString(input)
	if result != expected {
		t.Errorf("decodeString(%q) = %q; want %q", input, result, expected)
	}
}

func TestDecodeString_MultipleLetters(t *testing.T) {
	input := "abc"
	expected := "abc"
	result := decodeString(input)
	if result != expected {
		t.Errorf("decodeString(%q) = %q; want %q", input, result, expected)
	}
}

func TestDecodeString_DoubleDigitRepeat(t *testing.T) {
	input := "10[a]"
	expected := "aaaaaaaaaa"
	result := decodeString(input)
	if result != expected {
		t.Errorf("decodeString(%q) = %q; want %q", input, result, expected)
	}
}

func TestDecodeString_TripleDigitRepeat(t *testing.T) {
	input := "100[a]"
	expected := "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
	result := decodeString(input)
	if result != expected {
		t.Errorf("decodeString(%q) = %q; want %q", input, result, expected)
	}
}

func TestDecodeString_DeeplyNested(t *testing.T) {
	input := "2[a2[b2[c]]]"
	expected := "abccbccabccbcc"
	result := decodeString(input)
	if result != expected {
		t.Errorf("decodeString(%q) = %q; want %q", input, result, expected)
	}
}

func TestDecodeString_MultipleNested(t *testing.T) {
	input := "2[a2[b]]3[c]"
	expected := "abbabbccc"
	result := decodeString(input)
	if result != expected {
		t.Errorf("decodeString(%q) = %q; want %q", input, result, expected)
	}
}

func TestDecodeString_LeadingLetters(t *testing.T) {
	input := "ab2[c]"
	expected := "abcc"
	result := decodeString(input)
	if result != expected {
		t.Errorf("decodeString(%q) = %q; want %q", input, result, expected)
	}
}

func TestDecodeString_LettersBeforeAndAfter(t *testing.T) {
	input := "a2[b]c"
	expected := "abbc"
	result := decodeString(input)
	if result != expected {
		t.Errorf("decodeString(%q) = %q; want %q", input, result, expected)
	}
}

func TestDecodeString_ComplexNested(t *testing.T) {
	input := "2[ab3[cd]]"
	expected := "abcdcdcdabcdcdcd"
	result := decodeString(input)
	if result != expected {
		t.Errorf("decodeString(%q) = %q; want %q", input, result, expected)
	}
}

func TestDecodeString_SingleRepeat(t *testing.T) {
	input := "1[a]"
	expected := "a"
	result := decodeString(input)
	if result != expected {
		t.Errorf("decodeString(%q) = %q; want %q", input, result, expected)
	}
}

func TestDecodeString_MultiCharacterString(t *testing.T) {
	input := "2[abc]"
	expected := "abcabc"
	result := decodeString(input)
	if result != expected {
		t.Errorf("decodeString(%q) = %q; want %q", input, result, expected)
	}
}
