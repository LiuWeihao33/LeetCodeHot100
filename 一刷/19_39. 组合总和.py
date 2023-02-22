from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(start, candidate, target):
            if target == 0:
                ans.append(candidate)
                return
            if target < 0:
                return

            for i in range(start, len(candidates)):
                dfs(i, candidate + [candidates[i]], target - candidates[i])


        ans = []
        start = 0
        candidate = []
        dfs(start, candidate, target)
        return ans

s = Solution()
print(s.combinationSum(candidates = [2,3,6,7], target = 7))
