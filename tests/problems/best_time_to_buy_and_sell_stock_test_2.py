import pytest

from src.problems.best_time_to_buy_and_sell_stock_2 import Solution
from src.problems.best_time_to_buy_and_sell_stock_2_simplified import Solution as SolutionSimplified


@pytest.mark.parametrize(
    "prices,expected",
    [
        ([7, 1, 5, 3, 6, 4], 7),
        ([1, 2, 3, 4, 5], 4),
        ([7, 6, 4, 3, 1], 0),
        ([6, 1, 3, 2, 4, 7], 7)
    ],
)
def test_solution(prices, expected):
    assert Solution().maxProfit(prices) == expected


@pytest.mark.parametrize(
    "prices,expected",
    [
        ([7, 1, 5, 3, 6, 4], 7),
        ([1, 2, 3, 4, 5], 4),
        ([7, 6, 4, 3, 1], 0),
        ([6, 1, 3, 2, 4, 7], 7)
    ],
)
def test_solution_simplified(prices, expected):
    assert SolutionSimplified().maxProfit(prices) == expected
