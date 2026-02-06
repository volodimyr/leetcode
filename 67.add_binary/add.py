# 67. Add Binary
# Topics: 'Math', 'String', 'Bit Manipulation', 'Simulation'

# Given two binary strings a and b, return their sum as a binary string.

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"

# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

 

# Constraints:

#     1 <= a.length, b.length <= 104
#     a and b consist only of '0' or '1' characters.
#     Each string does not contain leading zeros except for the zero itself.


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0

        i, j = len(a)-1, len(b)-1
        while i>=0 or j >=0 or carry > 0:
            da = int(a[i]) if i >= 0 else 0
            db = int(b[j]) if j >= 0 else 0

            total = da + db + carry
            carry = total // 2
            res.append(total % 2)

            i-=1
            j-=1

        res.reverse()
        return ''.join(map(str, res))