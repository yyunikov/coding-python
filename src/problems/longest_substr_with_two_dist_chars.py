from collections import defaultdict
from typing import Dict


"""
PROBLEM

Given a string s, return the length of the longest substring that contains at most two distinct characters.

Example 1:

Input: s = "eceba"
Output: 3
Explanation: The substring is "ece" which its length is 3.
Example 2:

Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5.
"""


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        start: int = 0
        end: int = 1
        chars_freq: Dict[str, int] = defaultdict(int)
        chars_freq[s[0]] = 1
        longest_substring: int = 1

        while start < end:
            if len(chars_freq.keys()) <= 2:
                longest_substring = max(longest_substring, end - start)

            if len(chars_freq.keys()) <= 2 and end < len(s):
                chars_freq[s[end]] += 1
                end += 1
            else:
                chars_freq[s[start]] -= 1
                if chars_freq[s[start]] == 0:
                    del chars_freq[s[start]]
                start += 1

        return longest_substring
