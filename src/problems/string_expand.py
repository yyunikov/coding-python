"""
PROBLEM

Expand the String by parsing the digits and value in brackets.

a2[b]c -> abbc
ab3[abc]dd -> ababcabcabcdd
ab1[a2[b]c]ab3[ba]dd -> ababbcabbababadd
"""


class Solution:

    def expandString(self, s: str) -> str:
        result = ""

        i = 0
        while i < len(s):
            ch = s[i]

            if ch.isdigit():
                start_bracket_index = i + 1  # 4
                sub_str = s[start_bracket_index + 1:]  # abc]zy
                # need to find the end bracket index
                end_bracket_index = self.find_end_bracket_index(s,
                                                                start_bracket_index +
                                                                1)  # abc]zy
                expanded_sub_string = self.expandString(sub_str)  # abc
                i += end_bracket_index - start_bracket_index + 1
                expanded_few_times = int(ch) * expanded_sub_string
                result += expanded_few_times
            elif ch == ']':
                break
            else:
                result += ch
                i += 1

        return result

    def find_end_bracket_index(self, s: str, start_from: int) -> int:
        i = start_from
        bracket_count = 1

        while bracket_count != 0:
            ch = s[i]
            if ch == "[":
                bracket_count += 1
            if ch == "]":
                bracket_count -= 1
            i += 1

        return i
