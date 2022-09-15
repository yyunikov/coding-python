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
from collections import defaultdict
from typing import List


class Solution:
    """
    Explanation:

    The dict will store with the key being any particular sum,
    and the value being the number of times it has happened till the
    current iteration of the loop as we traverse the array from left to right.

    For example:
    k = 26.
    If a sub-array sums up to k, then the sum at the end of this sub-array
    will be sumEnd = sumStart + k. That implies: sumStart = sumEnd - k.
    Suppose, at index 10, sum = 50, and the next 6 numbers are 8,-5,-3,10,15,1.
    At index 13, sum will be 50 again
    (the numbers from indexes 11 to 13 add up to 0).
    Then at index 16, sum = 76.

    Now, when we reach index 16, sum - k = 76 - 26 = 50.
    So, if this is the end index of a sub-array(s) which sums up to k,
    then before this, just before the start of the sub-array,
    the sum should be 50.

    As we found sum = 50 at two places before reaching index 16,
    we indeed have two sub-arrays which sum up to k (26):
    from indexes 14 to 16 and from indexes 11 to 16.
    """

    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1 if nums[0] == k else 0

        total = 0
        sum_end = 0
        sum_occurrences = defaultdict(int)
        sum_occurrences[0] = 1

        for num in nums:
            sum_end += num
            start_sum = sum_end - k
            if start_sum in sum_occurrences:
                total += sum_occurrences[start_sum]

            sum_occurrences[sum_end] += 1

        return total
