
"""
PROBLEM

Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.

Example 1:

Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]
Example 3:

Input: words = ["a",""]
Output: [[0,1],[1,0]]
"""
from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        result_list = []

        for i, i_word in enumerate(words):
            for j, j_word in enumerate(words):
                if i == j:
                    continue

                concat_word = i_word + j_word
                if concat_word == concat_word[::-1]:
                    result_list.append([i, j])

        return result_list
