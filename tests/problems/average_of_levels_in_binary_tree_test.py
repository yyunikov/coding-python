import pytest

from src.problems.average_of_levels_in_binary_tree import Solution
from src.utils.tree_node import BTreeNode


@pytest.mark.parametrize(
    "root,expected",
    [
        (BTreeNode(3, left=BTreeNode(9),
                   right=BTreeNode(
                      20, left=BTreeNode(15), right=BTreeNode(7)
                  )),
         [3.00000, 14.50000, 11.00000]
         ),
        (BTreeNode(3, left=BTreeNode(9, left=BTreeNode(15), right=BTreeNode(7)),
                   right=BTreeNode(20)),
         [3.00000, 14.50000, 11.00000]
         ),
    ],
)
def test_solution(root, expected):
    assert Solution().averageOfLevels(root) == expected
