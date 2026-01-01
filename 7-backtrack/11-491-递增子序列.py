from typing import *
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        """
        去重逻辑不一样,因为数组不能排序
        注意,去重是要在宽度也就是同层维度上,因此要在每个宽度循环外面初始化used
        used下标值是nums值,元素是表示这个下标是否使用过
        同时注意,子序列并不需要连起来
        """
        res=[]
        def dfs(st,path:list):
            if len(path)>1:
                res.append(path[:])
            used=[0]*201 
            for i in range(st,len(nums)):
                # [4,6,7,3,8]
                if (path and nums[i]<path[-1]) or used[nums[i]+100]==1:
                    continue
                used[nums[i]+100]=1
                path.append(nums[i])
                dfs(i+1,path)
                path.pop()
        
        dfs(0,[])
        return res
                