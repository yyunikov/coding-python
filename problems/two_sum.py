"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = dict()
        for i, n in enumerate(nums):
            if n in nums_dict:
                nums_dict[n].append(i)
            else:
                nums_dict[n] = [i]

        for i, first_item in enumerate(nums):
            second_item = target - first_item
            if second_item in nums_dict:
                second_item_indexes = nums_dict[second_item]
                for second_item_index in second_item_indexes:
                    if second_item_index != i:
                        return [i, second_item_index]
        return []
