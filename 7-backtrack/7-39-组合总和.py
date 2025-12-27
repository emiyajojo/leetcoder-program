from typing import *
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        与前面的组合总和问题不一样的是,同一个候选数可以被重复选,但是不能出现多个相同的集合答案,比如[2,3,6,7],targetSum=7, [2,2,3]和[3,2,2]是同一个,不能都塞进去
        """
        res=[]
        def dfs(can_ind,path:list):
            path_sum=sum(path)
            if path_sum==target:
               res.append(path[:])
            if path_sum>=target:
                return
            
            for i in range(can_ind,len(candidates)):
                path.append(candidates[i])
                dfs(i,path)
                path.pop()
        
        dfs(0,[])
        return res
    
sol=Solution()
print(sol.combinationSum([2,3,6,7],7))
             