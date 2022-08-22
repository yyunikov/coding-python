from typing import List, Dict

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
        (quotient, remainder) = divmod(len(nums), m)
        max_sub_array_len = quotient if remainder > 0 else quotient
        max_sub_array = 0

        i = 0
        while i < len(nums):
            range_sub_array_len = 1
            range_sub_array_sum = 0
            for j in range(i, i + max_sub_array_len):
                if j < len(nums):
                    range_sub_array_sum += nums[j]
                    max_sub_array = max(max_sub_array, range_sub_array_sum)
                    range_sub_array_len += 1
            i += max_sub_array_len if not remainder or max_sub_array_len == 1 else max_sub_array_len - 1

        return max_sub_array
