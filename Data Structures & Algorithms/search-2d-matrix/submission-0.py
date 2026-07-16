class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rowlength = len(matrix[0])
        collength = len(matrix)

        left = 0
        right = rowlength * collength - 1

        while(left <= right):
            midpoint = (left + right) // 2
            col = midpoint % rowlength
            row = midpoint // rowlength

            print("col:"+str(col))
            print("row:"+str(row))

            element = matrix[row][col]
            print("element:"+str(element))

            if element == target:
                return True
            
            if target < element:
                right = midpoint - 1
            elif target > element:
                left = midpoint + 1

        return False
            
    