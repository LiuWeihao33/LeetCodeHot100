class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # index_list = []
        # for i in range(len(nums) - 1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             index_list.append(i)
        #             index_list.append(j)
        #             return index_list
        # return
        hashMap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashMap.keys():
                return [hashMap[diff], i]
            hashMap[num] = i

s = Solution()
print(s.twoSum(nums = [2,7,11,15], target = 9))