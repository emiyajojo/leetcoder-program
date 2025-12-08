# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。

# 注意：答案中不可以包含重复的三元组。

 

 

# 示例 1：

# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 解释：
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
# 不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
# 注意，输出的顺序和三元组的顺序并不重要。

# 示例 2：

# 输入：nums = [0,1,1]
# 输出：[]
# 解释：唯一可能的三元组和不为 0 。

# 示例 3：

# 输入：nums = [0,0,0]
# 输出：[[0,0,0]]
# 解释：唯一可能的三元组和为 0 。

 

# 提示：

#     3 <= nums.length <= 3000
#     -105 <= nums[i] <= 105


from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        思路：3指针处理处理过的有序数组,i是当前元素,l,r双指针一小一大这里哈希不好做,因为要去重
        3指针,有个问题是如何移动？其实就是要双重循环
        边界条件、特殊条件判断：
        1. nums[i-1]是重复的就要跳过，为什么是i-1？如果是i+1就跳过去那就漏了, 
        2. nums[i]>0,此时不可能满足nums[i]+nums[l]+nums[r]==0,后面两个大于nums[i],3个正数之和>0
        
        这里别忘了l也需要去重, nums[i]去重的逻辑对于l同样适用,对r不需要去重, 因为l从r左边过来,如果r去重那么可能会漏掉nums[l]==nums[r]的情况
        对于lr去重还有另一个操作,就是先添加满足和为0的三元组,然后如果l右边的元素重复,或者r左边的元素重复,lr都要往中间缩
        """
        nums=sorted(nums)
        res=[]
        for i in range(len(nums)):
            if nums[i]>0:   return res
            if i>0 and nums[i]==nums[i-1]:  
                print(f"nums[i]: {nums[i]}, i: {i}")
                continue
            
            l=i+1
            r=len(nums)-1
            while l<r:
                # print(f"{nums[i]},{nums[l]},{nums[r]}")
                
                if nums[i]+nums[l]+nums[r]==0:
                    if nums[l]!=nums[l-1] or i==l-1:
                        res.append([nums[i],nums[l],nums[r]])                 
                    l+=1
                elif nums[l]+nums[r]>-nums[i]:  r-=1
                else:   l+=1
        
        return res
                