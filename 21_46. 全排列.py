from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backTrack(first = 0):
            if first == n:
                ans.append(nums[:])
                return
            for idx in range(first, n):
                nums[first], nums[idx] = nums[idx], nums[first]
                backTrack(first + 1)
                nums[first], nums[idx] = nums[idx], nums[first]

        ans = []
        n = len(nums)
        backTrack()
        return ans

s = Solution()
print(s.permute(nums = [1,2,3]))
