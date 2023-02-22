from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        d = []
        for num in nums:
            if not d or d[-1] < num:
                d.append(num)
            else:
                left, right = 0, len(d) - 1
                loc = right
                while left <= right:
                    mid = (left + right) // 2
                    if num <= d[mid]:
                        loc = mid
                        right = mid - 1
                    else:
                        left = mid + 1
                d[loc] = num
        return len(d)