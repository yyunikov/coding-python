import pytest

from src.problems.power_of_two import Solution


@pytest.mark.parametrize(
    "num,expected",
    [
        (1, True),
        (4, True),
        (2, True),
        (15, False),
        (16, True),
        (256, True),
    ],
)
def test_solution(num, expected):
    assert Solution().isPowerOfTwo(num) == expected
