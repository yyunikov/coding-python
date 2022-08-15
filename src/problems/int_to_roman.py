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
    all_numbers = [1, 5, 10, 50, 100, 500, 1000]

    alphabet = {
        1: 'I',
        5: 'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D',
        1000: 'M'
    }

    def intToRoman(self, num: int) -> str:
        if num in self.alphabet:
            return self.alphabet[num]

        result = ""

        while num > 0:
            last_digit = num % 10
            # handle 0
            if last_digit == 0:
                tenths = 1

                while last_digit == 0 and num > 0:
                    part_from_zeros = (num // tenths) % tenths
                    last_digit = part_from_zeros % 10
                    # 40, 90, 400, 900 can be here
                    if last_digit == 4 and tenths == 10:
                        result = "XL" + result
                        num -= 40
                        break
                    elif last_digit == 9 and tenths == 10:
                        result = "XC" + result
                        num -= 90
                        break
                    elif last_digit == 4 and tenths == 100:
                        result = "CD" + result
                        num -= 400
                        break
                    elif last_digit == 9 and tenths == 100:
                        result = "CM" + result
                        num -= 900
                        break
                    elif last_digit == 0:
                        tenths *= 10
                    else:
                        num -= last_digit * tenths
                else:  # no breaks
                    number = last_digit * tenths
                    result = self.simple_int_to_roman(number) + result
            # handle non 0
            else:
                if last_digit == 4:
                    result = "IV" + result
                    num -= 4
                elif last_digit == 9:
                    result = "IX" + result
                    num -= 9
                else:
                    num -= last_digit
                    result = self.simple_int_to_roman(last_digit) + result

        return result

    def simple_int_to_roman(self, simple_num: int) -> str:
        result = ""
        for i, num in enumerate(self.all_numbers):
            if simple_num < num:
                first_symbol = self.alphabet[self.all_numbers[i - 1]]
                left_over = simple_num - self.all_numbers[i - 1]
                simple_num = left_over
                if left_over == 0:
                    result += first_symbol
                    break
                else:
                    result += first_symbol + self.simple_int_to_roman(simple_num)
                    break
            elif simple_num == num:
                return self.alphabet[num]
        else:  # number is > 1000
            result += "M" + self.simple_int_to_roman(simple_num - 1000)

        return result
