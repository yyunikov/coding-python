"""
PROBLEM

An integer array original is transformed into a doubled array changed by appending twice the value of every element in original, and then randomly shuffling the resulting array.

Given an array changed, return original if changed is a doubled array. If changed is not a doubled array, return an empty array. The elements in original may be returned in any order.

Example 1:

Input: changed = [1,3,4,2,6,8]
Output: [1,3,4]
Explanation: One possible original array could be [1,3,4]:
- Twice the value of 1 is 1 * 2 = 2.
- Twice the value of 3 is 3 * 2 = 6.
- Twice the value of 4 is 4 * 2 = 8.
Other original arrays could be [4,3,1] or [3,1,4].
Example 2:

Input: changed = [6,3,0,1]
Output: []
Explanation: changed is not a doubled array.
Example 3:

Input: changed = [1]
Output: []
Explanation: changed is not a doubled array.
"""
from collections import defaultdict
from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) <= 1 or len(changed) % 2 != 0:
            return []

        result_list = []

        seen_so_far = defaultdict(int)
        for num in sorted(changed):
            if len(result_list) == len(changed) // 2:
                return result_list

            num_divided_by_two, remainder = divmod(num, 2)
            if remainder == 0 and num_divided_by_two in seen_so_far:
                result_list.append(num_divided_by_two)
                seen_so_far[num_divided_by_two] -= 1
                if seen_so_far[num_divided_by_two] == 0:
                    del seen_so_far[num_divided_by_two]
            else:
                seen_so_far[num] += 1

        if len(result_list) != len(changed) // 2:
            return []

        return result_list
