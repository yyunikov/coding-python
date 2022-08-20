import pytest

from src.problems.climbing_stairs import Solution

test_parameters = [
    (1, 1),
    (2, 2),
    (3, 3),
    (38, 63245986),
]


@pytest.mark.parametrize(
    "num,expected",
    test_parameters,
)
def test_solution(num, expected):
    assert Solution().climbStairs(num) == expected

