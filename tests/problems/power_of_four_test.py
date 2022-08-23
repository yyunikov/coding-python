import pytest

from src.problems.power_of_four import Solution


@pytest.mark.parametrize(
    "num,expected",
    [
        (1, True),
        (4, True),
        (2, False),
        (15, False),
        (16, True),
    ],
)
def test_solution(num, expected):
    assert Solution().isPowerOfFour(num) == expected
