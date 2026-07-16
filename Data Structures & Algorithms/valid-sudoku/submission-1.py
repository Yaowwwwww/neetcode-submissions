class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check row
        for row in board:
            row = list(filter(lambda x: x != ".", row))
            if len(row) != len(set(row)):
                return False
        #check column
        for column_index in range(9): # 0-8
            seen = list()
            for row in board:
                item = row[column_index]
                if item != ".":
                    seen.append(item)
            if len(seen) != len(set(seen)):
                return False
        #check box
        for i in range(0, 8, 3): #0, 3, 6
            for j in range(0, 8, 3):
                #check 3*3 box
                seen = list()
                for row in range(i, i + 3):
                    for column in range(j, j + 3):
                        item = board[row][column]
                        if item != ".":
                            seen.append(item)
                if len(seen) != len(set(seen)):
                    return False
        return True

