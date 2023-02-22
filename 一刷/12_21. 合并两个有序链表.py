# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        mergeList = ListNode(0)
        res = mergeList

        while list1 and list2:
            if list1.val < list2.val:
                mergeList.next = list1
                list1 = list1.next
            else:
                mergeList.next = list2
                list2 = list2.next
            mergeList = mergeList.next

        # if list1:
        #     mergeList.next = list1
        # else:
        #     mergeList.next = list2
        mergeList.next = list1 if list1 is not None else list2

        return res.next

