import pytest

from src.problems.lowest_common_ancestor_btree import Solution
from src.utils.tree_node import BTreeNode


@pytest.mark.parametrize(
    "root,p,q,expected",
    [
        (BTreeNode(2, left=BTreeNode(1)), BTreeNode(2), BTreeNode(1), 2),
        (BTreeNode(6, left=BTreeNode(2,
                                     left=BTreeNode(0), right=BTreeNode(4,
                                                                        left=BTreeNode(3),
                                                                        right=BTreeNode(5)
                                                                        )
                                     ), right=BTreeNode(8,
                                                        left=BTreeNode(7),
                                                        right=BTreeNode(9)
                                                        )
                   ), BTreeNode(2), BTreeNode(8), 6
         ),
        (BTreeNode(9, left=BTreeNode(-1,
                                     left=BTreeNode(10, right=BTreeNode(5))
            , right=BTreeNode(3))
            , right=BTreeNode(-4))
         , BTreeNode(3), BTreeNode(5), -1),
    ],
)
def test_solution(root, p: BTreeNode, q: BTreeNode, expected: int):
    assert Solution().lowestCommonAncestor(root, p, q).val == expected
