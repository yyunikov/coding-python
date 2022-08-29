from heapq import heappush, heappop
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

        heap = []
        heappush(heap, (sorted_intervals[0][1], 1))
        latest_meeting_room = 1

        for i in range(1, len(sorted_intervals)):
            if heap[0][0] <= sorted_intervals[i][0]:
                min_available_time, meeting_room = heappop(heap)
                # we can put interval into same meeting room
                heappush(heap, (sorted_intervals[i][1], meeting_room))
            else:
                latest_meeting_room += 1
                heappush(heap, (sorted_intervals[i][1], latest_meeting_room))

        return latest_meeting_room
