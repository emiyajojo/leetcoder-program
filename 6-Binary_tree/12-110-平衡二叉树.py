from Tree import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.getDepth(self.root)==-1:
            return False
        else:   return True
        
    def getDepth(self,node:TreeNode):
        """
        这个求深度的函数应该叫‘平衡地求深度’，只要不平衡就返回-1
        """
        if node is None: return 0
        ld=self.getDepth(node.left)
        rd=self.getDepth(node.right)
        if (ld|rd)<0 or abs(ld-rd)>1: return -1
        return 1+max(ld,rd)