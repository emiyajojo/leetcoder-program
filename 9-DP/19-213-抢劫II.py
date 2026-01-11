from typing import *
from Tree import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            dp=(0,0)
            if node is None:
                return dp
            
            lt=dfs(node.left)
            rt=dfs(node.right)
            
            not_rob_cur=max(lt[0],lt[1])+max(rt[0],rt[1])
            rob_cur=node.val+lt[0]+rt[0]

            return (not_rob_cur,rob_cur)
        
        dp=dfs(root)
        return max(dp)

        