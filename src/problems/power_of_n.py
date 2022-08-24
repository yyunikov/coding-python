"""
PROBLEM

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
"""


class Solution:

    def myPow(self, x: float, n: int) -> float:
        # edge cases
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1 / x
        if x == 0:
            return 0
        if x == 1:
            return 1
        if x == -1 and n > 0:
            return -1
        if x == -1 and n < 0:
            return 1

        x = x if n > 0 else 1 / x
        n = n if n > 0 else abs(n)

        i = 1
        result = x
        last_computed = result
        middle = n // 2

        # fast pow:
        # once we reach the middle
        # then the x^n will be (x^(n/2))^2
        # for example x^10 would be the same as (x^5)^2
        while i <= n:
            if 0 < result <= 0.00001:
                return 0

            if i < middle:
                i += 1
                result = result * x
                last_computed = result
            else:
                if n % 2 == 0:
                    # if even
                    result = last_computed
                    result = result * result
                else:
                    # if odd
                    result = last_computed
                    result = result * result
                    result = result * x

                i += middle

        return result
