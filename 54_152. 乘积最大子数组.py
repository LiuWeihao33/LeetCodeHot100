from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res, preMax, preMin = nums[0], nums[0], nums[0]
        if len(nums) == 1:
            return res
        for i in range(1, len(nums)):
            numMax = max(preMax * nums[i], preMin * nums[i], nums[i])
            numMin = min(preMin * nums[i], preMax * nums[i], nums[i])
            res = max(numMax, res)
            preMax = numMax
            preMin = numMin
        return res
