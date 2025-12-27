from Tree import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        """
        这题‘难’在不知道递归要不要返回值，其实这里如果要返回的话，很难知道什么时候将一条完整路径加入路径集合，并且如果使用返回值，
        那么使不使用额外变量记录路径？使用了额外变量，那么好像就不需要返回值了；
        因此不返回值，而是使用传入迄今为止的当前路径记录，然后不返回值，这样方便
        """
        paths=[]
        def treePath(node,path):
            if node is None: return None
            path+=str(node.val)
            if node.left is None and node.right is None:
                paths.append(path)
            
            path+='->'
            treePath(node.left,path)
            treePath(node.right,path)
        
        if not root: return []
        treePath(root,'')
        return paths
            
            