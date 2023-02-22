class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if m * n == 0:
            return m + n
        dp = [[0] * (n+1) for _ in range(m+1)] # 需要多申请一个长度的list来方便下面的循环
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                left = dp[i][j-1]
                down = dp[i-1][j]
                left_down = dp[i-1][j-1]
                if word1[i-1] == word2[j-1]:
                    left_down -= 1
                dp[i][j] = 1 + min(left, down, left_down)
        return dp[m][n]

s = Solution()
print(s.minDistance(word1 = "intention", word2 = "execution"))