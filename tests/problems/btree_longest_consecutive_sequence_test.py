import pytest

from src.problems.btree_longest_consecutive_sequence import Solution
from src.utils.tree_node import TreeNode


@pytest.mark.parametrize(
    "root,expected",
    [
        (TreeNode.of(1), 1),
        (TreeNode.of(1, None, 2), 2),
        (TreeNode.of(1, 2), 2),
        (TreeNode.of(1, 2, 2), 2),
        (TreeNode.of(1, None, 3, 2, 4, None, None, None, 5), 3),
        (TreeNode.of(2, None, 3, 2, None, 1), 2),
        (TreeNode.of(1, 2, 2, 3, None, None, 3, 4, None, None, 4), 4)
    ],
)
def test_solution(root, expected):
    assert Solution().longestConsecutive(root) == expected
