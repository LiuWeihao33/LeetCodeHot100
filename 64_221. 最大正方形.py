from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        row, col = len(matrix), len(matrix[0])
        dp = [[0] * col for _ in range(row)]
        maxSquare = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxSquare = max(maxSquare, dp[i][j])
                else:
                    dp[i][j] = 0
        return maxSquare * maxSquare

s = Solution()
print(s.maximalSquare([["0","1"],["1","0"]]))