class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j > i and nums[i] > nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        start, end = i + 1, j
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1