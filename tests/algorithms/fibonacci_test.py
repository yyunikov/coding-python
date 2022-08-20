import pytest

from src.algorithms.fibonacci import fib, fib_with_lru_cache

test_parameters = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (20, 6765),
]


@pytest.mark.parametrize(
    "num,expected",
    test_parameters,
)
def test_algorithm(num, expected):
    assert fib(num) == expected


@pytest.mark.parametrize(
    "num,expected",
    test_parameters,
)
def test_algorithm_with_lru(num, expected):
    assert fib_with_lru_cache(num) == expected
