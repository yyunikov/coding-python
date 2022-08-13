import sys
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0

        water_total = 0
        current_pool_start = -1
        current_pool_end = -1
        ground_level_height = sys.maxsize

        for i, current_height in enumerate(height):
            # initialize the start of the pool if needed
            if current_pool_start == -1 and current_height != 0:
                current_pool_start = i
                continue

            ground_level_height = min(current_height, ground_level_height)
            # looking for the end of the pool
            if current_pool_start != -1:
                if current_pool_end == -1 or current_height > ground_level_height:
                    current_pool_end = i
                    ground_level_height = height[current_pool_end]

                if height[current_pool_end] >= height[current_pool_start]:  # we've found the end of the pool
                    # find how much water is in the pool
                    # distance between current_pool_start and current_pool_end should be > 1
                    water_total += self.find_water_total(current_pool_start, current_pool_end, height)
                    current_pool_start = current_pool_end
                    current_pool_end = -1
                # keep looking for the end

        # if we reached the end but didn't found the edge of the pool
        if current_pool_start != -1 and current_pool_end != -1:
            water_total += self.find_water_total(current_pool_start, current_pool_end, height)

        return water_total

    def find_water_total(self, current_pool_start: int, current_pool_end: int, height: List[int]) -> int:
        water_total = 0
        highest_edge = max(height[current_pool_start + 1: current_pool_end + 1])
        lowest_edge = min(height[current_pool_start], highest_edge)
        for i, current_height in enumerate(height[current_pool_start: current_pool_end]):
            if current_height < lowest_edge:
                water_total += lowest_edge - current_height
            elif current_height == highest_edge:
                highest_edge = max(height[current_pool_start + i + 1: current_pool_end + 1])
                lowest_edge = min(height[current_pool_start + i], highest_edge)

        return water_total
