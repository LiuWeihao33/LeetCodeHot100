from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1
                if cnt <= mid:
                    right = mid - 1
                else:
                    left = mid
        return mid

s = Solution()
print(s.findDuplicate(nums = [1,3,4,2,2]))

'''
输入：nums = [1,3,4,2,2]
输出：2
'''