"""
PROBLEM

(THIS WORKS ONLY FOR POSITIVE NUMBERS)

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
"""
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1 if nums[0] == k else 0

        total = 0
        start_pointer = 0
        end_pointer = 1
        current_total = nums[start_pointer]

        while start_pointer <= end_pointer and start_pointer < len(nums):
            if current_total == k:
                total += 1

            if current_total <= k and end_pointer < len(nums):
                current_total += nums[end_pointer]
                end_pointer += 1
            else:
                first_item = nums[start_pointer]
                start_pointer += 1
                current_total -= first_item

        return total
