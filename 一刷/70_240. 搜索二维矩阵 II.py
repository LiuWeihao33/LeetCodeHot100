from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        row, col = len(matrix), len(matrix[0])
        m, n = 0, col - 1
        while 0 <= m < row and 0 <= n < col:
            if target == matrix[m][n]:
                return True
            elif target > matrix[m][n]:
                m += 1
            else:
                n -= 1
        return False

s = Solution()
print(s.searchMatrix(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5))
