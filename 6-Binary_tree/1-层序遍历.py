# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import *
from Tree import *
import collections
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        使用队列作为数据结构，使用双重循环，内层循环的循环长度是队列长度，虽然队列长度其实一直在变，但是每次循环开始的时候使用的是固定的长度——就是将同层级的所有节点塞进去之后的长度
        """
        if not root:
            return []
        res=[]
        que=collections.deque([root])
        while que:
            level=[]
            for _ in range(len(que)):
                node=que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                level.append(node.val)
            
            res.append(level)
        return res
        
        