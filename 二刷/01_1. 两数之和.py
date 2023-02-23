class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = dict()
        for i in range(len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = i
            if target - nums[i] in hashMap and i != hashMap[target - nums[i]]:
                return [i, hashMap[target - nums[i]]]

s = Solution()
print(s.twoSum([3,2,4], 6))