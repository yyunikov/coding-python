from collections import defaultdict
from typing import List

from queue import PriorityQueue

"""
PROBLEM

You are given an integer array arr. You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.

Example 1:

Input: arr = [3,3,3,3,5,5,5,2,2,7]
Output: 2
Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
Possible sets of size 2 are {3,5},{3,2},{5,2}.
Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has a size greater than half of the size of the old array.
Example 2:

Input: arr = [7,7,7,7,7,7]
Output: 1
Explanation: The only possible set you can choose is {7}. This will make the new array empty.
"""


class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        ints_occurances_dict = defaultdict(lambda: 0)
        ints_occurances_queue = PriorityQueue()

        min_set = set()

        for a in arr:
            ints_occurances_dict[a] += 1  # { 3, 4 times }

        [ints_occurances_queue.put((-value, key)) for key, value in
         ints_occurances_dict.items()]  # ( -4, 3 )

        current_array_length = len(arr)  # 10

        while not ints_occurances_queue.empty():
            queue_item = ints_occurances_queue.get()
            occurances = 0 - queue_item[0]  # 4
            int_value = queue_item[1]  # 3

            min_set.add(int_value)

            if current_array_length - occurances > len(arr) // 2:
                current_array_length -= occurances
            else:
                break

        return len(min_set)


