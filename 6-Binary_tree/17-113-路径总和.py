from Tree import *
from copy import deepcopy
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        paths=[]
        def hasPathSum(root,tarsum,path):
            if root is None: return 
            path.append(root.val)
            diff=targetSum-root.val
            is_leave=root.left is None and root.right is None
            
            if diff!=0 or (diff==0 and not is_leave):
                lpath=deepcopy(path)
                rpath=deepcopy(path)
                hasPathSum(root.left,diff,lpath)
                hasPathSum(root.right,diff,rpath)
            else:
                paths.append(path)
        
        hasPathSum(root,targetSum)
        return paths
                    
            