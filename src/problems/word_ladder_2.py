"""
PROBLEM

A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
"""
from itertools import chain
from typing import List


class Vertex:
    def __init__(self, value):
        self.value = value
        self.neighbours = {}

    def add_neighbour(self, value: str):
        neighbour = Vertex(value)
        self.neighbours[value] = neighbour
        return neighbour


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        current_node = Vertex(beginWord)

        self.init_graph(current_node, wordList)

        paths = self.find_paths(current_node, endWord)

        min_paths = []
        min_path_len = len(min(paths))
        for path in paths:
            if len(path) == min_path_len:
                min_paths.append(path)

        return min_paths

    def find_paths(self, current_node: Vertex, endWord: str) -> List[List[str]]:
        paths = []
        # this function needs to be fixed
        path = [current_node.value]
        for key, neighbour in current_node.neighbours.items():
            path.append(neighbour.value)
            if neighbour.value == endWord:
                break
            found_paths = self.find_paths(neighbour, endWord)
            path.extend(list(chain.from_iterable(found_paths)))
            paths.append(path)

        return paths

    def init_graph(self, current_node: Vertex, wordList: List[str]):
        for word in wordList:
            if self.is_single_letter_diff(current_node.value, word):
                inserted = current_node.add_neighbour(word)
                copyWordList = wordList.copy()
                copyWordList.remove(word)
                self.init_graph(inserted, copyWordList)

    def add_to_dict(self, dictionary: dict, key: str, value: str):
        if key in dictionary:
            dictionary[key].add(value)
        else:
            dictionary[key] = set(value)

    def is_single_letter_diff(self, word1: str, word2: str) -> bool:
        diff_count = 0
        for ch in word1:
            if ch not in word2:
                diff_count += 1

            if diff_count > 1:
                return False

        return diff_count == 1