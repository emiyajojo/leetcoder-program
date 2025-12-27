from Tree import *
import collections
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None: return None
        que=collections.deque([root])
        while que:
            
            size=len(que)
            for _ in range(size):    
                node=que.popleft()

                node.left,node.right=node.right,node.left
                if node.left is not None:   que.append(node.left)
                if node.right is not None:   que.append(node.right)
            
        
        return root

            
    def rec_invert(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:    return root
        root.left,root.right=root.right,root.left
        self.rec_invert(root.left)
        self.rec_invert(root.right)
        return root