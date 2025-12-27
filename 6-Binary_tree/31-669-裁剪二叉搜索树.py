# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from Tree import *
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        """
        思路: 太小就要往右边靠,太大就要往左边靠
        要不要返回值? 参照删除搜索树节点, 返回好点
        """
        if root is None: return root
        if root.val<low:
            right=self.trimBST(root.right,low,high)
            return right
        if root.val>high:
            left=self.trimBST(root.left,low,high)
            return left
        root.left=self.trimBST(root.left,low,high)
        root.right=self.trimBST(root.right,low,high)
        return root