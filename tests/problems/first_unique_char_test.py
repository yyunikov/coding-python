import pytest as pytest

from src.problems.first_unique_char import Solution


@pytest.mark.parametrize(
    "s,expected",
    [("loveleetcode", 2), ("leetcode", 0), ("aabb", -1)],
)
def test_solution(s: str, expected):
    assert expected == Solution().firstUniqChar(s)
