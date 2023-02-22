from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backTrack(i, path):
            res.append(path)
            for j in range(i, len(nums)):
                backTrack(j + 1, path + [nums[j]])

        backTrack(0, [])
        return res

s = Solution()
print(s.subsets(nums = [1,2,3]))