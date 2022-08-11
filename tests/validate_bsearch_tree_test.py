import pytest

from problems.validate_bsearch_tree import Solution
from utils.tree_node import TreeNode


@pytest.mark.parametrize(
    "tree,expected",
    [
        (TreeNode(
            2, left=TreeNode(
                1
            ), right=TreeNode(
                3
            )
        ), True),
        (TreeNode(
            5, left=TreeNode(
                4
            ), right=TreeNode(
                6, left=TreeNode(3),
                right=TreeNode(7)
            )
        ), False),
        (TreeNode(
            3, left=TreeNode(
                1, left=TreeNode(0),
                right=TreeNode(2)
            ), right=TreeNode(
                5, left=TreeNode(4),
                right=TreeNode(6)
            )
        ), True)
    ],
)
def test_solution(tree, expected):
    assert Solution().isValidBST(tree) == expected
