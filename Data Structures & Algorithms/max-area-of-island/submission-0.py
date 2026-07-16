class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rlen, clen = len(grid[0]), len(grid)
        area = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= clen or c >= rlen or grid[r][c] != 1:
                return 0
            
            else:
                grid[r][c] = 0 
                add = 0
                for i, j in directions:
                    add += dfs(r + i, c + j)
                return 1 + add
        

        for i in range(clen):
            for j in range(rlen):
                if grid[i][j] == 1:
                    new = dfs(i, j)
                    if new > area:
                        area = new
    
        return area