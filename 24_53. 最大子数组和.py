from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        curCnt = 0

        for i in range(len(nums)):
            if nums[i] > 0:
                curCnt += nums[i]
                ans = max(ans, curCnt)
            else:
                curCnt += nums[i]
                ans = max(ans, curCnt)
                if curCnt < 0:
                    curCnt = 0
        return ans

s = Solution()
print(s.maxSubArray(nums = [5,4,-1,7,8]))