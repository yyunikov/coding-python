"""
You are given an integer n. We reorder the digits in any order (including the original order)
such that the leading digit is not zero.

Return true if and only if we can do this so that the resulting number is a power of two.

Example 1:

Input: n = 1
Output: true
Example 2:

Input: n = 10
Output: false
"""


class Solution:

    def __init__(self):
        self.all_power_of_two = {1: [[1]]}
        # 2^1=2 - 0b00..0010
        # 2^2=4 - 0b00..0100
        # 2^3=8 - 0b00..1000
        for i in range(1, 32):
            power_of_two = 1 << i
            digits = self._digit_breakdown(power_of_two)
            digits_len = len(digits)
            if digits_len not in self.all_power_of_two:
                self.all_power_of_two[digits_len] = []

            self.all_power_of_two[digits_len].append(digits)

    # Init O(1)
    # Reordered function O(m) where m is a number of digits in n
    def reorderedPowerOf2(self, n: int) -> bool:
        digits = self._digit_breakdown(n)
        all_power_of_two = self.all_power_of_two[len(digits)]

        for power_of_two in all_power_of_two:
            power_of_two_copy = power_of_two.copy()
            for digit in digits:
                if digit in power_of_two_copy:
                    power_of_two_copy.remove(digit)
                else:
                    continue

            if not power_of_two_copy:
                return True

        return False

    def _digit_breakdown(self, n: int):
        n_str = str(n)
        return [int(ch) for ch in n_str]
