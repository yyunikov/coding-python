from collections import defaultdict


"""
PROBLEM

Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        start_index = 0
        end_index = 1

        chars_to_count = defaultdict(int)
        chars_to_count[s[start_index]] = 1
        max_length = 1

        while end_index != len(s):
            ch = s[end_index]

            if ch in chars_to_count:
                if chars_to_count[s[start_index]] - 1 == 0:
                    del chars_to_count[s[start_index]]
                else:
                    chars_to_count[s[start_index]] -= 1

                start_index += 1
            else:
                chars_to_count[ch] += 1
                max_length = max(max_length, len(chars_to_count.keys()))
                end_index += 1

        return max_length
