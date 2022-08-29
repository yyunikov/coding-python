import heapq
from functools import cmp_to_key
from heapq import heappush, heappop, heapify
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

    def interval_comparator(self, interval1, interval2):
        if interval1[0] < interval2[0]:
            return -1
        elif interval1[0] > interval2[0]:
            return 1
        else:  # if equal
            # put shorter first
            if interval1[1] < interval2[1]:
                return -1
            elif interval1[1] > interval2[1]:
                return 1
            # if they're totally the same
            return 0

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key=cmp_to_key(self.interval_comparator))

        heap = []
        heapify(heap)
        heappush(heap, (sorted_intervals[0][1], 1))
        latest_meeting_room = 1

        for i in range(1, len(sorted_intervals)):
            back_to_queue = []
            while heap:
                min_available_time, meeting_room = heappop(heap)
                if min_available_time <= sorted_intervals[i][0]:
                    # we can put interval into same meeting room
                    heappush(heap, (sorted_intervals[i][1], meeting_room))
                    break
                else:
                    back_to_queue.append((min_available_time, meeting_room))

            if not heap:
                latest_meeting_room += 1
                heappush(heap, (sorted_intervals[i][1], latest_meeting_room))

            heap = list(heapq.merge(heap, back_to_queue))

        return latest_meeting_room
