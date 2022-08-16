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
from typing import List


class Vertex:
    def __init__(self, value):
        self.value: str = value
        self.neighbours: dict[str, Vertex] = {}

    def add_new_neighbour(self, value: str):
        neighbour = Vertex(value)
        self.neighbours[value] = neighbour
        return neighbour

    def add_neighbour(self, node: 'Vertex'):
        self.neighbours[node.value] = node

    def __eq__(self, other):
        if not other or not isinstance(other, self.__class__):
            return False

        return self.value == other.value and self.neighbours == other.neighbours

    def __hash__(self):
        return hash((self.value, tuple(self.neighbours.keys())))


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) \
            -> List[List[str]]:
        current_node = Vertex(beginWord)

        if beginWord in wordList:
            wordList.remove(beginWord)

        self.init_graph([current_node], wordList)

        paths = self.find_paths(current_node)
        paths_with_end_word = list(filter(lambda p: endWord in p, paths))

        if paths_with_end_word:
            min_paths = []
            min_path_len = len(min(paths_with_end_word))
            for path in paths_with_end_word:
                if len(path) == min_path_len:
                    min_paths.append(path)

            return min_paths
        else:
            return []

    def find_paths(self, current_node: Vertex) -> List[List[str]]:
        # bfs
        queue = [current_node]
        visited = set()
        paths = [[current_node.value]]

        while queue:
            node = queue.pop()

            new_paths = []
            paths_to_remove = []

            if node not in visited and node.neighbours:
                for path in paths:
                    if node.value in path:
                        for neighbour_value, neighbour in node.neighbours.items():
                            new_path = path.copy()
                            new_path.append(neighbour_value)
                            visited.add(node)
                            queue.append(neighbour)

                            new_paths.append(new_path)
                            paths_to_remove.append(path)

            [paths.remove(path) for path in paths_to_remove if path in paths]
            [paths.append(path) for path in new_paths]

        return paths

    def init_graph(self, nodes: List[Vertex], wordList: List[str]):
        if not wordList:
            return

        inserted_nodes = []
        words_to_remove = []

        for node in nodes:
            for word in wordList:
                if self.is_single_letter_diff(node.value, word):
                    inserted = node.add_new_neighbour(word)
                    words_to_remove.append(word)
                    inserted_nodes.append(inserted)

        [wordList.remove(word) for word in words_to_remove if word in wordList]

        self.init_graph(inserted_nodes, wordList)

    def is_single_letter_diff(self, word1: str, word2: str) -> bool:
        diff_count = 0
        for ch in word1:
            if ch not in word2:
                diff_count += 1

            if diff_count > 1:
                return False

        return diff_count == 1
