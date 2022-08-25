"""
PROBLEM

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dictionary = {}
        for ch in magazine:
            if ch in dictionary:
                dictionary[ch] += 1
            else:
                dictionary[ch] = 1

        for ch in ransomNote:
            if ch not in dictionary:
                return False

            dictionary[ch] = dictionary[ch] - 1
            if dictionary[ch] == 0:
                dictionary.pop(ch, None)

        return True
