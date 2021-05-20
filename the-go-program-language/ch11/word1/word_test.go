package word

import "testing"

// TestPalindrome 正例
func TestPalindrome(t *testing.T) {
	if !IsPalindrome("detartrated") {
		t.Error(`IsPalindrome("detartrated") = false`)
	}

	if !IsPalindrome("kayak") {
		t.Error(`IsPalindrome("kayak") = false`)
	}
}

// TestNonPalindrome 负例
func TestNonPalindrome(t *testing.T) {
	if IsPalindrome("palin") {
		t.Error(`IsPalindrome("palin") = true`)
	}
}

// TestFrenchPalindrome 法语回文
func TestFrenchPalindrome(t *testing.T) {
	if !IsPalindrome("été") {
		t.Error(`IsPalindrome("été") = false`)
	}
}

func TestCanalPalindrome(t *testing.T) {
	input := "A man, a plan, a canal: Panama"
	if !IsPalindrome(input) {
		t.Errorf(`IsPalindrome(%q) = false`, input)
	}
}
