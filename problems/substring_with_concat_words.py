from typing import List

"""
PROBLEM

You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.

You can return the answer in any order.

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
"""


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        words_dict = {}
        for word in words:
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 1

        word_length = len(words[0])
        starting_indexes = []

        for i, ch in enumerate(s):
            current_words_dict = words_dict.copy()
            current_index = i
            while current_words_dict:
                current_word = s[current_index:current_index + word_length]
                if current_word in current_words_dict:
                    current_words_dict[current_word] -= 1
                    if current_words_dict[current_word] == 0:
                        current_words_dict.pop(current_word)

                    current_index = current_index + word_length
                else:
                    break

            if not current_words_dict:
                starting_indexes.append(i)

        return starting_indexes
