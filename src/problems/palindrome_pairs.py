from collections import defaultdict
from typing import Dict, Set, List

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


class TrieNode:

    def __init__(self):
        self.val: str = "_"
        self.kids: Dict[str, "TrieNode"] = defaultdict(TrieNode)
        self.end_of_word: bool = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root

        for ch in word:
            node.kids[ch].val = ch
            node = node.kids[ch]

        node.end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root

        for ch in word:
            if ch in node.kids:
                node = node.kids[ch]
            else:
                return False

        return node.end_of_word

    def find_palindromes_by_prefix(self, prefix: str) -> Set[str]:
        prefix_node = self.root

        for ch in prefix:
            prefix_node = prefix_node.kids[ch]

        palindromes = set()
        # 3 cases:
        # 1) there is a word of the same length that produces palindrome - e.g. tab + bat = tabbat
        # 2) adding a shorter word to a larger word, e.g. s + lls = slls
        # 3) adding a longer word to a shorter word, e.g. ac + a = aca

        # case 1 will cover this
        if prefix_node.end_of_word and len(prefix) > 1:
            palindromes.add(prefix[::-1])
        # case 2 will cover this
        self._find_palindrome_words(prefix_node, prefix, prefix, palindromes)
        # case 3 will cover this
        self._find_palindrome_words(self.root, prefix, "", palindromes)

        return palindromes

    def _find_palindrome_words(self, root: TrieNode, prefix: str,
                               current_word: str, palindromes: Set[str]):
        for val, node in root.kids.items():
            original_word = (current_word + node.val)[::-1]
            full_word = prefix + original_word
            if node.end_of_word and full_word == full_word[::-1]:
                palindromes.add(original_word)

            self._find_palindrome_words(node, prefix, current_word + node.val,
                                        palindromes)


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # construct a trie, node should also contain index in the list
        trie = Trie()
        # create a dictionary of words to indexes
        word_indexes = dict()
        for i, word in enumerate(words):
            trie.insert(word[::-1])
            word_indexes[word] = i

        result_list = []
        # go through word and record it's string,
        # reverse it and search for such string in a trie
        for i, word in enumerate(words):
            palindromes = trie.find_palindromes_by_prefix(word)
            for palindrome in palindromes:
                if word == "":  # special case
                    result_list.append([i, word_indexes[palindrome]])
                    result_list.append([word_indexes[palindrome], i])
                elif i != word_indexes[palindrome]:
                    # we don't want to add same indexes if word is a palindrome
                    result_list.append([i, word_indexes[palindrome]])

        return result_list
