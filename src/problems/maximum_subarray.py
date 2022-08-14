from typing import List


def max_sub_array(nums: List[int]) -> int:
    total_max = nums[0]
    current_max = nums[0]

    if len(nums) == 1:
        return nums[0]

    for num in nums[1:]:
        current_max = max(num, num + current_max)
        total_max = max(current_max, total_max)

    return total_max
