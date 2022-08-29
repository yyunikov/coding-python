from functools import cmp_to_key
from queue import PriorityQueue
from typing import List

"""
PROBLEM

Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1
"""


class Solution:
    # [0,30] -> meeting room 1
    # [5,10] -> meeting room 1 busy, need new room (meeting room 2)
    # [15,20] -> meeting room 1 busy, meeting room 2 available  (meeting room 2)

    # heap: [ (min_available_time: 11): 2, (min_available_time 31: 1) ]

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key=lambda interval: interval[0])

        heap = PriorityQueue()
        heap.put((sorted_intervals[0][1], 1))  # [ (31, 1) ]
        latest_meeting_room = 1

        for i in range(1, len(sorted_intervals)):
            back_to_queue = []
            while not heap.empty():
                min_available_time, meeting_room = heap.get()
                if min_available_time <= sorted_intervals[i][0]:
                    # we can put interval into same meeting room
                    heap.put((sorted_intervals[i][1], meeting_room))
                    break
                else:
                    back_to_queue.append((min_available_time, meeting_room))

            if heap.empty():
                latest_meeting_room += 1
                heap.put((sorted_intervals[i][1], latest_meeting_room))

            [heap.put(i) for i in back_to_queue]

        return latest_meeting_room
