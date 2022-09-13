from typing import List


"""
PROBLEM

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda interval: (interval[0], interval[1]))

        i = 1

        while i < len(intervals):
            # previous range includes part of the current range
            if intervals[i - 1][1] >= intervals[i][0]:
                if intervals[i - 1][1] > intervals[i][1]:
                    # previous item fully consumes the current item
                    merged_result = [intervals[i - 1][0], intervals[i - 1][1]]
                else:
                    # previous item partially consumes the current item
                    merged_result = [intervals[i - 1][0], intervals[i][1]]

                intervals = self.merge_with_one(intervals, i, merged_result)
                continue

            i += 1

        return intervals

    def merge_with_one(self, intervals: List[List[int]], i: int,
                       merged_item: List[int]) -> List[List[int]]:
        new_intervals = []
        # merge previous part of array
        if i - 1 > 0:
            new_intervals.extend(intervals[0:i - 1])

        # append merged part
        new_intervals.append(merged_item)

        # merge next part of array
        if i + 1 < len(intervals):
            new_intervals.extend(intervals[i + 1:])

        return new_intervals
