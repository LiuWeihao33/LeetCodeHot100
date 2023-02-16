# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.res = 0
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxGain(root):
            if not root:
                return 0
            leftGain = max(maxGain(root.left), 0)
            rightGain = max(maxGain(root.right), 0)

            tmp = root.val + leftGain + rightGain
            self.res = max(self.res, tmp)

            return root.val + max(leftGain, rightGain)

        maxGain(root)
        return self.res