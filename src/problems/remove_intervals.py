from typing import List

"""
PROBLEM

A set of real numbers can be represented as the union of several disjoint intervals, where each interval is in the form [a, b). A real number x is in the set if one of its intervals [a, b) contains x (i.e. a <= x < b).

You are given a sorted list of disjoint intervals intervals representing a set of real numbers as described above, where intervals[i] = [ai, bi] represents the interval [ai, bi). You are also given another interval toBeRemoved.

Return the set of real numbers with the interval toBeRemoved removed from intervals. In other words, return the set of real numbers such that every x in the set is in intervals but not in toBeRemoved. Your answer should be a sorted list of disjoint intervals as described above.

Example 1:


Input: intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
Output: [[0,1],[6,7]]
Example 2:


Input: intervals = [[0,5]], toBeRemoved = [2,3]
Output: [[0,2],[3,5]]
Example 3:

Input: intervals = [[-5,-4],[-3,-2],[1,2],[3,5],[8,9]], toBeRemoved = [-1,4]
Output: [[-5,-4],[-3,-2],[4,5],[8,9]]
"""


class Solution:
    def removeInterval(self, intervals: List[List[int]],
                       toBeRemoved: List[int]) -> List[List[int]]:
        result_interval = []

        for interval in intervals:
            current_interval = []

            # interval fully consumes current interval
            if toBeRemoved[0] < interval[0] and toBeRemoved[1] > interval[1]:
                continue
            # if there are no overlap
            elif interval[0] > toBeRemoved[1] or interval[1] < toBeRemoved[0]:
                current_interval.append(interval[0])
                current_interval.append(interval[1])
            # inside the interval
            elif toBeRemoved[0] > interval[0] and toBeRemoved[1] < interval[1]:
                result_interval.append([interval[0], toBeRemoved[0]])

                current_interval.append(toBeRemoved[1])
                current_interval.append(interval[1])
            # part of interval is affected
            else:
                # consumes start of interval with removal end
                if toBeRemoved[0] <= interval[0] and \
                        toBeRemoved[1] < interval[1]:
                    current_interval.append(toBeRemoved[1])
                    current_interval.append(interval[1])
                # consumes end of interval with removal end
                elif toBeRemoved[0] > interval[0] and toBeRemoved[1] > \
                        interval[1]:
                    current_interval.append(interval[0])
                    current_interval.append(toBeRemoved[0])
                # consumes end of interval with removal start
                elif toBeRemoved[0] > interval[0] and toBeRemoved[0] < \
                        interval[1]:
                    current_interval.append(interval[0])
                    current_interval.append(toBeRemoved[0])

            if current_interval:
                result_interval.append(current_interval)

        return result_interval
