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
        ([["0", "1", "0"], ["1", "0", "1"], ["0", "1", "0"]], 4),
        # this test case is still failing, item at coordinates 0, 2 get assigned a different id before the other items
        ([["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]], 1),
    ],
)
def test_solution(grid, expected):
    assert Solution().numIslands(grid) == expected
