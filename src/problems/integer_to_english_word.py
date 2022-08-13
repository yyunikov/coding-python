"""
PROBLEM
Convert a non-negative integer num to its English words representation.

Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
"""


class Solution:
    dictionary = {
        '0': "Zero",
        '1': "One",
        '2': "Two",
        '3': "Three",
        '4': "Four",
        '5': "Five",
        '6': "Six",
        '7': "Seven",
        '8': "Eight",
        '9': "Nine",
        '10': "Ten",
        '11': "Eleven",
        '12': "Twelve",
        '13': "Thirteen",
        '14': "Fourteen",
        '15': "Fifteen",
        '16': "Sixteen",
        '17': "Seventeen",
        '18': "Eighteen",
        '19': "Nineteen",
        '20': "Twenty",
        '30': "Thirty",
        '40': "Forty",
        '50': "Fifty",
        '60': "Sixty",
        '70': "Seventy",
        '80': "Eighty",
        '90': "Ninety",
    }

    word = ""

    def numberToWords(self, num: int) -> str:
        billion_part = int(num / 1000000000)
        if billion_part != 0:  # billion or more
            self.word = self.full_word() + self.dictionary[str(billion_part)] + " Billion"
            num = num - (billion_part * 1000000000)
            if num == 0:
                return self.word

        million_part = int(num / 1000000)
        if million_part != 0:  # million or more (below billion)
            self.word = self.full_word() + self.three_digit_to_word(million_part) + " Million"
            num = num - (million_part * 1000000)
            if num == 0:
                return self.word

        thousand_part = int(num / 1000)
        if thousand_part != 0:  # thousand or more (below million)
            self.word = self.full_word() + self.three_digit_to_word(thousand_part) + " Thousand"
            num = num - (thousand_part * 1000)
            if num == 0:
                return self.word

        return self.full_word() + self.three_digit_to_word(num)

    def full_word(self):
        return self.word + " " if self.word else ""

    def three_digit_to_word(self, num: int) -> str:
        hundred_part = int(num / 100)
        if hundred_part == 0:  # two digit number
            return self.two_digit_to_word(num)
        else:  # three digit number
            num = num - (hundred_part * 100)
            if num == 0:
                return self.dictionary[str(hundred_part)] + " Hundred"

            return self.dictionary[str(hundred_part)] + " Hundred " + self.two_digit_to_word(num)

    def two_digit_to_word(self, num: int) -> str:
        tenth_part = int(num / 10)
        if tenth_part == 0:  # one digit number
            return self.dictionary[str(num)]
        elif tenth_part == 1:  # two digit number starting from 1
            return self.dictionary[str(num)]
        else:  # two digit number not starting from 1
            one_digit_part = num % 10
            if one_digit_part == 0:
                return self.dictionary[str(tenth_part) + "0"]
            else:
                return self.dictionary[str(tenth_part) + "0"] + " " + self.dictionary[str(one_digit_part)]
