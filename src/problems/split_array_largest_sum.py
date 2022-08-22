from typing import List

"""
PROBLEM

Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.

Example 1:

Input: nums = [7,2,5,10,8], m = 2
Output: 18
Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
Example 2:

Input: nums = [1,2,3,4,5], m = 2
Output: 9
Example 3:

Input: nums = [1,4,4], m = 3
Output: 4
"""


# note this is not actually correct according to leetcode
# looks like I didn't get the problem right
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        max_sub_array_sum = 0
        (quotient, remainder) = divmod(len(nums), m)
        max_sub_array_len = quotient

        current_sub_array_len = 1
        current_sub_array_sum = 0

        i = 0
        while i < len(nums):
            if current_sub_array_len > max_sub_array_len:
                current_sub_array_len = 1
                current_sub_array_sum = 0
                if max_sub_array_len > 1 and remainder:
                    i -= 1

            current_sub_array_sum += nums[i]
            max_sub_array_sum = max(max_sub_array_sum, current_sub_array_sum)
            current_sub_array_len += 1
            i += 1

        return max_sub_array_sum
