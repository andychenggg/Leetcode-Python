# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.buildTreeWithRange(preorder, (0, len(preorder)-1), inorder, (0, len(inorder)-1))

    def buildTreeWithRange(self, preorder: List[int], preorderRange: int, inorder: List[int], inorderRange: int) -> Optional[TreeNode]:
        if preorderRange[0] > preorderRange[1]:
            return None
        
        root = TreeNode(preorder[preorderRange[0]])
        splitIndex = -1
        for i in range(inorderRange[0], inorderRange[1]+1):
            if inorder[i] == preorder[preorderRange[0]]:
                splitIndex = i
                break

        preSplitIndex = preorderRange[0] + (splitIndex - inorderRange[0])

        root.left = self.buildTreeWithRange(preorder, (preorderRange[0]+1, preSplitIndex), inorder, (inorderRange[0], splitIndex-1))
        root.right = self.buildTreeWithRange(preorder, (preSplitIndex+1, preorderRange[1]), inorder, (splitIndex+1, inorderRange[1]))
        return root
    

