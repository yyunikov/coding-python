import pytest

from src.problems.valid_palindrome_2 import Solution


@pytest.mark.parametrize(
    "s,expected",
    [
        ("aba", True),
        ("abca", True),
        ("abc", False),
        ("eedede", True),
        ("tcaac", True),
        ("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga", True),
        ("ebcbbececabbacecbbcbe", True)
    ],
)
def test_solution(s, expected):
    assert Solution().validPalindrome(s) == expected
