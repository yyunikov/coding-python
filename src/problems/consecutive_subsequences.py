from queue import PriorityQueue
from typing import List

"""
PROBLEM

You are given an integer array nums that is sorted in non-decreasing order.

Determine if it is possible to split nums into one or more subsequences such that both of the following conditions are true:

Each subsequence is a consecutive increasing sequence (i.e. each integer is exactly one more than the previous integer).
All subsequences have a length of 3 or more.
Return true if you can split nums according to the above conditions, or false otherwise.

A subsequence of an array is a new array that is formed from the original array by deleting some (can be none) of the elements without disturbing the relative positions of the remaining elements. (i.e., [1,3,5] is a subsequence of [1,2,3,4,5] while [1,3,2] is not).

Example 1:

Input: nums = [1,2,3,3,4,5]
Output: true
Explanation: nums can be split into the following subsequences:
[1,2,3,3,4,5] --> 1, 2, 3
[1,2,3,3,4,5] --> 3, 4, 5
Example 2:

Input: nums = [1,2,3,3,4,4,5,5]
Output: true
Explanation: nums can be split into the following subsequences:
[1,2,3,3,4,4,5,5] --> 1, 2, 3, 4, 5
[1,2,3,3,4,4,5,5] --> 3, 4, 5
Example 3:

Input: nums = [1,2,3,4,4,5]
Output: false
Explanation: It is impossible to split nums into consecutive increasing subsequences of length 3 or more.
"""


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        q = PriorityQueue()
        for num in nums:
            if q.empty():
                q.put((1, [num]))
                continue

            back_to_queue = []
            circuit_break = False
            while not q.empty():
                queue_item = q.get()
                sub_sequence_size = queue_item[0]
                sub_sequence = queue_item[1]

                # circuit break
                if sub_sequence_size < 2 and abs(num - sub_sequence[sub_sequence_size - 1]) > 2:
                    circuit_break = True
                    break

                # is empty or one digit difference
                if abs(num - sub_sequence[sub_sequence_size - 1]) == 1:
                    sub_sequence.append(num)
                    back_to_queue.append(sub_sequence)
                    break
                # if size is 3 or more and the last item has difference for more than 2
                elif sub_sequence_size > 2 and abs(num - sub_sequence[sub_sequence_size - 1]) > 2:
                    # we don't need this item in the queue anymore
                    # no need to return sub_sequence back to queue
                    continue
                elif q.empty():
                    # save back item
                    back_to_queue.append(sub_sequence)
                    # initialize new sub sequence
                    back_to_queue.append([num])
                    break
                else:
                    # save back item
                    back_to_queue.append(sub_sequence)

            [q.put((len(s), s)) for s in back_to_queue]

            if circuit_break:
                return False

        return False if q.get()[0] < 3 else True
