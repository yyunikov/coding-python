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


class Solution:
    # 1 - 0b0..01
    # 3 - 0b0..11
    # 9 - 0b0..1001
    # 27 - 0b0..11011
    # 81 - 0b0...1010001
    def isPowerOfThree(self, n: int) -> bool:
        """
Knowing the limitation of n, we can now deduce that the maximum value of n that is also a power of three is 1162261467.
Therefore, the possible values of n where we should return true are 3^0, 3^1..3^19.
Since 3 is a prime number, the only divisors of 3^19 are 3^0, 3^1..3^19.
        """

        # this solution can work for any prime number really,
        # by replacing 1162261467 with the largest value smaller than 2^31
        return n >= 1 and 1162261467 % n == 0
