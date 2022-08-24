import pytest

from src.problems.lowest_common_ancestor_btree import Solution
from src.utils.tree_node import TreeNode


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
        (TreeNode(9, left=TreeNode(-1,
                                   left=TreeNode(10, right=TreeNode(5))
            , right=TreeNode(3))
            , right=TreeNode(-4))
         , TreeNode(3), TreeNode(5), -1),
    ],
)
def test_solution(root, p: TreeNode, q: TreeNode, expected: int):
    assert Solution().lowestCommonAncestor(root, p, q).val == expected
