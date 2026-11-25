class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        colNum = len(matrix[0])
        rowNum = len(matrix)

        l, r = 0, colNum - 1

        for i in range(1, len(matrix)):
            if target < matrix[i][0]:
                while l <= r:
                    m = (l + r) // 2
                    if target < matrix[i-1][m]:
                        r = m - 1
                    elif target > matrix[i-1][m]:
                        l = m + 1
                    else: 
                        return True
        
        while l <= r:
            m = (l + r) // 2
            if target < matrix[rowNum - 1][m]:
                r = m - 1
            elif target > matrix[rowNum - 1][m]:
                l = m + 1
            else: 
                return True
        return False
            