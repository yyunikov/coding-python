import pytest

from src.problems.my_calendar import MyCalendar


@pytest.mark.parametrize(
    "ranges,expected",
    [
        ([[10, 20], [15, 25], [20, 30]], [True, False, True]),
        ([[47, 50], [33, 41], [39, 45], [33, 42], [25, 32], [26, 35], [19, 25],
          [3, 8], [8, 13], [18, 27]],
         [True, True, False, False, True, False, True, True, True, False]),
        ([[40, 49], [40, 49], [49, 50], [49, 50], [27, 34], [23, 30], [39, 46],
          [8, 15], [3, 9], [2, 8], [48, 50], [46, 50], [4, 12], [4, 10],
          [30, 36], [47, 50], [15, 23], [43, 50], [49, 50], [24, 33], [17, 26],
          [3, 11], [45, 50], [3, 8], [32, 40], [37, 43], [5, 13], [0, 9],
          [48, 50], [14, 22]],
         [True, False, True, False, True, False, False, True, False, True,
          False, False, False, False, False, False, True, False, False, False,
          False, False, False, False, False, False, False, False, False,
          False]),
    ]
)
def test_my_calendar(ranges, expected):
    calendar = MyCalendar()

    for i, r in enumerate(ranges):
        assert calendar.book(r[0], r[1]) == expected[i]
