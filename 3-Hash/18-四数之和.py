# 给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：

#     0 <= a, b, c, d < n
#     a、b、c 和 d 互不相同
#     nums[a] + nums[b] + nums[c] + nums[d] == target

# 你可以按 任意顺序 返回答案 。

 

# 示例 1：

# 输入：nums = [1,0,-1,0,-2,2], target = 0
# 输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

# 示例 2：

# 输入：nums = [2,2,2,2,2], target = 8
# 输出：[[2,2,2,2]]

 

# 提示：

#     1 <= nums.length <= 200
#     -109 <= nums[i] <= 109
#     -109 <= target <= 109
from typing import *
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        思路和三数之和一样，不一样的是要加多一个遍历全数组的索引k
        除了最左边的索引，中间的索引去重逻辑还是要先加上第一次满足条件的元素到结果集，然后如果重复就往中间靠
        还有i,j这两个索引，要考虑target小于0的情况，不能像3数之和那样nums[i]>target就break,因为即使nums[i]在4个索引指向的元素中最小(也就是说此时所有元素都大于target)，但是他右边的元素还是有可能小于0,加上右边
        之后依然有可能等于target,这个剪枝需要加上nums[i]>0的条件
        同时别忘了在lr去重的分支，记得lr也要向前走，不然的话就死循环了
        """
        res=[]
        nums=sorted(nums)
        for i in range(len(nums)):
            if nums[i]>target and nums[i]>0 and target>0: break
            if i>0 and nums[i-1]==nums[i]: continue
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]>target and nums[j]+nums[i]>0: break
                if j>i+1 and nums[j-1]==nums[j]: continue
                
                l=j+1
                r=len(nums)-1
                while l<r:
                    sum_lr=nums[l]+nums[r]
                    sum_ij=nums[i]+nums[j]
                    if sum_lr==target-sum_ij:
                        res.append([nums[i],nums[j],nums[l],nums[r]])                        
                        while l<r and nums[l]==nums[l+1] : l+=1
                        while l<r and nums[r]==nums[r-1]: r-=1
                        l+=1
                        r-=1

                    elif sum_lr<target-sum_ij:
                        l+=1
                    else:
                        r-=1
                    
                    
            
        return res

if __name__=="__main__":
    nums=[-2,-1,-1,-1,-1,1,1,1,1,1,0,0,0,2,2,2,2]
    target=0
    sol=Solution()
    sol.fourSum(nums,target)
                    
                
        