# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 验证二叉搜索树
# 也就是看看二叉搜索树是否满足定义
from typing import *
from Tree import *
class Solution:
    def __init__(self):
        self.max_v=float('-inf')
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        中序遍历下, 节点顺序就是递增, 利用这一点, 使用一个值记录子树的当前最大值
        """
        if not root: return True


        l_bool=self.isValidBST(root.left)
        if self.max_v<root.val:
            self.max_v=root.val  
        else: return False
        r_bool=self.isValidBST(root.right)
        return l_bool and r_bool