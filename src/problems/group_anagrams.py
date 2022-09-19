from collections import defaultdict
from typing import List, Dict


class Anagram:
    def __init__(self, word: str):
        letter_to_count = defaultdict(int)

        for ch in word:
            letter_to_count[ch] += 1

        letter_counts_temp = []
        for key, value in letter_to_count.items():
            letter_counts_temp.append(key + str(value))

        self.letter_counts_set = frozenset(letter_counts_temp)

    def __eq__(self, other):
        if not other or not isinstance(other, self.__class__):
            return False

        return self.letter_counts_set == other.letter_counts_set

    def __hash__(self):
        return hash(self.letter_counts_set)


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_to_words: Dict[Anagram, List[str]] = defaultdict(lambda: [])

        for s in strs:
            anagram = Anagram(s)
            anagrams_to_words[anagram].append(s)

        result_list = []
        for a, s_list in anagrams_to_words.items():
            result_list.append(s_list)

        return result_list
