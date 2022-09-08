"""
PROBLEM

Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        start_pointer = 0
        end_pointer = len(s) - 1

        while start_pointer < end_pointer:
            if s[start_pointer] != s[end_pointer]:
                if s[start_pointer + 1] == s[end_pointer]:
                    if self.is_palindrome(s[start_pointer + 1:end_pointer + 1]):
                        return True

                if s[start_pointer] == s[end_pointer - 1]:
                    if self.is_palindrome(s[start_pointer:end_pointer]):
                        return True

                return False

            start_pointer += 1
            end_pointer -= 1

        return True

    def is_palindrome(self, s: str):
        return s == s[::-1]
