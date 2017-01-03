#!/usr/bin/env python
class Solution(object):

    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ret_count = 0
        for y in range(0, len(grid)):
            for x in range(0,len(grid[0])):
                if grid[y][x]:
                    ret_count += 4
                    if y+1 < len(grid) and grid[y+1][x]:
                        ret_count -= 2
                    if x+1 < len(grid[0]) and grid[y][x+1]:
                        ret_count -= 2
        return ret_count
