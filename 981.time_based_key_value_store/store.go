// 981. Time based key-value store
// Topics: 'String', 'Binary Search', 'Hash Table', 'Design'

// Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

// Implement the TimeMap class:

//     TimeMap() Initializes the object of the data structure.
//     void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
//     String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

// Example 1:

// Input
// ["TimeMap", "set", "get", "get", "set", "get", "get"]
// [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
// Output
// [null, null, "bar", "bar", null, "bar2", "bar2"]

// Explanation
// TimeMap timeMap = new TimeMap();
// timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
// timeMap.get("foo", 1);         // return "bar"
// timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
// timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
// timeMap.get("foo", 4);         // return "bar2"
// timeMap.get("foo", 5);         // return "bar2"

// Constraints:

//     1 <= key.length, value.length <= 100
//     key and value consist of lowercase English letters and digits.
//     1 <= timestamp <= 107
//     All the timestamps timestamp of set are strictly increasing.
//     At most 2 * 105 calls will be made to set and get.

package timebasedkeyvaluestore

type TimeMap struct {
	m map[string]ts
}

func Constructor() TimeMap {
	return TimeMap{m: map[string]ts{}}
}

func (tm *TimeMap) Set(key string, v string, t int) {
	values, ok := tm.m[key]
	if ok {
		values = append(values, timestamp{value: v, timestamp: t})
		tm.m[key] = values
		return
	}
	tm.m[key] = ts{timestamp{value: v, timestamp: t}}
}

func (tm *TimeMap) Get(key string, timestamp int) string {
	if len(tm.m) == 0 {
		return ""
	}
	values, ok := tm.m[key]
	if !ok {
		return ""
	}

	return values.search(timestamp)
}

type timestamp struct {
	timestamp int
	value     string
}

type ts []timestamp

func (ts ts) search(t int) string {
	L, R := 0, len(ts)-1

	var nearest timestamp
	for L <= R {
		mid := (L + R) / 2
		found := ts[mid]

		if found.timestamp == t {
			return found.value
		}
		if found.timestamp > t {
			R = mid - 1
		} else {
			if nearest.timestamp < found.timestamp {
				nearest = found
			}
			L = mid + 1
		}
	}
	return nearest.value
}
