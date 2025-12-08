
#     给你四个整数数组 nums1、nums2、nums3 和 nums4 ，数组长度都是 n ，请你计算有多少个元组 (i, j, k, l) 能满足：

#     0 <= i, j, k, l < n
#     nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

 

# 示例 1：

# 输入：nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
# 输出：2
# 解释：
# 两个元组如下：
# 1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0

# 示例 2：

# 输入：nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
# 输出：1

 

#   提示：

#     n == nums1.length
#     n == nums2.length
#     n == nums3.length
#     n == nums4.length
#     1 <= n <= 200
#     -228 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 228


from typing import List
from collections import Counter, defaultdict
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        """
        4个数组,元素为a,b,c,d 抽象表示
        大体思路是:4个数组分成两个循环,前面先统计所有的a+b, 记录a+b的次数
        后面两个数组, c+b==-(a+b),那么res+=count(a+b)
        """
        res=0
        c1=Counter(nums1)
        c2=Counter(nums2)
        c3=Counter(nums3)
        c4=Counter(nums4)
        
        ab_dict=defaultdict(int)
        for k1,v1 in c1.items():
            for k2,v2 in c2.items():
                ab_dict[k1+k2]+=v1*v2
        
        for k3,v3 in c3.items():
            for k4,v4 in c4.items():
                res+=v3*v4*ab_dict[-(k3+k4)]

        
        return res         
        