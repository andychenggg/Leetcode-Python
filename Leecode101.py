# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.subtreeSym(root.left, root.right)

    def subtreeSym(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        return (left == right == None or 
                left is not None and right is not None 
                and left.val == right.val 
                and self.subtreeSym(left.left, right.right) 
                and self.subtreeSym(left.right, right.left)
                )
    
