import pytest

from src.problems.find_leaves_of_btree import Solution
from src.utils.tree_node import BTreeNode


@pytest.mark.parametrize(
    "root,expected",
    [
        (BTreeNode.of(1, 2, 3, 4, 5), [[4, 5, 3], [2], [1]]),
        (BTreeNode.of(1), [[1]]),
        (BTreeNode.of(1, 2), [[2], [1]]),
        (None, []),
    ],
)
def test_solution(root, expected):
    assert Solution().findLeaves(root) == expected
