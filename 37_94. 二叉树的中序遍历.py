from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # def dfs(root):
        #     if not root:
        #         return
        #     dfs(root.left)
        #     ans.append(root.val)
        #     dfs(root.right)

        # ans = []
        # dfs(root)
        # return ans

        stack = []
        ans = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                temp = stack.pop()
                ans.append(temp.val)
                root = temp.right
        return ans