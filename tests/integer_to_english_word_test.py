import pytest as pytest

from problems.integer_to_english_word import Solution


@pytest.mark.parametrize(
    "num,expected",
    [
        (2, "Two"),
        (0, "Zero"),
        (14, "Fourteen"),
        (20, "Twenty"),
        (25, "Twenty Five"),
        (100, "One Hundred"),
        (105, "One Hundred Five"),
        (155, "One Hundred Fifty Five"),
        (1555, "One Thousand Five Hundred Fifty Five"),
        (10555, "Ten Thousand Five Hundred Fifty Five"),
        (20555, "Twenty Thousand Five Hundred Fifty Five"),
        (200555, "Two Hundred Thousand Five Hundred Fifty Five"),
        (5200555, "Five Million Two Hundred Thousand Five Hundred Fifty Five"),
        (12200555, "Twelve Million Two Hundred Thousand Five Hundred Fifty Five"),
        (112200555, "One Hundred Twelve Million Two Hundred Thousand Five Hundred Fifty Five"),
        (2112200555, "Two Billion One Hundred Twelve Million Two Hundred Thousand Five Hundred Fifty Five"),
    ],
)
def test_solution(num: int, expected):
    assert expected == Solution().numberToWords(num)
