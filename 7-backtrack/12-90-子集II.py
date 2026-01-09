from typing import *
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        结合 40.组合总和II 以及 78.子集的逻辑, 注意去重即可
        """
        res=[]
        nums.sort()
        def dfs(st,combine:list):
            if st==len(nums):
                return
            for i in range(st,len(nums)):

                if i>st and nums[i]==nums[i-1]:
                    continue
                combine.append(nums[i])
                res.append(combine[:])
                dfs(i+1,combine)
                combine.pop()
        
        
        res.append([])
        dfs(0,[])
        return res

sol=Solution()
nums = [1,2,2]
res=sol.subsetsWithDup(nums)
for r in res:
    print(r)