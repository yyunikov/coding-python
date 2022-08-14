from typing import List


def max_sub_array(nums: List[int]) -> int:
    current_max = 0
    total_max = 0

    for num in nums:
        current_max = max(num, current_max + num)
        total_max = max(current_max, total_max)

    return total_max
