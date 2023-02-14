# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: [ListNode]) -> [ListNode]:
        import heapq
        head = []
        tempList = ListNode(0)
        dummpy = tempList

        for i in range(len(lists)):
            if not lists[i]:
                continue
            heapq.heappush(head, (lists[i].val, i))
            lists[i] = lists[i].next

        while head:
            val, idx = heapq.heappop(head)
            tempList.next = ListNode(val)
            tempList = tempList.next
            if lists[idx]:
                heapq.heappush(head, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return dummpy.next
