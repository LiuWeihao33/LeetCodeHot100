# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        fast, slow = head.next, head
        if not fast:
            return False
        while fast:
            if fast == slow:
                return True
            if fast.next:
                fast = fast.next.next
            else:
                return False
            slow = slow.next
        return False