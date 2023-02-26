# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head1, head2 = l1, l2
        head = ListNode()
        dummy = head
        tmp = 0 # 表示前面进的位
        while head1 and head2:
            total = head1.val + head2.val + tmp
            tmp = total // 10
            value = total % 10
            head.next = ListNode(value)
            head = head.next
            head1 = head1.next
            head2 = head2.next
        headlast = head1 if head1 else head2
        while headlast:
            total = headlast.val + tmp
            tmp = total // 10
            value = total % 10
            head.next = ListNode(value)
            head = head.next
            headlast = headlast.next
        if tmp:
            head.next = ListNode(tmp)
            head = head.next
        return dummy.next