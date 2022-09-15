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
from typing import List, Dict


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) <= 1 or len(changed) % 2 != 0:
            return []

        result_list = []

        freq = defaultdict(int)
        for num in changed:
            freq[num] += 1

        for num in sorted(changed):
            if len(result_list) == len(changed) // 2:
                return result_list

            if freq[num] > 0:
                self._decrement_freq(freq, num)

                doubled = num * 2
                if doubled in freq:
                    self._decrement_freq(freq, doubled)
                    result_list.append(num)
                else:
                    return []

        if len(result_list) != len(changed) // 2:
            return []

        return result_list

    def _decrement_freq(self, freq: Dict[int, int], num: int):
        freq[num] -= 1
        if freq[num] == 0:
            del freq[num]
