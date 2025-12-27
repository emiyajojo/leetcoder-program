# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from Tree import *
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
         思路: 从上到下遍历只要root在[p,q]中就是最近的公共祖先
        """
        if root.val<=max(p.val,q.val) and root.val>=min(p.val,q.val): return root
        if root.val<min(p.val,q.val): return self.lowestCommonAncestor(root.right,p,q)
        else: return self.lowestCommonAncestor(root.left,p,q)