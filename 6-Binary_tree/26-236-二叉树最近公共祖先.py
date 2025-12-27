from Tree import *
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None


class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        """
        思路: 当root为空, 或者当前节点为其中一个目标,则返回. 为什么当前节点为其中一个目标就返回? 不怕忽略掉其中一个目标是另一个目标的子孙吗? 其实这种情况会包含在上层节点的运算中
        
        本题是得出左孩子以及中是否有p,q, 若两个孩子都有p或q那么证明当前节点即为答案, 若只有其中一个孩子有p或q则就证明孩子是答案
        """
        if p == root or q == root or root is None:
            return root
        lchild = self.lowestCommonAncestor(root.left, p, q)
        rchild = self.lowestCommonAncestor(root.right, p, q)

        le = lchild is not None
        re = rchild is not None

        if re and le:
            return root
        elif le and not re:
            return lchild
        elif not le and re:
            return rchild
        else:
            return None
