from collections import defaultdict

import pytest

from src.problems.random_pick_with_weight import Solution


@pytest.mark.parametrize(
    "w,expected",
    [
        ([1], {0: 1}),
        ([1, 3], {0: 1, 1: 3})
    ],
)
@pytest.mark.flaky(reruns=100)
# TODO mock random instead
def test_solution(w, expected):
    random_picker = Solution(w)

    executions = defaultdict(lambda: 0)
    for i in range(0, sum(expected.values())):
        index = random_picker.pickIndex()
        executions[index] += 1

    assert executions == expected
