import pytest

from src.problems.sorted_array_to_bin_search_tree import Solution
from src.utils.tree_node import TreeNode


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([-10, -3, 0, 5, 9], TreeNode(
            0, left=TreeNode(
                -3, left=TreeNode(-10)
            ), right=TreeNode(
                9, left=TreeNode(5)
            )
        ))
    ],
)
def test_solution(nums, expected):
    assert Solution().sortedArrayToBST(nums) == expected
