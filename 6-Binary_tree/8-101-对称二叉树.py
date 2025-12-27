# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
from Tree import *
from typing import *
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        本题需要注意，空节点也是对称的判断条件
        """
        if not root:
            return True
        res=False
        que=collections.deque([root.left,root.right])
        while que:
            size=len(que)
            if size%2!=0:
                return False
            level=[]
            for _ in range(size):
                node=que.popleft()
                if node:
                    que.append(node.left)
                    que.append(node.right)
                    level.append(node.val)
                else:
                    level.append(None)
            if level!=level[::-1]:
                return False

        return True
    
    def recurse_isSymmertric(self, root: Optional[TreeNode]) -> bool:
        """
        先同层对比，有4种情况, 3种是结构对比,一种是值不同
        然后是总和子层的bool
        """
        if root is None:    return True
        
        
        
        def compare(left,right):
            if left is None and right is not None: return False
            if left is not None and right is None: return False
            if left is not None and right is None: return True
            if left.val == right.val: return False

            outcompare=compare(left.left,right.right)
            inncompare=compare(left.right,right.left)
            res=outcompare and inncompare
            return res
        return compare(root.left,root.right)
        