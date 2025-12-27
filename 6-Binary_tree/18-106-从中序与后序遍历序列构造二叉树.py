# 给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder 是同一棵树的后序遍历，请你构造并返回这颗 二叉树 。

 

# 示例 1:

# 输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# 输出：[3,9,20,null,null,15,7]

# 示例 2:

# 输入：inorder = [-1], postorder = [-1]
# 输出：[-1]

 

# 提示:

#     1 <= inorder.length <= 3000
#     postorder.length == inorder.length
#     -3000 <= inorder[i], postorder[i] <= 3000
#     inorder 和 postorder 都由 不同 的值组成
#     postorder 中每一个值都在 inorder 中
#     inorder 保证是树的中序遍历
#     postorder 保证是树的后序遍历

from Tree import *
from typing import *
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        思路: 由于每个节点值都不一样,可以通过值来确定节点
        1. 首先, 通过后序遍历数组的最后一个节点值确定当前根节点
        2. 在inroder找到该节点返回下标, inorder左区间是左子树,右区间是右子树
        3. 通过indorder左区间和右区间, 确定postorder左区间右区间, 根据postorder性质,先左后右, 使用inorder遍历出来的左右区间长度直接在postorder切片就能得到postorder的左右子区间
        """
        
        if not inorder: return None

        root_val=postorder[-1]
        if root_val in inorder:
            root_ind=inorder.index(root_val)
        else: return None

        root=TreeNode(root_val)
        # 直接切割出左中序区间和右中序区间,要注意边界条件:根节点在inorder中是0位 或者在 postorder 中是-1位
        
        in_l_tree=inorder[:root_ind]
        in_r_tree=inorder[(root_ind+1):]
        
        post_ltree=postorder[:len(in_l_tree)]
        post_rtree=postorder[len(in_l_tree):-1]

        root.left=self.buildTree(in_l_tree,post_ltree)
        root.right=self.buildTree(in_r_tree,post_rtree)
        return root
    def buildTree_hash(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # 创建哈希表加速查找[2,4](@ref)
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        def build(in_start, in_end, post_start, post_end):
            if post_start > post_end:
                return None
                
            # 后序遍历最后一个元素是根节点[3,6](@ref)
            root_val = postorder[post_end]
            root = TreeNode(root_val)
            
            # 在中序中找到根节点位置
            root_idx = inorder_map[root_val]
            
            # 计算左子树节点数量[8](@ref)
            left_size = root_idx - in_start
            
            # 递归构建左右子树[7](@ref)
            root.left = build(in_start, root_idx - 1, post_start, post_start + left_size - 1)
            root.right = build(root_idx + 1, in_end, post_start + left_size, post_end - 1)
            
            return root
        
        return build(0, len(inorder) - 1, 0, len(postorder) - 1)
        
            
        