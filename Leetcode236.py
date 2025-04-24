class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.dfs(root, p, q)
        return self.ans

    def dfs(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> bool:
        if root is None:
            return False
        
        l_find = self.dfs(root.left, p, q)
        r_find = self.dfs(root.right, p, q)

        if root.val == p.val and (l_find or r_find):
            self.ans = root
            return True
        
        if root.val == q.val and (l_find or r_find):
            self.ans = root
            return True

        
        if l_find and r_find:
            self.ans = root
            return True
        
        return l_find or r_find or root.val==p.val or root.val == q.val

        