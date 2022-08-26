import pytest

from src.problems.reordered_power_of_two import Solution


@pytest.mark.parametrize(
    "number,expected",
    [(1, True), (10, False), (61, True), (2, True), (821, True)],
)
def test_solution(number, expected):
    assert Solution().reorderedPowerOf2(number) == expected
