import pytest

from src.algorithms.binary_search import bin_search


@pytest.mark.parametrize(
    "nums,item,expected",
    [
        ([1, 4, 3, 4], 1, 1),
        ([7, 5, 1, 3, 4], 3, 1),
        ([1, 2, 3], 4, -1),
        ([], 1, -1),
    ],
)
def test_algorithm(nums, item, expected):
    assert bin_search(nums, item) == expected
