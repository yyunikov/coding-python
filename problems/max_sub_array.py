from typing import List

"""
PROBLEM 

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub_array = nums[0]
        current_sub_array = nums[0]

        if len(nums) == 1:
            return nums[0]

        for num in nums[1:]:
            current_sub_array = max(num, num + current_sub_array)
            max_sub_array = max(current_sub_array, max_sub_array)

        return max_sub_array
