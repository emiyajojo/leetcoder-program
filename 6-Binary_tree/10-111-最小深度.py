from collections import deque
from Tree import *
class Solution:
    def minDepth(self,root:Optional[TreeNode])->int:
        if root is None: return 0
        que=deque([root])
        layer_cnt=0
        while que:
            size=len(que)
            for i in range(size):
                layer_cnt+=1
                node=que.popleft()
                if node.right is None and node.left is None:
                    return layer_cnt
                if node.left:que.append(node.left)
                if node.right:que.append(node.right)
                
            
        
        return layer_cnt
        