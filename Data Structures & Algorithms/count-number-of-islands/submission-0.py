class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        cl, rl = len(grid), len(grid[0])
        island = 0
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= cl or c >= rl or grid[r][c] == "0":
                return
            else:
                grid[r][c] = "0"
                for i, j in directions:
                    dfs(r + i, c + j)

        for i in range(cl):
            for j in range(rl):
                if grid[i][j] == "1":
                    island += 1
                    dfs(i, j)

        return island