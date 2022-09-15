from typing import List

"""
PROBLEM

Given an array of integers nums and an integer k, 
return the total number of subarrays whose sum equals to k.

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
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1 if nums[0] == k else 0

        total = 0
        sums_at_index = [0]

        i = 1
        while i <= len(nums):
            sums_at_index.append(sums_at_index[i - 1] + nums[i - 1])
            i += 1

        for start in range(0, len(nums)):
            for end in range(start + 1, len(nums) + 1):
                if sums_at_index[end] - sums_at_index[start] == k:
                    total += 1

        return total
