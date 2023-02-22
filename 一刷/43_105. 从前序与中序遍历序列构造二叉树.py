# Definition for a binary tree node.
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def MyBuildTree(preorder_left, preorder_right, inorder_left, inorder_right):
            if preorder_left > preorder_right:
                return None
            preorder_root = preorder_left
            inorder_root = haspMap[preorder[preorder_root]]
            left_subtree = inorder_root - inorder_left

            root = TreeNode(preorder[preorder_root])
            root.left = MyBuildTree(preorder_left + 1, preorder_left + left_subtree, inorder_left, inorder_root - 1)
            root.right = MyBuildTree(preorder_left + left_subtree + 1, preorder_right, inorder_root + 1, inorder_right)

            return root

        n = len(preorder)
        haspMap = {element: i for i, element in enumerate(inorder)}
        return MyBuildTree(0, n - 1, 0, n - 1)
