from typing import List


def max_sub_array(nums: List[int]) -> int:
    max_sub_array = nums[0]
    current_sub_array = nums[0]

    if len(nums) == 1:
        return nums[0]

    for num in nums[1:]:
        current_sub_array = max(num, num + current_sub_array)
        max_sub_array = max(current_sub_array, max_sub_array)

    return max_sub_array
