"""
PROBLEM

Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

Example 1:

Input: n = 27
Output: true
Example 2:

Input: n = 0
Output: false
Example 3:

Input: n = 9
Output: true

"""
from typing import Set


class Solution:
    memo: Set[int] = set()

    # 1 - 0b0..01
    # 3 - 0b0..11
    # 9 - 0b0..1001
    # 27 - 0b0..11011
    # 81 - 0b0...1010001
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True

        if n in self.memo:
            return True

        while n % 3 == 0:
            if n in self.memo:
                return True
            n = n / 3

        if n == 1:
            self.memo.add(n)

        return n == 1