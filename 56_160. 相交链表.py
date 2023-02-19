# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        ptra, ptrb = headA, headB
        while ptra != ptrb:
            ptra = ptra.next if ptra else headB
            ptrb = ptrb.next if ptrb else headA
        return ptra