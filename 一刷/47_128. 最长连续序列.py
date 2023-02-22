from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)
        max_length = 1

        for num in nums_set:
            if num - 1 not in nums_set:
                cur_length = 1
                num += 1
                while num in nums_set:
                    cur_length += 1
                    num += 1
                max_length = max(max_length, cur_length)
        return max_length

s = Solution()
print(s.longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1]))


a = [1,2,3,3,3,3,3,5,5,7]
b = set(a)
for item in b:
    print(item)