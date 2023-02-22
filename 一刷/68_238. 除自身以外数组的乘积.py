from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp_left = [1] * n
        dp_right = [1] * n
        for i in range(1, n):
            dp_left[i] = dp_left[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            dp_right[i] = dp_right[i+1] * nums[i+1]
        res = [0] * n
        for i in range(n):
            res[i] = dp_left[i] * dp_right[i]
        return res

s = Solution()
print(s.productExceptSelf(nums = [1,2,3,4]))