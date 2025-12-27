# 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

 

# 示例 1：

# 输入：nums = [1,1,1,2,2,3], k = 2

# 输出：[1,2]

# 示例 2：

# 输入：nums = [1], k = 1

# 输出：[1]

# 示例 3：

# 输入：nums = [1,2,1,2,1,2,3,1,3,2], k = 2

# 输出：[1,2]

 

# 提示：

#     1 <= nums.length <= 105
#     -104 <= nums[i] <= 104
#     k 的取值范围是 [1, 数组中不相同的元素的个数]
#     题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的

 
from typing import *
import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        使用小顶堆+字典解决:
        1. 字典统计频数
        2. 小顶堆构建+维护，这里借助元组的比较方式进行小顶堆的值的相对比较，同时当小顶堆容量不足就弹出
        3. 将小顶堆倒序输出到结果数组
        """
        map_=defaultdict(int)
        for i in nums:
            map_[i]+=1
        pri_heap=[]
        for key,val in map_.items():
            heapq.heappush(pri_heap,(val,key))
            if len(pri_heap)>k:
                heapq.heappop(pri_heap)
        
        res=[0]*k
        for i in range(k-1,-1,-1):
            res[i]=heapq.heappop(pri_heap)[1]
        
        return res

sol=Solution()
nums = [1,2,1,2,1,2,3,1,3,2]
print(sol.topKFrequent(nums,2))