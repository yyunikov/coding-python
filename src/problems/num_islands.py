from collections import defaultdict
from queue import Queue
from typing import List

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


class GraphNode:
    val: str
    neighbours: set
    horizontal_position: int
    vertical_position: int
    level: int

    def __init__(self, val, horizontal_position=0, vertical_position=0, level=0):
        self.val = val
        self.neighbours = set()
        self.horizontal_position = horizontal_position
        self.vertical_position = vertical_position
        self.level = level

    def __eq__(self, other):
        return self.horizontal_position == other.horizontal_position and \
               self.vertical_position == other.vertical_position

    def __hash__(self):
        return hash((self.horizontal_position, self.vertical_position))


# the solution assumes diagonal 1's are islands as well
# the problem though only talked about vertical and horizontal neighbours
# therefore there is a commented test
# this can be figured out based on level_visits
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        root = GraphNode(grid[0][0], 0, 0)
        root.level = 0
        level_visits = {0: 1 if root.val == "1" else 0}
        self.traverse_grid(grid, root, 1, level_visits)

        is_island = False
        islands_number = 0
        for key, value in level_visits.items():
            if not is_island and value >= 1:
                islands_number += 1
                is_island = True
            elif value == 0:
                is_island = False

        return islands_number

    def traverse_grid(self, grid: List[List[str]], current: GraphNode, level: int, level_visits: dict[int, int]):
        vertical_size = len(grid)
        horizontal_size = len(grid[0])

        if current.vertical_position < vertical_size and current.horizontal_position + 1 < horizontal_size:
            right_item = grid[current.vertical_position][current.horizontal_position + 1]
            current.neighbours\
                .add(GraphNode(right_item, current.horizontal_position + 1, current.vertical_position, level))

        if current.horizontal_position < horizontal_size and current.vertical_position + 1 < vertical_size:
            bottom_item = grid[current.vertical_position + 1][current.horizontal_position]
            current.neighbours\
                .add(GraphNode(bottom_item, current.horizontal_position, current.vertical_position + 1, level))

        for neighbour in current.neighbours:
            if level not in level_visits:
                level_visits[level] = 0
            if neighbour.val == "1":
                level_visits[level] += 1
            self.traverse_grid(grid, neighbour, level + 1, level_visits)
