import pytest

from src.algorithms.fibonacci import fib


@pytest.mark.parametrize(
    "num,expected",
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (20, 6765),
    ],
)
def test_fibonacci(num, expected):
    assert fib(num) == expected
