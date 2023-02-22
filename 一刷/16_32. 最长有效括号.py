class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        res = 0

        for i in range(n):
            if i > 0 and s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2
                elif s[i - 1] == ')' and s[i - dp[i - 1] - 1] == '(' and i - dp[i-1] - 1 >= 0:
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                if dp[i] > res:
                    res = dp[i]
        return res

s = Solution()
print(s.longestValidParentheses("()(())"))