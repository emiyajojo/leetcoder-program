# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

# 返回 滑动窗口中的最大值 。

 

# 示例 1：

# 输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
# 输出：[3,3,5,5,6,7]
# 解释：
# 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7

# 示例 2：

# 输入：nums = [1], k = 1
# 输出：[1]

 

# 提示：

#     1 <= nums.length <= 105
#     -104 <= nums[i] <= 104
#     1 <= k <= nums.length
from typing import *
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        思路：使用单调队列，从大到小，并且这个队列不需要维持窗口长度的数量的值
        遇到小的值就留下，遇到大的值就把队列的尾巴值全去掉
        初始化和边界条件的特别处理，看看能不能放进循环内一并完成，比如本函数‘初始化’第一个窗口，还有单调队列的维护判断队列是否为空
        """
        mn_que=deque()
        res_list=[]
        for i in range(len(nums)):
            self.mono_deque(mn_que,nums[i])
            # 有没有可能刚好滑动窗口需要丢弃的最左边的值是单调队列里的较小值？
            # 不可能！在单调队列里面可能存在的只有的比最大值更迟进队列的较小值！
            # 因此这里需要pop的只有队列头的当前最大值
            if i>=k and nums[i-k]==mn_que[0]:
                mn_que.popleft()
            if i>=k-1:
                res_list.append(mn_que[0])
        
        return res_list
            
            
    
    def mono_deque(self,mn_que:deque,val:int):
        while mn_que and mn_que[-1]<val:
            mn_que.pop()
        mn_que.append(val)
