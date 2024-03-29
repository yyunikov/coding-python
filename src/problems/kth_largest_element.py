from queue import PriorityQueue
from typing import List

"""
PROBLEM

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

You must solve it in O(n) time complexity.

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        queue = PriorityQueue()
        for num in nums:
            queue.put(num)

        i = 0
        item = 0
        while i != len(nums) - k + 1:
            item = queue.get()
            i += 1

        return item
