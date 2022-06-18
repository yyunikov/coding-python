import pytest

from shortest_unsorted_sub_array import Solution


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([2, 6, 4, 8, 10, 9, 15], 5),
        ([4, 1, 5, 9, 10, 12], 2),
        ([1, 2, 3, 4], 0),
        ([1, 3, 2, 2, 2], 4),
        ([1, 2, 3, 3, 3], 0),
        ([5, 4, 3, 2, 1], 5),
        ([3, 2, 3, 2, 4], 4),
        ([2, 3, 3, 2, 4], 3),
        ([1], 0)
    ]
)
def test_find_unsorted_subarray(nums, expected):
    assert Solution().findUnsortedSubarray(nums) == expected
