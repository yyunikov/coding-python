import pytest

from src.problems.power_of_n import Solution
from src.problems.power_of_n_brute_force import Solution as SolutionBruteForce


@pytest.mark.parametrize(
    "num,n,expected",
    [
        (1.0, 2, 1),
        (2.00000, 10, 1024.00000),
        (2.10000, 3, 9.261000000000001),
        (2.00000, -2, 0.25000),
        (0.00001, 2147483647, 0),
        (2147483647, 1, 2147483647),
        (0.001, -1, 1000.0),
        (-2.00000, 2, 4),
        (2.00000, -2147483648, 0),
        (-1.00000, 2147483647, -1)
    ],
)
def test_solution(num, n, expected):
    assert Solution().myPow(num, n) == expected


@pytest.mark.parametrize(
    "num,n,expected",
    [
        (1.0, 2, 1),
        (2.00000, 10, 1024.00000),
        (2.10000, 3, 9.261000000000001),
        (2.00000, -2, 0.25000),
        (0.00001, 2147483647, 0),
        (2147483647, 1, 2147483647),
        (0.001, -1, 1000.0),
        (-2.00000, 2, 4),
        (2.00000, -2147483648, 0),
        (-1.00000, 2147483647, -1)
    ],
)
def test_solution_brute_force(num, n, expected):
    assert SolutionBruteForce().myPow(num, n) == expected

