class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for first in range(n):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            target = -nums[first]
            third = n - 1
            for second in range(first + 1, n - 1):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                while third > second and nums[second] + nums[third] > target:
                    third -= 1
                if third == second:
                    break
                if nums[second] + nums[third] == target:
                    res.append([nums[first], nums[second], nums[third]])
        return res

s = Solution()
print(s.threeSum(nums = [1,2,-2,-1]))