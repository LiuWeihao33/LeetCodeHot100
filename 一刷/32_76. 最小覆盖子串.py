
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        import collections
        need = collections.defaultdict(int)
        for c in t:
            need[c] += 1
        needCnt = len(t)
        i = 0
        ans = [0, float('inf')]
        for j, c in enumerate(s):
            if need[c] > 0:
                needCnt -= 1
            need[c] -= 1
            if needCnt == 0:
                while i < j:
                    if need[s[i]] == 0:
                        break
                    need[s[i]] += 1
                    i += 1
                if j - i < ans[1] - ans[0]:
                    ans = [i, j]
                needCnt += 1
                need[s[i]] += 1
                i += 1
        return '' if ans[1] > len(s) else s[ans[0]: ans[1] + 1]

s = Solution()
print(s.minWindow(s = "ADOBECODEBANC", t = "ABC"))