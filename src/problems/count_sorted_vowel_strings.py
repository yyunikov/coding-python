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
Output: 10
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
Example 3:

Input: n = 5
"""


class Solution:
    count: int = 0

    class Node:
        value: str
        childs = []
        depth: int

        def __init__(self, value, depth):
            self.value = value
            self.depth = depth
            self.childs = []

        def insert(self, value: str, max_depth: int) -> bool:
            if self.depth + 1 > max_depth:
                return False

            if self.childs:
                if value not in list(map(lambda c: c.value, self.childs)):
                    child_node = Solution.Node(value, self.depth + 1)
                    self.childs.append(child_node)
                    if child_node.depth == max_depth:
                        Solution.count += 1

                    return True
                else:
                    inserted = False
                    for child in self.childs:
                        insert_result = child.insert(value, max_depth)
                        if not inserted and insert_result:
                            inserted = True
                    return inserted
            else:
                child_node = Solution.Node(value, self.depth + 1)
                self.childs.append(child_node)
                if child_node.depth == max_depth:
                    Solution.count += 1
                return True

    vowel_trees = {
        'a': Node('a', 1),
        'e': Node('e', 1),
        'i': Node('i', 1),
        'o': Node('o', 1),
        'u': Node('u', 1),
    }

    vowels = ["a", "e", "i", "o", "u"]

    def countVowelStrings(self, n: int) -> int:
        if n == 1:
            return 5

        for i, vowel in enumerate(self.vowels):
            tree = self.vowel_trees[vowel]

            # insert in tree
            for next_vowel in self.vowels[i:]:
                while True:
                    inserted = tree.insert(next_vowel, n)
                    if not inserted:
                        break

        for tree in self.vowel_trees.values():
            self.traverseAndPrint(tree)

        return Solution.count

    def traverseAndPrint(self, tree: Node):
        if not tree.childs:
            print(tree.value)

        for child in tree.childs:
            if tree.depth != 1:
                print(tree.value, end="")
            self.traverseAndPrint(child)
            if tree.depth != 1:
                print(tree.value, end="")


print(Solution().countVowelStrings(3))
