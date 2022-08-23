"""
PROBLEM:

Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16
Example 3:

Input: n = 3
Output: false
"""


class Solution(object):
    # 1=00000001
    # 2=00000010
    # 4=00000100
    # 8=00001000
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        return n & (n - 1) == 0  # set bit with 1 to 0 and verify if it's 0


x = 0b00000000000000000000000000000010
print(x)
print(x << 1)
print(x << 2)
