import pytest

from src.problems.btree_cameras import Solution
from src.utils.tree_node import BTreeNode


@pytest.mark.parametrize(
    "root,expected",
    [
        (BTreeNode(left=BTreeNode(), right=BTreeNode()), 1),
        (BTreeNode(left=BTreeNode(left=BTreeNode(), right=BTreeNode()), right=None), 1),
        (
                BTreeNode(
                left=BTreeNode(
                    left=BTreeNode(
                        left=BTreeNode(left=None, right=BTreeNode()), right=None
                    ),
                    right=None,
                ),
                right=None,
            ),
                2,
        ),
        (BTreeNode(left=None, right=BTreeNode()), 1),
        (
                BTreeNode(
                left=BTreeNode(
                    left=BTreeNode(
                        left=BTreeNode(),
                        right=None,
                    ),
                    right=None,
                ),
                right=None,
            ),
                2,
        ),
        (
                BTreeNode(
                left=BTreeNode(
                    left=None,
                    right=BTreeNode(
                        left=BTreeNode(left=BTreeNode(), right=BTreeNode()),
                        right=None,
                    ),
                ),
                right=None,
            ),
                2,
        ),
        (
                BTreeNode(
                left=BTreeNode(left=BTreeNode(), right=None),
                right=BTreeNode(left=BTreeNode(), right=BTreeNode()),
            ),
                2,
        ),
        (
                BTreeNode(
                left=BTreeNode(
                    left=None,
                    right=BTreeNode(
                        left=BTreeNode(
                            left=None, right=BTreeNode(left=BTreeNode(), right=None)
                        ),
                        right=None,
                    ),
                ),
                right=None,
            ),
                2,
        ),
    ],
)
def test_solution(root, expected):
    assert Solution().minCameraCover(root) == expected
