from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        leftMax, rightMax = 0, 0
        left, right = 0, len(height) - 1

        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if leftMax < rightMax:
                ans += leftMax - height[left]
                left += 1
            else:
                ans += rightMax - height[right]
                right -= 1
        return ans

s = Solution()
print(s.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]))