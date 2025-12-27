# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from Tree import *
import collections
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        val=root.val
        que=collections.deque([root])
        while que:
            size=len(que)
            for i in range(size):
                node=que.popleft()
                if i==0:   val=node.val
                if node.left is not None: que.append(node.left) 
                if node.right is not None: que.append(node.right) 

        return val
        
