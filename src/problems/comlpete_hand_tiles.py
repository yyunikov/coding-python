"""
PROBLEM

Given a tiles (such as "22211") you need to figure out if the tiles is a complete hand.
Tile can be a single digit, pair or three's (three digits).

Complete hand is considered when you have exactly one pair in the tile and zero or more three's.
No single digits are valid for complete hand.

You need to write a function which accepts a tiles string and verifies is that's a complete hand.
"""


def _tile_to_dict(tiles: str) -> dict:
    tile_dict = dict()

    for ch in tiles:
        if ch in tile_dict:
            digit_list = tile_dict[ch]
            was_incremented = False
            # this can be optimized by using a heap instead to come to O(N log N) solution
            for i, digit in enumerate(digit_list):
                # add +1 to reach 3
                if digit < 3:
                    tile_dict[ch][i] += 1
                    was_incremented = True
                    break
                # we already have a 3
                elif digit == 3:
                    continue
            # all are 3's
            if not was_incremented:
                digit_list.append(1)
        else:
            tile_dict[ch] = [1]

    return tile_dict


# O(n ^ 2) - time
# O(n) - space
def complete(tiles: str) -> bool:
    # change representation to dict
    tile_dict = _tile_to_dict(tiles)

    # iterate over it and validate
    number_of_twos = 0
    for digit, occurrences_list in tile_dict.items():
        for occurrences in occurrences_list:
            if number_of_twos > 1:
                return False
            if occurrences == 1:
                return False
            elif occurrences == 2:
                number_of_twos += 1
    return number_of_twos == 1
