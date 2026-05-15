# 244. Shortest Word Distance II
# Topics: 'Two Pointers', 'Array', 'Hash Table', 'String', 'Design'
# Level: 'Medium'

# Design a data structure that will be initialized with a string array, and then it should answer queries of the shortest distance between two different strings from the array.

# Implement the WordDistance class:

#     WordDistance(String[] wordsDict) initializes the object with the strings array wordsDict.

#     int shortest(String word1, String word2) returns the shortest distance between word1 and word2 in the array wordsDict.

# Example 1:

# Input:
# ["WordDistance", "shortest", "shortest"]
# [[["practice", "makes", "perfect", "coding", "makes"]], ["coding", "practice"], ["makes", "coding"]]

# Output:
# [null, 3, 1]

# Explanation:
# WordDistance wordDistance = new WordDistance(["practice", "makes", "perfect", "coding", "makes"]);
# wordDistance.shortest("coding", "practice"); // return 3
# wordDistance.shortest("makes", "coding");    // return 1


# Constraints:

#     1 <= wordsDict.length <= 3 * 10⁴
#     1 <= wordsDict[i].length <= 10
#     wordsDict[i] consists of lowercase English letters.
#     word1 and word2 are in wordsDict.
#     word1 != word2
#     At most 5000 calls will be made to shortest.

import math
from typing import List

class WordDistance:

    def __init__(self, wordsDict: List[str]):
        N = len(wordsDict)
        self.m = {}
        for i in range(N):
            word = wordsDict[i]
            if word in self.m:
                self.m[word].append(i)
            else:
                self.m[word] = [i]
            


    def shortest(self, word1: str, word2: str) -> int:
        i1, i2 = 0, 0
        words1 = self.m[word1]
        words2 = self.m[word2]

        res = math.inf
        while i1 < len(words1) and i2 < len(words2):
            res = min(res, abs(words1[i1]-words2[i2]))
            if res == 1:
                break
            if words1[i1] < words2[i2]:
                i1 += 1
            else:
                i2 += 1
        return res


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
