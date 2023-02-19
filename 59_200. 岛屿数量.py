from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col):
            grid[row][col] = '0'
            for r, c in directions:
                rowi, coli = r + row, c + col
                if 0 <= rowi < len(grid) and 0 <= coli < len(grid[0]) and grid[rowi][coli] == '1':
                    dfs(rowi, coli)

        row, col = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        res = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    res += 1
                    dfs(r, c)
        return res

s = Solution()
print(s.numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))