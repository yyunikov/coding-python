from collections import defaultdict
from typing import Set, List, Dict

"""
PROBLEM

You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.

Example 1:

Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
Example 2:

Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
Example 3:

Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.
"""


class WordTreeNode:
    def __init__(self):
        self.children = defaultdict(WordTreeNode)


class WordTree:
    def __init__(self):
        self.root = WordTreeNode()

    def insert(self, word, memo: Dict[str, WordTreeNode], parent_node: WordTreeNode):
        if len(word) == 0:
            return

        node = parent_node.children[word]

        for i, ch in enumerate(word):
            word_minus_one_ch = word[:i] + word[i + 1:]
            if word_minus_one_ch in memo:
                node.children[word_minus_one_ch] = memo[word_minus_one_ch]
            else:
                self.insert(word_minus_one_ch, memo, node)
                memo[word_minus_one_ch] = node.children[word_minus_one_ch]


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        memo: Dict[str, WordTreeNode] = dict()

        # would be faster to start from smaller words to re-use them later
        sorted_words = sorted(words, key=lambda w: len(w))

        tree = WordTree()
        for word in sorted_words:
            tree.insert(word, memo, tree.root)
            # this is space inefficient since we store everything in memo
            # probably can be optimized
            memo[word] = tree.root.children[word]

        # traverse the tree and find the longest word chain
        word_chains: Dict[str, int] = dict()

        for word in sorted_words:
            word_chains[word] = self._count_word_chains(tree.root.children[word], word_chains, sorted_words, 1, word)

        return max(word_chains.values())

    def _count_word_chains(self,
                           tree_node: WordTreeNode,
                           word_chains: Dict[str, int],
                           words: List[str],
                           words_count: int,
                           word_to_remove: str) -> int:
        if not tree_node.children:
            return words_count

        words = words.copy()
        words.remove(word_to_remove)
        max_words_count = words_count

        for sub_word in words:
            if sub_word in tree_node.children:
                children_node = tree_node.children[sub_word]
                if sub_word in word_chains:
                    # use previously computed results
                    max_words_count = max(max_words_count, words_count + word_chains[sub_word])
                else:
                    max_words_count = max(max_words_count,
                                          self._count_word_chains(
                                              children_node, word_chains, words, words_count + 1, sub_word)
                                          )

        return max_words_count
