# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import *
from Tree import *
from math import inf
import collections
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        """
        题意理解很重要: 注意这里的众数为频率最高的节点值, 并且可能有多个最高频率的节点值
        """
        mode_set={}
        cur=inf
        pre=-inf
        def dfs(node:Optional[TreeNode])->None:
            if not node: return None
            nonlocal cur,pre
            dfs(node.left)
            cur=node.val
            if cur not in mode_set.keys():
                mode_set[cur]=1
            if cur==pre: mode_set[cur]+=1
            pre=cur
            dfs(node.right)
        
        dfs(root)
        max_freq=0
        for k,v in mode_set.items():
            if max_freq<v: max_freq=v
        res=[k for k,v in mode_set.items() if v==max_freq]
        
        return res