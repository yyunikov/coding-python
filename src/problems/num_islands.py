import uuid
from queue import Queue
from typing import List, Tuple, Dict

"""
PROBLEM

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""


class GridItem:
    val: str
    horizontal_position: int
    vertical_position: int

    def __init__(self, val, vertical_position=0, horizontal_position=0):
        self.val = val
        self.horizontal_position = horizontal_position
        self.vertical_position = vertical_position

    def __eq__(self, other):
        return self.horizontal_position == other.horizontal_position and \
               self.vertical_position == other.vertical_position

    def __hash__(self):
        return hash((self.horizontal_position, self.vertical_position))


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands_num = 0
        vertical_size = len(grid)
        horizontal_size = len(grid[0])

        q = Queue()

        for vertical_coordinate in range(0, vertical_size):
            for horizontal_coordinate in range(0, horizontal_size):
                current_item = grid[vertical_coordinate][horizontal_coordinate]

                if current_item == "1":
                    islands_num += 1
                    q.put(GridItem(current_item, vertical_coordinate, horizontal_coordinate))
                else:
                    continue

                while not q.empty():
                    queued_item = q.get()
                    current_coordinates = (queued_item.vertical_position, queued_item.horizontal_position)

                    # look left
                    if current_coordinates[1] - 1 >= 0:
                        left_item = grid[current_coordinates[0]][current_coordinates[1] - 1]
                        if left_item == "1":
                            item = GridItem(left_item, current_coordinates[0], current_coordinates[1] - 1)
                            q.put(item)
                            grid[current_coordinates[0]][current_coordinates[1] - 1] = "0"

                    # look up
                    if current_coordinates[0] - 1 >= 0:
                        up_item = grid[current_coordinates[0] - 1][current_coordinates[1]]
                        if up_item == "1":
                            item = GridItem(up_item, current_coordinates[0] - 1, current_coordinates[1])
                            q.put(item)
                            grid[current_coordinates[0] - 1][current_coordinates[1]] = "0"

                    # look right
                    if current_coordinates[0] < vertical_size and current_coordinates[1] + 1 < horizontal_size:
                        right_item = grid[current_coordinates[0]][current_coordinates[1] + 1]
                        if right_item == "1":
                            item = GridItem(right_item, current_coordinates[0], current_coordinates[1] + 1)
                            q.put(item)
                            grid[current_coordinates[0]][current_coordinates[1] + 1] = "0"

                    # look bottom
                    if current_coordinates[1] < horizontal_size and current_coordinates[0] + 1 < vertical_size:
                        bottom_item = grid[current_coordinates[0] + 1][current_coordinates[1]]
                        if bottom_item == "1":
                            item = GridItem(bottom_item, current_coordinates[0] + 1, current_coordinates[1])
                            q.put(item)
                            grid[current_coordinates[0] + 1][current_coordinates[1]] = "0"

                    grid[queued_item.vertical_position][queued_item.horizontal_position] = "0"

        return islands_num
