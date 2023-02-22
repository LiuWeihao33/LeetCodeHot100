# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        preOrderList = []

        def PreOrder(root):
            if root:
                preOrderList.append(root)
                PreOrder(root.left)
                PreOrder(root.right)

        PreOrder(root)
        n = len(preOrderList)
        for i in range(1, n):
            pre, cur = preOrderList[i - 1], preOrderList[i]
            pre.left = None
            pre.right = cur