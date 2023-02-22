# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(leftRoot, rightRoot):
            if not leftRoot and not rightRoot:
                return True
            if not leftRoot or not rightRoot:
                return False
            if leftRoot.val != rightRoot.val:
                return False

            if dfs(leftRoot.left, rightRoot.left) and dfs(leftRoot.right, rightRoot.right):
                return True

            return False

        return dfs(root.left, root.right)
