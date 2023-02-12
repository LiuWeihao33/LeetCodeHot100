# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if len(s) < 2:
#             return s
#
#         n = len(s)
#         dp = [[False] * n for _ in range(n)]
#         maxLen, start = 1, 0
#         for i in range(n):
#             dp[i][i] = True
#
#         for L in range(2, n + 1): # 子串的长度
#             for i in range(n):
#                 j = i + L - 1
#                 if j >= n:
#                     break
#
#                 if s[i] != s[j]:
#                     dp[i][j] = False
#                 else:
#                     if j - i + 1< 3:
#                         dp[i][j] = True
#                     else:
#                         dp[i][j] = dp[i+1][j-1]
#
#                 if dp[i][j] and j - i + 1 > maxLen:
#                     maxLen = j - i + 1
#                     start = i
#
#         return s[start:start+maxLen]
class Solution:
    def expandAroundCenter(self, s, left, right):
        while left >=0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1


    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i + 1)

            if right1 - left1 > end - start:
                start = left1
                end = right1
            if right2 - left2 > end - start:
                start = left2
                end = right2
        return s[start:end+1]



s = Solution()
print(s.longestPalindrome(s = "ccc"))