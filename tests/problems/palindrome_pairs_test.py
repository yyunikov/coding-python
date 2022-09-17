import pytest

from src.problems.palindrome_pairs import Solution
from src.problems.palindrome_pairs_brute_force import Solution as SolutionBruteForce

test_cases = [
    (["abcd", "dcba", "lls", "s", "sssll"],
     [[0, 1], [1, 0], [2, 4], [3, 2]]),
    (["bat", "tab", "cat"], [[0, 1], [1, 0]]),
    (["a", ""], [[1, 0], [0, 1]]),
    (["a", "abc", "aba", ""], [[3, 2], [2, 3], [3, 0], [0, 3]]),
    (["abcd", "dcba", "lls", "s", "sssll", ""],
     [[0, 1], [1, 0], [2, 4], [3, 2], [5, 3], [3, 5]]),
    (["abcd", "dcba", "lls", "s", "sssll", "aba", ""],
     [[0, 1], [1, 0], [2, 4], [3, 2], [6, 3], [3, 6], [6, 5], [5, 6]]),
    (["a", "b", "c", "ab", "ac", "aa"],
     [[0, 5], [1, 3], [2, 4], [3, 0], [4, 0], [5, 0]]),
]


@pytest.mark.parametrize(
    "words,expected",
    test_cases,
)
def test_solution(words, expected):
    assert sorted(Solution().palindromePairs(words)) == sorted(expected)


@pytest.mark.parametrize(
    "words,expected",
    test_cases,
)
def test_solution_brute_force(words, expected):
    assert sorted(SolutionBruteForce().palindromePairs(words)) == sorted(expected)
