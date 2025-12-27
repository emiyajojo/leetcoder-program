from Tree import *
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None: return 0
        ld=self.maxDepth(root.left)
        rd=self.maxDepth(root.right)
        return 1+max(ld,rd)