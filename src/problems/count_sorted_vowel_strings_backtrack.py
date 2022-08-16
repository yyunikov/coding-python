"""
Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:

Input: n = 1
Output: 5
Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
Example 2:

Input: n = 2
Output: 15
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".

Example 3:

Input: n = 33
Output: 66045
"""


class Solution:
    class Vowel:
        value: str
        index: int

        def __init__(self, value, index):
            self.value = value
            self.index = index

    vowels = {
        1: "a",
        2: "e",
        3: "i",
        4: "o",
        5: "u"
    }

    def countVowelStrings(self, n: int) -> int:
        return self.countVowelStringsRecursive(n, 1)

    def countVowelStringsRecursive(self, n: int, vowel_key: int) -> int:
        if n == 0:
            return 1

        result = 0
        for i in range(vowel_key, len(self.vowels) + 1):
            result += self.countVowelStringsRecursive(n - 1, i)

        return result
