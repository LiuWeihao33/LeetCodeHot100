from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res = res ^ num
        return res

s = Solution()
print(s.singleNumber(nums = [4,1,2,1,2]))