import pytest

from src.problems.average_of_levels_in_binary_tree import Solution
from src.utils.tree_node import TreeNode


@pytest.mark.parametrize(
    "root,expected",
    [
        (TreeNode(3, left=TreeNode(9),
                  right=TreeNode(
                      20, left=TreeNode(15), right=TreeNode(7)
                  )),
         [3.00000, 14.50000, 11.00000]
         ),
        (TreeNode(3, left=TreeNode(9, left=TreeNode(15), right=TreeNode(7)),
                  right=TreeNode(20)),
         [3.00000, 14.50000, 11.00000]
         ),
    ],
)
def test_solution(root, expected):
    assert Solution().averageOfLevels(root) == expected
