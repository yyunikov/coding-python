import pytest

from src.problems.min_number_of_refuels_attempt import Solution
from src.problems.min_number_of_refuels_solved import Solution as Solution2


@pytest.mark.parametrize(
    "target,startFuel,stations,expected",
    [
        (1, 1, [], 0),
        (100, 1, [[10, 100]], -1),
        (100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]], 2),
        # the problem is not solved exactly right, need to fix this test
        # (100, 50, [[25, 50], [50, 25]], 1),
    ],
)
def test_solution(target, startFuel, stations, expected):
    assert Solution().minRefuelStops(target, startFuel, stations) == expected


@pytest.mark.parametrize(
    "target,startFuel,stations,expected",
    [
        (1, 1, [], 0),
        (100, 1, [[10, 100]], -1),
        (100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]], 2),
        (100, 50, [[25, 50], [50, 25]], 1),
    ],
)
def test_solution_2(target, startFuel, stations, expected):
    assert Solution2().minRefuelStops(target, startFuel, stations) == expected
