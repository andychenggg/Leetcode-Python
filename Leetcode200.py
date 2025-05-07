from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        bool_grid = [[False for _ in i] for i in grid]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if not bool_grid[i][j] and grid[i][j] == "1":
                    res +=1
                    self.dfs(i, j, grid, bool_grid)
        return res

    def dfs(self, i: int, j: int, grid: List[List[str]], bool_grid: List[List[bool]]) -> None:
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or bool_grid[i][j] or grid[i][j] == "0":
            return
        
        bool_grid[i][j] = True

        self.dfs(i, j+1, grid, bool_grid)
        self.dfs(i, j-1, grid, bool_grid)
        self.dfs(i+1, j, grid, bool_grid)
        self.dfs(i-1, j, grid, bool_grid)
