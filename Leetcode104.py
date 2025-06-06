# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.md = 0
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.maxD(root, 1)
        return self.md

    def maxD(self, root: Optional[TreeNode], depth) -> int:
        if root is None:
            return
            
        self.md = max(self.md, depth)
        self.maxD(root.left, depth+1)
        self.maxD(root.right, depth+1)

        