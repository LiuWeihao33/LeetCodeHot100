from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 用双指针的方法
        n = len(height)
        i, j = 0, n - 1
        ans = 0
        while i < j:
            square = min(height[i], height[j]) * (j - i)
            ans = max(ans, square)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return ans