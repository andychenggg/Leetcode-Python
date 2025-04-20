# Definition for a binary tree node.
from typing import List


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        res = []
        self.traversal(root, 0, res)
        return res

    def traversal(self, root: TreeNode, level: int, res: List[List[int]]) -> None:
        if root is None:
            return
        
        if len(res) <= level:
            res.append([])

        res[level].append(root.val)

        self.traversal(root.left, level+1, res)
        self.traversal(root.right, level+1, res)
       
        
        