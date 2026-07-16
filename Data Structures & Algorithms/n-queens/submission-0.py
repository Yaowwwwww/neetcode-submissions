class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for row in range(n)]

        colcheck = set() #visited
        posdiag = set() # r + c
        negdiag = set() # r - c

        def dfs(row):
            if row == n:
                res.append(["".join(row) for row in board[:]])
                return

            for col in range(n):
                if (col in colcheck) or ((row + col) in posdiag) or (row - col) in negdiag:
                    continue
                
                colcheck.add(col)
                posdiag.add(row + col)
                negdiag.add(row - col)
                board[row][col] = "Q"

                dfs(row + 1)

                colcheck.remove(col)
                posdiag.remove(row + col)
                negdiag.remove(row - col)
                board[row][col] = "."

        dfs(0)

        return res