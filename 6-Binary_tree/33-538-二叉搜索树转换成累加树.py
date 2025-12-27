# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from Tree import *
from collections import deque
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        右中左,迭代
        迭代的思路的中序遍历就是先一直往左,若是空值,才处理中,处理完就往右
        这里要反过来,先一直往右
        同时要注意,所有的处理和访问都放在中节点,左子树右子树只是遍历的不需要处理
        """
        if root is None: return None
        stack=[]
        node=root
        pre=0
        while node is not None or stack:
            
            if node is not None:
                stack.append(node)
                
                node=node.right
                
            else:
                node=stack.pop()
                node.val+=pre
                pre=node.val
                node=node.left
        
        return root

        
