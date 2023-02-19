from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            first, second = second, max(first + nums[i], second)
        return max(first, second)

s = Solution()
print(s.rob([2,7,9,3,1]))