from functools import cmp_to_key
from typing import List

"""
PROBLEM

You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

There are two types of logs:

Letter-logs: All words (except the identifier) consist of lowercase English letters.
Digit-logs: All words (except the identifier) consist of digits.
Reorder these logs so that:

The letter-logs come before all digit-logs.
The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
The digit-logs maintain their relative ordering.
Return the final order of the logs.

 

Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
Explanation:
The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".
Example 2:

Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
"""


class Solution:

    def compare_letter_logs(self, log_line1: str, log_line2: str) -> int:
        log_line_str_arr1 = log_line1.split()
        log_line_1_id = log_line_str_arr1[0]
        log_line_1_content = " ".join(log_line_str_arr1[1:])

        log_line_str_arr2 = log_line2.split()
        log_line_2_id = log_line_str_arr2[0]
        log_line_2_content = " ".join(log_line_str_arr2[1:])

        if log_line_1_content == log_line_2_content:
            if log_line_1_id == log_line_2_id:
                return 0
            else:
                return -1 if log_line_1_id < log_line_2_id else 1
        else:
            return -1 if log_line_1_content < log_line_2_content else 1

    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs: List[str] = []
        digit_logs: List[str] = []

        for log in logs:
            log_line_str_arr = log.split()
            identifier = log_line_str_arr[0]
            content = log_line_str_arr[1:]
            if content[0].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)

        output = sorted(letter_logs, key=cmp_to_key(self.compare_letter_logs))
        output.extend(digit_logs)

        return output
