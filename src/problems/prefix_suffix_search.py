"""
Design a special dictionary with some words that searchs the words in it by a prefix and a suffix.

Implement the WordFilter class:

- WordFilter(string[] words) Initializes the object with the words in the dictionary.
- f(string prefix, string suffix) Returns the index of the word in the dictionary, which has the prefix prefix and the suffix suffix. If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1.

Examples:

Input
["WordFilter", "f"]
[[["apple"]], ["a", "e"]]
Output
[null, 0]

Explanation
WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = 'e".
"""
from typing import Set, List


class TrieNode:
    symbol: chr
    childs: dict
    end_of_word: bool

    def __init__(self, symbol: chr):
        self.symbol = symbol
        self.childs = {}
        self.end_of_word = False

    def __eq__(self, other):
        return self.symbol == other.symbol and self.end_of_word == other.end_of_word

    def __hash__(self):
        return hash((self.symbol, self.end_of_word))

    def insert(self, symbol: chr):
        node = TrieNode(symbol)
        if node not in self.childs.values():
            self.childs[node] = node
            return node
        else:
            return self.childs.get(node)

    def set_end_of_word(self):
        self.end_of_word = True


class Trie:
    root: TrieNode

    def __init__(self, root: TrieNode):
        self.root = root

    def search(self, prefix: str) -> Set[str]:
        current_prefix_node = self.root
        for p in prefix:
            for child_node in current_prefix_node.childs.values():
                if child_node.symbol == p:
                    current_prefix_node = child_node
                    break

            if current_prefix_node.symbol != p:
                return set()

        words = set()
        if current_prefix_node.end_of_word:
            words.add(prefix)

        self.__find_words(words, prefix, current_prefix_node)
        return words

    def __find_words(self, words: Set[str], prefix: str, start_node: TrieNode):
        for child in start_node.childs:
            if child.end_of_word:
                words.add(prefix + child.symbol)
            else:
                self.__find_words(words, prefix + child.symbol, child)


class WordFilter:
    dictionary = {}
    prefix_trie: Trie
    suffix_trie: Trie

    def __init__(self, words: List[str]):
        self.dictionary = {word: i for i, word in enumerate(words)}
        self.prefix_trie = self.init_prefix_trie(words)
        self.suffix_trie = self.init_suffix_trie(words)

    def f(self, prefix: str, suffix: str) -> int:
        prefix_words = self.prefix_trie.search(prefix)
        if not prefix_words:
            return -1

        suffix_words = self.suffix_trie.search(suffix[::-1])
        if not suffix_words:
            return -1

        # need to reverse words returned from suffix trie to have them in the right order
        suffix_words_reversed = set(map(lambda w: w[::-1], suffix_words))
        words = prefix_words.intersection(suffix_words_reversed)
        max_index = -1
        for word in words:
            index = self.dictionary[word]
            if index > max_index:
                max_index = index

        return max_index

    def init_prefix_trie(self, words: List[str]) -> Trie:
        prefix_trie = Trie(TrieNode('0'))
        for word in words:
            current = prefix_trie.root
            for ch in word:
                current = current.insert(ch)
            current.set_end_of_word()

        return prefix_trie

    def init_suffix_trie(self, words: List[str]) -> Trie:
        suffix_trie = Trie(TrieNode('0'))
        for word in words:
            current = suffix_trie.root
            for ch in word[::-1]:
                current = current.insert(ch)
            current.set_end_of_word()

        return suffix_trie

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
