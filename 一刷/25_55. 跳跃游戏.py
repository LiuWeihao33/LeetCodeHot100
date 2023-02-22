from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, rightMost = len(nums), 0

        for i in range(n):
            if i <= rightMost:
                rightMost = max(rightMost, i + nums[i])
                if rightMost >= n - 1:
                    return True
        return False

s = Solution()
print(s.canJump(nums = [3,2,1,0,4]))