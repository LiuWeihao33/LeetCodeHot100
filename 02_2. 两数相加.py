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
        # l1Rev = reversed(l1)
        # l2Rev = reversed(l2)
        head = tree = ListNode()
        tmp = val = 0

        while tmp or l1 or l2:
            val = tmp
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next

            tmp = val // 10
            val = val % 10

            tree.next = ListNode(val)
            tree = tree.next

        return head.next


s = Solution()
print(s.addTwoNumbers(l1 = [0], l2 = [0]))