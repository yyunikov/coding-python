"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.
"""


class Solution:
    all_numbers = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]

    alphabet = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }

    def intToRoman(self, num: int) -> str:
        if num in self.alphabet:
            return self.alphabet[num]

        return self.simple_int_to_roman(num)

    def simple_int_to_roman(self, num: int) -> str:
        result = ""
        for i, n in enumerate(self.all_numbers):
            if num < n:
                first_symbol = self.alphabet[self.all_numbers[i - 1]]
                left_over = num - self.all_numbers[i - 1]
                num = left_over
                if left_over == 0:
                    result += first_symbol
                    break
                else:
                    result += first_symbol + self.simple_int_to_roman(num)
                    break
            elif num == n:
                return self.alphabet[n]
        else:  # number is > 1000
            result += "M" + self.simple_int_to_roman(num - 1000)

        return result
