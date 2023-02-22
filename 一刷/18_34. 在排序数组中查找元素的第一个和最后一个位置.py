class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def findIndex(t):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < t:
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        start = findIndex(target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = findIndex(target + 1)
        return [start, end - 1]

s = Solution()
print(s.searchRange(nums = [5,7,7,8,8,10], target = 6))