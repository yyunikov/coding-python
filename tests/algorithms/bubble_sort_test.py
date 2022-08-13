import pytest

from src.algorithms.bubble_sort import bubble_sort


@pytest.mark.parametrize(
    "n,expected",
    [
        ([1, 4, 1, 4], [1, 1, 4, 4]),
        ([7, 5, 1, 3], [1, 3, 5, 7]),
        ([1, 2, 3], [1, 2, 3]),
        ([7, 5, 1, 3, 5, 100, -1, 45], [-1, 1, 3, 5, 5, 7, 45, 100]),
    ],
)
def test_algorithm(n, expected):
    assert bubble_sort(n) == expected
