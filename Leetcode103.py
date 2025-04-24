# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

import queue
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        ans = []
        nor = []
        rev = []
        q = queue.Queue()
        
        q.put((0, root))
        while not q.empty():
            cur: tuple[int, TreeNode] = q.get()
            if cur[1].left is not None:
                q.put((cur[0]+1, cur[1].left))
            
            if cur[1].right is not None:
                q.put((cur[0]+1, cur[1].right))
            if cur[0] %2 == 0:
                nor.append(cur[1].val)
                if len(rev) != 0:
                    ans.append(rev[::-1])
                    rev = []
            
            else :
                rev.append(cur[1].val)
                if len(nor) != 0:
                    ans.append(nor)
                    nor = []
        if len(rev) != 0:
            ans.append(rev[::-1])
            rev = []
        if len(nor) != 0:
            ans.append(nor)
            nor = []
            
        return ans
        
        