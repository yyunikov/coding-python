import pytest

from src.problems.btree_inorder_traversal import Solution
from src.utils.tree_node import BTreeNode


@pytest.mark.parametrize(
    "root,expected",
    [
        (BTreeNode.of(1), [1]),
        (BTreeNode.of(1, None, 2), [1, 2]),
        (BTreeNode.of(1, 2), [2, 1]),
        (BTreeNode.of(1, 2, 2), [2, 1, 2]),
        (BTreeNode.of(1, None, 2, 3), [1, 3, 2]),
        (None, []),
    ],
)
def test_solution(root, expected):
    assert Solution().inorderTraversal(root) == expected
