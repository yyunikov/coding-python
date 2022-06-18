
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