# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from Tree import *
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
        把不满和满的二叉树都算成满的二叉树对待，因为即使是不满的二叉树到了最后一个节点也能当成局部的满二叉树
        
        计算一棵满二叉树的的方式是直接向下遍历，不用递归
        """
        if root is None: return 0
        ln,rn=root.left,root.right
        ld=rd=1
        while ln: 
            ld+=1
            ln=ln.left
        while rn:
            rd+=1
            rn=rn.right
        if ld==rd: return 2**ld-1
        
        return self.countNodes(root.left)+self.countNodes(root.right)+1