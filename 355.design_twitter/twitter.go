// 355. Design twitter
// Topics: 'Hash Table', 'Design', 'Linked List', 'Heap (Priority Queue)'
// Level: 'Medium'

// Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

// Implement the Twitter class:

//     Twitter() Initializes your twitter object.
//     void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
//     List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
//     void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
//     void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.

// Example 1:

// Input
// ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
// [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
// Output
// [null, null, [5], null, null, [6, 5], null, [5]]

// Explanation
// Twitter twitter = new Twitter();
// twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
// twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
// twitter.follow(1, 2);    // User 1 follows user 2.
// twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
// twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
// twitter.unfollow(1, 2);  // User 1 unfollows user 2.
// twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.

// Constraints:

//     1 <= userId, followerId, followeeId <= 500
//     0 <= tweetId <= 104
//     All the tweets have unique IDs.
//     At most 3 * 104 calls will be made to postTweet, getNewsFeed, follow, and unfollow.
//     A user cannot follow himself.

package designtwitter

import (
	"container/heap"
)

var ts int

type Twitter struct {
	followees map[int]map[int]struct{}
	tweets    map[int]tweetsfeed
}

func Constructor() Twitter {
	return Twitter{
		followees: map[int]map[int]struct{}{},
		tweets:    map[int]tweetsfeed{},
	}
}

func (t *Twitter) PostTweet(userId int, tweetId int) {
	tweets, ok := t.tweets[userId]
	if !ok {
		tweets = tweetsfeed{}
	}
	ts++
	tweets = append(tweets, message{ts: ts, id: tweetId})
	t.tweets[userId] = tweets
}

func (t *Twitter) GetNewsFeed(userId int) []int {
	tweets, ok := t.tweets[userId]
	if !ok {
		tweets = tweetsfeed{}
	}
	tweets = tweets.getLast10()
	heap.Init(&tweets)
	followees := t.followees[userId]
	for k := range followees {
		followeetweets, ok := t.tweets[k]
		if !ok {
			continue
		}
		for _, t := range followeetweets.getLast10() {
			heap.Push(&tweets, t)
		}
	}
	return tweets.get10()
}

func (t *Twitter) Follow(followerId int, followeeId int) {
	if followeeId == followerId {
		return
	}
	followees, ok := t.followees[followerId]
	if !ok {
		followees = map[int]struct {
		}{
			followeeId: {},
		}
	} else {
		followees[followeeId] = struct{}{}
	}
	t.followees[followerId] = followees
}

func (t *Twitter) Unfollow(followerId int, followeeId int) {
	followees, ok := t.followees[followerId]
	if ok {
		delete(followees, followeeId)
		t.followees[followerId] = followees
	}
}

type message struct {
	ts int
	id int
}

type tweetsfeed []message

func (t tweetsfeed) Len() int            { return len(t) }
func (t tweetsfeed) Less(i, j int) bool  { return t[i].ts > t[j].ts }
func (t tweetsfeed) Swap(i, j int)       { t[i], t[j] = t[j], t[i] }
func (t *tweetsfeed) Push(x interface{}) { *t = append(*t, x.(message)) }
func (t *tweetsfeed) Pop() interface{} {
	old := *t
	n := len(old)
	x := old[n-1]
	*t = old[:n-1]
	return x
}

// fetches last 10 tweets (no heap)
func (t tweetsfeed) getLast10() []message {
	var msgs []message
	count := 0
	for i := len(t) - 1; i >= 0 && count < 10; i-- {
		msgs = append(msgs, t[i])
		count++
	}
	return msgs
}

func (t *tweetsfeed) get10() []int {
	var ids []int
	for t.Len() > 0 && len(ids) < 10 {
		ids = append(ids, heap.Pop(t).(message).id)
	}
	return ids
}
