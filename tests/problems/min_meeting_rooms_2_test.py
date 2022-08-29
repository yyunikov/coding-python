import pytest

from src.problems.min_meeting_rooms_2_priority_queue import Solution as SolutionPriorityQueue
from src.problems.min_meeting_rooms_2_heapq import Solution as SolutionHeapq


@pytest.mark.parametrize(
    "intervals,expected",
    [
        ([[0, 30], [5, 10], [15, 20]], 2),
        ([[7, 10], [2, 4]], 1),
        ([[1, 5], [8, 9], [8, 9]], 2),
        ([[9, 10], [4, 9], [4, 17]], 2)
    ],
)
def test_solution_priority_queue(intervals, expected):
    assert SolutionPriorityQueue().minMeetingRooms(intervals) == expected


@pytest.mark.parametrize(
    "intervals,expected",
    [
        ([[0, 30], [5, 10], [15, 20]], 2),
        ([[7, 10], [2, 4]], 1),
        ([[1, 5], [8, 9], [8, 9]], 2),
        ([[9, 10], [4, 9], [4, 17]], 2)
    ],
)
def test_solution_priority_queue(intervals, expected):
    assert SolutionHeapq().minMeetingRooms(intervals) == expected
