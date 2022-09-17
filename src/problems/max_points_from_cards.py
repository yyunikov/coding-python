"""
PROBLEM

There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.
In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.
Your score is the sum of the points of the cards you have taken.
Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

Example 1:

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
Example 2:

Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.
Example 3:

Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.
"""


class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        dp_start = []
        dp_end = []

        dp_start.append(cardPoints[0])
        dp_end.append(cardPoints[len(cardPoints) - 1])

        begin = 1
        end = len(cardPoints) - 2

        for i in range(1, k):
            dp_start.append(cardPoints[begin] + dp_start[i - 1])
            dp_end.append(cardPoints[end] + dp_end[i - 1])
            begin += 1
            end -= 1

        max_score = 0
        for i in range(0, k + 1):
            # take i cards from start and k - i from the end
            take_from_start = dp_start[i - 1] if i > 0 else 0
            take_from_end = dp_end[k - i - 1] if k - i > 0 else 0

            current_score = take_from_start + take_from_end
            max_score = max(max_score, current_score)

        return max_score
