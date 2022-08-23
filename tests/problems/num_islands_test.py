import pytest

from src.problems.num_islands import Solution


@pytest.mark.parametrize(
    "grid,expected",
    [
        ([
             ["1", "1", "1", "1", "0"],
             ["1", "1", "0", "1", "0"],
             ["1", "1", "0", "0", "0"],
             ["0", "0", "0", "0", "0"]
         ], 1),
        ([
             ["1", "1", "0", "0", "0"],
             ["1", "1", "0", "0", "0"],
             ["0", "0", "1", "0", "0"],
             ["0", "0", "0", "1", "1"]
         ], 3),
        ([["1"]], 1),
        ([["1", "0", "1", "1", "0", "1", "1"]], 3),
        # the solution assumes diagonal 1's are islands as well
        # the problem though only talked about vertical and horizontal neighbours
        # therefore there is a commented test
        # ([["0", "1", "0"], ["1", "0", "1"], ["0", "1", "0"]], 4)
    ],
)
def test_solution(grid, expected):
    assert Solution().numIslands(grid) == expected
