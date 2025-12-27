# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
from Tree import *
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        """
        只能用递归, 层序无法判断当前叶子是否在左边
        使用递归, 深度遍历需要额外传入是否为左
        """
        left_sum=0
        def dfs(root:TreeNode,is_left:bool):
            if root is None: return
            dfs(root.left,True)
            dfs(root.right,False)
            nonlocal left_sum
            is_leave=root.left and root.right
            if is_leave and is_left:
                left_sum+=root.val
        
        dfs(root,False)
        return left_sum