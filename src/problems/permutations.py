"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        self.permutations(nums, permutations)
        return permutations

    def permutations(self, nums: List[int], permutations: List[List[int]], i: int = 0):
        if i == len(nums):
            permutations.append(nums)
        for index in range(i, len(nums)):
            # swap
            nums[index], nums[i] = nums[i], nums[index]

            self.permutations(nums.copy(), permutations, i + 1)

            # swap back
            nums[index], nums[i] = nums[i], nums[index]
