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
    island_id: str
    val: str
    horizontal_position: int
    vertical_position: int

    def __init__(self, val, vertical_position=0, horizontal_position=0):
        self.val = val
        self.horizontal_position = horizontal_position
        self.vertical_position = vertical_position
        self.island_id = None

    def __eq__(self, other):
        return self.horizontal_position == other.horizontal_position and \
               self.vertical_position == other.vertical_position

    def __hash__(self):
        return hash((self.horizontal_position, self.vertical_position))


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        root = GridItem(grid[0][0])
        root.level = 0
        islands = set()
        # coordinates to grid item
        grid_dict: Dict[Tuple[int, int], GridItem] = {(0, 0): root}
        if root.val == "1":
            root.island_id = str(uuid.uuid4())
            islands.add(root.island_id)

        self.init_grid_dict(grid, root, grid_dict)

        for v in grid_dict.values():
            if v.island_id:
                islands.add(v.island_id)

        return len(islands)

    def init_grid_dict(self,
                       grid: List[List[str]],
                       root: GridItem,
                       grid_dict: Dict[Tuple, GridItem]):
        vertical_size = len(grid)
        horizontal_size = len(grid[0])

        q = Queue()
        q.put(root)

        while not q.empty():
            current = q.get()
            current_coordinates = (current.vertical_position, current.horizontal_position)

            if current_coordinates[0] < vertical_size and current_coordinates[1] + 1 < horizontal_size:
                right_item_coordinates = (current_coordinates[0], current_coordinates[1] + 1)
                right_item = grid[right_item_coordinates[0]][right_item_coordinates[1]]
                item = GridItem(right_item, right_item_coordinates[0], right_item_coordinates[1]) \
                    if right_item_coordinates not in grid_dict else grid_dict[right_item_coordinates]
                if right_item == "1" and current.island_id:
                    item.island_id = current.island_id
                elif right_item == "1" and not item.island_id and not current.island_id:
                    item.island_id = str(uuid.uuid4())
                grid_dict[right_item_coordinates] = item
                q.put(item)

            if current_coordinates[1] < horizontal_size and current_coordinates[0] + 1 < vertical_size:
                bottom_item_coordinates = (current_coordinates[0] + 1, current_coordinates[1])
                bottom_item = grid[bottom_item_coordinates[0]][bottom_item_coordinates[1]]
                item = GridItem(bottom_item, bottom_item_coordinates[0], bottom_item_coordinates[1]) \
                    if bottom_item_coordinates not in grid_dict else grid_dict[bottom_item_coordinates]
                if bottom_item == "1" and current.island_id:
                    item.island_id = current.island_id
                elif bottom_item == "1" and not item.island_id and not current.island_id:
                    item.island_id = str(uuid.uuid4())
                grid_dict[bottom_item_coordinates] = item
                q.put(item)
