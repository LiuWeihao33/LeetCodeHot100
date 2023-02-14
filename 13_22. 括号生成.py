class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []
        def backTrack(l, left, right):
            if len(l) == 2 * n:
                ans.append(''.join(l))
                return
            if left < n:
                l.append('(')
                backTrack(l, left + 1, right)
                l.pop()
            if right < left:
                l.append(')')
                backTrack(l, left, right + 1)
                l.pop()

        backTrack([], 0, 0)
        return ans

s = Solution()
print(s.generateParenthesis(n = 3))