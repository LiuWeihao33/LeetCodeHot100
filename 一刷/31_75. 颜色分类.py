from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1, p2 = 0, len(nums) - 1
        i = 0
        while i <= p2:
            if nums[i] == 2:
                while i < p2 and nums[i] == 2:
                    nums[i], nums[p2] = nums[p2], nums[i]
                    p2 -= 1
            if nums[i] == 0:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1
            i += 1
