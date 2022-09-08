import pytest

from src.problems.validate_bsearch_tree import Solution
from src.utils.tree_node import BTreeNode


@pytest.mark.parametrize(
    "tree,expected",
    [
        (BTreeNode(
            2, left=BTreeNode(
                1
            ), right=BTreeNode(
                3
            )
        ), True),
        (BTreeNode(
            5, left=BTreeNode(
                4
            ), right=BTreeNode(
                6, left=BTreeNode(3),
                right=BTreeNode(7)
            )
        ), False),
        (BTreeNode(
            3, left=BTreeNode(
                1, left=BTreeNode(0),
                right=BTreeNode(2)
            ), right=BTreeNode(
                5, left=BTreeNode(4),
                right=BTreeNode(6)
            )
        ), True)
    ],
)
def test_solution(tree, expected):
    assert Solution().isValidBST(tree) == expected
