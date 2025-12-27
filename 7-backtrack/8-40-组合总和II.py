from typing import *
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        这里的去重需要使用排序后的数组, 防止结果集同时出现[1,2,6]和[2,1,6]
        """
        res=[]
        candidates.sort()
        n=len(candidates)
        def dfs(st,path:list):
            nonlocal n
            path_sum=sum(path)
            if path_sum==target:
                res.append(path[:])
                return
            if path_sum>target:
                return
            
            for i in range(st,n):
                if i>st and candidates[i]==candidates[i-1]:
                    continue
                path.append(candidates[i])
                dfs(i+1,path)
                path.pop()
            
        
        dfs(0,[])
        return res