# You are given an array A of non-negative numbers and a target sum S.
# Write an efficient function that finds one continuous sub-sequence of elements which sum up to precisely S.
# The return value should be a pair of array indices or null.

# Examples:
# A = [ 1, 2, 3 ], S = 5. Result = [ 1, 2 ] => brute-force O(n^2)
#

# A = [ 4, 4, 4, 7, 1 ], S = 9. Result = [ 1, 2 ] time - O(n), space O(1)-O(n)
# 9 - 3 - 2 - 7 < 0
# 9 - 2 - 7 == 0 << found it

# 0: 9 - 3 - 2 - 11 < 0 -- over our max sum, jump to 7
#


# sums_at_step (dict): { 0: 3, 1: 3 + 2 = 5, 2: 12 }
# 1st iteration: 0: 3 max(arr[i], sum(sums_at_step[i - 1] + arr[i]))
# 2st iteration: 1: 5
# 3rd iteration: 2: 11
from typing import List


class Solution:

    def find_indexes_for_sum(self, arr: List[int], total: int) -> List[int]:
        # [ 4, 4, 4, 5, 7, 2 ]
        start_pointer = 0
        end_pointer = 1
        current_total = arr[start_pointer]
        current_array = [start_pointer]

        while end_pointer < len(arr):
            current_total += arr[end_pointer]
            current_array.append(end_pointer)

            if arr[end_pointer] > total:
                start_pointer += 1
                end_pointer = start_pointer + 1
                current_total = arr[start_pointer]
                current_array = [start_pointer]
                continue

            if current_total > total:
                start_pointer += 1
                end_pointer = start_pointer + 1
                current_total = arr[start_pointer]
                current_array = [start_pointer]
                continue
            elif current_total == total:
                return current_array

            end_pointer += 1

        return []
