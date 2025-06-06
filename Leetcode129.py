# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.sum = 0


    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.getSum(root, 0)
        return self.sum

    def getSum(self, root: Optional[TreeNode], curSum: int):
        if root.left is None and root.right is None:
            self.sum += curSum * 10 + root.val
            return
        
        if root.left is not None:
            self.getSum(root.left, curSum * 10 + root.val)
        
        if root.right is not None:
            self.getSum(root.right, curSum * 10 + root.val)