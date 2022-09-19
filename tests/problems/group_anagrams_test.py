import pytest

from src.problems.group_anagrams import Solution


@pytest.mark.parametrize(
    "strs,expected",
    [
        (["eat","tea","tan","ate","nat","bat"], [["eat","tea","ate"],["tan","nat"],
                                                 ["bat"]]),
        ([""], [[""]]),
        (["a"], [["a"]]),
    ],
)
def test_solution(strs, expected):
    assert sorted(expected) == sorted(Solution().groupAnagrams(strs))
