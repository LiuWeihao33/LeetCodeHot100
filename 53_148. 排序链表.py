# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def sortFunc(head, tail):
            if not head:
                return head
            if head.next == tail:
                head.next = None
                return head
            fast, slow = head, head
            while fast != tail:
                fast = fast.next
                slow = slow.next
                if fast != tail:
                    fast = fast.next
                mid = slow
            return merge(sortFunc(head, mid), sortFunc(mid, tail))

        def merge(list1, list2):
            temp, temp1, temp2 = ListNode(), list1, list2
            dummpy = temp
            while temp1 and temp2:
                if temp1.val < temp2.val:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next
                temp = temp.next
            temp.next = temp1 if temp1 else temp2
            return dummpy.next

        return sortFunc(head, None)