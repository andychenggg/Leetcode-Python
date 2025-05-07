# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = root.val
        self.maxGain(root)
        return self.maxSum

    def maxGain(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        lGain = self.maxGain(root.left)
        rGain = self.maxGain(root.right)

        self.maxSum = max(lGain+root.val, rGain+root.val, lGain+root.val+rGain, self.maxSum, root.val)

        return max(lGain+root.val, rGain+root.val, root.val)


