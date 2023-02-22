# class Solution(object):
#     def findMedianSortedArrays(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: float
#         """
#         num_dict = dict()
#         n = len(nums1) + len(nums2)
#         if n % 2 == 0: # 偶数
#             flag = 1
#         else:
#             flag = 0
#         n = n // 2
#         idx = 0
#         n1, n2 = 0, 0
#         for i in range(n+1):
#             if n2 >= len(nums2) or n1 >= len(nums1):
#                 if n2 >= len(nums2):
#                     num_dict[i] = nums1[n1]
#                     n1 += 1
#                 else:
#                     num_dict[i] = nums2[n2]
#                     n2 += 1
#             else:
#                 if nums1[n1] < nums2[n2]:
#                     num_dict[i] = nums1[n1]
#                     n1 += 1
#                 else:
#                     num_dict[i] = nums2[n2]
#                     n2 += 1
#         if flag:
#             return (num_dict[n] + num_dict[n-1]) / 2
#         else:
#             return num_dict[n]
#
# s = Solution()
# print(s.findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        def twoDividen(k):

            index1, index2 = 0, 0
            while True:
                # 特殊情况
                if index1 == n:
                    return nums2[index2 + k - 1]
                if index2 == m:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                # 普通情况
                newIndex1 = min(index1 + k // 2 - 1, n - 1)
                newIndex2 = min(index2 + k // 2 - 1, m - 1)
                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
                if pivot1 <= pivot2:
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1

        n, m = len(nums1), len(nums2)
        totalLength = n + m
        if totalLength % 2 == 1: # 奇数
            return twoDividen((totalLength + 1) // 2)
        else:
            return (twoDividen(totalLength // 2) + twoDividen(totalLength + 1) // 2) / 2

s = Solution()
print(s.findMedianSortedArrays(nums1 = [1,3], nums2 = [2]))