import pytest

from problems.binary_tree_cameras import Solution
from utils.tree_node import TreeNode


@pytest.mark.parametrize(
    "root,expected",
    [
        (TreeNode(left=TreeNode(), right=TreeNode()), 1),
        (TreeNode(left=TreeNode(left=TreeNode(), right=TreeNode()), right=None), 1),
        (
            TreeNode(
                left=TreeNode(
                    left=TreeNode(
                        left=TreeNode(left=None, right=TreeNode()), right=None
                    ),
                    right=None,
                ),
                right=None,
            ),
            2,
        ),
        (TreeNode(left=None, right=TreeNode()), 1),
        (
            TreeNode(
                left=TreeNode(
                    left=TreeNode(
                        left=TreeNode(),
                        right=None,
                    ),
                    right=None,
                ),
                right=None,
            ),
            2,
        ),
        (
            TreeNode(
                left=TreeNode(
                    left=None,
                    right=TreeNode(
                        left=TreeNode(left=TreeNode(), right=TreeNode()),
                        right=None,
                    ),
                ),
                right=None,
            ),
            2,
        ),
        (
            TreeNode(
                left=TreeNode(left=TreeNode(), right=None),
                right=TreeNode(left=TreeNode(), right=TreeNode()),
            ),
            2,
        ),
        (
            TreeNode(
                left=TreeNode(
                    left=None,
                    right=TreeNode(
                        left=TreeNode(
                            left=None, right=TreeNode(left=TreeNode(), right=None)
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
