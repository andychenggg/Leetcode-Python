# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res = []
        q = deque()
        q.append((root, 0))
        last = (root, 0)
        while len(q) != 0:
            e = q.popleft()
            if e[1] != last[1]:
                res.append(last[0].val)
            last = e

            if e[0].left is not None:
                q.append((e[0].left, e[1]+1))

            if e[0].right is not None:
                q.append((e[0].right, e[1]+1))
        
        res.append(last[0].val)
        return res
            