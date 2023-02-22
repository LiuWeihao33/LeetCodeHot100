# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        if not head.next:
            return True
        mid = self.findMid(head)
        secondHead = self.reverseList(mid.next)

        firstHead = head
        while secondHead:
            if firstHead.val != secondHead.val:
                return False
            firstHead = firstHead.next
            secondHead = secondHead.next
        return True

    def findMid(self, head):
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverseList(self, head):
        previous = None
        cur = head
        while cur:
            post = cur.next
            cur.next = previous
            previous = cur
            cur = post
        return previous