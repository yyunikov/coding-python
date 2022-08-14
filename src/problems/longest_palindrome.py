"""
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

"""


class Solution:

    def longestPalindrome(self, s: str) -> str:
        palindromes = set()
        str_len = len(s)

        if str_len == 1:
            return s
        if str_len < 1 or str_len > 1000:
            return None
        if self.is_palindrome(s):
            return s

        longest_palindrome = None
        longest_palindrome_len = 0

        for i in range(0, str_len):
            current_str = s[i]

            left_border = i - 1
            right_border = i + 1

            while self.is_palindrome(current_str):
                if len(current_str) > longest_palindrome_len:
                    longest_palindrome = current_str
                    longest_palindrome_len = len(current_str)

                palindromes.add(current_str)
                palindromes.add(current_str[::-1])

                # try to expand from left only
                if left_border >= 0:
                    expanded_str = s[left_border] + current_str
                    if self.is_palindrome(expanded_str):
                        current_str = expanded_str
                        # expand left border
                        left_border -= 1
                        continue

                # try to expand the string from both sides
                if left_border >= 0 and right_border < len(s):
                    current_str = s[left_border] + current_str + s[right_border]
                    if self.is_palindrome(current_str):
                        # expand borders
                        left_border -= 1
                        right_border += 1
                        continue
                else:
                    # we've tried all options - no palindrome here
                    break

        return longest_palindrome

    def is_palindrome(self, s: str) -> bool:
        reversed_sub_str = s[::-1]
        return s == reversed_sub_str
