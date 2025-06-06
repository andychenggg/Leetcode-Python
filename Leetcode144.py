# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.preorder(root, res)
        return res

    def preorder(self, root, res: List[int]):
        if root is None:
            return
        
        res.append(root.val)
        self.preorder(root.left, res)
        self.preorder(root.right, res)