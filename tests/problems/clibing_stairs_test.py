import pytest

from src.problems.climbing_stairs import Solution

from src.problems.climbing_stairs_2 import Solution as Solution2

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


@pytest.mark.parametrize(
    "num,expected",
    test_parameters,
)
def test_solution_2(num, expected):
    assert Solution2().climbStairs(num) == expected
