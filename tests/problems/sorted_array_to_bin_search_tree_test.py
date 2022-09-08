import pytest

from src.problems.sorted_array_to_bin_search_tree import Solution
from src.utils.tree_node import BTreeNode


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([-10, -3, 0, 5, 9], BTreeNode(
            0, left=BTreeNode(
                -3, left=BTreeNode(-10)
            ), right=BTreeNode(
                9, left=BTreeNode(5)
            )
        ))
    ],
)
def test_solution(nums, expected):
    assert Solution().sortedArrayToBST(nums) == expected
