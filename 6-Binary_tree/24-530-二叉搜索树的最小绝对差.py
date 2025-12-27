# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import *
from Tree import *
from math import inf
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """
        对于二叉搜索树的典型结构有错误的认识!
        [236,104,701,null,227,null,911] 这是一棵有典型结构的二叉搜索树
        本题思路是找左子树的最大值和右子树的最小值
        
        还有更快的思路: 例如中序遍历的单调递增特性, 使用双指针记录当前和前一个节点值
        """
        if not root:
            return float('inf')
        l_r_node=root.left
        if l_r_node:
            while l_r_node.right:
                l_r_node=l_r_node.right
            l_diff=root.val-l_r_node.val 
        else: l_diff=float('inf')    
        r_l_node=root.right
        if r_l_node:
            while r_l_node.left:
                r_l_node=r_l_node.left
            r_diff=r_l_node.val-root.val
        else: r_diff=float('inf')    
        return min(l_diff,r_diff,self.getMinimumDifference(root.left),self.getMinimumDifference(root.right))
    
    def double_pointer(self,root:TreeNode)->int:
        ans=inf
        pre=-inf
        def dfs(root:TreeNode):
            if not root:  return
            dfs(root.left)
            nonlocal ans,pre
            ans=min(ans,root.val-pre)
            pre=root.val
            dfs(root.right)
        
        dfs(root)
        return ans
        
        
        