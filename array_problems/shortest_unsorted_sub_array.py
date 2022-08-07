from typing import List

"""
Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.

Example 1:

Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Example 2:

Input: nums = [1,2,3,4]
Output: 0
Example 3:

Input: nums = [1]
Output: 0
"""


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = nums.copy()
        sorted_nums.sort()

        start_subarray = len(nums)
        end_subarray = 0

        for i, n in enumerate(nums):
            if sorted_nums[i] != nums[i]:
                start_subarray = min(start_subarray, i)
                end_subarray = max(end_subarray, i)

        return end_subarray - start_subarray + 1 if end_subarray - start_subarray >= 0 else 0
