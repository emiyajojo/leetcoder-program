# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from Tree import *
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        思路: 这道题还是需要递归的
        主要难点就在处理相等的情况,这里又有4种情况:
        1. 左右空
        2. 左空又不空
        3. 右空左不空
        4. 左右不空,这里需要找到右子树的最左叶子节点,把左子树接到右子树的最左叶子节点左边就可
        """
        if root is None: return root
        if root.val==key:
            l_exist=root.left is not None
            r_exist=root.right is not None

            if l_exist and r_exist:
                cur=root.right
                while cur.left: # 这个循环终止条件要注意,cur要停在叶子节点,不能为空
                    cur=cur.left
                cur.left=root.left
                return root.right
            elif not l_exist and r_exist:
                return root.right
            elif l_exist and not r_exist:
                return root.left
            else: return None
        if root.val<key:
            root.right=self.deleteNode(root.right,key)
        else: 
            root.left=self.deleteNode(root.left,key)
        return root
            
        
        