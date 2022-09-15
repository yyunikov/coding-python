from typing import List

"""
PROBLEM

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0

        for i in range(0, len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]

                if current_sum == k:
                    total += 1

        return total
