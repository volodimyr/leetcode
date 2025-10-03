package designbrowserhistory

import (
	"testing"
)

func TestBrowserHistory(t *testing.T) {
	bh := Constructor("leetcode.com")

	// initial state
	if got := bh.String(); got != "leetcode.com" {
		t.Errorf("expected history leetcode.com, got %s", got)
	}

	// visit google.com
	bh.Visit("google.com")
	if bh.curr.url != "google.com" {
		t.Errorf("expected current google.com, got %s", bh.curr.url)
	}
	if got := bh.String(); got != "leetcode.com -> google.com" {
		t.Errorf("expected history 'leetcode.com -> google.com', got %s", got)
	}

	// visit facebook.com
	bh.Visit("facebook.com")
	if bh.curr.url != "facebook.com" {
		t.Errorf("expected current facebook.com, got %s", bh.curr.url)
	}
	if got := bh.String(); got != "leetcode.com -> google.com -> facebook.com" {
		t.Errorf("expected history 'leetcode.com -> google.com -> facebook.com', got %s", got)
	}

	// visit youtube.com
	bh.Visit("youtube.com")
	if bh.curr.url != "youtube.com" {
		t.Errorf("expected current youtube.com, got %s", bh.curr.url)
	}
	if got := bh.String(); got != "leetcode.com -> google.com -> facebook.com -> youtube.com" {
		t.Errorf("expected history chain mismatch, got %s", got)
	}

	// back(1) -> facebook.com
	if got := bh.Back(1); got != "facebook.com" {
		t.Errorf("Back(1) expected facebook.com, got %s", got)
	}

	// back(1) -> google.com
	if got := bh.Back(1); got != "google.com" {
		t.Errorf("Back(1) expected google.com, got %s", got)
	}

	// forward(1) -> facebook.com
	if got := bh.Forward(1); got != "facebook.com" {
		t.Errorf("Forward(1) expected facebook.com, got %s", got)
	}

	// visit linkedin.com (forward history cleared)
	bh.Visit("linkedin.com")
	if bh.curr.url != "linkedin.com" {
		t.Errorf("expected current linkedin.com, got %s", bh.curr.url)
	}
	if got := bh.String(); got != "leetcode.com -> google.com -> facebook.com -> linkedin.com" {
		t.Errorf("expected history chain with forward cleared, got %s", got)
	}

	// forward(2) -> stays on linkedin.com
	if got := bh.Forward(2); got != "linkedin.com" {
		t.Errorf("Forward(2) expected linkedin.com, got %s", got)
	}

	// back(2) -> google.com
	if got := bh.Back(2); got != "google.com" {
		t.Errorf("Back(2) expected google.com, got %s", got)
	}

	// back(7) -> leetcode.com
	if got := bh.Back(7); got != "leetcode.com" {
		t.Errorf("Back(7) expected leetcode.com, got %s", got)
	}
}
