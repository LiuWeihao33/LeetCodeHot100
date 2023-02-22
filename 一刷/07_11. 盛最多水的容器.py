class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        area = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            ans = max(ans, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans

s = Solution()
print(s.maxArea(height = [1,1]))