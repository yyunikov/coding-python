"""
PROBLEM

You're given a special book which has multiple of endings.
At the same time book has page links, so when you reach a certain page
you're jumping straight away to one of the possible links.

For the example you're given an endings of (4, 5, 6).
And a list of page links where:
- First item in the array corresponds to a page
- Other items in the array correspond to pages it links

[[3, 16, 24]] - 3 is the page, 16 and 24 are possible links

In addition to this you're given an option which corresponds to an index of the link in the array.
For example 1 would correspond to 16 in array below.

You need to return an ending which you've reached if any or -1 if you hit the loop.

Good example:

endings = (25, 26)
choices = [[3, 16, 24], [17, 2, 25]]
option = 2

1 -> 2 -> 3 -> 24 -> 25 (hit the ending!)
          ^ (jump to page 24)

Loop example:

endings = (25, 26)
choices = [[3, 16, 24], [17, 2, 25]]
option = 1

1 -> 2 -> 3 -> 16 -> 17 -> 2 -> 3 -> ...
"""

from typing import List


def findEnding(endings: List[int], choices: List[List[int]],
               option: int) -> int:
    current_page = 1
    choices_dict = {}
    endings_set = set(endings)
    pages_seen = set()

    for choice in choices:
        choices_dict[choice[0]] = choice[1:]

    while True:
        if current_page in pages_seen:
            return -1

        if current_page in endings_set:
            return current_page

        if current_page in choices_dict:
            # jump to new page
            pages_seen.add(current_page)
            current_page = choices_dict[current_page][option - 1]
            continue

        current_page += 1

    raise Exception("Something went wrong")
