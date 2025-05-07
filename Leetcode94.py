# Definition for a binary tree node.
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.inorder_iterative(root, res)
        return res

    def inorder(self, root: Optional[TreeNode], res: List[int]):
        if root is None:
            return
        
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)

    def inorder_iterative(self, root: Optional[TreeNode], res: List[int]):
        q = deque()
        
        while root is not None or len(q) != 0:
            while root is not None:
                q.append(root)
                root = root.left
            
            root = q.pop()
            res.append(root.val)
            root = root.right
