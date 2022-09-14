import pytest

from src.problems.directions_from_btree_node_to_another import Solution
from src.utils.tree_node import BTreeNode


@pytest.mark.parametrize(
    "root,startValue,destValue,expected",
    [
        (BTreeNode.of(5, 1, 2, 3, None, 6, 4), 3, 6, "UURL"),
        (BTreeNode.of(2, 1), 2, 1, "L"),
        (BTreeNode.of(2, None, 1), 2, 1, "R"),
        (BTreeNode.of(2, 1), 1, 2, "U"),
    ],
)
def test_solution(root, startValue, destValue, expected):
    assert Solution().getDirections(root, startValue, destValue) == expected
