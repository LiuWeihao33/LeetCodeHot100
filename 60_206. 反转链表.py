# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if not head:
        #     return None
        # cur = head
        # if not head.next:
        #     return cur
        # while head.next:
        #     post = head.next
        #     head.next = post.next
        #     post.next = cur
        #     cur = post
        # return cur
        if not head or not head.next:
            return head
        cur = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return cur