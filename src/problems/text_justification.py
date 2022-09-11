from typing import List

"""
PROBLEM

Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
 

Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.
Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
"""


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        if len(words) == 1:
            return [self._add_trailing_spaces(words[0], maxWidth)]

        output = []
        words_in_line = []
        words_length = 0

        for i in range(0, len(words)):
            word = words[i]
            words_length += len(word)
            words_in_line.append(word)

            # check length with one space between words
            line_length = words_length + len(words_in_line) - 1

            # exceeds the maximum - put the last word to words_in_line
            # and combine the string
            if line_length > maxWidth:
                # remove last word
                last_word = words_in_line.pop() if line_length > maxWidth else None
                if last_word:
                    # adjust length
                    words_length = words_length - len(last_word)
                    line_length = words_length + len(words_in_line) - 1

                if len(words_in_line) == 1:
                    output.append(
                        self._add_trailing_spaces(words_in_line[0], maxWidth))
                else:
                    spaces = self._init_spaces(words_in_line, line_length,
                                               maxWidth, words_length)
                    output.append(
                        self._create_text_line(words_in_line, spaces))

                # reset
                words_in_line = [last_word] if last_word else []
                words_length = len(last_word) if last_word else 0

        # handle the last line
        text_line = ""
        if words_in_line:
            last_line = self._create_text_line(words_in_line, [" "] * (
                        len(words_in_line) - 1))
            last_line = self._add_trailing_spaces(last_line, maxWidth)

            output.append(last_line)

        return output

    def _init_spaces(self, words_in_line: List[str], line_length, maxWidth,
                     words_length) -> List[str]:
        spaces = [" "] * (len(words_in_line) - 1)  # start from one space
        spaces_total = len(spaces)
        space_num = 0
        while line_length != maxWidth:
            if space_num == len(spaces):
                space_num = 0

            spaces[space_num] += " "
            spaces_total += 1

            line_length = words_length + spaces_total
            space_num += 1

        return spaces

    def _create_text_line(self, words_in_line: List[str],
                          spaces: List[str]) -> str:
        text_line = ""
        for i in range(0, len(words_in_line) - 1):
            text_line += words_in_line[i] + spaces[i]
        # add the last word
        text_line += words_in_line[len(words_in_line) - 1]
        return text_line

    def _add_trailing_spaces(self, line, maxWidth) -> str:
        if len(line) != maxWidth:
            # add spaces in the end
            line += (" " * (maxWidth - len(line)))

        return line
