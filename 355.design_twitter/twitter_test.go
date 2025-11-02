package designtwitter

import (
	"reflect"
	"testing"
)

func TestTwitterBasicOperations(t *testing.T) {
	twitter := Constructor()

	twitter.PostTweet(1, 5)
	feed := twitter.GetNewsFeed(1)
	expected := []int{5}
	if !reflect.DeepEqual(feed, expected) {
		t.Errorf("Expected %v, got %v", expected, feed)
	}

	twitter.Follow(1, 2)
	twitter.PostTweet(2, 6)
	feed = twitter.GetNewsFeed(1)
	expected = []int{6, 5}
	if !reflect.DeepEqual(feed, expected) {
		t.Errorf("Expected %v, got %v", expected, feed)
	}

	twitter.Unfollow(1, 2)
	feed = twitter.GetNewsFeed(1)
	expected = []int{5}
	if !reflect.DeepEqual(feed, expected) {
		t.Errorf("Expected %v, got %v", expected, feed)
	}
}

func TestTwitterEmptyFeed(t *testing.T) {
	twitter := Constructor()

	feed := twitter.GetNewsFeed(1)
	if len(feed) != 0 {
		t.Errorf("Expected empty feed, got %v", feed)
	}
}

func TestTwitterMultipleTweets(t *testing.T) {
	twitter := Constructor()

	twitter.PostTweet(1, 1)
	twitter.PostTweet(1, 2)
	twitter.PostTweet(1, 3)
	twitter.PostTweet(1, 4)
	twitter.PostTweet(1, 5)

	feed := twitter.GetNewsFeed(1)
	if len(feed) != 5 {
		t.Errorf("Expected 5 tweets, got %d", len(feed))
	}
}

func TestTwitterMoreThan10Tweets(t *testing.T) {
	twitter := Constructor()

	for i := 1; i <= 15; i++ {
		twitter.PostTweet(1, i)
	}

	feed := twitter.GetNewsFeed(1)
	if len(feed) != 10 {
		t.Errorf("Expected 10 tweets, got %d", len(feed))
	}
}

func TestTwitterMultipleFollowees(t *testing.T) {
	twitter := Constructor()

	twitter.PostTweet(1, 1)
	twitter.PostTweet(2, 2)
	twitter.PostTweet(3, 3)

	twitter.Follow(1, 2)
	twitter.Follow(1, 3)

	feed := twitter.GetNewsFeed(1)
	if len(feed) != 3 {
		t.Errorf("Expected 3 tweets, got %d", len(feed))
	}
}

func TestTwitterUnfollowNonExistent(t *testing.T) {
	twitter := Constructor()

	twitter.PostTweet(1, 1)
	twitter.Unfollow(1, 2)

	feed := twitter.GetNewsFeed(1)
	expected := []int{1}
	if !reflect.DeepEqual(feed, expected) {
		t.Errorf("Expected %v, got %v", expected, feed)
	}
}

func TestTwitterFollowMultipleTimes(t *testing.T) {
	twitter := Constructor()

	twitter.PostTweet(2, 5)
	twitter.Follow(1, 2)
	twitter.Follow(1, 2)

	feed := twitter.GetNewsFeed(1)
	if len(feed) != 1 {
		t.Errorf("Expected 1 tweet, got %d", len(feed))
	}
}

func TestTwitterComplexScenario(t *testing.T) {
	twitter := Constructor()

	twitter.PostTweet(1, 5)
	twitter.PostTweet(2, 3)
	twitter.PostTweet(1, 101)
	twitter.PostTweet(2, 13)
	twitter.PostTweet(2, 10)

	twitter.Follow(1, 2)

	feed := twitter.GetNewsFeed(1)
	if len(feed) > 10 {
		t.Errorf("Expected at most 10 tweets, got %d", len(feed))
	}

	twitter.Unfollow(1, 2)
	feed = twitter.GetNewsFeed(1)

	hasUser2Tweet := false
	for _, tweetId := range feed {
		if tweetId == 3 || tweetId == 13 || tweetId == 10 {
			hasUser2Tweet = true
			break
		}
	}

	if hasUser2Tweet {
		t.Error("Feed should not contain user 2's tweets after unfollow")
	}
}

func TestTwitterNoFollowers(t *testing.T) {
	twitter := Constructor()

	twitter.PostTweet(1, 1)
	twitter.PostTweet(2, 2)

	feed := twitter.GetNewsFeed(1)
	expected := []int{1}
	if !reflect.DeepEqual(feed, expected) {
		t.Errorf("Expected %v, got %v", expected, feed)
	}
}
