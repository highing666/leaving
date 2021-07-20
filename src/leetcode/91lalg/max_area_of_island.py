# -*- coding: utf-8 -*-

from collections import deque
from typing import List

from loguru import logger


class Solution:

    def max_area_of_island(self, grid: List[List[int]]) -> int:
        ans = 0
        for i, row in enumerate(grid):
            for j, _ in enumerate(row):
                ans = max(self.dfs(grid, i, j), ans)
        
        return ans

    def dfs(self, grid: List[List[int]], row_idx: int, col_idx: int) -> int:
        if row_idx < 0 or col_idx < 0 or row_idx == len(grid) or col_idx == len(grid[0]) or grid[row_idx][col_idx] != 1:
            return 0
        
        grid[row_idx][col_idx] = 0
        count = 1
        for i, j in [[0, 1], [0, -1], [-1, 0], [1, 0]]:
            next_row, next_col = row_idx + i, col_idx + j
            count += self.dfs(grid, next_row, next_col)
        
        return count

    def bfs(self, grid: List[List[int]]) -> int:
        ans = 0
        for i, row in enumerate(grid):
            for j, _ in enumerate(row):
                count = 0
                q = deque([(i, j)])
                while q:
                    row_idx, col_idx = q.popleft()
                    if (row_idx < 0 or col_idx < 0 or row_idx == len(grid) or col_idx == len(grid[0])
                            or grid[row_idx][col_idx] != 1):
                        continue
                    count += 1
                    grid[row_idx][col_idx] = 0
                    for di, dj in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
                        next_row, next_col = row_idx + di, col_idx + dj
                        q.append((next_row, next_col))
                
                ans = max(count, ans)
        
        return ans


if __name__ == '__main__':
    test_case = [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]
    test_solution = Solution()
    # res = test_solution.max_area_of_island(test_case)
    # logger.debug(res)
    logger.debug(test_solution.bfs(test_case))
