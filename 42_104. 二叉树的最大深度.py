# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 层次遍历的时候标记下层数
        if not root:
            return 0
        queue = [root]
        depth = 0
        while queue:
            depth += 1
            size = len(queue)
            for _ in range(size):
                root = queue.pop(0)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
        return depth