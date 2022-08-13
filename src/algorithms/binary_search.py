from typing import List


def bin_search(nums: List[int], item: int) -> int:
    if not nums:
        return -1

    sorted_nums = sorted(nums)
    left = 0
    right = len(sorted_nums)

    while left <= right:
        middle = (left + right) // 2
        if middle < 0 or middle >= len(sorted_nums):
            return - 1

        if item > sorted_nums[middle]:
            left = middle + 1
        elif item < sorted_nums[middle]:
            right = middle - 1
        else:
            return 1

    return -1

