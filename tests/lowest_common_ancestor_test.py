import pytest

from problems.lowest_common_ancestor import Solution
from utils.tree_node import TreeNode


@pytest.mark.parametrize(
    "root,p,q,expected",
    [
        (TreeNode(2, left=TreeNode(1)), TreeNode(2), TreeNode(1), 2),
        (TreeNode(6, left=TreeNode(2,
                                   left=TreeNode(0), right=TreeNode(4,
                                                                    left=TreeNode(3),
                                                                    right=TreeNode(5)
                                                                    )
                                   ), right=TreeNode(8,
                                                     left=TreeNode(7),
                                                     right=TreeNode(9)
                                                     )
                  ), TreeNode(2), TreeNode(8), 6
         ),
    ],
)
def test_solution(root, p: TreeNode, q: TreeNode, expected: int):
    assert Solution().lowestCommonAncestor(root, p, q).val == expected
