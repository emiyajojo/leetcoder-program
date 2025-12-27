from typing import *
from Tree import *
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        迭代遍历的难点在于，中序遍历处理节点和访问节点的顺序不一致
        统一迭代遍历，使用多一个boolean记录该节点是否访问过，若是访问过就处理并跳到下一次循环防止重复
        """
        if not root:
            return []
        res=[]
        stack=[(root,False)]
        while stack:
            node,visited=stack.pop()
            if visited:
                res.append(node.val)
                continue
            
            if node.right:
                stack.append((node.right,False))
            stack.append((node,True))
            if node.left:
                stack.append((node.left,False))
        
        return res
        
    
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res=[]
        stack=[root]
        node=root
        while stack:
            if node:
                stack.append(node)
                node=node.right
            else:
                node=stack.pop()
                res.append(node.val)
                node=node.left
        
        return res