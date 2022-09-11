"""
PROBLEM

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
"""


class Solution:
    mapping = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch in self.mapping:
                stack.append(self.mapping[ch])
            else:
                if not stack:
                    return False

                bracket = stack.pop()
                if bracket != ch:
                    return False

        if stack:
            return False

        return True
