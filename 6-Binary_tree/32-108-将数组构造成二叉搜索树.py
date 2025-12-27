# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from Tree import *
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        递归区间取中间坐标,每次的middle不是(right-left)//2而是(right+left)//2
        """
        def dfs(st,end):
            if st>end:
                return None
            root_ind=(end+st)//2
            root_val=nums[root_ind]
            root=TreeNode(root_val)
            
            root.left=dfs(st,root_ind-1)
            root.right=dfs(root_ind+1,end)
            
            return root
        root=dfs(0,len(nums)-1)
        return root 