class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            if matrix[row][-1] < target:
                continue
            
            l, r = 0, len(matrix[row]) - 1
            while l <= r:
                middle = (l + r) // 2
                if matrix[row][middle] > target:
                    r = middle - 1
                elif matrix[row][middle] < target:
                    l = middle + 1
                else:
                    return True
        return False