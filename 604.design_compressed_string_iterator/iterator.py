# 604. Design Compressed String Iterator
# Topics: 'Design', 'String'

# Design and implement a data structure for a compressed string iterator.
# The given compressed string will be in the form: each letter is followed by
# a positive integer representing the number of times this letter appears in the
# uncompressed form.

# Implement the StringIterator class:
# - next() Returns the next character if the original string still has
#   uncompressed characters, otherwise returns a white space.
# - hasNext() Returns true if there is any letter needs to be uncompressed in
#   the original string, otherwise returns false.

# Example 1:
# Input: ["StringIterator", "next", "next", "next", "next", "next", "next", "hasNext", "next", "hasNext"]
#        [["L1e2t1C1o1d1e1"], [], [], [], [], [], [], [], [], []]
# Output: [null, "L", "e", "e", "t", "C", "o", true, "d", true]

# Constraints:
# 1 <= compressedString.length <= 1000
# compressedString consists of lower-case an upper-case English letters and digits.
# The number of a single character repetitions in compressedString is in the range [1, 10^9]
# At most 100 calls will be made to next and hasNext.


class StringIterator:

    def __init__(self, compressedString: str):
        self.compressed = compressedString
        self.cur = 0
        self.cur_count = 0
        i = 1
        n = ''
        while i < len(self.compressed) and self.compressed[i].isdigit():
            n += self.compressed[i]
            i += 1
        if n:
            self.cur_count = int(n)

    def next(self) -> str:
        if not self.hasNext():
            return ' '
        self.cur_count -= 1
        res = self.compressed[self.cur]

        if self.cur_count <= 0:
            self.cur += 1

            while self.cur < len(self.compressed) and self.compressed[self.cur].isdigit():
                self.cur += 1

            i = self.cur + 1
            n = ''
            while i < len(self.compressed) and self.compressed[i].isdigit():
                n += self.compressed[i]
                i += 1
            if n:
                self.cur_count = int(n)

        return res

    def hasNext(self) -> bool:
        return self.cur_count > 0
