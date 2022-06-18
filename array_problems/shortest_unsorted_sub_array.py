from typing import List


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
